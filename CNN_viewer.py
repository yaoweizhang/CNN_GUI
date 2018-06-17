import sys
import numpy as np
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import convolution

class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        self.filter_size = 3
        self.input_filter = np.zeros((self.filter_size, self.filter_size), dtype=np.float)
        self.pic_path = None

        #top part of window
        file_btn = QPushButton("Choose a picture")
        file_btn.clicked.connect(self.get_pic)

        self.label1 = QLabel("No picture avilable")
        self.label1.setAlignment(Qt.AlignCenter)
        
        top_layout = QVBoxLayout()
        top_layout.addWidget(file_btn)
        top_layout.addWidget(self.label1)

        #bottom part of window
        add_btn = QPushButton("Add filter")
        add_btn.clicked.connect(self.add_filter)

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.addWidget(add_btn)
        self.bottom_layout.addStretch()
        self.add_filter()


        #Whole structe
        win_layout = QVBoxLayout()
        win_layout.addLayout(top_layout)
        win_layout.addStretch()
        win_layout.addLayout(self.bottom_layout)

        self.setLayout(win_layout)
        self.setWindowTitle("CNN convolution simulator")

    def get_pic(self):
        fname = QFileDialog.getOpenFileName(self, "open file", ".", "Image files(*.jpg *.gif)")
        self.label1.setPixmap(QPixmap(fname))
        self.pic_path = str(fname)

    def add_filter(self):
        values = {}
        grid = QGridLayout()
        for i in range(1, self.filter_size+1):
            for j in range(1, self.filter_size+1):
                input_num = QLineEdit("0")
                if i == j == (self.filter_size+1)/2:
                    input_num.setText("1")
                values[(i, j)] = input_num
                input_num.setValidator(QDoubleValidator())
                grid.addWidget(input_num, i, j)

        conv_pic = QLabel("Press submit to show result")
        conv_pic.setAlignment(Qt.AlignCenter)

        submit_btn = QPushButton("Submit")
        submit_btn.clicked.connect(lambda state, values=values, conv_pic=conv_pic:\
                self.submit(values, conv_pic))

        single_filter = QVBoxLayout()
        single_filter.addLayout(grid)
        single_filter.addWidget(submit_btn)
        single_filter.addStretch()
        single_filter.addWidget(conv_pic)

        self.bottom_layout.addLayout(single_filter)

    def submit(self, values, conv_pic):
        if self.pic_path == None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please choose a picture")
            msg.exec_()
        else:
            for i in range(1, self.filter_size+1):
                for j in range(1, self.filter_size+1):
                    self.input_filter[i-1][j-1] = float(str(values[(i, j)].text()))

            #print(self.pic_path)
            #print(self.input_filter)

            new_path = convolution.compute(self.pic_path, self.input_filter)
            conv_pic.setPixmap(QPixmap(new_path))


def main():
    app = QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
