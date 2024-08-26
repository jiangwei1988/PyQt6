from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QTextEdit,
                             QHBoxLayout)
import sys
from PyQt6.QtCore import Qt
import webbrowser


class MyWinDow(QWidget):
    def __init__(self, parent=None):
        super(MyWinDow, self).__init__(parent)
        self.setUi()
        self.show()

    def setUi(self):
        self.setWindowTitle('观看VIP视频')
        self.resize(800, 200)
        '''设置标签'''
        lable = QLabel()
        lable.setText('电影地址：')
        lable.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        lable.setFixedSize(100, 60)
        lable.setStyleSheet("QLabel{color:blue;font-size:20px}")
        '''设置文本框'''
        self.text_Edit = QTextEdit()
        self.text_Edit.setFixedSize(800, 40)
        '''设置按钮'''
        btn1 = QPushButton("爱奇艺")
        btn1.clicked.connect(self.open_aqy)
        btn1.setFixedSize(100, 50)
        btn2 = QPushButton("腾讯")
        btn2.clicked.connect(self.open_tx)
        btn2.setFixedSize(100, 50)
        btn3 = QPushButton("优酷")
        btn3.clicked.connect(self.open_yk)
        btn3.setFixedSize(100, 50)
        self.btn4 = QPushButton("播放")
        self.btn4.setStyleSheet("QPushButton{background-color:yellow}")
        self.btn4.clicked.connect(self.get_Movie)
        self.btn4.setFixedSize(100, 50)
        self.btn5 = QPushButton("清空")
        self.btn5.clicked.connect(self.txt_clear)
        self.btn5.setStyleSheet("QPushButton{ background-color: red}")
        self.btn5.setFixedSize(100, 40)
        '''设置布局'''
        layout_V = QVBoxLayout()  # 垂直布局
        layout_H = QHBoxLayout()  # 水平布局1
        layout_H1 = QHBoxLayout()  # 水平布局2
        '''布局1放置控件'''
        layout_H.addWidget(lable)
        layout_H.addWidget(self.text_Edit)
        layout_H.addWidget(self.btn5)
        '''布局2放置控件'''
        layout_H1.addWidget(btn1)
        layout_H1.addWidget(btn2)
        layout_H1.addWidget(btn3)
        layout_H1.addWidget(self.btn4)
        '''布局1和2加入垂直布局'''
        layout_V.addLayout(layout_H)
        layout_V.addLayout(layout_H1)
        self.setLayout(layout_V)

    def get_Movie(self):
        url = 'https://jx.xmflv.cc/?url='
        text = self.text_Edit.toPlainText()
        webbrowser.open(url + text)

    def txt_clear(self):
        self.text_Edit.clear()

    def open_aqy(self):
        url = 'https://www.iqiyi.com/'
        webbrowser.open(url)

    def open_tx(self):
        url = 'https://v.qq.com/'
        webbrowser.open(url)

    def open_yk(self):
        url = 'https://www.youku.com/'
        webbrowser.open(url)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWinDow()
    sys.exit(app.exec())
