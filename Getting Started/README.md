# What is Differential Privacy?

Privacy is one important human right, but it doesn't mean it is easy to preserve it. It is actually really difficult. In order to systematize and formalize the preservation of privacy, the Differential Privacy constraints were developed.

There is a mathematical definition for it, that can be intimidating at first. But don't worry, we're going to make it as intuitive as possible. Let's start with some formulas and then dissect it into smaller and more comprehensible parts.

```
A mechanism M with domain N|𝒳| is 𝜀-differentially private if for all 𝒮 ⊆ 𝑅𝑎𝑛𝑔𝑒(M) and for all 𝑥, 𝑦 ∈ N|𝒳| such that ||𝑥 − 𝑦|| ≤ 1:

𝑃[M(𝑥) ∈ 𝒮]/𝑃[M(𝑦) ∈ 𝒮] ≤ exp(𝜀)

In this definition, we have 𝑃[𝐸] as the probability of a certain event 𝐸 happening and ||𝑥|| is the sum of the absolute value of all dimentions of 𝑥.
```