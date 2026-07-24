import pandas as pd
from logger import logger

class SalaryAnalyzer:

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
    try:
        self.data = pd.read_csv(self.file_path)
        logger.info("Employee data loaded successfully")
        return self.data
        
    def average_salary(self):
    avg_salary = self.data["Salary"].mean()
    logger.info(f"Average Salary: {avg_salary}")
    return avg_salary
    
    def highest_salary(self):
    highest = self.data["Salary"].max()
    logger.info(f"Highest Salary: {highest}")
    return highest

    def lowest_salary(self):
    lowest = self.data["Salary"].min()
    logger.info(f"Lowest Salary: {lowest}")
    return lowest

    def department_average_salary(self):
    dept_avg = self.data.groupby("Department")["Salary"].mean()
    logger.info("Calculated department-wise average salary")
    return dept_avg

    def top_5_highest_paid(self):
    top_employees = self.data.sort_values(by="Salary", ascending=False).head(5)
    logger.info("Fetched top 5 highest paid employees")
    return top_employees

    except Exception as e:
        logger.error(f"Error loading file: {e}")
        print("Failed to load employee data.")

if __name__ == "__main__":
    analyzer = SalaryAnalyzer("data/employees.csv")
    df = analyzer.load_data()
    print(df)
print("Average Salary:", analyzer.average_salary())
print("Highest Salary:", analyzer.highest_salary())
print("Lowest Salary:", analyzer.lowest_salary())
print("\nDepartment-wise Average Salary")
print(analyzer.department_average_salary())
print("\nTop 5 Highest Paid Employees")
print(analyzer.top_5_highest_paid())
