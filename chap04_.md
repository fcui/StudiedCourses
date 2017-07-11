<h1  id="随机变量的数字特征">随机变量的数字特征</h1>
<h2  id="数学期望">数学期望</h2>
1.
    (1) 以<img src="https://latex.codecogs.com/gif.latex?X"/>表示取到的单词所包含的字母个数, 则其分布律为
    <p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{array}{c|cccc}			&#x5C;hline			X&amp;2&amp;3&amp;4&amp;9&#x5C;&#x5C;			&#x5C;hline			p_k&amp;&#x5C;frac{1}{8}&amp;&#x5C;frac{5}{8}&amp;&#x5C;frac{1}{8}&amp;&#x5C;frac{1}{8}&#x5C;&#x5C;			&#x5C;hline		&#x5C;end{array}"/></p>
	则期望<img src="https://latex.codecogs.com/gif.latex?E(X)=&#x5C;dfrac{15}{4}=3.75"/>.
    (2) 以<img src="https://latex.codecogs.com/gif.latex?Y"/>表示取到的字母所在单词所包含的字母数, 则其分布律为
        <p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{array}{c|cccc}			&#x5C;hline			Y&amp;2&amp;3&amp;4&amp;9&#x5C;&#x5C;			&#x5C;hline			p_k&amp;&#x5C;frac{1}{15}&amp;&#x5C;frac{1}{2}&amp;&#x5C;frac{2}{15}&amp;&#x5C;frac{3}{10}&#x5C;&#x5C;			&#x5C;hline		&#x5C;end{array}"/></p>
	则期望<img src="https://latex.codecogs.com/gif.latex?E(Y)=&#x5C;dfrac{73}{15}=4.87"/>.
    (3) 得到分布律为
    <p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{array}{c|ccccccccccc}			&#x5C;hline			X&amp;1&amp;2&amp;3&amp;4&amp;5&amp;7&amp;8&amp;9&amp;10&amp;11&amp;12&#x5C;&#x5C;			&#x5C;hline			p_k&amp;&#x5C;frac{1}{6}&amp;&#x5C;frac{1}{6}&amp;&#x5C;frac{1}{6}&amp;&#x5C;frac{1}{6}&amp;&#x5C;frac{1}{6}			&amp;&#x5C;frac{1}{36}&amp;&#x5C;frac{1}{36}&amp;&#x5C;frac{1}{36}&amp;&#x5C;frac{1}{36}&amp;&#x5C;frac{1}{36}&amp;&#x5C;frac{1}{36}&#x5C;&#x5C;			&#x5C;hline		&#x5C;end{array}"/></p>
	则期望<img src="https://latex.codecogs.com/gif.latex?E(X)=&#x5C;dfrac{49}{12}=4.08"/>.
2.
3.
4.
5.
6.
    (1) 容易计算得到
    <p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{gather*}		E(X)=(-2)&#x5C;times 0.4+0&#x5C;times 0.3+2&#x5C;times 0.3=-0.2,&#x5C;&#x5C;		E(X^2)=(-2)^2&#x5C;times 0.4+0^2&#x5C;times 0.3+2^2&#x5C;times 0.3=2.8,&#x5C;&#x5C;		E(3X^2+5)=17&#x5C;times 0.4+5&#x5C;times 0.3+17&#x5C;times 0.3=13.4,&#x5C;&#x5C;		&#x5C;color{red}{{E(3X^2+5)=3E(X^2)+5=13.4}}.    &#x5C;end{gather*}"/></p>
    (2) 因为<img src="https://latex.codecogs.com/gif.latex?X&#x5C;sim&#x5C;pi(&#x5C;lambda)"/>, 即
	<p align="center"><img src="https://latex.codecogs.com/gif.latex?P&#x5C;{X=k&#x5C;}=&#x5C;frac{&#x5C;lambda^k&#x5C;text{e}^{-&#x5C;lambda}}{k!},&#x5C;quad k=0,1,2,&#x5C;ldots."/></p>
	于是有
	<p align="center"><img src="https://latex.codecogs.com/gif.latex?E[1&#x2F;(X+1)]=&#x5C;sum_{k=0}^&#x5C;infty &#x5C;frac{1}{k+1}&#x5C;cdot&#x5C;frac{&#x5C;lambda^k&#x5C;text{e}^{-&#x5C;lambda}}{k!}		=&#x5C;frac{&#x5C;text{e}^{-&#x5C;lambda}}{&#x5C;lambda}&#x5C;sum_{k=0}^&#x5C;infty &#x5C;frac{&#x5C;lambda^{k+1}}{(k+1)!}		=&#x5C;frac{&#x5C;text{e}^{-&#x5C;lambda}}{&#x5C;lambda}&#x5C;left(&#x5C;text{e}^&#x5C;lambda-1&#x5C;right)=&#x5C;frac{1-&#x5C;text{e}^{-&#x5C;lambda}}{&#x5C;lambda}."/></p>
