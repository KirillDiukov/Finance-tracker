import sys

from ui import Ui_loginWidget, Ui_signupWidget
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget


class FinanceWindow(QMainWindow):
    def __init__(self):
        super().__init__()


class SignupWidget(QWidget, Ui_signupWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.signupButton.clicked.connect(self.signupClicked)

    def signupClicked(self):
        txt = open('loginPassword.txt', 'w', encoding='utf8')
        username = self.usernameLine.text()
        password = self.passwordLine.text()
        txt.write(f'{username}\n{password}\n')
        txt.close()
        self.close()
        self.loginWindow = LoginWidget()
        self.loginWindow.show()


class LoginWidget(QWidget, Ui_loginWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginButton.clicked.connect(self.loginClicked)
        self.errorLabel.hide()

    def loginClicked(self):
        txt = open('loginPassword.txt', 'r', encoding='utf8')
        data = txt.read().split('\n')
        txt.close()
        trueLogin = data[0]
        truePassword = data[1]
        writenLogin = self.usernameLine.text()
        writenPassword = self.passwordLine.text()
        if trueLogin == writenLogin and truePassword == writenPassword:
            self.mainWindow = FinanceWindow()
            self.close()
            self.mainWindow.show()
        elif trueLogin == writenLogin:
            self.errorLabel.setText('Неправильный пароль')
            self.errorLabel.show()
        elif truePassword == writenPassword:
            self.errorLabel.setText('Неправильный логин')
            self.errorLabel.show()
        else:
            self.errorLabel.setText('Неправильный логин и пароль')
            self.errorLabel.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    txt = open('loginPassword.txt', 'r', encoding='utf8')
    if txt.read() == '':
        ex = SignupWidget()
    else:
        ex = LoginWidget()
    txt.close()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
