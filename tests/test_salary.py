from src.salary_analyzer import SalaryAnalyzer


def test_load_data():
    analyzer = SalaryAnalyzer("data/employees.csv")
    data = analyzer.load_data()
    assert data is not None
