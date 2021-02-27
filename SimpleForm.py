from PySide2.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QLineEdit, \
    QLabel, QHBoxLayout
import sys


class MyForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Form")
        main_layout = QVBoxLayout(self)

        # name layout
        name_layout = QHBoxLayout()
        main_layout.addLayout(name_layout)

        name_label = QLabel("Name:")
        name_label.setMinimumWidth(100)
        name_layout.addWidget(name_label)

        self.name_field = QLineEdit()
        name_layout.addWidget(self.name_field)
        
        # address layout
        address_layout = QHBoxLayout()
        main_layout.addLayout(address_layout)

        address_label = QLabel("Address:")
        address_label.setMinimumWidth(100)
        address_layout.addWidget(address_label)

        self.address_field = QLineEdit()
        address_layout.addWidget(self.address_field)
        
        # phone layout
        phone_layout = QHBoxLayout()
        main_layout.addLayout(phone_layout)

        phone_label = QLabel("Phone:")
        phone_label.setMinimumWidth(100)
        phone_layout.addWidget(phone_label)

        self.phone_field = QLineEdit()
        phone_layout.addWidget(self.phone_field)

        save_button = QPushButton("Save")
        main_layout.addWidget(save_button)

        # signal/slots
        save_button.clicked.connect(self.save_action)

    def save_action(self):
        name = self.name_field.text()
        address = self.address_field.text()
        phone = self.phone_field.text()

        print(name, address, phone)


app = QApplication(sys.argv)
win = MyForm()
win.show()
app.exec_()