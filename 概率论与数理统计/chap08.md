---
html:
  embed_local_images: false
  embed_svg: true
  offline: false
export_on_save:
  html: true
---
# 假设检验
## 假设检验
## 正态总体均值的假设检验
1. 此题要求在$\alpha=0.01$下检验假设
$$
    H_0: \mu=0.25,\qquad H_1=\mu\neq 0.25.
$$
因为$\sigma^2$未知, 故采用$t$检验, 需取统计量$t=\dfrac{\overline{X}-\mu_0}{S/\sqrt{n}}$. 而题中$\alpha=0.01$, $n=5$, 可知$k=t_{0.005}=4.6041$. 又已知样本标准差$s=0.01303$, 样本均值$\overline{x}=3.252$, 那么由于
$$
    \frac{\overline{X}-\mu_0}{S/\sqrt{n}}\sim t(n-1),
$$
则
$$
    \left|\frac{\overline{x}-\mu_0}{s/\sqrt{n}}\right|=0.343<t_{0.005},
$$
从而可知在显著性水平$\alpha=0.01$下, 可接受原假设$H_0$.
    ```python {cmd=true, id="package"}
    import numpy as np
    from scipy.stats import norm
    from scipy.stats import t
    ```
    ```python {cmd=true, continue=true}
    print(-t.ppf(0.005, 4))
    x = np.array([3.25, 3.27, 3.24, 3.26, 3.24])
    print(x.mean())
    s = x.std(ddof=1)
    print(s)
    print((x.mean() - 3.25) / (s / 5 ** 0.5))
    ```
2.
3.
4.
5.
6. 由题中可知, 其总体$X\sim N(\mu_1, \sigma^2)$, $Y\sim N(\mu_2, \sigma^2)$且相互独立. 但由于$\sigma$未知, 故本题在显著水平$\alpha=0.01$下检验假设
$$
    H_0:\mu=\mu_2,\qquad H_1:\mu_1\neq\mu_2
$$
需采用t检验, 即取统计量
$$
    t=\frac{(\overline{X}-\overline{Y})-\delta}{S_w\sqrt{\dfrac{1}{n_1}+\dfrac{1}{n_2}}}.
$$
现从题中可知
$$
    n_1=8, \quad\overline{x}=0.2319,\quad s_1^2=0.0146^2,\quad
    n_2=10,\quad\overline{y}=0.2097,\quad s_2^2=0.009661^2,
$$
从而计算可得
$$
    s_w^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}=0.01205^2, \qquad
    t_{0.025}(16)=2.1199,
$$
另外注意到
$$
    t=\frac{\overline{x}-\overline{y}}{s_w\sqrt{\dfrac{1}{n_1}+\dfrac{1}{n_2}}}
    =3.878>t_{0.025}(16)
$$
落在拒绝域内, 故拒绝$H_0$, 也即认为两位作家所写的小品文中包含由3个字母组成的单字比例有显著的差异.
    ```python {cmd=true, continue="package"}
    x = np.array([0.225, 0.262, 0.217, 0.240, 0.230, 0.229, 0.235, 0.217])
    n1 = x.size
    x_bar = x.mean()
    sx = x.std(ddof=1)
    print(x_bar, sx)    
    y = np.array([0.209, 0.205, 0.196, 0.210, 0.202, 0.207, 0.224, 0.223, 0.220, 0.201])
    n2 = y.size
    y_bar = y.mean()
    sy = y.std(ddof=1)
    print(y_bar, sy)
    sw2 = ((n1 - 1) * sx ** 2 + (n2 - 1) * sy ** 2) / (n1 + n2 -2)
    sw = sw2 ** 0.5
    print(sw2, sw)
    print(-t.ppf(0.025, n1 + n2 - 2))
    print((x_bar - y_bar) / sw / (1 / n1 + 1 / n2) ** 0.5)
    ```
7.
8.
9.
10.
## 正态总体方差的假设检验
11.
## 置信区间与假设检验之间的关系
## 样本容量的选取
## 分布拟合检验
## 秩和检验
