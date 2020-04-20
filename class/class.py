class FourCal:
    def __init__(self, name, age, university):
        self.name = name
        self.age = age
        self.university = university

    def add(self, num1, num2):
        return num1+num2

    def sub(self, num1, num2):
        return num1-num2

    def mul(self, num1, num2):
        return num1*num2

    def div(self, num1, num2):
        if(num2 == 0):
            print('0으로 나눌 수 없습니다')
            return None
        return num1/num2


class MoreFourCal(FourCal):
    def sub(self, num1, num2):
        return num2 - num1

    def pow(self, a, b):
        return a**b

# computer = MoreFourCal('박지환', 25, '고려대학교')
# print(computer.pow(2,3))
# print(computer.name, computer.age, computer.university)
# print(computer.add(3,4))
# print(computer.sub(3,4))
# print(computer.mul(3,4))
# print(computer.div(3,4))

# calculator1 = FourCal('박지환', 25, '고려대학교')
# print(calculator1.name, calculator1.age, calculator1.university)
# print(calculator1.add(3,4))
# print(calculator1.sub(3,4))
# print(calculator1.mul(3,4))
# print(calculator1.div(3,0))
