# migrate.py —— 一次性迁移：给旧账补 id / created_at
# 用途：只跑一次；跑完保留在仓库里作为历史记录
# 幂等保证：只补不覆盖（缺了才补）
import json, os, uuid
from datetime import datetime

PATH = os.path.join(os.path.dirname(__file__), "expenses.json")

def load():
    with open(PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save(records):
    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

def migrate(records, file_mtime):
    for rec in records:
        if "id" not in rec:                    # 幂等关卡
            rec["id"] = uuid.uuid4().hex[:8]
        if "created_at" not in rec:
            rec["created_at"] = file_mtime            # 洞 3：用 file_mtime，还是现在？
    return records

if __name__ == "__main__":
    mtime = datetime.fromtimestamp(os.path.getmtime(PATH)).isoformat(timespec="seconds")
    print("文件最后写入时间：" , mtime)
    records = load()
    print(f"迁移前：{len(records)} 笔")
    records = migrate(records, mtime)
    save(records)
    print("迁移完成")