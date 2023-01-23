import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Simple PyQt6 Program')

label = QLabel('Hello, PyQt6!', parent=window)
label.resize(label.sizeHint())
label.move(50, 50)

window.show()

sys.exit(app.exec())
