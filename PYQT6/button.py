import sys
from PyQt6.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton,QTextEdit,QVBoxLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My First App')
        self.resize(300,300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        #widget
        self.inputField = QLineEdit()
        button = QPushButton('&say hello',clicked = self.SayHello)
        # button.clicked.connect(self.SayHello)
        self.output = QTextEdit()

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)

    def SayHello(self):
        inputText = self.inputField.text()
        self.output.setText('hello {0}'.format(inputText))

app = QApplication(sys.argv)

app.setStyleSheet('''
    QWidget{
        font-size : 25px;
    }
    QPushButton{
        font-size : 20px;
    }
    QLineEdit{
        font-size:20px;
        background-color:red;
       height: 50px;
    }
''')

window = MyApp()
window.show()
sys.exit(app.exec())