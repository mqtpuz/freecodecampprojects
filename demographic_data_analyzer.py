import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the
    # index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = np.round((df[df['sex'] == 'Male']['age'].mean()), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bool_mask = df['education'] == 'Bachelors'
    percentage_bachelors = np.round(100 * bool_mask.sum() / bool_mask.size, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') |
                          (df['education'] == 'Doctorate')]['salary']
    lower_education = df[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') |
                           (df['education'] == 'Doctorate'))]['salary']

    # percentage with salary >50K
    higher_education_rich = np.round(100 * higher_education.value_counts().loc['>50K'] /
                                     higher_education.value_counts().sum(), 1)
    lower_education_rich = np.round(100 * lower_education.value_counts().loc['>50K'] /
                                    lower_education.value_counts().sum(), 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    bool_mask = df[df['hours-per-week'] == df['hours-per-week'].min()]['salary'] == '>50K'

    num_min_workers = bool_mask.size

    rich_percentage = np.round(100 * bool_mask.sum() / num_min_workers, 1)

    # What country has the highest percentage of people that earn >50K?
    countries = df['native-country'].unique()
    countries.sort()

    high_wage_prcnt = pd.Series(dtype=np.float32)

    for country in countries:
        bool_mask = df[df['native-country'] == country]['salary'] == '>50K'
        high_wage_prcnt[country] = np.round(100 * bool_mask.sum() / bool_mask.size, 1)

    highest_earning_country = high_wage_prcnt.loc[high_wage_prcnt == high_wage_prcnt.max()].index[0]
    highest_earning_country_percentage = high_wage_prcnt.max()

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') |
                           (df['salary'] == '>50K')]['occupation'].describe().loc['top']

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
