---
aliases:
  - continuous semimartingales
  - continsemimartingales
  - semimartingales
---
***
**Definition (continuous semi-martingale)** a continuous semi-martingale is a process of the form
$$
M_t = X_t + A_t
$$
where $X_t$ is a [[Continuous Local Martingales|continuous local martingale]] and $A_t$ is a [[Finite-variation Process|finite variation process]]. Given two such processes $(M_t)_{t \geq 0}$ and $N_t = Y_t + B_t$,  we define their [[Quadratic Variation|bracket]] by
$$
\langle M, N \rangle_t = \langle X, Y \rangle_t
$$
***

Note that this decomposition is unique since [[Continuous Local Martingales#Continuous Local Martingales and Finite-variation Processes|continuous local martingales with finite variation are zero]]. This also gives some motivation for why we can ignore the finite variation part. For any finite variation $(A_t)_{t \geq 0}$ and continuous local martingale $(X_t)_{t \geq 0}$, the bracket $\langle A, X\rangle_t = 0$ so the above definition is indeed reasonable. 

***
**Proposition (approximation by partitions)**. let $M, N$ be continuous semi-martingales. Let $0 = t_0^n < t_1^n < \ldots < t_{p_n}^n = t$ be an increasing subdivision of $[0, t]$ with mesh tending to zero. Then,
$$
\lim_{n \to \infty}\sum_{i=1}^{p_n}(M_{t_i^n}-M_{t_{i-1}^n})(N_{t_i^n}-N_{t_{i-1}^n}) = \langle M, N \rangle_t
$$
***
<em>Proof sketch</em>. it is sufficient to consider the case $X = Y$, and the proof involves expanding out the partition in terms of $X, Y, A, B$ and proving that terms which contain increments of $A, B$ vanish in the limit. 
