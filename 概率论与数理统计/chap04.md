---
html:
  embed_local_images: false
  embed_svg: true
  offline: false
export_on_save:
  html: true
---
# 随机变量的数字特征
## 数学期望
1.
    (1) 以$X$表示取到的单词所包含的字母个数, 则其分布律为
    $$
		\begin{array}{c|cccc}
			\hline
			X&2&3&4&9\\
			\hline
			p_k&\frac{1}{8}&\frac{5}{8}&\frac{1}{8}&\frac{1}{8}\\
			\hline
		\end{array}
	$$
	则期望$E(X)=\dfrac{15}{4}=3.75$.
    (2) 以$Y$表示取到的字母所在单词所包含的字母数, 则其分布律为
        $$
		\begin{array}{c|cccc}
			\hline
			Y&2&3&4&9\\
			\hline
			p_k&\frac{1}{15}&\frac{1}{2}&\frac{2}{15}&\frac{3}{10}\\
			\hline
		\end{array}
        $$
	则期望$E(Y)=\dfrac{73}{15}=4.87$.
    (3) 得到分布律为
    $$
		\begin{array}{c|ccccccccccc}
			\hline
			X&1&2&3&4&5&7&8&9&10&11&12\\
			\hline
			p_k&\frac{1}{6}&\frac{1}{6}&\frac{1}{6}&\frac{1}{6}&\frac{1}{6}
			&\frac{1}{36}&\frac{1}{36}&\frac{1}{36}&\frac{1}{36}&\frac{1}{36}&\frac{1}{36}\\
			\hline
		\end{array}
    $$
	则期望$E(X)=\dfrac{49}{12}=4.08$.
2.
3.
4.
5.
6.
    (1) 容易计算得到
    $$
    \begin{gather*}
		E(X)=(-2)\times 0.4+0\times 0.3+2\times 0.3=-0.2,\\
		E(X^2)=(-2)^2\times 0.4+0^2\times 0.3+2^2\times 0.3=2.8,\\
		E(3X^2+5)=17\times 0.4+5\times 0.3+17\times 0.3=13.4,\\
		\color{red}{{E(3X^2+5)=3E(X^2)+5=13.4}}.
    \end{gather*}
    $$
    (2) 因为$X\sim\pi(\lambda)$, 即
	$$
		P\{X=k\}=\frac{\lambda^k\text{e}^{-\lambda}}{k!},\quad k=0,1,2,\ldots.
	$$
	于是有
	$$
		E[1/(X+1)]=\sum_{k=0}^\infty \frac{1}{k+1}\cdot\frac{\lambda^k\text{e}^{-\lambda}}{k!}
		=\frac{\text{e}^{-\lambda}}{\lambda}\sum_{k=0}^\infty \frac{\lambda^{k+1}}{(k+1)!}
		=\frac{\text{e}^{-\lambda}}{\lambda}\left(\text{e}^\lambda-1\right)=\frac{1-\text{e}^{-\lambda}}{\lambda}.
	$$
7.
8.
9.
10.
11. 因为使用寿命小于1年的概率为
$$
    P\{X\leqslant 1\}=\int_0^1\frac{1}{4}\text{e}^{-x/4}\text{d} x=1-\text{e}^{-1/4},
$$
则$P\{X>1\}=\text{e}^{-1/4}$. 于是赢利的数学期望为
$$
    100\times\text{e}^{-1/4}-\color{red}{200}\times(1-\text{e}^{-1/4})=33.6402.
$$
12.
13.
14.
15.
16.
    (1) 写出分布律
    $$
		\begin{array}{c|cccc}
			\hline
			X & 1 & 2 & \cdots &n\\
			\hline
			p_k & \frac{1}{n} & \frac{n-1}{n}\cdot\frac{1}{n-1} & \cdots &\frac{1}{n}\\
			\hline
		\end{array}
	$$
	所以期望是
	$$
		E(X)=\sum_{i=1}^{n}i\cdot \frac{1}{n}=\frac{n+1}{2}.
	$$
    (2) (**Mark**)如果不写出$X$分布律, 这时可假设有随机变量
    $$
		\begin{aligned}
			X_1&=1,\\
			X_k&=
			\begin{cases}
				1, &\textrm{前}k-1\textrm{次均未找到合适的钥匙};\\
				0, &\textrm{前}k-1\textrm{次中有一次试开成功}.
			\end{cases}
			\qquad k=2,3,\ldots,n.
		\end{aligned}
    $$
		那么$E(X_1)=1$, 同时对于$k=2,3,\ldots, n$可以求得
        $$
			\begin{gather*}
			P\{X_k=1\}=\frac{n-1}{n}\cdot\frac{n-2}{n-1}\cdots\frac{n-(k-1)}{n-k}=\frac{n-k+1}{n},\\
			E(X_k)=1\cdot P\{X_k=1\}+0\cdot P\{X_k=0\}=\frac{n-k+1}{n}.
			\end{gather*}
        $$
		于是最后我们有
		$$
			E(X)=1+\sum_{k=2}^nE(X_k)=1+\sum_{k=2}^n \frac{n-k+1}{n}=\frac{n+1}{2}.
		$$

