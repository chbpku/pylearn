# 准备测试数据
from time import sleep
from faker import Faker
f = Faker("en-us")
alist = [f.name() for _ in range(50)]

# 导入tqdm模块
from tqdm.gui import tqdm
s = ""
for name in tqdm(alist):
    s += f"{name=} "  # 假装处理一下
    sleep(0.05)
print(s)
