# -*- coding: utf-8 -*-
import sqlite3

import pandas as pd
# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from PyQt5.QtWidgets import QListWidget, QTableWidgetItem


class ListBoxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(600, 600)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().urls():
                # https://doc.qt.io/qt-5/qurl.html
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
                else:
                    links.append(str(url.toString()))
            self.addItems(links)
        else:
            event.ignore()

class Ui_Title(object):
    def setupUi(self, Title):
        Title.setObjectName("Title")
        Title.setWindowModality(QtCore.Qt.WindowModal)
        Title.resize(1323, 865)
        Title.setStyleSheet("background-color: rgb(169, 230, 255)")
        self.centralwidget = QtWidgets.QWidget(Title)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 10, 761, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_2.setObjectName("label_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 420, 1301, 401))
        self.scrollArea.setStyleSheet("background-color: rgb(180, 203, 213)")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1299, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setStyleSheet("background-color: rgb(236, 234, 234)")
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setGeometry(QtCore.QRect(20, 130, 321, 271))
        self.verticalFrame.setStyleSheet("background-color: rgb(211, 211, 211)")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalFrame)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)


        self.listWidget = QtWidgets.QListWidget(self.verticalFrame)
        self.listWidget.setStyleSheet("background-color: rgb(235, 235, 235)")
        self.listWidget.setObjectName("listWidget")
        # Enable drag and drop
        self.listWidget.setAcceptDrops(True)
        self.listWidget.setDropIndicatorShown(True)
        # Connect the drag and drop signals
        self.listWidget.dragEnterEvent = self.dragEnterEvent
        self.listWidget.dragMoveEvent = self.dragMoveEvent
        self.listWidget.dropEvent = self.dropEvent



        self.verticalLayout_2.addWidget(self.listWidget)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButton_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n""")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(920, 260, 381, 155))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_3.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_2.setStyleSheet("background-color: rgb(206, 206, 206)")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_7 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_7.setChecked(True)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 1, 2, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 0, 2, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 1, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 0, 1, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_11.setChecked(True)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout.addWidget(self.checkBox_11, 3, 1, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_9.setChecked(True)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 2, 1, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_8.setChecked(True)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 2, 2, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 1, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 3, 0, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_12.setChecked(True)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout.addWidget(self.checkBox_12, 3, 2, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_10.setChecked(True)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout.addWidget(self.checkBox_10, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_3.addWidget(self.widget_2)
        Title.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Title)
        self.statusbar.setObjectName("statusbar")
        Title.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(Title)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1323, 21))
        self.menuBar.setStyleSheet("background-color: rgb(194, 194, 194) ")
        self.menuBar.setObjectName("menuBar")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setStyleSheet("background-color: rgb(199, 226, 255)")
        self.menuSettings.setObjectName("menuSettings")
        Title.setMenuBar(self.menuBar)
        self.actionSave = QtWidgets.QAction(Title)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtWidgets.QAction(Title)
        self.actionQuit.setObjectName("actionQuit")
        self.menuSettings.addAction(self.actionSave)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(Title)
        QtCore.QMetaObject.connectSlotsByName(Title)

    def retranslateUi(self, Title):
        _translate = QtCore.QCoreApplication.translate
        Title.setWindowTitle(_translate("Title", "FinTrack Home"))
        self.label_2.setText(_translate("Title", "<html><head/><body><p><span style=\" color:#101010;\">FinTrack - Bank Statement Analytics Tool</span></p></body></html>"))
        self.label_5.setText(_translate("Title", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; text-decoration: underline; color:#0d0d0d;\">Your Purchase History</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Title", "Transaction Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Title", "Processed Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Title", "Transaction Type"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Title", "Details"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Title", "Particulars"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Title", "Code"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Title", "Reference"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Title", "Amount"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Title", "Balance"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Title", "To/From Account"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Title", "Conversion Charge"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Title", "Foreign Currency Amount"))
        self.label.setText(_translate("Title", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#15008f;\">Drop Bank Statement</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#15008f;\">(Supported: .xlsx)</span></p></body></html>"))

        self.pushButton_2.setText(_translate("Title", "Submit"))
        self.pushButton_2.clicked.connect(self.submit_button_clicked)


        self.label_3.setText(_translate("Title", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600;\">Search:</span></p></body></html>"))
        self.pushButton.setText(_translate("Title", "View Results"))
        self.checkBox_7.setText(_translate("Title", "To/From Account"))
        self.checkBox_6.setText(_translate("Title", "Balance"))
        self.checkBox_5.setText(_translate("Title", "P. Date"))
        self.checkBox_3.setText(_translate("Title", "Particulars"))
        self.checkBox_11.setText(_translate("Title", "Amount"))
        self.checkBox_9.setText(_translate("Title", "References"))
        self.checkBox_8.setText(_translate("Title", "Conversion Charge"))
        self.checkBox_4.setText(_translate("Title", "Code"))
        self.checkBox.setText(_translate("Title", "T. Type"))
        self.checkBox_2.setText(_translate("Title", "Details"))
        self.checkBox_12.setText(_translate("Title", "Foreign Currency "))
        self.checkBox_10.setText(_translate("Title", "T. Date"))
        self.menuSettings.setTitle(_translate("Title", "File"))
        self.actionSave.setText(_translate("Title", "Save "))
        self.actionQuit.setText(_translate("Title", "Quit"))

        checkBoxList = [self.checkBox_10, self.checkBox_5, self.checkBox, self.checkBox_2
                        , self.checkBox_3, self.checkBox_4, self.checkBox_9, self.checkBox_11,
                        self.checkBox_6, self.checkBox_7, self.checkBox_8, self.checkBox_12]

        for i, check_box in enumerate(checkBoxList):
            check_box.clicked.connect(lambda state, index=i: self.toggle_column(state, index))
            



    def submit_button_clicked(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            file_path = selected_item.text()
            conn = self.read_and_connect(file_path)
            results = self.run_query(conn)
            self.populate_table(results)

    def dragEnterEvent(self, event: QDragEnterEvent):
        mime_data = event.mimeData()
        if mime_data.hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        mime_data = event.mimeData()
        if mime_data.hasUrls():
            urls = mime_data.urls()
            for url in urls:
                if url.isLocalFile():
                    self.listWidget.addItem(url.toLocalFile())

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()


    def read_and_connect(self, path):
        # Read Excel data into a DataFrame
        excel_file = path
        print(excel_file)
        df = pd.read_excel(excel_file)

        # Create an in-memory SQLite database
        conn = sqlite3.connect(':memory:')
        df.to_sql('my_table', conn, index=False)

        return conn

    def run_query(self, conn):
        # Run SQL queries using pandas and SQLite
        query = '''SELECT * FROM my_table'''
        results = pd.read_sql_query(query, conn)
        conn.close()
        return results

    def toggle_column(self, state, col):
        if (state == True):
            self.tableWidget.setColumnHidden(col, False)  # 2 corresponds to Checked state
        else:
            self.tableWidget.setColumnHidden(col, True)  # 2 corresponds to Checked state




    def populate_table(self, results):
        # Set the table widget dimensions
        num_rows, num_cols = results.shape
        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_cols)

        # Populate the QTableWidget
        for row_idx, row_data in enumerate(results.values):
            for col_idx, cell_data in enumerate(row_data):
                if ((col_idx == 0 or col_idx == 1) and cell_data != None):
                    cell_data = cell_data.split()[0]

                item = QTableWidgetItem(str(cell_data))
                item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(row_idx, col_idx, item)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Title = QtWidgets.QMainWindow()
    ui = Ui_Title()
    ui.setupUi(Title)
    Title.show()
    sys.exit(app.exec_())
