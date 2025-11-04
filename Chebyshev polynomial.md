* [[Lower bounds for iterative quadratic optimization#Chebyshev Acceleration|Chebyshev Acceleration]]

An identity: 
$$
T_k(x) =
\begin{cases}
\cos(k \ \text{acos}(x)) & x \in [-1, 1] \\
\cosh(k \ \text{acosh}(x)) & x > 1 \\
(-1)^k \cosh(k \ \text{acosh}(-x)) & x < -1 \\
\end{cases}
$$
from [[Acceleration Methods (d'Aspremont et al)]] (or apparently Mason and Handscomb 2002). 