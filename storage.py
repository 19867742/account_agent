# storage.py（新文件）
import json

FILENAME = "expenses.json"

def load_expenses():
    """读账本。返回 list；文件不存在时返回空列表 []。"""
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)          # 洞 A：这行我写好了，你读懂它
    except FileNotFoundError:
        return []                        # 洞 B：第一次运行没有文件，返回 []
        # 想一想：为什么不直接报错？

def save_expenses(expenses):
    """把整个账本覆盖写回文件。expenses 是 list。"""
    with open(FILENAME, "w", encoding="utf-8") as f:
        # 洞 C：把 expenses 写进去，提示 json.dump(..., ensure_ascii=False, indent=2)
        json.dump(expenses, f, ensure_ascii=False, indent=2)