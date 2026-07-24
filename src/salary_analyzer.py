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

    except Exception as e:
        logger.error(f"Error loading file: {e}")
        print("Failed to load employee data.")

if __name__ == "__main__":
    analyzer = SalaryAnalyzer("data/employees.csv")
    df = analyzer.load_data()
    print(df)
