class Volunteer:
    def __init__(self, name, city):
        self.name = name
        self.city = city

class Person(Volunteer):
    def __init__(self, name, city, status):
        Volunteer.__init__(self, name, city)
        self.status = status

    def add_to_list(self, g_list):
        return g_list.append(f'{self.name}, г.{self.city}, статус "{self.status}"')

    def display_person(self):
        return f'{self.name}, г.{self.city}, статус "{self.status}"'

person_list = []
person1 = Person('Иван Петров', 'Москва', 'Волонтер')
person2 = Person('Петр Иванов', 'Казань', 'Стрелок')
person1.add_to_list(person_list)
person2.add_to_list(person_list)
print(person1.display_person())
print(person_list)
