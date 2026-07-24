# Employee Salary Analyzer - Project Notes

## Project Objective
Analyze employee salary data using Python and Pandas.

---

# src/salary_analyzer.py

## __init__()
Purpose:
- Store CSV file path.
- Initialize DataFrame variable.

---

## load_data()
Purpose:
- Read employee data from CSV.

Methods Used:
- pd.read_csv()
- try/except

Interview:
Reads CSV safely using exception handling.

---

## average_salary()
Purpose:
- Calculate average salary.

Method Used:
- mean()

Interview:
Returns average employee salary.

---

## highest_salary()
Purpose:
- Find highest salary.

Method Used:
- max()

Interview:
Returns highest employee salary.

---

## lowest_salary()
Purpose:
- Find lowest salary.

Method Used:
- min()

Interview:
Returns lowest employee salary.

---

## department_average_salary()
Purpose:
- Calculate average salary for each department.

Methods Used:
- groupby()
- mean()

Interview:
Groups employees by department and calculates average salary.

---

## top_5_highest_paid()
Purpose:
- Display top 5 highest paid employees.

Methods Used:
- sort_values()
- head()

Interview:
Sorts salaries in descending order and returns top 5 employees.

---

## employee_count_by_department()
Purpose:
- Count employees in each department.

Methods Used:
- groupby()
- size()

Interview:
Returns employee count for every department.

---

# src/logger.py

Purpose:
- Store application logs.

Methods Used:
- logging.basicConfig()
- logger.info()
- logger.error()

Interview:
Logs application events and errors.

---

# tests/test_salary.py

Purpose:
- Verify CSV loading works correctly.

Methods Used:
- pytest
- assert

Interview:
Checks whether employee data is loaded successfully.

---

# .github/workflows/python.yml

Purpose:
- Run tests automatically after every push.

Interview:
Configured GitHub Actions for Continuous Integration (CI).

---

# README.md

Purpose:
- Explain project, features and setup.

---

# Skills Used

- Python
- Pandas
- OOP
- Exception Handling
- Logging
- Pytest
- GitHub Actions
- GitHub
