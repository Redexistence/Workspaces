import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QButtonGroup, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class CodingQuiz(QWidget):
    def __init__(self):
        super().__init__()
        self.questions = [
            {'type': 'mc', 'question': 'What does HTML stand for?', 'options': ['HyperText Markup Language', 'High Tech Modern Language', 'Home Tool Markup Language'], 'answer': 'HyperText Markup Language'},
            {'type': 'tf', 'question': 'Python is a compiled language.', 'answer': False},
            {'type': 'sa', 'question': 'What keyword is used to define a function in Python?', 'answer': 'def'},
            {'type': 'mc', 'question': 'Which of the following is a Python data type?', 'options': ['int', 'string', 'float', 'all of the above'], 'answer': 'all of the above'},
            {'type': 'tf', 'question': 'In JavaScript, arrays are zero-indexed.', 'answer': True},
            {'type': 'sa', 'question': 'What does CSS stand for?', 'answer': 'Cascading Style Sheets'},
            {'type': 'mc', 'question': 'Which loop is used for iterating over a sequence in Python?', 'options': ['for', 'while', 'do-while', 'foreach'], 'answer': 'for'},
            {'type': 'tf', 'question': 'SQL is used for styling web pages.', 'answer': False},
            {'type': 'sa', 'question': 'What is the extension for a Python file?', 'answer': '.py'},
            {'type': 'mc', 'question': 'Which company developed Java?', 'options': ['Microsoft', 'Sun Microsystems', 'Google', 'Apple'], 'answer': 'Sun Microsystems'}
        ]
        self.current_question = 0
        self.score = 0
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.question_label = QLabel()
        self.layout.addWidget(self.question_label)

        self.options_group = QButtonGroup()
        self.radio_buttons = []
        for i in range(4):
            rb = QRadioButton()
            self.radio_buttons.append(rb)
            self.options_group.addButton(rb, i)
            self.layout.addWidget(rb)
            rb.hide()

        self.tf_group = QButtonGroup()
        self.true_rb = QRadioButton('True')
        self.false_rb = QRadioButton('False')
        self.tf_group.addButton(self.true_rb, 0)
        self.tf_group.addButton(self.false_rb, 1)
        self.layout.addWidget(self.true_rb)
        self.layout.addWidget(self.false_rb)
        self.true_rb.hide()
        self.false_rb.hide()

        self.short_answer = QLineEdit()
        self.layout.addWidget(self.short_answer)
        self.short_answer.hide()

        self.next_button = QPushButton('Next')
        self.next_button.clicked.connect(self.next_question)
        self.layout.addWidget(self.next_button)

        self.setLayout(self.layout)
        self.setWindowTitle('Coding Quiz')
        self.setGeometry(300, 300, 400, 300)
        self.show_question()

    def show_question(self):
        if self.current_question >= len(self.questions):
            self.show_results()
            return

        q = self.questions[self.current_question]
        self.question_label.setText(q['question'])

        if q['type'] == 'mc':
            for i, option in enumerate(q['options']):
                self.radio_buttons[i].setText(option)
                self.radio_buttons[i].show()
            self.true_rb.hide()
            self.false_rb.hide()
            self.short_answer.hide()
        elif q['type'] == 'tf':
            self.true_rb.show()
            self.false_rb.show()
            for rb in self.radio_buttons:
                rb.hide()
            self.short_answer.hide()
        elif q['type'] == 'sa':
            self.short_answer.show()
            self.short_answer.clear()
            for rb in self.radio_buttons:
                rb.hide()
            self.true_rb.hide()
            self.false_rb.hide()

    def next_question(self):
        q = self.questions[self.current_question]
        correct = False

        if q['type'] == 'mc':
            selected = self.options_group.checkedId()
            if selected != -1 and self.radio_buttons[selected].text() == q['answer']:
                correct = True
        elif q['type'] == 'tf':
            selected = self.tf_group.checkedId()
            if selected == 0 and q['answer'] or selected == 1 and not q['answer']:
                correct = True
        elif q['type'] == 'sa':
            if self.short_answer.text().strip().lower() == q['answer'].lower():
                correct = True

        if correct:
            self.score += 1

        self.current_question += 1
        self.show_question()

    def show_results(self):
        QMessageBox.information(self, 'Quiz Complete', f'Your score: {self.score}/{len(self.questions)}')
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    quiz = CodingQuiz()
    sys.exit(app.exec_())