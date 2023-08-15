import sys
import random
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class GraphWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(678, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 678, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.layout = QVBoxLayout(self.centralwidget)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Display the graph when the MainWindow is created

        #self.display_random_chart()
        #self.display_random_pie_chart()
        #self.display_line_plot()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graph Display"))

    def display_random_chart(self):
        self.figure.clear()

        # Generate random data for the chart
        num_values = 5
        labels = [f"Category {i}" for i in range(1, num_values + 1)]
        values = [random.randint(1, 100) for _ in range(num_values)]

        # Create a bar chart using the random data
        ax = self.figure.add_subplot(111)
        ax.bar(labels, values)

        # Set labels and title
        ax.set_xlabel("Categories")
        ax.set_ylabel("Values")
        ax.set_title("Random Bar Chart")

        # Redraw the canvas to display the updated chart
        self.canvas.draw()



    def display_random_pie_chart(self):
        # Generate random data for the pie chart
        num_slices = 4
        labels = [f"Slice {i}" for i in range(1, num_slices + 1)]
        sizes = [random.randint(1, 100) for _ in range(num_slices)]

        # Create a pie chart using the random data
        ax = self.figure.add_subplot(122, aspect="equal")
        ax.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
            shadow=False,
            startangle=90,
            wedgeprops={"edgecolor": "black"},  # Set edgecolor to "white" for seamless appearance
        )

        # Set title
        ax.set_title("Random Pie Chart")

        # Adjust subplot position and size to center and make the pie chart bigger
        # Adjust subplot position and size to center and make the pie chart 2 times bigger
        left = 0  # Adjusting the left position to center the pie chart
        bottom = -0.06
        width = 0.6 * 1.7  # Making the pie chart 2 times wider
        height = 0.6 * 1.7  # Making the pie chart 2 times taller
        ax.set_position([left, bottom, width, height])

        # Redraw the canvas to display the updated chart
        self.canvas.draw()


    def display_line_plot(self):
        self.figure.clear()

        # Generate data for the line plot
        x = [1, 2, 3, 4, 5]
        y = [10, 23, 18, 32, 25]

        # Create a line plot using the data
        ax = self.figure.add_subplot(111)
        ax.plot(x, y, marker='o')

        # Set labels and title
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")
        ax.set_title("Line Plot")

        # Redraw the canvas to display the updated plot
        self.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GraphWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())