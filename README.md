# PT Modeling and Simulation: Family of Distribution

---

## 1. Exponential Distribution

**Problem:**  
The average time between arrivals of buses is 15 minutes. What is the probability that the next bus arrives in less than 10 minutes?

**Formula:**  
**P(X < x) = 1 - e<sup>−λx</sup>**

**Given:**  
- Mean = 15  
- λ = 1 / 15 = 0.0667  
- x = 10

**Steps:**  
1. λx = 0.0667 × 10 = 0.6667  
2. P(X < 10) = 1 - e<sup>-0.6667</sup> ≈ 1 - 0.5134 = 0.4866

**Answer:** 48.66%

---

## 2. Normal Distribution

**Problem:**  
A test has a mean of 70 and a standard deviation of 10. What is the probability that a student scores above 85?

**Formula:**  
**Z = (X - μ) / σ**

**Given:**  
- μ = 70  
- σ = 10  
- X = 85

**Steps:**  
1. Z = (85 - 70) / 10 = 1.5  
2. P(Z < 1.5) = 0.9332  
3. P(Z > 1.5) = 1 - 0.9332 = 0.0668

**Answer:** 6.68%

---

## 3. Poisson Distribution

**Problem:**  
A call center receives 3 calls per minute. What is the probability of receiving exactly 5 calls in a minute?

**Formula:**  
**P(X = k) = (e<sup>-λ</sup> × λ<sup>k</sup>) / k!**

**Given:**  
- λ = 3  
- k = 5  
- λ⁵ = 243  
- 5! = 120  
- e<sup>-3</sup> ≈ 0.0498

**Steps:**  
P(X = 5) = (0.0498 × 243) / 120 ≈ 0.1008

**Answer:** 10.08%

---

## 4. Binomial Distribution

**Problem:**  
A coin is flipped 10 times. What is the probability of getting exactly 6 heads?

**Formula:**  
**P(X = k) = C(n, k) × p<sup>k</sup> × (1 - p)<sup>n - k</sup>**

**Given:**  
- n = 10  
- k = 6  
- p = 0.5  
- C(10,6) = 210  
- p⁶ = 0.015625  
- (1 - p)⁴ = 0.0625

**Steps:**  
P = 210 × 0.015625 × 0.0625 = 0.2051

**Answer:** 20.51%

---

## 5. Triangular Distribution

**Problem:**  
A delivery takes between 20 and 40 minutes, most likely 30 minutes. What is the probability it takes less than 25 minutes?

**Formula (x < c):**  
**P(X < x) = (x - a)² / ((b - a)(c - a))**

**Given:**  
- a = 20  
- b = 40  
- c = 30  
- x = 25

**Steps:**  
1. (25 - 20)² = 25  
2. (40 - 20)(30 - 20) = 200  
3. P = 25 / 200 = 0.125

**Answer:** 12.5%

---

## 6. Lognormal Distribution

**Problem:**  
If Y = ln(X) is normally distributed with μ = 2 and σ = 0.5, what is the probability that X < 10?

**Given:**  
- μ = 2  
- σ = 0.5  
- ln(10) ≈ 2.3026

**Steps:**  
1. Z = (2.3026 - 2) / 0.5 = 0.6052  
2. P(Z < 0.6052) ≈ 0.7291

**Answer:** 72.91%

---

## 7. Gamma Distribution

**Problem:**  
A Gamma distribution has shape k = 2 and rate λ = 0.5. Find P(X < 3).

**Formula (for k = 2):**  
**P(X < x) = 1 - e<sup>−λx</sup> × (1 + λx)**

**Given:**  
- k = 2  
- λ = 0.5  
- x = 3

**Steps:**  
1. λx = 0.5 × 3 = 1.5  
2. e<sup>-1.5</sup> ≈ 0.2231  
3. 1 + λx = 2.5  
4. P = 1 - 0.2231 × 2.5 = 1 - 0.5578 = 0.4422

**Answer:** 44.22%

---

## 8. Beta Distribution

**Problem:**  
For a Beta(2, 3) distribution, what is the probability that X < 0.5?

**Formula:**  
**P(X < x) = Beta CDF(x; α, β)**

**Given:**  
- α = 2  
- β = 3  
- x = 0.5

**Note:** Use a calculator or statistical software for exact Beta CDF values.  
P(X < 0.5) ≈ 0.6875

**Answer:** 68.75%

---

## 9. Weibull Distribution

**Problem:**  
A Weibull distribution has shape k = 2 and scale λ = 5. Find P(X < 4).

**Formula:**  
**P(X < x) = 1 - e<sup>−(x/λ)<sup>k</sup></sup>**

**Given:**  
- k = 2  
- λ = 5  
- x = 4

**Steps:**  
1. (4 / 5)<sup>2</sup> = 0.64  
2. e<sup>-0.64</sup> ≈ 0.5273  
3. P = 1 - 0.5273 = 0.4727

**Answer:** 47.27%

---

## 10. Uniform Distribution

**Problem:**  
A variable is uniformly distributed between 10 and 30. What is the probability that it takes a value less than 18?

**Formula:**  
**P(X < x) = (x - a) / (b - a)**

**Given:**  
- a = 10  
- b = 30  
- x = 18

**Steps:**  
P = (18 - 10) / (30 - 10) = 8 / 20 = 0.4

**Answer:** 40%
