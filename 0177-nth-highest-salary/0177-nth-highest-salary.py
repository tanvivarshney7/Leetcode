import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salary = employee["salary"].drop_duplicates().nlargest(N)

    if N <= 0 or len(salary) < N:
        return pd.DataFrame(
            {f"getNthHighestSalary({N})": [None]}
        )

    return pd.DataFrame(
        {f"getNthHighestSalary({N})": [salary.iloc[-1]]}
    )