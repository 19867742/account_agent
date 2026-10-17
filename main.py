import sys

from expense import new_record
from storage import load_expenses, save_expenses


def format_record(rec: dict) -> str:
    sign = "-" if rec["amount"] < 0 else "+"
    return f"{rec['category']} {sign}{abs(rec['amount']):.2f} 元  #{rec['id'][:8]}"


def cmd_add(text):
    record = new_record(text) 
    expenses = load_expenses()
    expenses.append(record)
    save_expenses(expenses)
    print("已记账：" + format_record(record))


def cmd_list():
    expenses = load_expenses()
    if not expenses:
        print("还没有任何记录")
        return
    for e in expenses:
        print(format_record(e))
    total = sum(e["amount"] for e in expenses)
    print(f"\n共 {len(expenses)} 笔，合计 {total}")


def cmd_remove(expense_id):
    expenses = load_expenses()
    rest  = [e for e in expenses if e["id"] != expense_id]
    if len(rest) == len(expenses):
        print(f"未找到 id 为 {expense_id} 的记录")
        return False
    save_expenses(rest)
    print(f"已删除 1 笔，剩余 {len(rest)} 笔")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:          
        print('用法：py main.py add "午饭 25"  |  py main.py list')
        sys.exit(1)               
    command = sys.argv[1]
    if command == "add":
        if len(sys.argv) < 3:        
            print('用法：py main.py add "午饭 25"')
            sys.exit(1)
        cmd_add(sys.argv[2])
    elif command == "list":
        cmd_list()
    elif command == "remove":
        if len(sys.argv) < 3:
            print('用法：py main.py remove 3b0cd39a    （id 从 list 结果的第一列复制）')
            sys.exit(1)
        if not cmd_remove(sys.argv[2]):
            sys.exit(1)
    else:
        print(f"未知命令：{command}")
        sys.exit(1)