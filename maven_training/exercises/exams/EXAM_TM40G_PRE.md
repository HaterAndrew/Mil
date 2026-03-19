# PRE-TEST — TM-40G: ORSA
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Course** | TM-40G: ORSA |
| **Form** | Pre-Test |
| **Level** | TM-40G (Specialist) |
| **Audience** | FA49 / ORSA analysts; prerequisite: TM-10+20+30 + graduate-level quantitative methods + Python or R proficiency |
| **Time Allowed** | 30 minutes |
| **Passing Score** | N/A — diagnostic only |

---

## INSTRUCTIONS

This diagnostic assessment establishes your baseline knowledge before training. Your score does not affect course eligibility. Answer honestly — results help the instructor tailor instruction to gaps.

---

## SECTION 1 — MULTIPLE CHOICE

*Circle the letter of the best answer. (2 points each)*

**1. In a linear regression model, the coefficient of determination (R²) represents:**

A. The probability that the model's predictions are correct
B. The average absolute difference between predicted and actual values
C. The proportion of variance in the dependent variable explained by the independent variables
D. The statistical significance of the largest coefficient in the model

**2. A residual in a regression model is defined as:**

A. The coefficient assigned to a predictor variable
B. The difference between the observed value and the model's predicted value
C. The variance of the dependent variable not explained by the model
D. The intercept term in the regression equation

**3. In time series analysis, an "ARIMA(p,d,q)" model's "d" parameter specifies:**

A. The number of autoregressive lags
B. The number of moving average terms
C. The order of differencing applied to make the series stationary
D. The seasonal period of the time series

**4. A Monte Carlo simulation is used to:**

A. Estimate the probability distribution of an outcome by running many random trials
B. Solve linear programming problems with continuous decision variables
C. Fit a regression model to historical time series data
D. Optimize a supply chain by minimizing total transportation cost

**5. In operations research, a "sensitivity analysis" on a linear program answers:**

A. How much the optimal solution changes if a constraint or objective coefficient is varied
B. How well the model fits the training data
C. Whether the LP solution is unique or has multiple optima
D. The confidence interval around the predicted optimal value

**6. In a COA analysis, "risk" is most accurately quantified as:**

A. The commander's subjective preference for the riskiest option
B. The probability of an adverse outcome multiplied by the magnitude of its impact
C. The number of enemy courses of action that defeat a given friendly COA
D. The variance of the forecast model used to support the analysis

**7. A "confidence interval" for a point estimate means:**

A. The minimum and maximum values in the dataset
B. The accuracy of a single prediction from the model
C. The range within which the true population parameter falls with a specified probability over repeated sampling
D. The interval within which the model was trained

**8. "Cross-validation" in model evaluation is primarily used to:**

A. Validate that the model's code produces the same result on two different machines
B. Estimate how well a model will generalize to new data by testing it on held-out subsets
C. Compare the model's coefficients against a theoretical distribution
D. Validate that input data meets schema requirements before modeling

**9. In the context of a commander's brief, a "BLUF" (Bottom Line Up Front) means:**

A. The key finding and recommended action are stated at the beginning before supporting analysis
B. The most detailed technical section is placed first
C. The brief opens with background context and builds to conclusions
D. All charts are placed before any text explanation

**10. Setting a "random seed" in a simulation is important because:**

A. It makes the simulation run faster by reducing randomness
B. It is required by Army policy for all approved modeling tools
C. It prevents the simulation from producing extreme outliers
D. It ensures reproducibility — the same seed produces the same sequence of random numbers

**11. A linear programming (LP) formulation must include:**

A. A loss function, training data, and validation metrics
B. A network diagram showing the flow of resources
C. A probability distribution for each decision variable
D. An objective function to optimize and a set of constraints that bound the solution space

**12. In Army operations research, the distinction between "prediction interval" and "confidence interval" matters most when:**

A. Presenting findings to a commander who will make a resource allocation decision based on a specific future value
B. Selecting the appropriate regression algorithm for the dataset
C. Configuring the model's training/test split ratio
D. Deciding whether to use Python or R for the analysis

**13. "Stationarity" in a time series means:**

A. The series has no missing values or gaps
B. The statistical properties (mean, variance, autocorrelation) do not change over time
C. The series follows a linear trend that can be removed by differencing
D. The series has been smoothed to remove seasonal variation

**14. An ORSA analyst produces a demand forecast with a point estimate of 450 units and 90% confidence bounds of [380, 520]. How should this result be presented in a commander's brief?**

A. "The model predicts 450 units."
B. "Demand will be between 380 and 520 units."
C. "The model has 90% accuracy."
D. "Estimated demand is 450 units (90% CI: 380–520). We are 90% confident the true demand falls within this range."

