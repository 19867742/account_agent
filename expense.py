# expense.py

import re

# ---------- 可照抄区：分类表 ----------
# 结构：分类 -> 关键词列表。想加词，只改这里，不用碰下面的逻辑。
# 注意：列表里请把"更长/更具体"的词写在前面（例："自助餐" 要写在 "餐" 前面）
CATEGORY_KEYWORDS = {
    "餐饮": ["午饭", "晚饭", "早饭", "早餐", "晚餐", "外卖", "食堂", "奶茶", "饭"],
    "交通": ["打车", "地铁", "公交", "高铁", "加油"],
    "购物": ["买书", "买衣服", "超市", "快递"],
}


# ---------- 填空区 1：金额 ----------
def parse_amount(text):
    """从一句话里提取金额。返回 float；找不到就返回 None。
    契约：调用方必须判断 None。
    """
    m = re.search(r"\d+(?:\.\d+)?", text)
    # 洞 1：用 re.search 匹配数字（支持小数），提示 r"\d+(?:\.\d+)?"
    if m is not None:
        m = None
    # 洞 2：如果没匹配到 → return None
    return float(m.group())
    # 洞 3：匹配到了 → return float(...)，注意要用 .group() 取文本


# ---------- 填空区 2：分类 ----------
def match_category(text):
    """返回分类名，匹配不到返回 '其他'。"""
    for category, keywords in CATEGORY_KEYWORDS.items():
        for word in keywords:
            if word in text:
                return category
    return "其他"


# ---------- 组装（这段我写好，你只需读懂） ----------
def parse_expense(text):
    amount = parse_amount(text)
    if amount is None:
        raise ValueError(f"没找到金额：{text!r}")
    # 洞 5：金额缺失时怎么办？按你选的契约处理（返回 None 键 / 抛错 / 归 0）
    category = match_category(text)
    return {"amount": amount, "category": category}