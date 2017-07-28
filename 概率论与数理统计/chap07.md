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
    ```python {cmd:true, modify_source:true}
    import numpy as np
    x = np.array([74.001, 74.005, 74.003, 74.001, 74.000, 73.998, 74.006, 74.002])
    print(x.mean())
    print(x.std()**2)
    print(x.std(ddof=1)**2)
    ```
2.
    (1) 由题意计算可得
    $$
        \mu_1=\int_{-\infty}^{+\infty}x\theta c^\theta x^{-(\theta+1)}\text{d}x
        =\theta c^\theta \int_{c}^{+\infty}x^{-\theta}\text{d}x
        =\theta c^\theta \cdot\frac{x^{-\theta+1}}{-\theta+1}\Bigg|^{+\infty}_c
        =\frac{c\theta}{\theta-1},
    $$
    从而有
    $$
        \theta=\frac{\mu_1}{\mu_1-c}.
    $$
    在上式中以$\overline{X}$来代替$\mu_1$, 可得$\theta$的矩估计量与矩估计值
    $$
        \hat{\theta}=\frac{\overline{X}}{\overline{X}-c},\qquad
        \hat{\theta}=\frac{\overline{x}}{\overline{x}-c}.
    $$
    (2) 由题意计算可知
    $$
        \mu_1=\int_{-\infty}^{+\infty}x\sqrt{\theta}x^{\sqrt{\theta}-1}\text{d}x
        =\sqrt{\theta}\int_0^1x^{\sqrt{\theta}}\text{d}x
        =\frac{\sqrt{\theta}}{\sqrt{\theta}+1},
    $$
    于是解得
    $$
        \theta=\left(\frac{\mu_1}{\mu_1-1}\right)^2.
    $$
    在上式中以$\overline{X}$来代替$\mu_1$, 可得$\theta$的矩估计量与矩估计值
    $$
        \hat{\theta}=\left(\frac{\overline{X}}{\overline{X}-1}\right)^2,\qquad
        \hat{\theta}=\left(\frac{\overline{x}}{\overline{x}-1}\right)^2.
    $$
    (3) 因为$\mu_1=E(X)=mp$, 可得$p=\dfrac{\mu_1}{m}$, 以$\overline{X}$代替$\mu_1$可得
    $$
        \hat{p}=\frac{\overline{X}}{m},\qquad \hat{p}=\frac{\overline{x}}{m}.
    $$
3.
    (1) 考虑$x_1,x_2,\ldots,x_n$为一样本值, 则似然函数为
    $$
        L(\theta)=\prod_{i=1}^n\theta c^\theta x_i^{-(\theta+1)}
        =\theta^nc^{n\theta}\left(\prod_{i=1}^nx_i\right)^{-(\theta+1)},
    $$
    于是有
    $$
        \ln L(\theta)=n\ln \theta +n\theta\ln c-(\theta+1)\sum_{i=1}^n\ln x_i.
    $$
    令
    $$
        \frac{\text{d}}{\text{d}\theta}\ln L(\theta)=\frac{n}{\theta}+n\ln c
        -\sum_{i=1}^n\ln x_i=0,
    $$
    得
    $$
        \theta=\frac{n}{\sum\limits_{i=1}^n\ln x_i-n\ln c}.
    $$
    从而可知$\theta$的最大似然估计量为
    $$
        \hat{\theta}=\frac{n}{\sum\limits_{i=1}^n\ln X_i-n\ln c}.
    $$
    (2) 考虑一个样本值$x_1,x_2,\ldots,x_n$, 有似然函数
    $$
        L(\theta)=\prod_{i=1}^n\sqrt{\theta}x_i^{\sqrt{\theta}-1}
        =\theta^{\frac{n}{2}}\left(\prod_{i=1}^nx_i\right)^{\sqrt{\theta}-1}.
    $$
    于是有
    $$
        \ln L(\theta)=\frac{n}{2}\ln \theta+(\sqrt{\theta}-1)\sum_{i=1}^n\ln x_i,
    $$
    令
    $$
        \frac{\text{d}}{\text{d}\theta}\ln L(\theta)=\frac{n}{2\theta}
        +\frac{1}{2\sqrt{\theta}}\sum_{i=1}^n\ln x_i=0,
    $$
    得
    $$
        \theta=\frac{n^2}{\left(\sum\limits_{i=1}^n\ln x_i\right)^2}.
    $$
    从而可知$\theta$的最大似然估计量为
    $$
        \hat{\theta}=\frac{n^2}{\left(\sum\limits_{i=1}^n\ln X_i\right)^2}.
    $$
    (3) 考虑一个样本值$x_1,x_2,\ldots,x_n$, 有似然函数
    $$
        L(p)=\prod_{i=1}^n {m\choose x_i}p^{x_i}(1-p)^{m-x_i}
        =p^{\sum\limits_{i=1}^n x_i}(1-p)^{nm-\sum\limits_{i=1}^n x_i}
        \prod_{i=1}^n {m\choose x_i}.
    $$
    于是有
    $$
        \ln L(p)=\ln p\sum_{i=1}^n x_i+\left(nm-\sum_{i=1}^n x_i\right)\ln(1-p)
        +\ln \prod_{i=1}^n {m\choose x_i},
    $$
    令
    $$
        \frac{\text{d}}{\text{d}p}\ln L(p)=\frac1p\sum_{i=1}^n x_i
        +\frac{1}{p-1}\left(nm-\sum_{i=1}^n x_i\right)=0,
    $$
    得
    $$
        p=\frac{\sum\limits_{i=1}^n x_i}{nm}=\frac{\overline{x}}{m},
        \qquad \text{其中}\overline{x}=\frac{1}{n}\sum\limits_{i=1}^n x_i.
    $$
    从而可知$p$的最大似然估计量为
    $$
        \hat{p}=\frac{\overline{X}}{m}.
    $$