**15. In a resource allocation problem where the G4 must distribute 500 maintenance man-hours across 12 units to maximize fleet readiness, the MOST appropriate analytical approach is:**

A. Descriptive statistics on historical maintenance data
B. A regression model predicting readiness from man-hours
C. A linear programming model with man-hour constraints and a readiness objective function
D. A Monte Carlo simulation of maintenance outcomes

---

## SECTION 2 — SHORT ANSWER

*Answer in 2–5 sentences. (6 points each)*

**SA-1. Explain what "heteroscedasticity" is in a regression context and describe how you would detect it in your model's residuals.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-2. A G4 asks you to provide a "best estimate" of fuel consumption for the next 30 days. Explain why providing only a point estimate without uncertainty bounds would be analytically inadequate, and describe what you would provide instead.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-3. Describe the ACF (Autocorrelation Function) and PACF (Partial Autocorrelation Function) plots and how you use them to identify the p and q parameters of an ARIMA model.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-4. An LP model you built for ammunition allocation recommends a distribution that the G4 says is "operationally unacceptable" because it leaves one unit with zero reserves. Explain how you would modify the formulation to incorporate this operational constraint.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-5. Explain the concept of "overfitting" in a statistical model and describe two techniques you would use to detect and address it.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

---

## SCORING SUMMARY

| Section | Questions | Points Each | Total Points |
|---|---|---|---|
| Multiple Choice | 15 | 2 | 30 |
| Short Answer | 5 | 6 | 30 |
| **Total** | — | — | **60** |

Passing: N/A — Pre-test is diagnostic only.

---

## ANSWER KEY — INSTRUCTOR USE ONLY

*Do not distribute to students.*

**Multiple Choice:**
1. C — R² is the proportion of variance explained by the model (coefficient of determination).
2. B — Residual = observed value minus predicted value.
3. C — The "d" in ARIMA is the order of differencing.
4. A — Monte Carlo estimates outcome probability distributions through random trials.
5. A — Sensitivity analysis shows how the optimal solution changes with parameter variation.
6. B — Risk = probability × impact is the standard operations research definition.
7. C — Confidence interval is the range capturing the true parameter with specified probability over repeated sampling.
8. B — Cross-validation estimates generalization performance on held-out data.
9. A — BLUF places key finding and recommended action first.
10. D — Random seed ensures reproducibility of simulation results.
11. D — LP requires an objective function and constraints.
12. A — Prediction vs. confidence interval distinction is critical when a commander needs a bound on a specific future value.
13. B — Stationarity = statistical properties do not change over time.
14. D — Full uncertainty communication with CI label and interpretation is the correct format.
15. C — LP with man-hour constraints and readiness objective is the appropriate formulation.

**Short Answer Guidance:**

SA-1. Full credit: heteroscedasticity = non-constant variance of residuals across the range of fitted values; detection methods include a residual vs. fitted plot (fan shape indicates heteroscedasticity), Breusch-Pagan test, or White test. Partial credit (3 pts) for correct definition without a detection method.

SA-2. Full credit: a point estimate conveys false precision — fuel demand is uncertain and a single number gives the commander no sense of the range of possible outcomes; should provide a forecast interval (e.g., 90% prediction interval) with explicit interpretation, plus sensitivity analysis or scenario bounds for planning purposes. Partial credit (3 pts) for identifying the limitation without describing what to provide.

SA-3. Full credit: ACF plot shows correlation of a series with its own lagged values — significant spikes at lag q indicate the MA order; PACF plot shows partial correlation controlling for intermediate lags — significant spikes at lag p indicate the AR order; use ACF to identify q and PACF to identify p; patterns differ for AR, MA, and ARMA processes. Partial credit (3 pts) for correct description of one plot without connecting to parameter identification.

SA-4. Full credit: add a minimum reserve constraint to the LP formulation — a lower-bound constraint on each unit's allocation (e.g., unit_i allocation ≥ minimum_reserve_i); this is a valid operational constraint that narrows the feasible region; note that adding constraints may reduce the objective function value (total allocation) and that trade-off should be presented to the G4. Partial credit (3 pts) for identifying the need for a constraint without formulating it.

SA-5. Full credit: overfitting = model learns the noise in training data and performs poorly on new data; detection: compare in-sample and out-of-sample (cross-validation) performance — large gap indicates overfitting; techniques to address: regularization (L1/L2), cross-validation for model selection, reducing model complexity, or collecting more training data. Partial credit (3 pts) for correct definition and one technique.

---

*USAREUR-AF Operational Data Team*
*TM-40G Pre-Test | Version 1.0 | March 2026*
