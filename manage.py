import os
import re
import shutil
import subprocess
import sys


def clean_log():
    log_dir = os.path.abspath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "Logs")
    )
    if os.path.exists(log_dir):
        shutil.rmtree(log_dir)
        print("Логи успешно удалены.")
    else:
        print("Папка с логами не найдена.")


def clean_pycache(path="."):
    for root, dirs, files in os.walk(path):
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            try:
                shutil.rmtree(pycache_path)
                print(f"Удален pycache: {pycache_path}")
            except Exception as e:
                print(f"Не удалось удалить {pycache_path}: {e}")
            dirs.remove("__pycache__")

        for file in files:
            if file.endswith(".pyc"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Удален файл: {file_path}")
                except Exception as e:
                    print(f"Не удалось удалить файл {file_path}: {e}")


def clean_cache(path="."):
    cache_dir = os.path.join(path, "cache")

    if os.path.isdir(cache_dir):
        for item in os.listdir(cache_dir):
            item_path = os.path.join(cache_dir, item)
            try:
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)
                print(f"Удален кеш: {item_path}")
            except Exception as e:
                print(f"Не удалось удалить {item_path}: {e}")
    else:
        print(f"Папка с кешем не найдена")

    for i in os.listdir(path):
        if re.match(r".*_cache$", i):
            full_path = os.path.join(path, i)
            if os.path.isdir(full_path):
                try:
                    shutil.rmtree(full_path)
                    print(f"Удалена скрытая папка кеша: {full_path}")
                except Exception as e:
                    print(f"Не удалось удалить {full_path}: {e}")


def clean_build(path="."):
    target_dir = os.path.abspath(path)
    found_any = False

    for root, dirs, files in os.walk(target_dir, topdown=False):
        for directory in dirs:
            if directory == "build":
                full_path = os.path.join(root, directory)
                try:
                    shutil.rmtree(full_path)
                    print(f"удалена папка сборки {full_path}")
                    found_any = True
                except Exception as e:
                    print(f"Не удалось удалить {full_path}: {e}")
            elif directory.endswith(".egg-info"):
                full_path = os.path.join(root, directory)
                try:
                    shutil.rmtree(full_path)
                    print(f"удалена папка egg-info {full_path}")
                    found_any = True
                except Exception as e:
                    print(f"Не удалось удалить {full_path}: {e}")

    if not found_any:
        print(" Все чисто! Папки build и *.egg-info не найдены.")
    else:
        print("\n Очистка успешно завершена!")


def check_commands():
    print(
        "Использование:\n"
        "  python manage.py test (требуется pytest)\n"
        "  python manage.py install\n"
        "  python manage.py clean [cache|log|build]\n"
        "  python manage.py help"
    )


def main():
    if len(sys.argv) < 2:
        check_commands()
        return

    command = sys.argv[1]

    if command == "install":
        requirements = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "requirements.txt"
        )
        if not os.path.exists(requirements):
            with open(requirements, "w", encoding="utf-8"):
                pass
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements])

    elif command == "clean":
        sub_command = sys.argv[2] if len(sys.argv) > 2 else "all"

        if sub_command == "all":
            clean_log()
            clean_pycache()
            clean_cache()
            clean_build()
        elif sub_command in ["pycache", "cache"]:
            clean_pycache()
            clean_cache()
        elif sub_command == "build":
            clean_build()
        elif sub_command in ["logs", "log"]:
            clean_log()
        else:
            print(
                "Чтобы удалить кеш введите: python manage.py clean cache\n"
                "Чтобы удалить логи: python manage.py clean log\n"
                "Чтобы удалить все сразу: python manage.py clean"
            )
    elif command == "help":
        try:
            from Game.Help import menu
            menu.run()
        except ModuleNotFoundError:
            print("Ошибка: Модуль Game.Help не найден!")
    elif command == "test":
        import importlib.util
        if importlib.util.find_spec("pytest") is None:
            print("У вас не установлена библиотека pytest. Для установки напишите: pip install pytest")
            return
        subprocess.run([sys.executable, "-m", "pytest"])
    else:
        print("Вы ввели несуществующую команду")
        check_commands()


if __name__ == "__main__":
    main()
