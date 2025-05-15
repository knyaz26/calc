from PyQt6 import QtCore as qc, QtGui as qg, QtWidgets as qw
import sys

class calc(qw.QMainWindow):
    def __init__(self):
        super(calc, self).__init__()
        self.init_ui()

        self.setFixedSize(150, 200)
        self.setWindowTitle("calc")
        self.setStyleSheet("background-color: #2E3440; color: #D8DEE9;")
        # self.setWindowIcon(qg.QIcon("icon.png"))

    def init_ui(self):
        self.central_widget = qw.QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = qw.QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.display = qw.QLineEdit()
        #self.display.setReadOnly(True)
        self.display.setStyleSheet("background-color: #3B4252; color: #D8DEE9;")
        self.layout.addWidget(self.display)

        self.buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        self.grid_layout = qw.QGridLayout()
        for i, button in enumerate(self.buttons):
            btn = qw.QPushButton(button)
            btn.setStyleSheet("background-color: #4C566A; color: #D8DEE9;")
            btn.clicked.connect(self.on_button_click)
            self.grid_layout.addWidget(btn, i // 4, i % 4)

        self.layout.addLayout(self.grid_layout)

    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            result = self.calculate(self.display.text())
            self.display.setText(str(result))
        else:
            self.display.setText(self.display.text() + text)

    def calculate(self, expression):
        try:
            answer = eval(expression)
            if type(answer) == int or type(answer) == float:
                return answer
            else:
                return "Wrong Type"
        except:
            return "Wrong Input"


if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    window = calc()
    window.show()
    sys.exit(app.exec())