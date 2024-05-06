import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    ses = pd.Series((df.groupby(['race']).race.count()))
    race_count = pd.Series(df.race.value_counts(), name='race names')
    
    # What is the average age of men?
    average_age_men = round(df.loc[(df.sex == 'Male')].age.mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    bechx = (df.education[(df.education=='Bachelors')].count())
    percentage_bachelors = round(bechx/len(df)*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    bech = (df.loc[((df.education=='Bachelors') | (df.education=='Masters') | (df.education=='Doctorate')) & ((df.salary=='>50K'))].salary.count())
    base = (df.loc[((df.education=='Bachelors') | (df.education=='Masters') | (df.education=='Doctorate'))].salary.count())
    bech1 = (df.loc[~((df.education=='Bachelors') | (df.education=='Masters') | (df.education=='Doctorate')) & ((df.salary=='>50K'))].salary.count())
    base1 = (df.loc[~((df.education=='Bachelors') | (df.education=='Masters') | (df.education=='Doctorate'))].salary.count())

    higher_education = base
    lower_education = base1

    # percentage with salary >50K
    higher_education_rich = round(bech/base*100,1)
    lower_education_rich = round(bech1/base1*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df.loc[:]['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K? 
    num_min_workers = (df.loc[(df.loc[:]['hours-per-week']==min_work_hours)].salary.count())
    bech2 = (df.loc[(df.loc[:]['hours-per-week']==min_work_hours) & ((df.salary=='>50K'))].salary.count())
    rich_percentage = round(bech2/num_min_workers*100,1)

    # What country has the highest percentage of people that earn >50K?
    x = (df.loc[:]['native-country'][df.salary=='>50K']).value_counts()
    y = (df.loc[:]['native-country']).value_counts()
    z = x/y
    subseries =z[z == max(x/y)]
    label = subseries.index[0]

    highest_earning_country = label
    highest_earning_country_percentage = round(max(x/y)*100,1)

    # Identify the most popular occupation for those who earn >50K in India.

    rich = df.occupation[(df.salary=='>50K') & (df.loc[:]['native-country']=='India')].value_counts()
    rich = rich.sort_values(ascending=False)
    top_IN_occupation = rich.index[0]

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
