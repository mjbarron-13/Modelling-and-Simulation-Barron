# PT Modeling and Simulation: Family of Distribution

---

## 1. Exponential Distribution

**Problem:**  
The average time between arrivals of buses is 15 minutes. What is the probability that the next bus arrives in less than 10 minutes?

**Solution:**  
The exponential distribution models the time between events in a Poisson process. The formula for cumulative distribution is:

**P(X < x) = 1 - e^(-λx)**

Where:  
- `λ` is the rate parameter = `1 / mean` = `1 / 15 = 0.0667`  
- We're solving for `P(X < 10)`

**Steps:**  
1. `λx = 0.0667 × 10 = 0.6667`  
2. `P(X < 10) = 1 - e^(-0.6667) ≈ 1 - 0.5134 = 0.4866`

**Answer:** 48.66%

---

## 2. Normal Distribution

**Problem:**  
A test has a mean of 70 and a standard deviation of 10. What is the probability that a student scores above 85?

**Solution:**  
Standardize the value:

**Z = (X - μ) / σ = (85 - 70) / 10 = 1.5**

Look up `P(Z < 1.5)` = `0.9332`, so:  
`P(Z > 1.5) = 1 - 0.9332 = 0.0668`

**Answer:** 6.68%

---

## 3. Poisson Distribution

**Problem:**  
A call center receives 3 calls per minute. What is the probability of receiving exactly 5 calls in a minute?

**Formula:**  
**P(X = k) = (e^-λ × λ^k) / k!**

Where:  
- `λ = 3`, `k = 5`  
- `λ^k = 243`, `k! = 120`, `e^-3 ≈ 0.0498`

**P(X = 5) = (0.0498 × 243) / 120 ≈ 0.1008**

**Answer:** 10.08%

---

## 4. Binomial Distribution

**Problem:**  
A coin is flipped 10 times. What is the probability of getting exactly 6 heads?

**Formula:**  
**P(X = k) = C(n, k) × p^k × (1 - p)^(n - k)**

Given:  
- `n = 10`, `k = 6`, `p = 0.5`  
- `C(10,6) = 210`, `0.5^6 = 0.015625`, `0.5^4 = 0.0625`

**P = 210 × 0.015625 × 0.0625 = 0.2051**

**Answer:** 20.51%

---

## 5. Triangular Distribution

**Problem:**  
A delivery takes between 20 and 40 minutes, most likely 30 minutes. What is the probability it takes less than 25 minutes?

**Formula (x < c):**  
**P(X < x) = (x - a)² / ((b - a)(c - a))**

Given: `a = 20`, `b = 40`, `c = 30`, `x = 25`

1. `(25 - 20)² = 25`  
2. `(40 - 20)(30 - 20) = 200`  
3. `P = 25 / 200 = 0.125`

**Answer:** 12.5%

---

## 6. Lognormal Distribution

**Problem:**  
If `Y = ln(X)` is normally distributed with `μ = 2`, `σ = 0.5`, find the probability that `X < 10`.

**Steps:**  
1. `ln(10) ≈ 2.3026`  
2. `Z = (2.3026 - 2) / 0.5 = 0.6052`  
3. `P(Z < 0.6052) ≈ 0.727`

**Answer:** 72.7%

---

## 7. Gamma Distribution

**Problem:**  
Gamma with shape `k = 2` and rate `λ = 0.5`, find `P(X < 3)`.

**Formula for k = 2:**  
**P(X < x) = 1 - e^(-λx) × (1 + λx)**

1. `λx = 0.5 × 3 = 1.5`  
2. `e^-1.5 ≈ 0.2231`  
3. `1 + λx = 2.5`  
4. `P = 1 - 0.2231 × 2.5 ≈ 0.4422`

**Answer:** 44.22%

---

## 8. Beta Distribution

**Problem:**  
Beta(2, 3), what is `P(X < 0.5)`?

**Note:** Use calculator or table.

**Answer:** Approx. 68.75%

---

## 9. Weibull Distribution

**Problem:**  
Weibull with shape `k = 2`, scale `λ = 5`, find `P(X < 4)`.

**Formula:**  
**P(X < x) = 1 - e^(-(x/λ)^k)**

1. `(4 / 5)^2 = 0.64`  
2. `e^-0.64 ≈ 0.5273`  
3. `P = 1 - 0.5273 = 0.4727`

**Answer:** 47.27%

---

## 10. Uniform Distribution

**Problem:**  
Uniformly distributed between 10 and 30. Find `P(X < 18)`.

**Formula:**  
**P(X < x) = (x - a) / (b - a)**

1. `(18 - 10) / (30 - 10) = 8 / 20 = 0.4`

**Answer:** 40%
