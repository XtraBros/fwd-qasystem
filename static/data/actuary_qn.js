const questionsData = [
    {
        "question": "Critique the statement: Stochastic models should only be used when it is explicitly required by a regulatory standard.",
        "correctAnswer": "False. Stochastic models can also be used for tail risk analysis, calculation of diversification effects, and risk-adjusted strategies.",
        "explanation": "Stochastic models can also be used for tail risk analysis, calculation of diversification effects, and risk-adjusted strategies.",
        "score": 2
    },
    {
        "question": "Critique the statement: Real-world scenarios cannot be connected with risk-neutral scenarios due to different usage of expected cash flows and a discount rate.",
        "correctAnswer": "False. Two scenarios can be connected via deflators to ensure consistency between risk-adjusted cash flows.",
        "explanation": "Risk-adjusted cash flows are adjusted to align expected present values, allowing scenarios to be connected via deflators.",
        "score": 2
    },
    {
        "question": "Critique the statement: For nested stochastic modeling, real-world scenarios and risk-neutral scenarios should be used for inner-loop and outer-loop, respectively.",
        "correctAnswer": "False. Real-world scenarios should be used for the outer loop and risk-neutral scenarios for the inner loop.",
        "explanation": "Outer loop drives market scenarios for fund returns, while inner loop calculates market-consistent fair values.",
        "score": 2
    },
    {
        "question": "Critique the statement: When using a random number generator, a true random number generator is more efficient than a pseudo-random number generator.",
        "correctAnswer": "False. Pseudo-random number generators are more efficient as they generate large sets of numbers more quickly.",
        "explanation": "Pseudo-random number generators (PRNGs) offer computational efficiency compared to true random number generators (TRNGs).",
        "score": 2
    },
    {
        "question": "A Generalized Linear Model (GLM) is due for an update. The form of the GLM is: Y = β 1 X1+ β 2 X2 +β 3 X3 + ε Where: β 1= Parameter for Male, β 2 = Parameter for Female, β 3 = Parameter for Smoking Status. The following data is provided regarding claim severity.",
        "correctAnswer": "β1 = 550, β2 = 350, β3 = 300",
        "explanation": "Solving involves differentiating the sum of squared errors and solving the resulting equations for β1, β2, and β3.",
        "score": 2,
        "data": [
            ["", "Smoker", "Non-smoker"],
            ["Male", 900, 500],
            ["Female", 600, 400]
        ]
    },
    {
        "question": "Evaluate the limitations of using a normal error structure in GLMs.",
        "correctAnswer": "1. Difficult to assert normality and constant variance. 2. Response variable restricted to positive values violates normality. 3. Variance depends on the mean.",
        "explanation": "Normal error structures may violate assumptions for non-negative response variables and exhibit variable-dependent variance.",
        "score": 1
    },
    {
        "question": "Describe a drawback of using a normal distribution with constant volatility to project equity returns.",
        "correctAnswer": "Economic variables typically exhibit fatter tails and stronger central peaks than those modeled by a normal distribution.",
        "explanation": "The normal distribution does not adequately capture the variability and extremes of economic variables.",
        "score": 1
    },
    {
        "question": "Recommend two alternatives to using constant volatility.",
        "correctAnswer": "1. Stochastic volatility models introduce mean-reverting stochastic processes for volatility. 2. Regime-switching models use multiple volatility regimes (high and low).",
        "explanation": "Alternatives like stochastic volatility and regime-switching address limitations of constant volatility by introducing dynamic variations.",
        "score": 2
    },
    {
        "question": "Identify the option(s) granted to policyholders in an annuity product.",
        "correctAnswer": "1. Deposit option is a call option for purchasing growth at a guaranteed rate. 2. Withdrawal is a put option to sell back the policy for fund value.",
        "explanation": "Policyholders have embedded options like calls for deposits and puts for withdrawals, influenced by interest rates.",
        "score": 2
    },
    {
        "question": "Assess how interest rate changes trigger policyholder option exercise.",
        "correctAnswer": "1. Low rates encourage deposits for guaranteed returns. 2. High rates encourage surrenders to reinvest in higher-yielding products.",
        "explanation": "Interest rates influence policyholder behavior by altering the relative attractiveness of guaranteed returns or market alternatives.",
        "score": 2
    },
    {
        "question": "Calculate time-weighted return for an annuity policy.",
        "correctAnswer": "Total TWR = 0.393%",
        "explanation": "Calculated using chain linking of subperiod returns.",
        "score": 3,
        "data": 
        [
            ["Transaction Item", "Day", "Value"],
            ["Initial Deposit", 1, "100,000"],
            ["Policy charges / fees", 1, 150],
            ["Interest credited", 15, 165],
            ["Additional deposit (after interest crediting)", 15, "10,000"],
            ["Interest credited", 30, 250],
            ["End of period account value", 30, "110,265"],
        ]
    },
    {
        "question": "Estimate money-weighted return for the same annuity policy.",
        "correctAnswer": "Money-weighted return ≈ 0.396%",
        "explanation": "Calculated by solving the equation: Final Value = Initial Value(1+r)^1 + Additional Deposit(1+r)^0.5.",
        "score": 3,
        "data": 
        [
            ["Transaction Item", "Day", "Value"],
            ["Initial Deposit", 1, 100000],
            ["Policy charges / fees", 1, 150],
            ["Interest credited", 15, 165],
            ["Additional deposit (after interest crediting)", 15, 10000],
            ["Interest credited", 30, 250],
            ["End of period account value", 30, 110265],
        ]
    },
    {
        "question": "Assess whether Cash Flow Testing (CFT) should be performed on reinsured blocks in a modified coinsurance agreement.",
        "correctAnswer": "Not required for ceded blocks as risks are minimal.",
        "explanation": "While CFT isn't required for ceded blocks, actuaries should review the assuming company's CFT for confirmation.",
        "score": 2
    },
    {
        "question": "Recommend whether reserves for reinsured blocks should be included in asset adequacy analysis.",
        "correctAnswer": "Yes, reserves should be included as minimal asset risk in the actuarial opinion.",
        "explanation": "Reserves must appear in the asset adequacy analysis to ensure a complete financial picture.",
        "score": 2
    },
    {
        "question": "Critique the statement: Interest rate modeling is simpler than stock price modeling as it only requires one variable.",
        "correctAnswer": "Incorrect. Interest rate modeling is more complex as it requires modeling the term structure, involving multiple variables.",
        "explanation": "Interest rate modeling requires managing a curve and adhering to the no-arbitrage principle, which complicates it.",
        "score": 2
    },
    {
        "question": "Critique the recommendation to use analytical solutions instead of ESGs for variable annuities.",
        "correctAnswer": "Analytical solutions save time but are unsuitable for multiperiod projections with tail risks like GMxBs.",
        "explanation": "Analytical methods are limited by assumptions like known distributions and cannot handle complex joint distributions effectively.",
        "score": 3
    },
    {
        "question": "Describe the purpose of establishing stylized facts before developing an ESG.",
        "correctAnswer": "Stylized facts guide model design and calibration by providing generalized empirical insights.",
        "explanation": "They ensure the model captures essential behaviors and priorities for its intended application.",
        "score": 2
    },
    {
        "question": "Calculate the risk-neutral probability of an account value increasing by 8% in a year given the data: Risk-free interest rate: 3%, Account value: 100,000, Guarantee value: 100,000, Ratchet: Annual, Maturity: 10 years",
        "correctAnswer": "Probability of up move = 69.03%",
        "explanation": "Calculated using: (S(0) * exp(R) - S(1)d) / (S(1)u - S(1)d), where S(0): $10,000, S(1)u: $10,800, S(1)d: $9,200, R: 3%. (10,000 * exp(0.03) - 9,200) / (10,800 - 9,200) = 69.03%.",
        "score": 2
    },
    {
        "question": "Critique the statement: Only risk-neutral scenarios are used for hedging variable annuities.",
        "correctAnswer": "Incorrect. Both real-world and risk-neutral scenarios are used: real-world for risk assessment and risk-neutral for pricing.",
        "explanation": "Real-world scenarios assess overall risk and hedging effectiveness, while risk-neutral scenarios price liabilities.",
        "score": 2
    },
    {
        "question": "Critique the statement: Arbitrage-free models are necessary for ESG applications in real-world scenarios.",
        "correctAnswer": "Partially correct. Arbitrage-free models are essential for risk-neutral pricing but not always necessary for real-world simulations.",
        "explanation": "Real-world modeling focuses on empirical behaviors, while arbitrage-free models are critical for derivative pricing.",
        "score": 2
    },
    {
        "question": "State whether the following concepts are illustrated in the risk-neutral model: (i) Replication, (ii) No-arbitrage, (iii) Risk-neutral probability distribution, (iv) Dynamic hedging.",
        "correctAnswer": "All four concepts are illustrated.",
        "explanation": "(i) Replication: Creates a portfolio that replicates payoffs. (ii) No-arbitrage: Ensures identical outcomes have identical values. (iii) Risk-neutral: Models equate expected returns. (iv) Dynamic hedging: Adjusts portfolios to match liabilities.",
        "score": 3
    },
    {
        "question": "Describe the return objectives and risk tolerance for the company’s investment policy.",
        "correctAnswer": "Return objectives: Meet liabilities, exceed pricing returns, grow surplus. Risk tolerance: Maintain solvency with low-risk appetite.",
        "explanation": "Return objectives ensure financial stability and competitiveness. Risk tolerance accounts for market uncertainty and capital constraints.",
        "score": 3
    },
    {
        "question": "Identify four investment constraints the company should consider in its portfolio management.",
        "correctAnswer": "Liquidity, regulatory compliance, time horizon, taxation.",
        "explanation": "Constraints ensure timely liability payments, adherence to regulations, alignment with investment durations, and tax efficiency.",
        "score": 3
    },
    {
        "question": "Assess the company’s asset allocation strategy: Treasury bonds (25%), Bonds (25%), Equities (20%), Commercial paper (15%), Cash (15%).",
        "correctAnswer": "The allocation violates homogeneity principles and poses risks (e.g., excessive commercial paper and cash holdings).",
        "explanation": "Homogeneity ensures clear asset categorization. Excessive cash reduces return potential, and high commercial paper allocation increases risk.",
        "score": 3
    },
    {
        "question": "Critique the statement: The assets purchased should match the average liability duration to protect against all market yield curve changes.",
        "correctAnswer": "Incorrect. Matching average duration mitigates parallel shifts but fails to address non-parallel yield curve changes.",
        "explanation": "Liabilities should be separately immunized, and duration-matching only handles specific market changes.",
        "score": 2
    },
    {
        "question": "Evaluate bonds for a 10-year liability in a rising interest rate environment. Bond data: (1) 11%, 10 years, 5.0%; (2) 7%, 20 years, 6.1%; (3) 0%, 15 years, 2.2%; (4) 6%, 5 years, 8.4%.",
        "correctAnswer": "Bond 4 is recommended for minimizing duration risk and enabling reinvestment at higher rates.",
        "explanation": "Short-term assets mitigate interest rate risks by allowing flexibility to reinvest at prevailing higher rates.",
        "score": 3,
        "data":
        [
            ["Bond", "Coupon Rate", "Coupon frequency", "Term (Years)", "Yield to maturiy", "Maturity value"],
            ["Bond 1", "11%", "Semi-annual", 10, "5.0%", "$1,000"],
            ["Bond 2", "7%",  "Semi-annual", 20, "6.1%", "$1,000"],
            ["Bond 3", "0%", "N/A", 15, "2.2%", "$1,000"],
            ["Bond 4", "6%", "Semi-annual", 5, "8.4%", "$1,000"],
        ]

    },
    {
        "question": "Assess whether the bullet structure is appropriate for managing asset-liability mismatch risk in deferred annuities.",
        "correctAnswer": "The bullet structure is inappropriate due to uncertain liability cashflows in deferred annuities.",
        "explanation": "Laddered structures better handle variability in liability cashflows compared to the concentrated cashflow of bullet structures.",
        "score": 3
    },
    {
        "question": "Critique the statement: By investing annuity premiums in junk bonds, the spread represents risk-free arbitrage.",
        "correctAnswer": "Incorrect. Arbitrage implies risk-free profit. Junk bond investments amplify risk.",
        "explanation": "Investing in junk bonds involves accepting increased risk from policyholder behavior and bond defaults.",
        "score": 2
    },
    {
        "question": "Critique the statement: For simplicity, the same credit transition can be used for investment-grade and high-yield bonds.",
        "correctAnswer": "Incorrect. Default loss rates differ between high-grade and low-grade bonds.",
        "explanation": "High-grade bonds experience increasing default risk over time, whereas low-grade bonds face early high default rates.",
        "score": 2
    },
    {
        "question": "Critique the statement: We can take advantage of falling interest rates by selling older, higher-yielding bonds to realize gains.",
        "correctAnswer": "Incorrect. Realized capital gains are amortized under statutory accounting, delaying immediate earnings boosts.",
        "explanation": "Statutory accounting prevents immediate profit realization from bond sales through mechanisms like the Interest Maintenance Reserve (IMR).",
        "score": 2
    },
    {
        "question": "Calculate the price of each bond and recommend one for a 10-year liability given rising interest rates. Data: (1) 11%, 10 years, 5.0%; (2) 7%, 20 years, 6.1%; (3) 0%, 15 years, 2.2%; (4) 6%, 5 years, 8.4%.",
        "correctAnswer": "Prices: Bond 1 = $1,467.67, Bond 2 = $1,127.49, Bond 3 = $742.10, Bond 4 = $872.59. Recommend Bond 4.",
        "explanation": "Bond 4 minimizes duration risk and allows reinvestment at higher rates, aligning with the rising interest rate environment.",
        "score": 3,
        "data":
        [
            ["Bond", "Coupon Rate", "Coupon frequency", "Term (Years)", "Yield to maturiy", "Maturity value"],
            ["Bond 1", "11%", "Semi-annual", 10, "5.0%", "$1,000"],
            ["Bond 2", "7%",  "Semi-annual", 20, "6.1%", "$1,000"],
            ["Bond 3", "0%", "N/A", 15, "2.2%", "$1,000"],
            ["Bond 4", "6%", "Semi-annual", 5, "8.4%", "$1,000"],
        ]
    }
]
    
