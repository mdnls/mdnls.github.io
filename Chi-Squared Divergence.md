---
tags:
  - statistics/information-theory
---
***
**Definition**. The $\chi^2$-divergence is,
$$
\chi^2(\mu, \nu) = \int \frac{(\mu(x) - \nu(x))^2}{\nu(x)} \, dx
$$it is a [[f-divergence]] for $f(x) = x^2$.
***

***
**Proposition (Variational characterization)**. The chi-squared divergence is basically the squared $\Lcl^2$ distance between measures: 
$$

^8b1a19

\chi^2(\mu, \nu) = \sup_{g : \Var_\nu(g) \leq 1} |\E_\mu[g] - \E_\nu[g]|^2
$$
***
One nice consequence of this proposition is that for any function $g : \R \to \R$, 
$$
\begin{align*}
|\E_\mu[g] - \E_\nu[g]|^2 & \leq  \Var_\nu(g)\,  \chi^2(\mu, \nu),
\end{align*}
$$
which is sort of like the [[Cramer-Rao Lower Bound]] and which also provides a simple way to bound LHS. 


The chi-squared divergence between gaussians has a nice expression. 

***
**Proposition (Chi-squared between Gaussians)** let $Q(x) = \E_{\theta \sim \pi} [\Ncl(x; \theta, \sigma^2)]$ be a Gaussian mixture and let $P(x) = \Ncl(x; 0, \sigma^2)$. Then 
$$
\chi^2(Q_\pi \mid P) = \E_{\theta, \theta' \sim \pi} \exp (\langle \theta, \theta'\rangle) - 1
$$
***
<em>Proof idea</em>: $\chi^2(Q \mid P) = \E_{P}[(\frac{dQ}{dP}(X))^2] + 1$. The ratio evaluates as $\E_{P}\left( \E_\theta \exp \left(\langle X , \theta \rangle - \frac{\|\theta\|^2}{2}\right)\right)^2$ and the expectation inside $P$ can be rewritten 
$$
\left(\E_\theta \exp \left( \langle X, \theta \rangle - \frac{\|\theta\|^2}{2}\right) \right)^2 = \E_{\theta, \theta'} \exp \left( \langle X, \theta + \theta' \rangle - \frac{\|\theta\|^2+ \|\theta'\|^2}{2}\right).
$$
which simplifies according to the claim once you integrate over $X \sim \Ncl(0, \sigma^2)$. 


**Remark**: 
- This is often useful in hypothesis testing for Gaussian denoising settings, such as in the [[Gaussian Location Model]]. In this example, the use case is in testing between the hypothesis $H_0 : X \sim \Ncl(0, I_d)$ and $H_1 : X \sim \Ncl(\theta, I_d)$ for some $\theta \not = 0$. 