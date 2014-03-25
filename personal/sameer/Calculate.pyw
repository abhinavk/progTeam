from _future_ import division
import sys
from math import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
class Form(QDialog):
    def _init_(self, parent=None):
        super(Form, self)._init_(parent)
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an Expression and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.connect(self.lineedit,SIGNAL("returnPressed()"),
                     self.updateUi)
        sel.setWindowTitle("Caculate")
    def updateUi(self):
        try:
            text = unicode(elf.lineedit.text())
            self.browser.append("%s= <b>%s</b>" % (text, eval(text)))
        except:
            self.browser.append("<font color=red>%s is invalid!</font>" % text)
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
    
        
