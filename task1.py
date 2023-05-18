from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QPushButton, QHBoxLayout
app = QApplication([])
win = QWidget()
win.show()

main_layout = QHBoxLayout() 
win.setLayout(main_layout) 
b1 = QPushButton()
main_layout.addWidget(b1)
b2 = QPushButton()
main_layout.addWidget(b2)

b3 = QPushButton()
main_layout.addWidget(b3) 



app.exec()
