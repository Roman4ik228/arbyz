#импорты
from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
 


class Guestion():
    def __init__(self, guestion_var, right_answer, w1, w2, w3):
        self.right_answer = right_answer
        self.wrong1 = w1
        self.wrong2 = w2
        self.wrong3 = w3
        self.guestion = guestion_var


#ТЕКСТ ВОПРОСА ВОЗВРАСТ ИЛОНА МАСКА
app = QApplication([])
 
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('вопрос') 
 
RadioGroupBox = QGroupBox("Варианты ответов")
 
rbtn_1 = QRadioButton('вариант 1')
rbtn_2 = QRadioButton('вариант 2')
rbtn_3 = QRadioButton('вариант 3')
rbtn_4 = QRadioButton('вариант 4')




#КНОПКИ
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)







#РОЗПОЛОЖЕНИЕ ВОПРОСА
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








#РОЗПОЛОЖЕНИЕ ОТВЕТА
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
layout_card.setSpacing(5)









#ЗАМЕНА КНОПОК И ТЕКСТА 
def show_results():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_guestion():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)





#Проверка на правильность
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(g):
    shuffle(answers)
    answers[0].setText(g.right_answer)
    answers[1].setText(g.wrong1)
    answers[2].setText(g.wrong2)
    answers[3].setText(g.wrong3)
    lb_Question.setText(g.guestion)
    lb_Correct.setText(g.right_answer)
    show_guestion()

def show_correct(res):
    lb_Result.setText(res)
    show_results()



def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов:  ', window.total,'\n-Правильных ответов:  ', window.score) 
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
    print('Рейтинг: ', (window.score/window.total*100), '%')


def next_guestion():
    window.total += 1
    print('Статистика\n-Всего вопросов:  ', window.total,'\n-Правильных ответов:  ', window.score)
    if window.cur_guest == len(g_list3[window.cur_pack]) - 1:
        g = g_list3[window.cur_pack][window.cur_guest]
        window.cur_guest = 0
        raiting()
        window.total = 0
        window.score = 0
        if g == g_list[0]:
            g_list[0] = g_list[1]
            g_list[1] = g

    else:
        window.cur_guest += 1
        ask(g_list3[window.cur_pack][window.cur_guest])



def click_OK():
    if btn_OK.text() == 'Следующий вопрос':
        next_guestion()
    elif btn_OK.text() == 'Попробовать ещё раз':
        window.cur_pack +=1
        window.cur_guest = -1
        next_guestion()
    else:
        check_answer()
g_list = []





g_list2 = []
g_list2.append(Guestion('как зовут создателя компьютера?', 'Конрад Цузе', 'Майкл Фассбендер', 'Вольфганг Петерсен', 'Элиаш М’Барек'))
g_list2.append(Guestion('Самый дорогой фильм?', 'Пираты Карибского моря: На странных берегах', 'Мстители: Эра Альтрона', 'Мстители: Финал', 'Мстители: Война Бесконечности'))
g_list2.append(Guestion('Самый дорогой автомобиль?', 'Bugatti La Voiture Noire', 'Aston Martin Valkyrie', 'Lamborghini Veneno', 'Mercedes-Maybach Exelero'))

g_list3 = []
g_list3.append(g_list)
g_list3.append(g_list2)




def raiting():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    lb_Result.setText('Твой рейтинг '+str(window.score/(window.total-1)*100) + '%')
    lb_Correct.setText('Вы ответили на ' + str(window.score) + ' из '+ str(window.total-1))
    btn_OK.setText('продолжить отвечать')
    






#Проверка на правильность ответа
window = QWidget()
window.cur_guest = -1
window.cur_pack = 0
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
g = Guestion('Сколько лет Илону Маску?', '50', '43', '52', '55')
g1 = Guestion('Как зовут самого богатого человека?', 'Джефф Безос', 'Билл Гейтс', 'Бернар Арно', 'Марк Цукерберг')
g2 = Guestion('Квадратный корень из 2209', '47', '39', '42', '51')
g3 = Guestion('Сколько серий в one piece?', '953', '948', '991', '916')
g4 = Guestion('Сколько весит солнце?', '1,989E30 кг', '1,9107E00 кг', '2,031E04 кг', '0,893E40 кг')
g5 = Guestion('Сколько людей на земле?', '7 827 000 000 ', '7 192 000 000 ', '6 975 000 000 ', '8 127 000 000 ')
g6 = Guestion('Сколько лет Земле?', '4,543E9 лет', '5,214E3 лет', '3,981E4 лет', '2,163E9 лет')

window.total = 0
window.score = 0

g_list.append(g)
g_list.append(g1)
g_list.append(g2)
g_list.append(g3)
g_list.append(g4)
g_list.append(g5)
g_list.append(g6)
shuffle(g_list)

next_guestion()

btn_OK.clicked.connect(click_OK)
window.show()
app.exec()

