7.
8.
9.
10.
11. 因为使用寿命小于1年的概率为
<p align="center"><img src="https://latex.codecogs.com/gif.latex?P&#x5C;{X&#x5C;leqslant 1&#x5C;}=&#x5C;int_0^1&#x5C;frac{1}{4}&#x5C;text{e}^{-x&#x2F;4}&#x5C;text{d} x=1-&#x5C;text{e}^{-1&#x2F;4},"/></p>
则<img src="https://latex.codecogs.com/gif.latex?P&#x5C;{X&gt;1&#x5C;}=&#x5C;text{e}^{-1&#x2F;4}"/>. 于是赢利的数学期望为
<p align="center"><img src="https://latex.codecogs.com/gif.latex?100&#x5C;times&#x5C;text{e}^{-1&#x2F;4}-&#x5C;color{red}{200}&#x5C;times(1-&#x5C;text{e}^{-1&#x2F;4})=33.6402."/></p>
12.
13.
14.
15.
16.
    (1) 写出分布律
    <p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{array}{c|cccc}			&#x5C;hline			X &amp; 1 &amp; 2 &amp; &#x5C;cdots &amp;n&#x5C;&#x5C;			&#x5C;hline			p_k &amp; &#x5C;frac{1}{n} &amp; &#x5C;frac{n-1}{n}&#x5C;cdot&#x5C;frac{1}{n-1} &amp; &#x5C;cdots &amp;&#x5C;frac{1}{n}&#x5C;&#x5C;			&#x5C;hline		&#x5C;end{array}"/></p>
	所以期望是
	<p align="center"><img src="https://latex.codecogs.com/gif.latex?E(X)=&#x5C;sum_{i=1}^{n}i&#x5C;cdot &#x5C;frac{1}{n}=&#x5C;frac{n+1}{2}."/></p>
    (2) (Mark)如果不写出<img src="https://latex.codecogs.com/gif.latex?X"/>分布律, 这时可假设有随机变量
    <p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}			X_1&amp;=1,&#x5C;&#x5C;			X_k&amp;=			&#x5C;begin{cases}				1, &amp;&#x5C;textrm{前}k-1&#x5C;textrm{次均未找到合适的钥匙};&#x5C;&#x5C;				0, &amp;&#x5C;textrm{前}k-1&#x5C;textrm{次中有一次试开成功}.			&#x5C;end{cases}			&#x5C;qquad k=2,3,&#x5C;ldots,n.		&#x5C;end{aligned}"/></p>
		那么<img src="https://latex.codecogs.com/gif.latex?E(X_1)=1"/>, 同时对于<img src="https://latex.codecogs.com/gif.latex?k=2,3,&#x5C;ldots, n"/>可以求得
        <p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{gather*}			P&#x5C;{X_k=1&#x5C;}=&#x5C;frac{n-1}{n}&#x5C;cdot&#x5C;frac{n-2}{n-1}&#x5C;cdots&#x5C;frac{n-(k-1)}{n-k}=&#x5C;frac{n-k+1}{n},&#x5C;&#x5C;			E(X_k)=1&#x5C;cdot P&#x5C;{X_k=1&#x5C;}+0&#x5C;cdot P&#x5C;{X_k=0&#x5C;}=&#x5C;frac{n-k+1}{n}.			&#x5C;end{gather*}"/></p>
		于是最后我们有
		<p align="center"><img src="https://latex.codecogs.com/gif.latex?E(X)=1+&#x5C;sum_{k=2}^nE(X_k)=1+&#x5C;sum_{k=2}^n &#x5C;frac{n-k+1}{n}=&#x5C;frac{n+1}{2}."/></p>
  
<h2  id="方差">方差</h2>
21. 求得期望
<p align="center"><img src="https://latex.codecogs.com/gif.latex?E(X)=&#x5C;sum_{k=1}^{&#x5C;infty}k&#x5C;cdot p(1-p)^{k-1}=p&#x5C;sum_{k=1}^{&#x5C;infty}k(1-p)^{k-1}=&#x5C;frac{1}{p},"/></p>
而方差
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{gather*}    E(X^2)=&#x5C;sum_{k=1}^{&#x5C;infty}k^2&#x5C;cdot p(1-p)^{k-1}=p&#x5C;sum_{k=1}^{&#x5C;infty}k^2&#x5C;cdot (1-p)^{k-1}    =p&#x5C;cdot&#x5C;frac{2-p}{p^3}=&#x5C;frac{2-p}{p^2},&#x5C;&#x5C;    D(X)=E(X^2)-[E(X)]^2=&#x5C;frac{1-p}{p^2}.&#x5C;end{gather*}"/></p>
22.
23.
24.
25.
<h2  id="协方差及相关系数">协方差及相关系数</h2>
<h2  id="矩-协方差矩阵">矩、协方差矩阵</h2>
  