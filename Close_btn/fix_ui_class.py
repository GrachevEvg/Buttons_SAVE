import re

with open("letstry.py", "r", encoding="utf-8") as f:
    content = f.read()

# Заменяем class Ui_MainWindow(object) на class MainWindow(QMainWindow)
content = re.sub(
    r"class Ui_MainWindow\(object\):",
    "from PyQt5.QtWidgets import QMainWindow\n\nclass MainWindow(QMainWindow):",
    content
)

# Добавляем __init__, если его нет
if "def __init__" not in content:
    init_code = "\n    def __init__(self):\n        super().__init__()\n        self.setupUi(self)\n"
    content = content.replace(
        "class MainWindow(QMainWindow):", "class MainWindow(QMainWindow):" + init_code)

with open("letstry.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Файл успешно исправлен!")