## 方差
21. 求得期望
$$
    E(X)=\sum_{k=1}^{\infty}k\cdot p(1-p)^{k-1}=p\sum_{k=1}^{\infty}k(1-p)^{k-1}=\frac{1}{p},
$$
而方差
$$
\begin{gather*}
    E(X^2)=\sum_{k=1}^{\infty}k^2\cdot p(1-p)^{k-1}=p\sum_{k=1}^{\infty}k^2\cdot (1-p)^{k-1}
    =p\cdot\frac{2-p}{p^3}=\frac{2-p}{p^2},\\
    D(X)=E(X^2)-[E(X)]^2=\frac{1-p}{p^2}.
\end{gather*}
$$
22.
23.
24.
25.
## 协方差及相关系数
26.
	(1) 容易知道,
$$
	\begin{aligned}
		P\{X_1=2,X_2=2,X_3=5\}&=P\{X_1=2\}\cdot P\{X_2=2\}\cdot P\{X_3=5\}\\
		&= {4 \choose 2}\left(\frac{1}{2}\right)^2\left(\frac{1}{2}\right)^2
		\cdot {6\choose 2}\left(\frac{1}{3}\right)^2\left(\frac{2}{3}\right)^4
		\cdot {6\choose 5}\left(\frac{1}{3}\right)^5\left(\frac{2}{3}\right)\\
		&= 0.002032,
	\end{aligned}
$$
	$$\begin{gather*}
		E(X_1X_2X_2X_3)=E(X_1)E(X_2)E(X_3)=2\cdot 2\cdot 2=8,\\
		E(X_1-X_2)=2-2=0,\\
		E(X_1-2X_2)=2-2\cdot 2=-2.
	\end{gather*}$$
	(2)
		(i) $X$与$Y$相互独立, 则
		$$\begin{gather*}
			E(Z)=E(5X-Y+15)=5\cdot 3-1+15=29,\\
			D(Z)=D(5X-Y+15)=\color{red}{D(5X)+D(-Y)}=5^2\cdot 4+9+0=109.
		\end{gather*}$$
		(ii) 若$X$与$Y$不相关, 则
		$$\begin{gather*}
			E(Z)=E(5X-Y+15)=5\cdot 3-1+15=29,\\
			D(Z)=D(5X-Y+15)=D(5X-Y)=109.
		\end{gather*}$$
		(iii) 若$X$与$Y$相关系数为0.25, 则注意到$\color{red}{\text{Cov}(X,Y)=\sqrt{D(x)}\cdot\sqrt{D(Y)}\cdot\rho_{XY}}=2\cdot 3\cdot 0.25=1.5$, 从而有
		$$\begin{aligned}
			D(Z)&=D(5X-Y+15)=D(5X-Y)\\
			&=D(5X)+D(-Y)+2E\{(5X-E(5X))(-Y-E(-Y))\}\\
			&=D(5X)+D(-Y)+2\cdot (-5)\cdot E\{(X-E(X))(Y-E(Y))\}\\
			&=5^2\cdot 4+9-10\cdot 1.5=94.
		\end{aligned}$$
27.
28.
29.
30.
31. 注意到$x$和$y$的非零区域, 则可以得到
$$\begin{gather*}
    E(X)=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}x\cdot 1\text{d}x\text{d}y=\int_0^1x\text{d}x\int_{-x}^{x}\text{d}y=\frac23,\\
	E(Y)=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}y\cdot 1\text{d}x\text{d}y=\int_0^1\text{d}x\int_{-x}^{x}y\text{d}y=0,\\
	E(XY)=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}xy\text{d}x\text{d}y=\int_0^1x\text{d}x\int_{-x}^{x}y\text{d}y=0,\\
	\text{Cov}(X,Y)=E(X)E(Y)-E(XY)=0.
\end{gather*}$$
32.
33.
34.
35.
36. 由切比雪夫不等式可知
$$
    P\{|X-7300|\geqslant \varepsilon\}\leqslant \frac{700^2}{\varepsilon^2},
$$
故有
$$
    P\{|X-7300|< 2100\}\geqslant 1- \frac{700^2}{2100^2}=0.8889.
$$
37.
38.
## 矩、协方差矩阵
