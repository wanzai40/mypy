import os
import time

# 在这里改成你要处理的文件夹路径
folder = r"C:\Users\wz\Desktop\vs test\c"

# 获取所有文件（不含子文件夹）
files = []
for name in os.listdir(folder):
    path = os.path.join(folder, name)
    if os.path.isfile(path):
        files.append(path)

# 按 修改时间 从远到近排序
files.sort(key=lambda x: os.path.getmtime(x))

# 重命名：1_xxx、2_xxx、3_xxx...
for i, path in enumerate(files, start=1):
    dirname = os.path.dirname(path)
    filename = os.path.basename(path)
    new_name = f"{i}_{filename}"
    new_path = os.path.join(dirname, new_name)
    os.rename(path, new_path)

print("重命名完成！")
