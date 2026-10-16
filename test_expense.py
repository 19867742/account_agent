# test_expense.py —— Day 3/5 检查点
# 运行：python test_expense.py
# 目的：验证 ①分类 ②金额 是否配对；顺带验证"坏输入"不会打垮程序
import sys

sys.stdout.reconfigure(encoding="utf-8")   # 让控制台按 UTF-8 输出

from expense import parse_expense

# 格式：(输入句子, 期望分类, 期望金额)
# 期望金额 = None 表示：这句话本来就该没有金额（程序该抛错，而不是瞎猜）
CASES = [
    ("午饭 25", "餐饮", 25),
    ("打车 18.5", "交通", 18.5),
    ("买书 120", "购物", 120),
    ("地铁 3", "交通", 3),
    ("晚餐 50", "餐饮", 50),
    # ---- 你加的边界用例（按"预期正确行为"标注） ----
    ("早餐 15.5", "餐饮", 15.5),
    ("奶茶 6.6", "餐饮", 6.6),
    ("¥18.5", "其他", 18.5),
    ("￥18.5 咖啡", "其他", 18.5),
    ("今天没花钱", None, None),        # 无金额 → 应当抛错
    ("买书 120,用券 20", "购物", 120),  # 现在只认第一个数字，先按现状标注
    ("-12 退款", "其他", -12),          # 负数：你的正则现在做不到，先按理想值标注
    ("1,200 房租", "其他", 1200),       # 千分位逗号：现在也做不到，先按理想值标注
]

if __name__ == "__main__":
    passed = 0
    total = len(CASES)

    for text, want_cat, want_amt in CASES:
        try:
            got = parse_expense(text)
            cat_ok = got.get("category") == want_cat
            amt_ok = got.get("amount") == want_amt
        except Exception as e:       # noqa: BLE001 —— 测试立场：任何抛错都算失败
            cat_ok = amt_ok = (want_amt is None)
            got = f"抛错: {type(e).__name__}: {e}"

        passed += cat_ok and amt_ok
        if isinstance(got, dict):
            print(f"{'✔' if cat_ok else '✘'} 分类 | {text!r} 期望={want_cat} 实际={got.get('category')!r}")
            print(f"{'✔' if amt_ok else '✘'} 金额 | {text!r} 期望={want_amt} 实际={got.get('amount')!r}")
        else:
            print(f"{'✔' if cat_ok else '✘'} 异常 | {text!r} → {got}")

    print(f"\n结果：{passed}/{total} 条用例全部通过（满分为理想值，不是今天的必须目标）")