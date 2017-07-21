---
html:
  embed_local_images: false
  embed_svg: true
  offline: false
export_on_save:
  html: true
---
# 大数定理及中心极限定理
## 大数定理
## 中心极限定理
1. 以$X_i(i=1,2,\ldots,16)$表示第$i$个电器元件的寿命, 以$X$记为16个电器元件的寿命总和. 由题设可知$E(X_i)=100$, $D(X_i)=10000$, 从而由中心极限定理可知
$$\begin{aligned}
    P\{X>1920\}&=P\left\{\frac{X-16\cdot 100}{4\cdot 100 }>\frac{1920-16\cdot 100}{4\cdot 100 }\right\}\\
    &=1-P\left\{\frac{X-16\cdot 100}{4\cdot 100 }\leqslant0.8\right\}\\
    &=1-\varPhi(0.8)=0.2119.
\end{aligned}$$
    ```python {cmd:true}
    (1920 - 16 * 100) / 400
    print((1920 - 16 * 100) / 400)
    from scipy import stats
    print(1 - stats.norm.cdf(0.8))
    ```
2.
3.
4.
5.
6. 分别以$X_i$, $Y_i(i=1,2,\ldots,20)$记为20台机器第一阶段和第二阶段的修理时间,
以$Z=\sum_{i=1}^{20}(X_i+Y_i)$记为修理时间总和. 由题意可知$E(X_i)=0.2$, $D(X_i)=0.2^2$, $E(Y_i)=0.3$, $D(Y_i)=0.3^2$, 从而有
$$\begin{gather*}
    E(X_i+Y_i)=E(X_i)+E(Y_i)=0.5,\\
    D(X_i+Y_i)=D(X_i)+E(Y_i)=0.2^2+0.3^2,
\end{gather*}$$
以及
$$\begin{aligned}
    P\{Z<8\}&=P\left\{\frac{Z-20\cdot 0.5}{\sqrt{20\cdot(0.2^2+0.3^2)}}<\frac{8-20\cdot 0.5}{\sqrt{20\cdot(0.2^2+0.3^2)}}\right\}\\
    &=\varPhi(-1.24)=0.1075.
\end{aligned}$$
    ```python {cmd:true}
    print((8 - 20 * 0.5) / (20 * (0.2 ** 2 + 0.3 ** 2)) ** 0.5)
    from scipy import stats
    print(stats.norm.cdf(-1.24))
    ```
7.
8.
9.
10.
11.
    (1) 由中心极限定理可知$\overline{X}$近似服从$N(5, 0.3/80)$, 故
    $$\begin{aligned}
        P\{4.9<\overline{X}<5.1\}&=P\{\overline{X}<5.1\}-P\{\overline{X}<4.9\}\\
        &=P\left\{\color{red}{\frac{\overline{X}-5}{\sqrt{0.3/80}}}<\frac{5.1- 5}{\sqrt{0.3/80}}\right\}-P\left\{\frac{\overline{X}-5}{\sqrt{0.3/80}}<\frac{4.9- 5}{\sqrt{0.3/80}}\right\}\\
        &=\varPhi(1.63)-\varPhi(-1.63)=2\varPhi(1.63)-1=0.8969.
    \end{aligned}$$
    ```python {cmd:true}
    print((5.1 - 5) / (0.3 / 80) ** 0.5)
    print((4.9 - 5) / (0.3 / 80) ** 0.5)
    from scipy import stats
    print(stats.norm.cdf(1.63) * 2 - 1)
    ```
    (2) 由题意可知
    $$\begin{gather*}
        E(\overline{X})=E(\overline{Y})=5,\qquad D(\overline{X})=D(\overline{Y})=\frac{0.3}{80},\\
        E(\overline{X}-\overline{Y})=0,\qquad
        D(\overline{X}-\overline{Y})=\frac{0.3}{40},
    \end{gather*}$$
    从而$\overline{X}-\overline{Y}$近似服从$N(0,0.3/40)$, 于是就有
    $$\begin{aligned}
        P\{-0.1<\overline{X}-\overline{Y}<0.1\}&=P\left\{\frac{-0.1-0}{\sqrt{0.3/40}}<\frac{\overline{X}-\overline{Y}-0}{\sqrt{0.3/40}}<\frac{0.1-0}{\sqrt{0.3/40}}\right\}\\
        &=2\varPhi(1.155)-1=0.7519.
    \end{aligned}$$
    ```python {cmd:true}
    print(0.1 / (0.3 / 40) ** 0.5)
    from scipy import stats
    print(stats.norm.cdf(1.155) * 2 - 1)
    ```
12.
13.
14.
