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

### Feauture Engineering

- Generate machine learning features using only historical match data
- Prevent data leakage by calculating statistics from matches played before each fixture
- Create a training dataset containing:
  - Home team
  - Away team
  - Home win percentage
  - Away win percentage
  - Match winner (target variable)

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
    ├── afl_analysis.ipynb
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

### Next Version
- Expand feature engineering with additional team statistics

---

## Author

**Ciaran Ellett**

Bachelor of Computer Science (Software Engineering)
Edith Cowan University
