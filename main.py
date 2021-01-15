import csv
import glob


class Refer:
    """
    Класс объекта Справка
    """
    def __init__(self, number, dat, faculty, group, full_name, grants, where_to):       # конструктор класса
        self.number = number
        self.dat = dat
        self.faculty = faculty
        self.group = group
        self.full_name = full_name
        self.grants = grants
        self.where_to = where_to
        peremen = 12

    def __setattr__(self, attr, value):     # установка атрибутов
        if attr == 'number':
            self.__dict__[attr] = value
        elif attr == 'dat':
            self.__dict__[attr] = value
        elif attr == 'faculty':
            self.__dict__[attr] = value
        elif attr == 'group':
            self.__dict__[attr] = value
        elif attr == 'full_name':
            self.__dict__[attr] = value
        elif attr == 'grants':
            self.__dict__[attr] = value
        elif attr == 'where_to':
            self.__dict__[attr] = value

        else:
            raise AttributeError

    def __repr__(self):
        return "Номер справки: " + self.number.join(("'", "'")) + " Дата: " + self.dat.join(("'", "'")) + \
               " Факультет: " + self.faculty.join(("'", "'")) + " Группа: " + self.group.join(("'", "'")) + \
               " ФИО студента: " + self.full_name.join(("'", "'")) + " Размер стипендии: " + \
               self.grants.join(("'", "'")) + " Куда выдается справка: " + self.where_to.join(("'", "'"))


class FileWriter:
    @staticmethod
    def number_of_files():
        """
        Статический метод number_of_files выполняет подсчёт файлов в директории Windows
        """
        print(len(glob.glob('/Windows/*.txt')))

    @staticmethod
    def reader_file():
        """
        Статический метод reader_file считывает строки из файла и записывает данные в словарь
        """
        dict = []
        with open("data.csv", "r") as fl:
            file = csv.DictReader(fl, delimiter=";")
            for row in file:
                elem = Refer(row['number'], row['dat'], row['faculty'], row['group'], row['full_name'], row['grants'], row['where_to'])
                dict.append(elem)
            return dict


class DictProc(FileWriter):
    def __init__(self, table):
        self.table_all = table

    def __getitem__(self, i):
        return self.table_all[i]

    def output_data(self):
        """
        Вывод всех данных, содержит иттератор
        """
        obj_dict = iter(self)
        while True:
            try:
                print(next(obj_dict))
            except StopIteration:
                break
        print('\n')

    def sort_by_name(self):
        """
        Сортировка списка объектов по имени
        """
        self.table_all = sorted(self.table_all, key=lambda name: name.full_name)
        self.output_data()

    def sort_by_condition(self):
        """
        Вывод данных, где размер стипендии больше 2200
        """
        for elem in self:   # self - поле со стипендией в каждой строчке таблицы
            if int(elem.grants) > 2200:
                print(elem)
        print('\n')


def main():
    """
    Функция, в которой вызываются все остальные функции
    """
    data = DictProc.reader_file()
    dat = DictProc(data)
    print("Введите 1, чтобы вывести все записи")
    print("Введите 2, чтобы отсортировать записи по полному имени")
    print("Введите 3, чтобы произвести выборку данных по критерию")
    print("Введите 4, чтобы подсчитать количество файлов директории")
    while True:
        num = input()
        if num == "1":
            dat.output_data()
        elif num == "2":
            dat.sort_by_name()
        elif num == "3":
            dat.sort_by_condition()
        elif num == "4":
            DictProc.number_of_files()
        else:
            print("Завершение работы")
            break


main()
