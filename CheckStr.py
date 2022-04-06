class BaseData(): #класс для проверки строки на содержание
    def __init__(self):
        self.spi1 = [] #список для маленьких букв латиницы
        self.spi2 = [] #список для больших букв латиницы
        self.spi_numbers = ['0','1','2','3','4','5','6','7','8','9']

    def alpha1(self): #метод генерирующий малые буквы
       #for i in range(65, 91):
            #self.spi1.append(chr(i))
        self.spi1 = [chr(i) for i in range(65, 91)]

    def alpha2(self): #метод генерирующий большие буквы
        self.spi2 = [chr(p) for p in range(97, 123)]


clasik = BaseData() #вызов класса
clasik.alpha1() #вызов генерации
clasik.alpha2()


def alphanumeric(password): #main функция для этой программы
    if (len(password) == 0): #проверяем пустая ли строка
        return False
    list_passwords = list(password)
    for i in list_passwords: #проверяем содержание строки на числа и буквы
        if(((i in clasik.spi1) or (i in clasik.spi2)) or (i in clasik.spi_numbers)):
            continue
        else:
            return False
    return True


stroka = ""
f = alphanumeric(stroka)
print(f)