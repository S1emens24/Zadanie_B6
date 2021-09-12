class Balance:
    def __init__(self, name, surname, balance):
        self.name = name
        self.surname = surname
        self.balance = balance

    def get_gold_of_user(self):
        return "Клиент «" + self.name + " " + self.surname + "». Баланс: " + str(self.balance) + " руб."

user1 = Balance("Иван", "Петров", 50)

print(user1.get_gold_of_user())