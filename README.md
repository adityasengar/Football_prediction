
# Bundesliga Predictive Modeling

This repository contains code snippets for building a predictive model for English Premier League (EPL) matches using various machine learning techniques. The goal is to predict the outcome of future EPL matches based on historical data.

## Dataset

The dataset used for this project consists of historical EPL match data, including information such as match results, team statistics, and matchweek. The dataset is divided into multiple files for different seasons.

## Features

The code snippets perform various feature engineering steps to extract relevant information from the dataset. The features include:

- Home team and away team statistics
- Goals scored and conceded by teams
- Points accumulated by teams
- Recent form of teams
- Win streaks and loss streaks of teams
- TrueSkill rankings of teams

## Data Preprocessing

Before training the machine learning models, the data is preprocessed and transformed. The preprocessing steps include:

- Standardizing the numerical features
- Converting categorical variables into dummy variables

## Machine Learning Models

The following machine learning models are implemented and trained on the preprocessed data:

- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier
- Multilayer Perceptron (Neural Network)

## TrueSkill Ranking

In addition to the machine learning models, the code includes an implementation of TrueSkill ranking. TrueSkill is a ranking system that models the skill of players/teams based on the outcomes of matches. The TrueSkill rankings are updated after each match to reflect the updated skill levels of the teams.

## Evaluation

The performance of the predictive models is evaluated using classification metrics such as confusion matrix, precision, recall, and F1-score. The models are trained on a portion of the dataset and tested on the remaining portion to assess their accuracy in predicting match outcomes.

---

This README file provides a brief overview of the code snippets included in this repository. For detailed implementation and usage instructions, please refer to the code comments and documentation provided within the code files.

