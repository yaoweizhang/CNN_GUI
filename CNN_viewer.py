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

    def get_pic(self):
        fname = QFileDialog.getOpenFileName(self, "open file", ".", "Image files(*.jpg *.gif)")
        self.label1.setPixMap(QPixmap(fname))
        self.pic_path = str(fname)


def main():
    app = QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()