from PyQt5.QtCore import Qt
from sqlalchemy import create_engine  # pip install SQLAlchemy
from sqlalchemy.engine import URL
import pypyodbc  # pip install pypyodbc
import pandas as pd  # pip install pandas
import pyodbc
import sqlite3
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.express as px
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtChart import QChartView, QChart, QPieSeries, QPieSlice


class TransactionPieChartApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Transaction Pie Chart")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        # Create a QChart and QChartView
        chart = QChart()
        chart.setTitle("Distribution of Transactions by Business Code")
        chart_view = QChartView(chart)
        layout.addWidget(chart_view)

        conn = self.read_and_connect()
        query_results = self.run_query(conn)


        conn.close()

        # Extract data for plotting
        #labels = x_data
        #sizes = y_data

        # Create a QPieSeries and add slices
        #series = QPieSeries()
        #for label, size in zip(labels, sizes):
        #    slice = QPieSlice(label, size)
        #    series.append(slice)

        # Add the series to the chart
        #chart.addSeries(series)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        self.show()


    def run_query(self, conn):
        # Run SQL queries using pandas and SQLite
        query = '''
                                      SELECT "Code", COUNT(*) AS TotalTransactions
                                      FROM my_table
                                      GROUP BY "Code"
                                      ORDER BY TotalTransactions DESC
                                  '''
        results = conn.execute(query)
        return results



    def read_and_connect(self):
        # Read Excel data into a DataFrame
        excel_file = 'states.xlsx'
        df = pd.read_excel(excel_file)

        # Create an in-memory SQLite database
        conn = sqlite3.connect(':memory:')
        df.to_sql('my_table', conn, index=False)

        return conn

def main():
    app = QApplication(sys.argv)
    window = TransactionPieChartApp()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
