import pandas as pd

data = {
    'Names': ["Messi","Aishik","Kushagra","Sambhav","Jackson","Shaw"],
    "Age": [38,23,25,25,28,29],
    "Salary": [50000,10000,150000,250000,240000,210000]
}
dataframe=pd.DataFrame(data)
print(dataframe)
print(dataframe.head(3))
print(dataframe.tail(3))
series=pd.Series(data['Names'])
print(series)
print(dataframe.describe())   #all mathematical values for our data
print(dataframe.info)
print(dataframe[['Names','Salary']])
print(dataframe[(dataframe["Age"] > 26) & (dataframe["Salary"] > 50000)])
print(dataframe[(dataframe["Age"]==25)])

unique_salaries = dataframe["Salary"].unique()  
sorted_salaries = sorted(unique_salaries, reverse=True) 

if len(sorted_salaries) > 1:
    second_max_salary = sorted_salaries[1]  
    print(f"The second maximum salary is: {second_max_salary}")

max_salary=dataframe["Salary"].max()
print(max_salary)
#or

def max_salaryy(dataframe):
    max_sal=dataframe['Salary'][0]
    sec_max_sal=dataframe['Salary'][0]
    for i in dataframe['Salary']:
        if i>=max_sal:
            max_sal,sec_max_sal=i,max_sal
        elif i>sec_max_sal:
            i=sec_max_sal
    print(sec_max_sal)

max_salaryy(dataframe)
