from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import  shuffle
from random import randint

class Question():
    def __init__(self,question, right_answer,wr1,wr2,wr3):
        self.question = question
        self.right_answer = right_answer
        self.wr1 = wr1
        self.wr2 = wr2
        self.wr3 = wr3
def ask(q: Question):
    
    shuffle(ans)
    ans[0].setText(q.right_answer)
    ans[1].setText(q.wr1)
    ans[2].setText(q.wr2)
    ans[3].setText(q.wr3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def check_ans():
    if ans[0].isChecked():
        lb_Result.setText("Правильно")
        show_result()
    elif ans[1].isChecked() or ans[2].isChecked() or ans[3].isChecked():
        lb_Result.setText("Неправильно")
        show_result()
app = QApplication([])
window = QWidget()
questionlist = list()
questionlist.append(Question("104 42 33....",'15','76','0','1'))
questionlist.append(Question("Сколько стоитWaffentrage Auf e 100?",'34523$','80000$','33000$','99987$'))
questionlist.append(Question("Сколько сухариков в одной пачке3 корочки",'3','600','21','9'))

window.cur = -1
def next_question():
    window.cur = randint(0, (len(questionlist)- 1))
    if window.cur >= len(questionlist):
        window.cur = 0
    q = questionlist[window.cur]
    ask(q)
def clickOK():
    if btn_OK.text() == "Ответить":
        check_ans()
    else:
        next_question()
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!') 
 
RadioGroupBox = QGroupBox("Варианты ответов")
 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
ans = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1)
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
 
# ----------------------------------------------------------
# Виджеты и макеты созданы, далее - функции:
# ----------------------------------------------------------
 
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана
 
def test():
    ''' временная функция, которая позволяет нажатием на кнопку вызывать по очереди
    show_result() либо show_question() '''
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()
 
#window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
q = Question('1+1','2','3','4','1')
ask(q)#ask("Кто у нас учитель?","Антонов Егор","Виктор Корнеплод","Майкль Джордан","Райан Гослинг")
btn_OK.clicked.connect(clickOK) # проверяем, что панель ответов показывается при нажатии на кнопку
window.show()
app.exec()
