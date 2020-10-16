import sys

from PyQt5.QtWidgets import (QWidget, QApplication, QGridLayout, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout, QFileDialog)
from PyQt5 import QtGui
from PyQt5 import QtCore

from Lib import CalendarManager


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.set_window()

    def set_window(self):
        self.setWindowTitle('Lunar Date Converter')
        self.setGeometry(150, 150, 400, 100)
        main_layout = QVBoxLayout()
        field_layout = QGridLayout()
        label_subject = QLabel('INPUT SUBJECT | ')
        self.field_subject = QLineEdit()
        label_first_year = QLabel('FIRST YEAR | ')
        self.first_year = QLineEdit()
        label_last_year = QLabel('LAST YEAR | ')
        self.last_year = QLineEdit()
        label_date = QLabel('INPUT DATE | ')
        self.field_date = QLineEdit()

        self.field_path = QLineEdit()
        self.btn_find_path = QPushButton('FIND PATH')

        self.btn_export = QPushButton('EXPORT CSV')
        field_layout.addWidget(label_subject, 0, 0, 1, 1)
        field_layout.addWidget(self.field_subject, 0, 1, 1, 5)
        field_layout.addWidget(label_first_year, 1, 0, 1, 1)
        field_layout.addWidget(self.first_year, 1, 1, 1, 2)
        field_layout.addWidget(label_last_year, 1, 3, 1, 1)
        field_layout.addWidget(self.last_year, 1, 4, 1, 2)
        field_layout.addWidget(label_date, 2, 0, 1, 1)
        field_layout.addWidget(self.field_date, 2, 1, 1, 5)
        field_layout.addWidget(self.btn_find_path, 3, 0, 1, 1)
        field_layout.addWidget(self.field_path, 3, 1, 1, 5)
        main_layout.addLayout(field_layout)
        main_layout.addWidget(self.btn_export)
        self.setLayout(main_layout)

        self.btn_find_path.clicked.connect(self.find_path)
        self.btn_export.clicked.connect(self.export_csv)
        self.show()

    def find_path(self):
        path = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.field_path.setText(path)

    def export_csv(self):
        path = self.field_path.text()
        subject = self.field_subject.text()
        first_year = self.first_year.text()
        last_year = self.last_year.text()
        date = self.field_date.text().split()
        csv_getter = CalendarManager.CSVGetter(subject, int(first_year),
                                               int(last_year), int(date[0]),
                                               int(date[1]))
        csv_getter.get_solar_days()
        csv_getter.write_csv(path)
        return True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
