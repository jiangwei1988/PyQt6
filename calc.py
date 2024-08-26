import sys

from PyQt6.QtWidgets import QGridLayout, QWidget, QPushButton, QApplication, QVBoxLayout, QLineEdit
from PyQt6.QtCore import Qt


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.express = ''
        self.sum = ''
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle("计算器")
        self.express = QLineEdit()
        self.express.setReadOnly(True)
        self.express.setFixedHeight(50)
        self.express.setStyleSheet("QLineEdit {color:blue; font-size:20px}")
        self.express.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout = QVBoxLayout()
        layout.addWidget(self.express)
        grid = QGridLayout()

        txt = [
            ['C', '0', '/', '+'],
            ['1', '2', '3', '-'],
            ['4', '5', '6', '*'],
            ['7', '8', '9', '='],
        ]

        for i in range(0, 4):
            for j in range(0, 4):
                btn = QPushButton(txt[i][j])
                btn.setFixedSize(30, 30)
                if txt[i][j] == 'C':
                    btn.clicked.connect(self.btn_clear_txt)
                else:
                    btn.clicked.connect(self.btn_click_txt)
                grid.addWidget(btn, i, j)

        layout.addLayout(grid)
        self.sum = ''
        self.setLayout(layout)
        self.setFixedSize(250, 300)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def btn_click_txt(self):
        text = self.sender().text()
        try:
            if text == '=':
                result = str(eval(self.sum))
                self.express.setText(result)
                self.sum = result
            else:
                self.sum = self.sum + text
                self.express.setText(self.sum)
        except:
            print("输入错误！")
            self.sum = ''
            self.express.clear()

    def btn_clear_txt(self):
        self.sum = ''
        self.express.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWidget()
    sys.exit(app.exec())
