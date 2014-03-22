import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
app=QApplication(sys.argv)
print len(sys.argv)
print sys.argv[1]

try:
	due = QTime.currentTime()
	message="Alert"
	if len(sys.argv)<2:
		raise ValueError
	h,m=sys.argv[1].split(":")
	due=QTime(int(h),int(m))
	print due
	if not due.isValid():
		raise ValueError
	if len(sys.argv)>2:
		message=" ".join(sys.argv[2:])
except ValueError:
	message="Usage: app1.pyw HH:MM"
while QTime.currentTime()<due:
	time.sleep(20)
label=QLabel("<font color=red size=72><b>" + message + "</b></font>")
label.setWindowFlags(Qt.SpalshScreen)
label.show()
QTimer.singleShot(60000,app.quit)
app.exec_()


