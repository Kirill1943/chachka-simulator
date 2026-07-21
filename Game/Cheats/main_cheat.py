

def run():
    print("=== ЧИТЫ ===")
    while True:
        try:
            print("   [ Читы пока разрабатываются ]       ")
            print("[ Введите клавиши Ctrl + C для выхода ]")
            print("        [ Или напиши exit ]"            )
            cmd = input()
            if cmd == "exit": break
        except KeyboardInterrupt:
            print('Выход...')
            break

if __name__ == "__main__":
    run()