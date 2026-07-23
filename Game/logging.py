import datetime


def info(message, file_path):
    time = datetime.datetime.now()
    log = f"{time.day}.{time.month}.{time.year} {time.hour}:{time.minute}:{time.second}:{int(time.microsecond / 1000)} [INFO] {message}"
    with open(file_path, "a", encoding="utf-8") as logfile:
        logfile.write(f"{log}\n")

def warning(message, file_path):
    time = datetime.datetime.now()
    log = f"{time.day}.{time.month}.{time.year} {time.hour}:{time.minute}:{time.second}:{int(time.microsecond / 1000)} [WARNING] {message}"
    with open(file_path, "a", encoding="utf-8") as logfile:
        logfile.write(f"{log}\n")

def error(message, file_path):
    time = datetime.datetime.now()
    log = f"{time.day}.{time.month}.{time.year} {time.hour}:{time.minute}:{time.second}:{int(time.microsecond / 1000)} [ERROR] {message}"
    with open(file_path, "a", encoding="utf-8") as logfile:
        logfile.write(f"{log}\n")