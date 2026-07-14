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

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Git
- GitHub

---

## Project Structure

afl-match-predictor/
│
├── data/
├── docs/
│   └── graphs/
├── notebooks/
│   ├── afl_analysis.ipynb
├── source/
│   ├── stats.py
│   ├── visualisation.py
│   └── features.py
├── README.md

## Future Development

### Machine Learning

- Expand feature engineering
  - Average points scored
  - Average points conceded
  - Average point differential
  - Recent team form
  - Head-to-head statistics
- Train baseline classification models
- Evaluate model performance
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

### Next Version
- Train baseline machine learning models
- Evaluate prediction accuracy

---

## Author

**Ciaran Ellett**

Bachelor of Computer Science (Software Engineering)
Edith Cowan University
