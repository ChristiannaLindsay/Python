import streamlit as st

st.title("Using Logistic Regression to Predict Happiness with the General Social Survey")

# Overview
st.write("\n")
st.write("R Code for this project: https://github.com/ChristiannaLindsay/GSS_Happiness_project")
st.subheader("Project Overview", anchor=False)
st.write(
    """
    The goal of this project is to predict the likelihood of someone being very happy,
    given factors such as political orientation, race, age, and marital status.
    Logistic regression is used to measure the importance of independent variables in
    predicting the likelihood of a binary outcome variable. In this case, the outcome
    of interest is being “very happy” as opposed to “pretty happy,” “not too happy,”
    or “do not know/cannot choose,” and the independent variables are certain other
    survey responses. Figure 4 shows the estimated effect of each variable on the odds
    that a person is “very happy,” while holding constant all other variables in the
    model.

    The data for this project is from the General Social Survey, using the years
    2016-2022. The GSS data is available for the even-numbered years between 2000 and 2022,
    excepting 2020 and including 2021. Among the several variables available to weight
    the GSS survey data, WTSSNRPS is chosen for this project, as it contains a nonresponse adjustment
    and is recommended for the years 2004-2022 (Post-stratification Weights for GSS
    1972-2022).
    """
)
st.subheader("Model 1", anchor=False)

st.write(
    """
    In this first model, the probability of being “very happy” is modeled with
    logistic regression using partisanship, age, race, and sex. The significant
    predictors of happiness in this model are partisanship, age, and race. Sex is
    not a significant predictor of happiness. The model is summarized in Table 1,
    and we can interpret the results as follows:

    - The odds of being very happy are 1.541 times greater for Republicans than Democrats, with all other variables being equal.
    - The odds of being very happy are increased by a factor of 1.006 for each one-year increase in age, with all other variables being equal.
    - The odds of being very happy are 1.455 times greater for “other” races than white people, with all other variables being equal
    """
)
with st.columns(6)[1]:
     st.image("./assets/Model1.png", width=500)
     st.caption("Table 1")

st.subheader("Model 2", anchor=False)
st.write(
    """
     In the second model, marital status is added as a predictor. This time,
     the significant predictors of happiness are partisanship, race, and marital
     status. Age is not a significant predictor of happiness, nor is sex. The model
     is summarized in Table 2, and the results are interpreted as follows:
     - The odds of being very happy are 1.451 times greater for Republicans than Democrats, with all other variables being equal.
     - The odds of being very happy are 1.448 times greater for “other” races than white people, with all other variables being equal.
     - The odds of being very happy are 2.415 times greater for married adults than unmarried adults, with all other variables being equal.
    """
)
#st.image("./assets/Model2.png", width=600)
#st.caption("Figure 2")

with st.columns(6)[1]:
     st.image("./assets/Model2.png", width=500)
     st.caption("Table 2")



st.subheader("Model 3", anchor=False)
st.write(
    """
    Model 3: In this third model, marital status is replaced by marital happiness,
    where marital happiness is a binary variable outcome defined by being “very happy”
    in marriage versus “pretty happy,” “not too happy,” “do not know/cannot choose,” or
    “inapplicable.” Note that unmarried people count as not “very happy” in marriage.
    This time, the significant predictors of happiness are partisanship, race, and
    marital happiness. Neither age nor sex are significant predictors of happiness.
    The model is summarized in Table 3, and the results are interpreted as follows:
    - The odds of being very happy are 1.328 times greater for Republicans than Democrats, with all other variables being equal.
    - The odds of being very happy are 1.278 times greater for black vs. white people, with all other variables being equal.
    - The odds of being very happy are 1.659 times greater for “other” races than white people, with all other variables being equal.
    - The odds of being very happy are 5.697 times greater for very happily married adults, with all other variables being equal.
    """
)
with st.columns(6)[1]:
     st.image("./assets/Model3.png", width=500)
     st.caption("Table 3")

st.subheader("Happiness and Political Affiliation", anchor=False)

st.image("./assets/odds_ratios.png", width=700)
st.caption("Figure 1")

st.write(
    """
    In the above models, we see that happiness is associated with partisanship,
    where a Republican has 1.541 times the odds a Democrat does of being very happy,
    holding constant age, race, and sex. We may wonder whether someone's political
    orientation influences their happiness or
    whether there is another underlying variable causing the association.
    """)

with st.columns(6)[1]:
     st.image("./assets/married.png", width=500)
     st.caption("Figure 2")

st.write(
    """
    To investigate this question, consider Model 2, where marital status is added as
    a predictor variable. In Model 2, the odds ratio for Republican vs. Democrat decreases
    to 1.451 (Table 2), while the odds ratio for married vs. unmarried is larger,
    at 2.415 (Figure 1). The larger odds ratio for marital status means being married has a greater effect
    on happiness than partisanship does. The fact that the odds ratio for partisanship
    decreases when marital status is added to the model means that the association between partisanship
    and happiness may be due to in part to marital status, as more Republicans tend to
    be married than Democrats.
    """
)

with st.columns(6)[1]:
     st.image("./assets/happily_married.png", width=500)
     st.caption("Figure 3")

st.write(
    """
    Considering marital happiness rather than marital status in Model 3 gives us greater insight.
    Comparing Model 3 with Model 2, the effect of partisanship on happiness decreases further to an
    odds ratio of 1.328,
    while the odds ratio of marital happiness is a weighty 5.697 (the greatest effect size yet). Given the strong effect
    of marital happiness on overall happiness, and given that more Republicans tend to be
    in very happy marriages than Democrats (Figure 3), this may partially explain why
    Republicans tend to be more happy.
    """
)

st.subheader("Takeaways", anchor=False)

st.write(
    """
    Even when holding constant age, race, and marital happiness, Republicans are still a bit happier
    on average than Democrats (Model 3).
    Thus, marriage and marital happiness appear to partially but not completely explain the partisan-happiness
    link. The significant predictors of happiness in our three models are race, political affiliation,
    age, marital status, and marital happiness, with marital happiness being the most important factor.
    While it may or may not be a causal factor,
    having a very happy marriage is strongly associated with being very happy generally.
    """
)