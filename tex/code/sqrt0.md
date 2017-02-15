md(r'''正数$a$の平方根を数値的に求める標準解法は
方程式$f(x) = x^2 - a = 0$へのNewton-Raphson法の適用です．
この手法では，解$x$の近似解$x_n$の近似度を漸次改善します．
このために関数$f$の$(x_n, f(x_n))$周辺におけるTaylor展開の一次近似
$x_n - f(x_n) / f'(x_n)$を用います．$f$の定義をこれにあてはめて
\begin{align}
f(x)    &= x^2 - a \\
f'(x)   &= 2x \\
x_{n+1} &= x_n - \frac {f(x_n)}{f'(x_n)}
         = x_n - \frac {x_n^2 - a} {2x_n}
         = \frac {x + a / x} 2
\end{align}が得られます．''')
