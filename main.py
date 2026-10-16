# main.py（新文件）—— 程序的入口
import sys

from expense import new_record  # 不再是 parse_expense
from storage import load_expenses, save_expenses


def cmd_add(text):
    record = new_record(text)            # ← 一行拿到完整记录
    expenses = load_expenses()
    expenses.append(record)
    save_expenses(expenses)
    print("已记账：", record)


def cmd_list():
    expenses = load_expenses()
    if not expenses:
        print("还没有任何记录")
        return
    # 洞 G：遍历 expenses 打印每一笔，最后打印总笔数和总金额
    # 提示：total = sum(e["amount"] for e in expenses)
    for e in expenses:
        print(f'{e["category"]}  {e["amount"]}')
    total = sum(e["amount"] for e in expenses)
    print(f"\n共 {len(expenses)} 笔，合计 {total}")

if __name__ == "__main__":
    if len(sys.argv) < 2:                # 先检查"够不够用"
        print('用法：py main.py add "午饭 25"  |  py main.py list')
        sys.exit(1)                      # 1 = 非正常退出
    command = sys.argv[1]
    if command == "add":
        if len(sys.argv) < 3:            # add 还需要一句话
            print('用法：py main.py add "午饭 25"')
            sys.exit(1)
        cmd_add(sys.argv[2])
    elif command == "list":
        cmd_list()
    else:
        print(f"未知命令：{command}")
        sys.exit(1)