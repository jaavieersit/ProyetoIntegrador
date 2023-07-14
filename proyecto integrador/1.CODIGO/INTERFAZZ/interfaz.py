import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import csv

class Dataset(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visor de CSV")
        self.setGeometry(200, 200, 600, 400)

        self.table = QTableWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        self.load_csv_data()

    def load_csv_data(self):
        with open("Dataset.csv", newline="", encoding="utf-8-sig") as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            self.table.setRowCount(len(data))
            self.table.setColumnCount(len(data[0]))

            for row_idx, row_data in enumerate(data):
                for col_idx, col_data in enumerate(row_data):
                    item = QTableWidgetItem(col_data)
                    self.table.setItem(row_idx, col_idx, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = Dataset()
    viewer.show()
    sys.exit(app.exec())
