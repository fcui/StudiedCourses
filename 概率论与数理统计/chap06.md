---
html:
  embed_local_images: false
  embed_svg: true
  offline: false
export_on_save:
  html: true
---
# 样本及抽样分布
## 随机样本
## 直方图和箱线图
## 抽样分布
1. 样本均值$\overline{X}$服从分布$N(52, 6.3^2/36)$, 那么可知
$$\begin{aligned}
    P\{50.8<\overline{X}<53.8\}&=P\left\{\frac{50.8-52}{6.3/6}
        <\frac{\overline{X}-52}{6.3/6}<\frac{53.8-52}{6.3/6}\right\}\\
    &=\varPhi(1.714)-\varPhi(-1.143)=0.8302.
\end{aligned}$$
    ```python {cmd:true, modify_source:true}
    print((53.8 - 52) / (6.3 / 6))
    print((50.8 - 52) / (6.3 / 6))
    from scipy.stats import norm
    print(norm.cdf(1.714) - norm.cdf(-1.143))
    ```
2.
3.
4.
5.
6.
    (1) (**Mark**)由题设可知, $X_i(i=1,2,\ldots,n)$相互独立, 且$X_i\sim b(1,p)$, $P\{X_i=x_i\}=p^{x_i}(1-p)^{1-x_i}$, 其中$x_i=0,1$. 于是得到
    $$\begin{aligned}
        P\{X_1=x_1, X_2=x_2,\ldots, X_n=x_n\}&=\prod_{i=1}^nP\{X_i=x_i\}
        =\prod_{i=1}^n p^{x_i}(1-p)^{1-x_i}\\
        &=p^{\sum_{i=1}^nx_i}(1-p)^{n-\sum_{i=1}^nx_i}.
    \end{aligned}$$
    (2) (**Mark**)因为$X_i(i=1,2,\ldots,n)$相互独立, 且$X_i\sim b(1,p)$, 故$\sum\limits_{i=1}^nX_i\sim b(n,p)$, 所以其分布律为
    $$
        P\left\{\sum_{i=1}^nX_i=k\right\}={n\choose k}p^k(1-p)^{1-k}, \qquad
        k=0,1,\ldots,n.
    $$
    (3) 由第四章第2节例6可知
    $$
        E(\overline{X})=p,\quad D(\overline{X})=\frac{p(1-p)}{n}, \quad
        E(S^2)=p(1-p).
    $$
7.
8.
9.
10.
    (1) 频率直方图如下:
    ```python {cmd: true, matplotlib: true, modify_source:true}
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.figure(figsize=(5, 4))
    x = np.array([225, 232, 232, 245, 235, 245, 270, 225, 240, 240,
                  217, 195, 225, 185, 200, 220, 200, 210, 271, 240,
                  220, 230, 215, 252, 225, 220, 206, 185, 227, 236])
    plt.hist(x, bins=5, range=(179.5, 279.5))
    plt.show()
    ```
    (2) 箱线图如下:
    ```python {cmd: true, matplotlib: true, modify_source:true}
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.figure(figsize=(5, 4))
    x = np.array([225, 232, 232, 245, 235, 245, 270, 225, 240, 240,
                  217, 195, 225, 185, 200, 220, 200, 210, 271, 240,
                  220, 230, 215, 252, 225, 220, 206, 185, 227, 236])
    plt.boxplot(x)
    plt.show()
    ```
11. 上题中30个数据的$\alpha=0.2$的截尾均值为$226.33$.
    ```python {cmd:true, modify_source:true}
    import numpy as np
    import math
    x = np.array([225, 232, 232, 245, 235, 245, 270, 225, 240, 240,
                  217, 195, 225, 185, 200, 220, 200, 210, 271, 240,
                  220, 230, 215, 252, 225, 220, 206, 185, 227, 236])
    num = math.floor(30 * 0.2)
    x_alpha = np.sort(x)[num : -num]
    print('origin data: ', np.sort(x))
    print('sorted data: ', x_alpha)
    print('mean: ', x_alpha.mean())
    ```
