import os
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
            shutil.rmtree(pycache_path)
            print(f"Удален кеш: {pycache_path}")

        for file in files:
            if file.endswith(".pyc"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Удален файл: {file_path}")


def main():
    if len(sys.argv) < 2:
        print(
            "Использование:\n"
            "  python manage.py install\n"
            "  python manage.py clean [cache|log]"
        )
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
        elif sub_command in ["pycache", "cache"]:
            clean_pycache()
        elif sub_command in ["logs", "log"]:
            clean_log()
        else:
            print(
                "Чтобы удалить кеш введите: python manage.py clean cache\n"
                "Чтобы удалить логи: python manage.py clean log\n"
                "Чтобы удалить все сразу: python manage.py clean"
            )


if __name__ == "__main__":
    main()
