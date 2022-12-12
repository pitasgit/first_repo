# try:
#     assert 1 == 2, 'comparatia nu este corecta'  #propozitia dintre ghilimele este atribuita
# except AssertionError as e:
#     print(e, ' programul nu a executat linia respectiva')
#
# print('Hello')
# -------------------------------------mai sus am exersat tratarea exceptiilor
from abc import abstractmethod, ABC
# class Masina:
#     def numar_roti(self):
#         print('Masina are 4 roti')
#
#
# class Jeep(Masina):
#     def suspensii(self):
#         print('Jeepul are suspensii mari')
#
#
# hummer = Jeep()
# hummer.numar_roti()
# hummer.suspensii()
# logan = Jeep()
# logan.numar_roti()
# logan.suspensii()
# ford = Masina()
# ford.numar_roti()
# --------------------------------mai sus avem mostenirea inheritance


class Masina(ABC):  # aici implementam o clasa abstracta(interfata)
    @abstractmethod
    def numar_roti(self):
        raise NotImplementedError

    @abstractmethod
    def culoare(self):
        raise NotImplementedError


class Suv(Masina):
    def __suspensii(self):
        print('Jeepul are suspensii mari')

    def numar_roti(self):
        print('4 roti de teren')

    def culoare(self):
        print('neagra')


class Sport(Masina):
    def numar_roti(self):
        print('4 roti de circuit')

    def culoare(self):
        print('rosu')


ferrari = Sport()
ferrari.numar_roti()
volvo = Suv()
volvo.culoare()  # am implementat polymprhism
ferrari.culoare()
# volvo.suspensii()

try:
    volvo.suspensii()
except NameError:
    print('sunt expert pe tratarea erorilor')
except AttributeError:
    print("test")
