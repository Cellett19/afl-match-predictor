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

### Logistic Regression

The current baseline model uses a time-based train/test split:

- Training data: 2000–2020
- Testing data: 2021–2023
- Model: Logistic Regression
- Features: Historical team performance and recent form

| Metric | Result |
|---------|-------:|
| Accuracy | 65.37% |
| Home Precision | 65% |
| Home Recall | 84% |
| Away Precision | 67% |
| Away Recall | 41% |
| Macro F1 | 0.62 |

The model currently performs better at identifying home wins than away wins, indicating a bias toward predicting the home team.

### Random Forest

A Random Forest model was also evaluated using the same training and testing data.

| Model | Accuracy |
|-------|---------:|
| Accuracy | 62.20% |
| Home Precision | 63% |
| Home Recall | 81% |
| Away Precision | 61% |
| Away Recall | 38% |
| Macro F1 | 0.59 |

Logistic Regression currently performs better than Random Forest and is therefore the current baseline model.

All evaluation uses a chronological train/test split rather than a random split. This better represents the real-world scenario of training on historical seasons and predicting future matches.
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

- Analyse Logistic Regression feature coefficients
- Add head-to-head statistics
- Add rolling team form features
- Add additional team performance features
- Compare additional machine learning models
  - Logistic Regression
  - Random Forest
  - Gradient Boosting
- Tune model hyperparameters
- Evaluate feature importance
- Experiment with different feature combinations
- Evaluate model performance using time-based validation

### Data

- Expand the historical dataset
- Investigate automated AFL data collection
- Build a data scraping pipeline
- Automatically update the processed dataset with new matches

### Application

- Build an interactive Streamlit dashboard
- Predict match winners
- Display prediction probabilities
- Allow users to select upcoming matches
- Simulate AFL seasons

---

## Development Log

### Version 0.1
- Initial repository setup
- Imported historical AFL dataset

### Version 0.2
- Completed exploratory data analysis
- Created visualisations for team statistics

### Version 0.3
- Refactored notebook analysis into reusable functions

### Version 0.4
- Moved analysis code into Python modules

### Version 0.5
- Built initial feature engineering pipeline
- Generated historical match features without data leakage
- Created first machine learning training dataset

### Version 0.6
- Expanded feature engineering with:
  - Home & away average points for
  - Home & away average points conceded
  - Home & away average point differential
  - Last 5 match win percentage
  - Last 5 average points for
  - Last 5 average points conceded
  - Last 5 average point differential

### Version 1.0
- Built initial Logistic Regression prediction model
- Created model evaluation pipeline
- Added accuracy, confusion matrix and classification report
- Created first machine learning release

### Version 1.1
- Implemented chronological train/test split
- Trained on 2000–2020 seasons
- Tested on 2021–2023 seasons
- Added feature scaling
- Compared Logistic Regression against Random Forest
- Logistic Regression achieved 65.37% accuracy
- Random Forest achieved 62.20% accuracy

### Next Steps
- Analyse feature coefficients
- Add head-to-head statistics
- Add additional rolling form features
- Test further machine learning models
- Improve model performance

---

## Author

**Ciaran Ellett**

Bachelor of Computer Science (Software Engineering)
Edith Cowan University
