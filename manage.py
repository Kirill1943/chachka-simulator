import os
import subprocess
import sys

if len(sys.argv) > 1:
    if sys.argv[1] == "install":
        requirements = os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements.txt")
        if not os.path.exists(requirements):
            a = open(requirements, "w", encoding="utf-8")
            a.close()
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])