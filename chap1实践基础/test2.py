import matplotlib.pyplot as plt
import numpy as np

# 假设在x轴上12个点是均匀分布的
reconstruction_error = np.linspace(0.0, 0.06, 12)

# 用从图中估计出的数据替换这些列表
ours_estimated = [24, 23, 12, 6, 3, 2, 1, 0.5, 0.3, 0.2, 0.1, 0.05]
apss_estimated = [8, 7, 6, 5, 4, 3, 2, 1.5, 1, 0.7, 0.5, 0.3]
rimls_estimated = [20, 18, 10, 5, 3.5, 2.5, 1.5, 1, 0.6, 0.4, 0.2, 0.1]
poisson_estimated = [15, 14, 8, 4, 3, 2, 1.3, 0.8, 0.6, 0.4, 0.2, 0.1]

# 绘制估计数据
plt.figure(figsize=(8, 6))
plt.plot(reconstruction_error, ours_estimated, 'b-o', label='Ours')
plt.plot(reconstruction_error, apss_estimated, 'r-o', label='APSS')
plt.plot(reconstruction_error, rimls_estimated, 'k-^', label='RIMLS')
plt.plot(reconstruction_error, poisson_estimated, 'g-s', label='Poisson')

# 添加图形标题和标签
plt.title('重建错误比较')
plt.xlabel('重建错误')
plt.ylabel('百分比')
plt.legend()
plt.grid(True)

# 显示图形
plt.show()
