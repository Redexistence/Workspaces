import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QButtonGroup, QLineEdit, QPushButton, QMessageBox, QProgressBar
from PyQt5.QtCore import QTimer, Qt

# Defining a global style for the app
STYLE_SHEET = """
QWidget {
    font-family: 'Segoe UI', Arial;
    font-size: 14px;
    background-color: #f0f2f5;
}
QProgressBar {
    border: 1px solid #bbb;
    border-radius: 5px;
    text-align: center;
}
QProgressBar::chunk {
    background-color: #05B8CC;
    width: 20px;
}
QPushButton {
    background-color: #0078d4;
    color: white;
    border-radius: 4px;
    padding: 8px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #005a9e;
}
"""

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
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMaximum(len(self.questions))
        self.layout.addWidget(self.progress_bar)

        self.question_label = QLabel()
        self.question_label.setWordWrap(True)
        self.layout.addWidget(self.question_label)

        self.options_group = QButtonGroup()
        self.radio_buttons = [QRadioButton() for _ in range(4)]
        for i, rb in enumerate(self.radio_buttons):
            self.options_group.addButton(rb, i)
            self.layout.addWidget(rb)
            rb.hide()

        self.tf_group = QButtonGroup()
        self.true_rb, self.false_rb = QRadioButton('True'), QRadioButton('False')
        self.tf_group.addButton(self.true_rb, 0)
        self.tf_group.addButton(self.false_rb, 1)
        self.layout.addStretch()
        self.layout.addWidget(self.true_rb)
        self.layout.addWidget(self.false_rb)
        self.true_rb.hide(); self.false_rb.hide()

        self.short_answer = QLineEdit()
        self.layout.addWidget(self.short_answer)
        self.short_answer.hide()

        self.next_button = QPushButton('Submit Answer')
        self.next_button.clicked.connect(self.next_question)
        self.layout.addWidget(self.next_button)

        self.setLayout(self.layout)
        self.setWindowTitle('Coding Quiz')
        self.setGeometry(300, 300, 450, 400)
        self.show_question()

    def show_question(self):
        if self.current_question >= len(self.questions):
            self.show_results()
            return

        self.progress_bar.setValue(self.current_question)
        self.reset_selections()

        q = self.questions[self.current_question]
        self.question_label.setText(f"<b>Question {self.current_question + 1}:</b><br>{q['question']}")

        if q['type'] == 'mc':
            for i, option in enumerate(q['options']):
                self.radio_buttons[i].setText(option)
                self.radio_buttons[i].show()
            self.true_rb.hide(); self.false_rb.hide(); self.short_answer.hide()
        elif q['type'] == 'tf':
            self.true_rb.show(); self.false_rb.show()
            for rb in self.radio_buttons: rb.hide()
            self.short_answer.hide()
        elif q['type'] == 'sa':
            self.short_answer.show(); self.short_answer.clear()
            for rb in self.radio_buttons + [self.true_rb, self.false_rb]: rb.hide()

    def reset_selections(self):
        for group in [self.options_group, self.tf_group]:
            group.setExclusive(False)
            for btn in group.buttons(): btn.setChecked(False)
            group.setExclusive(True)

    def next_question(self):
        q = self.questions[self.current_question]
        correct = False

        if q['type'] == 'mc':
            selected = self.options_group.checkedId()
            if selected != -1 and self.radio_buttons[selected].text() == q['answer']:
                correct = True
        elif q['type'] == 'tf':
            selected = self.tf_group.checkedId()
            if selected == (0 if q['answer'] else 1):
                correct = True
        elif q['type'] == 'sa':
            if self.short_answer.text().strip().lower() == q['answer'].lower():
                correct = True

        self.show_feedback(correct, q['answer'] if not correct else "")

    def show_feedback(self, correct, correct_answer):
        if correct:
            self.score += 1
            msg, color = "Correct!", "#d4edda"
        else:
            msg, color = f"Incorrect!<br>Correct: <b>{correct_answer}</b>", "#f8d7da"

        self.feedback_box = QMessageBox(self)
        self.feedback_box.setWindowTitle('Feedback')
        self.feedback_box.setText(msg)
        
        # Apply QSS styling directly to the pop-up
        self.feedback_box.setStyleSheet(f"""
            QMessageBox {{ background-color: {color}; border: 2px solid #ccc; }}
            QLabel {{ font-size: 16px; color: #333; }}
            QPushButton {{ min-width: 80px; }}
        """)
        
        self.feedback_box.finished.connect(self.proceed_to_next)
        self.feedback_box.show()
        
        # Smoothly move to the side of the main window
        main_geo = self.geometry()
        self.feedback_box.move(main_geo.right() + 20, main_geo.top())

        QTimer.singleShot(2500, self.feedback_box.close)

    def proceed_to_next(self):
        self.current_question += 1
        self.show_question()

    def show_results(self):
        self.progress_bar.setValue(len(self.questions))
        QMessageBox.information(self, 'Quiz Complete', f'Final Score: {self.score}/{len(self.questions)}')
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLE_SHEET) # Loading our custom QSS
    quiz = CodingQuiz()
    quiz.show()
    sys.exit(app.exec_())