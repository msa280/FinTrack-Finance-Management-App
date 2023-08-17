import sys
import random
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QVBoxLayout
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class GraphWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(778, 900)
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


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graph Display"))



    def display_random_chart(self, tag, results):

        self.figure.clear()

        if (tag == "tt"):

            labels = results['YearMonth'].tolist()
            sizes = results['TotalAmount'].tolist()

            # Customize bar colors and width
            bar_colors = ['red' if value < 0 else 'blue' for value in sizes]
            bar_width = 0.4

            # Create a bar chart using the random data
            ax = self.figure.add_subplot(111)
            ax.bar(labels, sizes, color=bar_colors, width=bar_width)

            ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

            # Set labels and title
            ax.set_xlabel("YearMonth")
            ax.set_ylabel("Sizes")
            ax.set_title("Transaction Amounts - All Time")

            # Redraw the canvas to display the updated chart
            self.canvas.draw()





    def display_pie_chart(self, tag, results, date=None):

        self.figure.clear()  # Very important. Clears the figure on from the previous query.

        # Generate random data for the pie chart
        colors = ['crimson', 'yellow', 'chartreuse', 'dodgerblue', 'darkorange', 'cyan', 'magenta', 'blueviolet',
                  'ghostwhite', 'gold', 'lime', 'blue', 'teal', 'turquoise', 'silver']

        # Create a pie chart using the random data
        ax = self.figure.add_subplot(122, aspect="equal")

        if (tag == "tsc" or tag == "ms"):

            labels = results['Code'].tolist()
            counts = results['TotalCount'].tolist()
            amounts = results['TotalAmount'].tolist()

            new_amounts = []
            for amount in amounts:
                if amount < 0:
                    amount *= -1
                    new_amounts.append(amount)
                else:
                    new_amounts.append(amount)

            patches, texts, autotexts = ax.pie(
                new_amounts,  # We multiply by -1 because wedge sizes cant be negative
                autopct='',
                startangle=90,
                colors=colors,
                radius=1,
                wedgeprops={"edgecolor": "black"},  # Set edgecolor to "white" for seamless appearance
            )

            legend_labels = ['{} - {} Transactions - ${}'.format(code, count, amount) for code, count, amount in
                             zip(labels, counts, amounts)]
            # Add legend to the best location

            if (tag == "ms"):
                month_dict = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May',
                              '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October',
                              '11': 'November', '12': 'December'}
                year, month = date.split("-")
                ax.set_title("Transactions for {}, {}".format(month_dict[month], year))
                ax.legend(legend_labels, title="Monthly Summary", loc='upper left')
            else:
                ax.set_title("Transactions - All Time")
                ax.legend(legend_labels, title="Transaction Breakout", loc='upper left')

            # Set aspect ratio to be equal so that pie is drawn as a circle.
            ax.axis('equal')


        elif (tag == "tpm"):
                labels = results['Type'].tolist()
                sizes = results['TotalTypes'].tolist()
                ax.set_title("Top Payment Methods")
                colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'yellowgreen', 'gold', 'lightskyblue',
                          'lightcoral']

                patches, texts, _ = ax.pie(
                    sizes,
                    autopct='',
                    startangle=90,
                    colors=colors,
                    radius=1,
                    wedgeprops={"edgecolor": "black"},  # Set edge color to "white" for seamless appearance
                )

                legend_labels = ['{} {}s'.format(size, label) for label, size in zip(labels, sizes)]
                # Add legend to the best location
                ax.legend(legend_labels, title="Payment Types", loc='upper left')
                # Set aspect ratio to be equal so that pie is drawn as a circle.
                ax.axis('equal')


        # Adjust subplot position and size to center and make the pie chart bigger
        # Adjust subplot position and size to center and make the pie chart 2 times bigger
        left = 0  # Adjusting the left position to center the pie chart
        bottom = -0.06
        width = 0.6 * 1.7  # Making the pie chart 2 times wider
        height = 0.6 * 1.7  # Making the pie chart 2 times taller
        ax.set_position([left, bottom, width, height])
        # Redraw the canvas to display the updated chart
        self.canvas.draw()



    def display_line_plot(self, tag, results):

        self.figure.clear()

        ax = self.figure.add_subplot(111)

        if (tag == "bc"):
            # Generate data for the line plot
            labels = results['YearMonth'].tolist()
            sizes = results['AverageBalance'].tolist()

            # Create a line plot using the data
            ax.plot(labels, sizes, marker='o')

            ax.plot(labels, sizes, marker='o', color='limegreen', linestyle='-', linewidth=2, markersize=8,
                    label='Average Balance')

            # Customize x-axis tick labels
            ax.set_xticks(range(len(labels)))  # Set tick positions
            ax.set_xticklabels(labels, rotation=45, ha='right')

            # Customize y-axis formatting
            ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "${:,.2f}".format(x)))

            # Add a grid
            ax.grid(which='major', linestyle='--', linewidth=0.45, color='blue', alpha=0.8)
            ax.legend()

            # Add data labels to markers
            for label, size in zip(labels, sizes):
                ax.text(label, size, f"{size:.2f}", ha='center', va='top', fontsize=10, color='red')

            # Tight layout for better appearance
            plt.tight_layout()

            # Set labels and title
            ax.set_xlabel("Year-Month")
            ax.set_ylabel("Average Balance / Month")
            ax.set_title("Average Monthly Balances")


        elif (tag == "dtt"):

            # Generate data for the line plot
            labels = results['YearMonth'].tolist()
            sizes = results['Count'].tolist()

            # Create a line plot using the data
            ax.plot(labels, sizes, marker='o')

            ax.plot(labels, sizes, marker='o', color='limegreen', linestyle='-', linewidth=2, markersize=8,
                    label='Average Balance')

            # Customize x-axis tick labels
            ax.set_xticks(range(len(labels)))  # Set tick positions
            ax.set_xticklabels(labels, rotation=45, ha='right')

            # Customize y-axis formatting
            ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "${:,.2f}".format(x)))

            # Add a grid
            ax.grid(which='major', linestyle='--', linewidth=0.45, color='blue', alpha=0.8)
            ax.legend()

            # Add data labels to markers
            for label, size in zip(labels, sizes):
                ax.text(label, size, f"{size:.2f}", ha='center', va='top', fontsize=10, color='red')

            # Tight layout for better appearance
            plt.tight_layout()

            # Set labels and title
            ax.set_xlabel("Year-Month")
            ax.set_ylabel("Average Balance / Month")
            ax.set_title("Average Monthly Balances")


        # Redraw the canvas to display the updated plot
        self.canvas.draw()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GraphWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())