class Human:
    def __init__(self, name):
        self.name = name

    # ответ по умолчанию для всех одинаковый, можно
    # доверить его родительскому классу
    def answer_question(self, question):
        print(f'Очень интересный вопрос! Не знаю.')


#    def __str__(self):
#        return (f'someone: {self.someone}, '
#                f'question:{self.question},')

class Student(Human):
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос;
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, someone, question):
        #self.someone = someone
        #elf.question = question
        # напечатайте на экран вопрос в нужном формате
        print(str(f'{someone.name}, {question}'))
        # запросите ответ на вопрос у someone
        someone.answer_question(question)
        print()  # этот print выводит разделительную пустую строку


class Curator(Human):
    # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
    # если да - ответить на него
    # если нет - вызвать метод answer_question() у родительского класса
    def answer_question(self, question):
        self.question = question
        if self.question == f'мне грустненько, что делать?':
            print(f'Держись, всё получится. Хочешь видео с котиками?')
        else:
            super().answer_question(question)


# объявите и реализуйте классы CodeReviewer и Mentor
class CodeReviewer(Human):
    def answer_question(self, question):
        self.question = question
        if self.question == f'когда каникулы?':
            print(f'Очень интересный вопрос! Не знаю.')
        elif self.question == f'что не так с моим проектом?':
            print(f'О, вопрос про проект, это я люблю.')
        else:
            super().answer_question(question)


class Mentor(Human):
    def answer_question(self, question):
        self.question = question
        if self.question == f'мне грустненько, что делать?':
            print(f'Отдохни и возвращайся с вопросами по теории.')
        elif self.question == f'как устроиться работать питонистом?':
            print(f'Сейчас расскажу.')
        else:
            super().answer_question(question)


# следующий код менять не нужно, он работает, мы проверяли
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')