---
html:
  embed_local_images: false
  embed_svg: true
  offline: false
export_on_save:
  html: true
---
# 参数估计
## 点估计
1. 计算总体均值$\mu$及方差$\delta^2$的矩估计值的公式为
$$
    \hat{\mu}=\overline{x}=\frac1n\sum_{i=1}^nx_i,\qquad
    \hat{\delta^2}=\frac1n\sum_{i=1}^n(x_i-\overline{x})^2,
$$
故得$\hat{\mu}=74.002$, $\hat{\delta^2}=6.000\times 10^{-6}$. 由于样本方差的公式为
$$
    s^2=\frac{1}{n-1}\sum_{i=1}^n(x_i-\overline{x})^2,
$$
故有$s^2=6.8571\times 10^{-6}$.
    ```python {cmd:true}
    import numpy as np
    x = np.array([74.001, 74.005, 74.003, 74.001, 74.000, 73.998, 74.006, 74.002])
    print(x.mean())
    print(x.std()**2)
    print(x.std(ddof=1)**2)
    ```
2.
3.
4.
5.
6.
## 基于截尾样本的最大似然估计
## 估计量的评选标准
## 区间估计
## 正态总体均值与方差的区间估计
## (0-1)分布参数的区间估计
## 单侧置信区间
