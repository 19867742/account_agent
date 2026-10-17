# account-agent
这是一个可以记录自己的资金流动的应用，给自己记的、命令行版记账本，不联网、数据只在本机

## 现在能做什么
- 1.记录数据
'''py main.py add "午饭 15"已记账：
 {'id': '3ed045dc', 'created_at': '2026-10-17T19:02:59', 'amount': 15.0, 'category': '餐饮'}
'''
- 2.打印数据
'''
py main.py list
3b0cd39a 餐饮  25.0
ffc67422 交通  18.5
1f832db4 购物  120.0
ed21609f 餐饮  6.6
bc9f6df8 交通  3.0
f5aaba4a 餐饮  6.6
d58d9499 其他  3.0
96f4ec5a 其他  3.0
'''
- 3.删除数据
'''
用法：py main.py remove 3b0cd39a    （id 从 list 结果的第一列复制）
已删除 1 笔，剩余 7 笔
'''

## 怎么跑起来
1. 装 Python 3.10+（python.org，安装时勾选 Add Python to PATH）
2. 拿到代码：'''git clone'''
'''https://github.com/19867742/account_agent.git'''
9. 进入目录：'''cd account_agent'''
13. 试一下：'''py main.py list'''

本项目只用 Python 标准库，不需要 pip install。

## 项目结构

- `main.py` —— 命令行入口，只管分发命令
- `expense.py` —— 把一句话解析成一条记录
- `storage.py` —— 读写 expenses.json
- `migrate.py` —— 一次性脚本，给旧账本补 id 和时间
- `test_expense.py` —— 测试用例


## 已知限制
- 1.分类靠关键词表，“可乐”会被归到“其他”，不认识自然语言
- 2.'''-12 退款 → 记成 12.0（负号丢失）'''
- 3.'''1,200 房租 → 记成 1.0（千分位逗号）'''
- 4.只能在命令行用，需要 Python 3.10+，数据存在本地单文件


## 为什么写这个
现成的记账 App 为什么不用？因为自己写，才知道钱花在哪；顺便把 Python 练一遍
