import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
        def __init__(self):
            super().__init__()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self)
            self.ui.students.itemClicked.connect(self.student_fail)
            self.ui.uczen.editingFinished.connect(self.add)
            self.show()

        def student_fail(self):
            students = self.ui.students.selectedItems()
            self.ui.failedstudents.clear()
            for student in students:
                self.ui.failedstudents.addItem(student.text())

        def add(self):
            uczen = self.ui.uczen.text()
            self.ui.students.addItem(uczen)
            self.ui.uczen.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())
