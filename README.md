# AFL Match Predictor

A Python-based data analysis and machine learning project that explores historical AFL match data to identify performance trends and predict future match outcomes.

This project is being developed as part of my software engineering portfolio while completing my Bachelor of Computer Science (Software Engineering).

---

## Project Goals

- Analyse historical AFL match data
- Engineer features suitable for machine learning
- Train models to predict AFL match winners
- Build an interactive prediction application using Streamlit

---

## Current Features

### Feature Engineering

- Historical home win percentage
- Historical away win percentage
- Historical average points scored
- Historical average points conceded
- Historical average point differential
- Last 5 match win percentage
- Last 5 match average points scored
- Last 5 match average points conceded
- Last 5 match average point differential

All features are generated using only information available before each match, preventing data leakage and ensuring the model can be used for future match prediction.

### Exploratory Data Analysis

- Calculate games played for every AFL team
- Calculate total wins for every AFL team
- Calculate overall team win percentages
- Calculate home and away win percentages
- Calculate average points scored
- Calculate average points conceded
- Calculate average winning margins
- Analyse league-wide home ground advantage
- Calculate average point differential

### Visualisations

- Competition Home Advantage
![Competition Home Advantage](docs/graphs/winning_percentage_by_home_and_away_teams_(2000-2023).png)
- Team win percentage
![Team Win Percentage](docs/graphs/team_win_percentages_(2000-2023).png)
- Home win percentage
![Home Win Percentage](docs/graphs/teams_home_win_percentages_(2000-2023).png)
- Away win percentage
![Away Win Percentage](docs/graphs/teams_away_win_percentages_(2000-2023).png)
- Average points scored
![Average Points Scored](docs/graphs/average_points_per_team_(2000-2023).png)
- Average points conceded
![Average Points Conceded](docs/graphs/average_points_conceded_per_team_(2000-2023).png)
- Average winning margin
![Average Winning Margin](docs/graphs/average_winning_margin_per_team_(2000-2023).png)
- Average point differential
![Average Point Differential](docs/graphs/teams_average_points_differential_(2000-2023).png)

## Current Model Performance

Baseline Logistic Regression (2000–2023 dataset)

| Metric | Result |
|---------|-------:|
| Accuracy | 67.1% |
| Precision (Home) | 68% |
| Recall (Home) | 82% |
| Precision (Away) | 65% |
| Recall (Away) | 47% |

This baseline model was trained using engineered historical features generated only from matches that occurred before each prediction, preventing data leakage.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- scikit-learn
- Jupyter Notebook
- Git
- GitHub

---

## Project Structure

afl-match-predictor/
│
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   └── graphs/
├── notebooks/
│   └── afl_analysis.ipynb
├── source/
│   ├── stats.py
│   ├── features.py
│   ├── visualisation.py
│   └── model.py
├── README.md

## Future Development

### Machine Learning

- Compare multiple machine learning models
  - Logistic Regression
  - Random Forest
  - Gradient Boosting
- Tune model hyperparameters
- Evaluate using time-based validation
- Analyse feature importance
- Add additional predictive features
- Optimise features and hyperparameters

### Application

- Build an interactive Streamlit dashboard
- Predict match winners
- Display prediction probabilities
- Simulate AFL seasons

---

## Machine Learning Pipeline

1. Load historical AFL data
2. Perform exploratory data analysis
3. Generate historical features using previous matches only
4. Train prediction models
5. Evaluate model performance
6. Predict future AFL matches

---

## Development Log

### Version 0.1
- Initial repository setup
- Imported historical AFL dataset

### Version 0.2
- Completed exploratory data analysis
- Created visualisations for team statistics

### Version 0.3
- Refactor notebook into reusable functions

### Version 0.4
- Move code into Python modules in VScode

### Version 0.5
- Built initial feature engineering pipeline
- Generated historical match features without data leakage
- Created first machine learning training dataset

### Version 0.6
- Expanded feature engineering with
    - Home & Away teams average points for
    - Home & Away teams average points against
    - Home & Away teams average points differentials
    - Last 5 games feature engineering

### Version 1.0
- Built baseline Logistic Regression model
- Achieved 67.1% prediction accuracy
- Added model evaluation using confusion matrix and classification report

### Next Version
- Compare Logistic Regression with Random Forest
- Implement time-based train/test split
- Add head-to-head statistics
- Add rolling team form features

---

## Author

**Ciaran Ellett**

Bachelor of Computer Science (Software Engineering)
Edith Cowan University
