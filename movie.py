from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel, QTextEdit,
                             QHBoxLayout)
import sys
from PyQt6.QtCore import Qt
from bs4 import BeautifulSoup
import requests
import lxml


class MyWinDow(QWidget):
    def __init__(self, parent=None):
        super(MyWinDow, self).__init__(parent)
        self.setUi()
        self.show()

    def setUi(self):
        self.setWindowTitle('电影下载')
        self.resize(800, 200)
        '''设置标签'''
        lable = QLabel()
        lable.setText('电影地址：')
        lable.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        lable.setFixedSize(100, 60)
        lable.setStyleSheet("QLabel{color:blue;font-size:20px}")
        '''设置文本框'''
        text_Edit = QTextEdit()
        text_Edit.setFixedSize(800, 40)
        '''设置按钮'''
        btn1 = QPushButton("爱奇艺")
        btn1.setFixedSize(100, 50)
        btn2 = QPushButton("腾讯")
        btn2.setFixedSize(100, 50)
        btn3 = QPushButton("优酷")
        btn3.setFixedSize(100, 50)
        btn4 = QPushButton("下载")
        btn4.setFixedSize(100, 50)
        '''设置布局'''
        layout_V = QVBoxLayout()  # 垂直布局
        layout_H = QHBoxLayout()  # 水平布局1
        layout_H1 = QHBoxLayout()  # 水平布局2
        '''布局1放置控件'''
        layout_H.addWidget(lable)
        layout_H.addWidget(text_Edit)
        '''布局2放置控件'''
        layout_H1.addWidget(btn1)
        layout_H1.addWidget(btn2)
        layout_H1.addWidget(btn3)
        layout_H1.addWidget(btn4)
        '''布局1和2加入垂直布局'''
        layout_V.addLayout(layout_H)
        layout_V.addLayout(layout_H1)
        self.setLayout(layout_V)


class Movie():
    def __init__(self):
        self.get_html()

    def get_html(self):
        # url = 'https://v.youku.com/v_show/id_XNjQwOTk1ODUyNA==.html?spm=a2hja.14919748_WEBHOME_NEW.drawer2.d_zj1_2&s=683d803b7de4478891bc&scm=20140719.rcmd.46210.show_683d803b7de4478891bc&s=683d803b7de4478891bc'
        url = 'https://www.youku.com/'
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'cookie': 'isI18n=false; _m_h5_tk=8b28e6a2091e24ec95baefe6fbb48bce_1724611400208; _m_h5_tk_enc=bb21ba548a5eaf2ceca08118fc862900; cna=mFVSH16LiHwBASQOA7Y8J03P; __ysuid=1724606359276aAD; __ayft=1724606359276; __aysid=1724606359276Kuw; __ayscnt=1; xlly_s=1; __arpvid=1724606364088fGZK4A-1724606364092; __arycid=dz-3-00; __arcms=dz-3-00; __aypstp=2; __ayspstp=2; P_F=1; __ayvstp=6; __aysvstp=6; isg=BDU0k0s6vz9JAd6y6uVBUqBHRLHvsunEmEpz07dbCqz6jlSAfwK8lj1E2FK49QF8; tfstk=fEwoEI9Bc7lW6s-dr-D59THM07fYd4MZLpzKJ2EE800jzBEewyvUzlcUeYE8oBP4Ay3JeYWnxSPrOkhWeriYzD07d0O8GxixmXzKJuIHV-4MpLQ5NkJnpv7OWOBTVuHILNQ3xcapNcmlpBuyLWSzzxQOWOBOankhrNFLlWL-oDgq4DRr8iXqjDHEY0kFmqonfB8z8vS00qiHTBJyUjkqA0oEaMtqyyz73a5Czp0Z1HzSqb0Hpqv3F8vtaVrrop5bn0vS7uuDLpuWvoIbmuQkCoH7BPmTytJuSkr_Tj2HuN0QnoyzToTl8mNUyxu-Q_-me8Zz_XyNRBziEycaUjxFxuErrxm4QMdsk-0888cVXdcK3RhZUSCfyXHojyy7rHvU7oETFjwhSEuQwcMqxJswt2cF4-R2_FZJdmSL3BOIamim51I-tqR5h1dcmiAa1boj4OIcmBOIamimWijD_NGrc0WO.'}
        data = {'spm': 'a2hja.14919748_WEBHOME_NEW.drawer2.d_zj1_2', 's': '683d803b7de4478891bc',
                'scm': '20140719.rcmd.46210.show_683d803b7de4478891bc', 's': '683d803b7de4478891bc'}
        r1 = requests.get(url=url, headers=header, params=data)
        r1.encoding = 'utf-8'
        html = r1.text
        soup = BeautifulSoup(html, 'lxml')
        print(soup)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWinDow()
    sys.exit(app.exec())
    # M = Movie()
