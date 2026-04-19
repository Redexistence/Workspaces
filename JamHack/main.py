import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("My First App")
window.setGeometry(100, 100, 400, 200)
label = QLabel("Hello, JamHacks!", parent=window)
label.move(100, 80)
window.show()
sys.exit(app.exec_())