4.
5.
6. 因为
$$
    \overline{x}=\frac{1+2\times6+3\times7+4\times23+5\times26+6\times21+7\times12+8\times3+9}{100}=4.99,
$$
由前面的习题3(3)中的结论知$p$的最大似然估计值为
$$
    \hat{p}=\frac{4.99}{10}=0.499.
$$
    ```python {cmd:true, modify_source:true}
    print((1 + 2 * 6 + 3 * 7 + 4 * 23 + 5 * 26 + 6 * 21 + 7 * 12 + 8 * 3 + 9) / 100)
    ```
7.
8.
## 基于截尾样本的最大似然估计
## 估计量的评选标准
9.
10.
11.
    (1) 考虑一个样本值$x_1,x_2,\ldots,x_n$, 由题意可得似然函数
    $$
        L(\theta)=\prod_{i=1}^n \frac1\theta x_i^{(1-\theta)/\theta}
        =\frac{1}{\theta^n}\left(\prod_{i=1}^nx_i\right)^{(1-\theta)/\theta},
    $$
    于是有
    $$
        \ln L(\theta)=\frac{1-\theta}{\theta}\sum_{i=1}^n\ln x_i-n\ln\theta.
    $$
    令
    $$
        \frac{\text{d}}{\text{d}\theta}\ln L(\theta)=-\frac{1}{\theta^2}\sum_{i=1}^n\ln x_i-\frac n\theta=0,
    $$
    得
    $$
        \theta=-\frac1n\sum_{i=1}^n\ln x_i,
    $$
    从而得到$\theta$最大似然估计量是
    $$
        \hat{\theta}=-\frac1n\sum_{i=1}^n\ln X_i.
    $$
    (2) 由于
    $$
        E(\hat{\theta})=-\frac{1}{n}\sum_{i=1}^nE(\ln X_i),
    $$
    而
    $$
        E(\ln X)=\int_0^1\ln x\cdot \frac1\theta x^{(1-\theta)/\theta}\text{d}x
        =-\theta,
    $$
    所以有$E(\hat{\theta})=\theta$, 即$\hat{\theta}$是$\theta$的无偏估计量.
12.
13.
14.
15.
## 区间估计
16.
    (1) 首先取得样本均值$\overline{X}=6$, $\alpha=0.5$, 而
    $$
        \frac{\overline{X}-\mu}{\sigma/3}\sim N(0,1),
    $$
    那么按标准正态分布的上$\alpha$分位点的定义, 有
    $$
        P\left\{\left|\frac{\overline{X}-\mu}{\sigma/3}\right|<z_{0.025}\right\}
        =0.95,
    $$
    得到$z_{0.025}=1.96$, 于是有$\mu$的置信水平为$0.95$的置信区间为
    $$
        \left(\overline{X}\pm0.2\times 1.96\right),\quad \text{即}
        (5.608, 6.392).
    $$

    ```python {cmd:true}
    import numpy as np
    from scipy.stats import norm
    x = np.array([6.0, 5.7, 5.8, 6.5, 7.0, 6.3, 5.6, 6.1, 5.0])
    print(x.mean())
    print(norm.ppf((1 + 0.95) / 2))
    print(norm.ppf(1 - 0.025))
    ```
    (2) 首先得到样本标准差$S=0.5745$, $\alpha=0.5$, 而此时
    $$
        \frac{\overline{X}-\mu}{S/3}\sim t(8),
    $$
    那么我们有
    $$
        P\left\{\left|\frac{\overline{X}-\mu}{S/3}\right|<t_{0.025}(8)\right\}
        =0.95,
    $$
    至于$t_{0.025}(8)=2.306$, 于是得到$\mu$的置信水平为$0.95$的置信区间为
    $$
        \left(\overline{X}\pm \frac{S}{3}t_{0.025}(8)\right)\qquad
        \text{即} (5.558, 6.442).
    $$
    ```python {cmd:true}
    import numpy as np
    from scipy.stats import t
    x = np.array([6.0, 5.7, 5.8, 6.5, 7.0, 6.3, 5.6, 6.1, 5.0])
    print(x.std(ddof=1))
    print(t.ppf(1 - 0.025, 8))
    print(-t.ppf(0.025, 8))
    print('interval: ({}, {})'.format(6 - 0.5745 * 2.306 / 3, 6 + 0.5745 * 2.306 / 3))
    print(t.interval(0.95, df=8, loc=6, scale=x.std(ddof=1)/3))
    ```
## 正态总体均值与方差的区间估计
17.
18.
19.
20.
21.
22.
23.
## (0-1)分布参数的区间估计
24.
## 单侧置信区间
25.
26.
27.
