import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    distinct_salaries = employee['salary'].drop_duplicates()
    
    sorted_salaries = distinct_salaries.sort_values(ascending=False)
    
    if len(sorted_salaries) >= 2:
        second_highest = sorted_salaries.iloc[1]
    else:
        second_highest = None
    
    return pd.DataFrame({'SecondHighestSalary': [second_highest]})