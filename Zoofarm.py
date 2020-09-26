class Critter:
    """Виртуальный питомец"""
    total = 0

    @staticmethod   
    def status():
        print("Общее число зверюшек", Critter.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total += 1

    def __str__(self):
        ans = 'Объект класса Critter\n'
        ans += 'имя: ' + self.name + '\n'
        return ans
    
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверушки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def unhappiness(self):
        unhappiness = self.hunger + self.boredom
        return unhappiness

    def talk(self):
        print("Меня зовут", self.name, 
              ", и сейчас я чувствую себя", self.mood, 'Я голоден на', self.hunger, 'единиц, и мне скучно на', self.boredom, 'единиц.')
        self.__pass_time()

    def eat(self, food):
        self.food=food
        print("Мррр...  Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        self.fun=fun
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    import random
    count=int(input('Введите изначальное количество зверюшек на ферме: '))
    animals=[]
    for i in range(count):
        crit_name = input("Как вы назовете свою зверюшку?: ")
        crit = Critter(crit_name, random.randint(1, 10), random.randint(1,10))
        animals.append(crit)

    choice = None  
    while choice != "0":
        print \
        ("""
        Мои зверюшки
    
        0 - Выйти
        1 - Узнать о самочувствии зверюшек
        2 - Покормить зверюшек
        3 - Поиграть со зверюшками
        4 - Купить еще одну зверюшку
        """)
    
        choice = input("Ваш выбор: ")
        print()

        # выход
        if choice == "0":
            print("До свидания.")

        # беседа со зверюшкой
        elif choice == "1":
            for i in animals:
                animal=i
                animal.talk()
        
        # кормление зверюшки
        elif choice == "2":
            food=int(input('Введите количество еды, которое вы хотите дать зверушкам: '))
            for i in animals:
                animal=i
                animal.eat(food)
         
        # игра со зверюшкой
        elif choice == "3":
            fun=int(input('Введите количество времени, которое вы хотите провести со зверюшками: '))
            for i in animals:
                animal=i
                animal.play(fun)

        # Купить зверюшку
        elif choice=='4':
            crit_name=input('Введите имя новой зверюшки: ')
            crit = Critter(crit_name, random.randint(1, 10), random.randint(1,10))
            animals.append(crit)

        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)
    
main()
