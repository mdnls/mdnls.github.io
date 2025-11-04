---
tags:
  - research/empirical-process-theory
  - math/probability/stochastic-processes
---
The chaining method is a powerful approach to bounding the suprema of a random process $(X_t)_{t \in T}$. It is based on decomposing the index set $T$ into finite increasing subsets $T_k \nearrow T$ that represent discretizations of $T$ with increasing granularity. It is often easier to bound how much the suprema changes when moving from $T_k$ to $T_{k+1}$, and bounds over on $T$ can be recovered by summing (or 'chaining together') the bounds at each scale.

This general purpose method has many instantiations: 
- [[One-step Chaining Inequality]]
- [[Dudley's Entropy Integral]], improvements via generic chaining
- [[Bracketing Inequality]]

The goal of this note is to compare, contrast, and remark on general themes, especially in the context of empirical process theory and statistics. 

<del>It would be useful to organize the following approaches on examples on a model problem, like nonparametric constrained linear regression. My current understanding:</del>
1. [[Van de Geer's One-shot Localization Technique]], a simplified localization method that can be used in situations where one can locally approximate the population loss by the square of the norm used for localization. 
2. [[Dudley's Entropy Integral]] with Ell-infinity coverings: Ell infinity coverings of the parameter space are convenient because, via Hoeffding's inequality, it is easy to verify the sub-Gaussianity requirements of Dudley's entropy integral directly from boundedness. However, the tradeoff is that the population loss must locally approximate $\Lcl(\theta) \approx \|\theta-\theta^*\|_{\Lcl^\infty}^2$, which is a very strong requirement on the population loss and/or on the regularity of $\theta$.
3. [[Ossiander's Theorem]] with Ell-two bracketing numbers: one can altogether avoid sub-Gaussianity requirements by using bracketing bounds instead. One would hope to argue that: if $\hat{\theta}_n$ has small population loss, then $\|\hat{\theta}_n - \theta^*\|_{\Lcl^2(\mu^*)}$ is small, so I can improve a bound on the population loss of $\hat{\theta}_n$ using uniform convergence over $\Theta \cap B(\theta^*, \|\cdot\|_{\Lcl^2(\mu^*)})$. But bounding the bracketing number of an $\Lcl^2$-ball can't be done generically!
4. [[Bernstein Maximal Inequality]]: the Goldilocks approach. Using a Bernstein version of Dudley's integral, one can work instead with ell-two coverings of the parameter space, which plays nice with one-shot localization.