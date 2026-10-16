# migrate.py —— 一次性迁移：给旧账补 id / created_at
# 用途：只跑一次；跑完保留在仓库里作为历史记录
# 幂等保证：只补不覆盖（缺了才补）
import os
import uuid
from datetime import datetime

from storage import expenses_path, load_expenses, save_expenses


def migrate(records, file_mtime):
    for rec in records:
        if "id" not in rec:                    # 幂等关卡
            rec["id"] = uuid.uuid4().hex[:8]
        if "created_at" not in rec:
            rec["created_at"] = file_mtime         
    return records

if __name__ == "__main__":
    mtime = datetime.fromtimestamp(os.path.getmtime(expenses_path())).isoformat(timespec="seconds")
    print("文件最后写入时间：" , mtime)
    records = load_expenses()
    print(f"迁移前：{len(records)} 笔")
    records = migrate(records, mtime)
    save_expenses(records)
    print("迁移完成")