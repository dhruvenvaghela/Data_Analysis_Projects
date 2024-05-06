import pandas as pd

df = pd.read_csv('adult.data.csv')

#Q1: 
# series = pd.Series((df.groupby(['race']).race.count()))
# series.index.set_names(['race names'], inplace=True)

# seies = pd.Series((df.race.unique().sum()))
# print(seies)

#Q2:
#avage  = round(df.loc[(df.sex == 'Male')].age.mean(),1)
#print(avage)

#Q3:
# bech = (df.education[(df.education=='Bachelors')].count())
# per = round(bech/len(df)*100,1)
# print(per)

#Q4 & Q5:
# bech = (df.loc[((df.education=='Bachelors') | (df.education=='Masters') | (df.education=='Doctorate')) & ((df.salary=='>50K'))].salary.count())
# base = (df.loc[((df.education=='Bachelors') | (df.education=='Masters') | (df.education=='Doctorate'))].salary.count())
# per = round(bech/base*100,1)


# bech1 = (df.loc[~((df.education=='Bachelors') | (df.education=='Masters') | (df.education=='Doctorate')) & ((df.salary=='>50K'))].salary.count())
# base1 = (df.loc[~((df.education=='Bachelors') | (df.education=='Masters') | (df.education=='Doctorate'))].salary.count())
# per1 = round((bech1/base1)*100,1)
# print(per1)

#Q6:
# minw = df.loc[:]['hours-per-week']
# print(minw.min())

#Q7
# min_work_hours = df.loc[:]['hours-per-week'].min()
# bech2 = (df.loc[(df.loc[:]['hours-per-week']==min_work_hours) & ((df.salary=='>50K'))].salary.count())
# base2 = (df.loc[(df.loc[:]['hours-per-week']==min_work_hours)].salary.count())
# print(bech2/base2*100)

#Q8
# x = (df.loc[:]['native-country'][df.salary=='>50K']).value_counts()
# y = (df.loc[:]['native-country']).value_counts()

# z = x/y
# subseries =z[z == max(x/y)]
# label = subseries.index[0]
# print(label)
# print(round(max(x/y)*100,1))

#Q9: India
rich = df.occupation[(df.salary=='>50K') & (df.loc[:]['native-country']=='India')].value_counts()
rich = rich.sort_values(ascending=False)
occu = rich.index[0]
print(occu)