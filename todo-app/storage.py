import json
import os

TODO_FILE = "tasks.json"

# Fayldan vazifalarni yuklash
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []  # Agar fayl bo'lmasa, bo‘sh ro‘yxat qaytaramiz
    
    with open(TODO_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []  # Agar fayl buzilgan bo'lsa, bo‘sh ro‘yxat qaytaramiz

# Vazifalarni faylga saqlash
def save_tasks(tasks):
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
