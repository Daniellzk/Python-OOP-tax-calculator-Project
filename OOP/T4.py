class T4:
    def __init__(self, income, sin_number, name, year, pre_deducted_tax):
        self.__income = income
        self.__sin_number = sin_number
        self.__name = name
        self.__year = year
        self.__pre_deducted_tax = pre_deducted_tax

    def get_income(self):
        return self.__income

    def get_sin_number(self):
        return self.__sin_number

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def get_pre_deducted_tax(self):
        return self.get_pre_deducted_tax()

    def set_income(self, new_amount):
        return


