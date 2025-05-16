
# PT Modeling and Simulation Family of Distributions

---

## 1. 📌 Exponential Distribution

**Problem:**  
The average time between arrivals of buses is 15 minutes. What is the probability that the next bus arrives in less than 10 minutes?

**Solution:**  
The exponential distribution models the time between events in a Poisson process. The formula for cumulative distribution is:

\[ P(X < x) = 1 - e^{-\lambda x} \]

Where:  
- \( \lambda \) is the rate parameter, which is the reciprocal of the mean.  
- Mean = 15 → \( \lambda = 1/15 \)  
- We want \( P(X < 10) \)

**Step-by-step:**  
1. Compute the rate parameter: \( \lambda = 1 / 15 = 0.0667 \)  
2. Multiply \( \lambda \) by \( x = 10 \):  
   \( \lambda x = 0.0667 \times 10 = 0.6667 \)  
3. Apply to the formula:  
   \( P(X < 10) = 1 - e^{-0.6667} \approx 1 - 0.5134 = 0.4866 \)

**Answer:** 48.66% chance the next bus arrives in less than 10 minutes.

---

## 2. 📌 Normal Distribution

**Problem:**  
A test has a mean of 70 and a standard deviation of 10. What is the probability that a student scores above 85?

**Solution:**  
Use the standard normal distribution (Z-distribution). First, convert the score to a Z-score:

\[ Z = \frac{X - \mu}{\sigma} \]

**Step-by-step:**  
1. Plug in the values: \( Z = \frac{85 - 70}{10} = 1.5 \)  
2. Use Z-table to find the area to the left of Z = 1.5: \( P(Z < 1.5) = 0.9332 \)  
3. To find the area to the right (P > 85):  
   \( P(Z > 1.5) = 1 - 0.9332 = 0.0668 \)

**Answer:** 6.68% chance a student scores above 85.

---

## 3. 📌 Poisson Distribution

**Problem:**  
A call center receives 3 calls per minute. What is the probability of receiving exactly 5 calls in a minute?

**Solution:**  
Poisson formula:  
\[ P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!} \]

Where:  
- \( \lambda = 3 \), \( k = 5 \)

**Step-by-step:**  
1. Calculate \( \lambda^k = 3^5 = 243 \)  
2. Calculate \( k! = 5! = 120 \)  
3. Compute the formula:  
   \( P(X = 5) = \frac{e^{-3} \cdot 243}{120} \approx \frac{0.0498 \cdot 243}{120} \approx 0.1008 \)

**Answer:** 10.08% chance of receiving exactly 5 calls.

---

## 4. 📌 Binomial Distribution

**Problem:**  
A coin is flipped 10 times. What is the probability of getting exactly 6 heads?

**Solution:**  
Binomial formula:  
\[ P(X = k) = C(n, k) \cdot p^k \cdot (1 - p)^{n - k} \]

Where:  
- \( n = 10 \), \( k = 6 \), \( p = 0.5 \) (fair coin)

**Step-by-step:**  
1. Compute combinations: \( C(10,6) = 210 \)  
2. Calculate \( (0.5)^6 = 0.015625 \)  
3. Calculate \( (0.5)^4 = 0.0625 \)  
4. Combine: \( P = 210 \cdot 0.015625 \cdot 0.0625 = 0.2051 \)

**Answer:** 20.51% chance of getting exactly 6 heads.

---

## 5. 📌 Triangular Distribution

**Problem:**  
A delivery takes between 20 and 40 minutes, most likely 30 minutes. What is the probability it takes less than 25 minutes?

**Solution:**  
Triangular CDF when \( x < c \):  
\[ P(X < x) = \frac{(x - a)^2}{(b - a)(c - a)} \]

Where:  
- \( a = 20 \), \( b = 40 \), \( c = 30 \), \( x = 25 \)

**Step-by-step:**  
1. \( x - a = 25 - 20 = 5 \) → square it: \( 25 \)  
2. \( b - a = 20 \), \( c - a = 10 \)  
3. Multiply: \( (b - a)(c - a) = 200 \)  
4. Final: \( P(X < 25) = 25 / 200 = 0.125 \)

**Answer:** 12.5% chance delivery takes less than 25 minutes.

---

## 6. 📌 Lognormal Distribution

**Problem:**  
If \( Y = \ln(X) \) is normally distributed with \( \mu = 2 \), \( \sigma = 0.5 \), what is the probability that \( X < 10 \)?

**Solution:**  
We convert to a normal problem:  
\[ P(X < 10) = P(\ln(X) < \ln(10)) = P(Y < 2.3026) \]

**Step-by-step:**  
1. Calculate Z-score: \( Z = \frac{2.3026 - 2}{0.5} = 0.6052 \)  
2. Find cumulative probability: \( P(Z < 0.6052) \approx 0.727 \)

**Answer:** 72.7% chance that \( X < 10 \).

---

## 7. 📌 Gamma Distribution

**Problem:**  
For a Gamma distribution with shape \( k = 2 \) and rate \( \lambda = 0.5 \), what is the probability that \( X < 3 \)?

**Solution:**  
Use the simplified CDF for \( k = 2 \):  
\[ P(X < x) = 1 - e^{-\lambda x}(1 + \lambda x) \]

**Step-by-step:**  
1. \( \lambda x = 0.5 \times 3 = 1.5 \)  
2. Compute exponent: \( e^{-1.5} \approx 0.2231 \)  
3. Compute full: \( 1 - 0.2231(1 + 1.5) = 1 - 0.2231(2.5) = 1 - 0.5578 = 0.4422 \)

**Answer:** 44.22% chance that \( X < 3 \).

---

## 8. 📌 Beta Distribution

**Problem:**  
Given a Beta(2,3) distribution, what is the probability that \( X < 0.5 \)?

**Solution:**  
Beta CDF doesn't have a closed form. Use standard tables or calculators.

**Step-by-step:**  
1. Use a Beta CDF calculator or software: \( P(X < 0.5) \approx 0.6875 \)

**Answer:** 68.75% chance that \( X < 0.5 \).

---

## 9. 📌 Weibull Distribution

**Problem:**  
In a Weibull distribution with shape \( k = 2 \) and scale \( \lambda = 5 \), find \( P(X < 4) \).

**Solution:**  
Weibull CDF:  
\[ P(X < x) = 1 - e^{-(x/\lambda)^k} \]

**Step-by-step:**  
1. \( x / \lambda = 4 / 5 = 0.8 \)  
2. \( (x/\lambda)^k = 0.8^2 = 0.64 \)  
3. \( e^{-0.64} \approx 0.5273 \)  
4. Final: \( 1 - 0.5273 = 0.4727 \)

**Answer:** 47.27% chance that \( X < 4 \).

---

## 10. 📌 Uniform Distribution

**Problem:**  
A variable is uniformly distributed between 10 and 30. What is the probability that it takes a value less than 18?

**Solution:**  
Uniform CDF:  
\[ P(X < x) = \frac{x - a}{b - a} \]

**Step-by-step:**  
1. \( a = 10 \), \( b = 30 \), \( x = 18 \)  
2. Compute: \( P = (18 - 10) / (30 - 10) = 8 / 20 = 0.4 \)

**Answer:** 40% chance that \( X < 18 \).
