class Tv:

    def __init__(self, channel=0, volume=0):
        self.channel=channel
        self.volume=volume

    def set_volume(self, volume=0):
        volume=int(input('Введите какую громкость вы хотите поставить: '))
        self.volume=volume
        if self.volume>100:
            print('Ишь чего захотел')
            self.volume=100
        elif self.volume<0:
            print('Ишь чего захотел')
            self.volume=0


    def set_channel(self, channel=0):
        channel=int(input('Введите какой канал вы хотите включить: '))
        self.channel=channel
        if self.channel>225:
            print('Такого канала не существует')
            self.channel=0
        elif self.channel<0:
            print('Такого канала не существует')
            self.channel=0
    
    def talk(self):
        print('Вы смотрите', self.channel, 'канал, на громкости', self.volume)

def main():
    tv=Tv()
    choice=None
    while choice!='0':
        print \
        ('''
        *Шумит по телевизорски*
                Меню

        0-выключить телевизор
        1-изменить громкость
        2-изменить канал
        3-просмотреть параметры
        ''')
        choice=input('Ваш выбор: ')
        print()

        #Выход

        if choice=='0':
            print('*Агрессивно выключается*')

        #Изменение звука

        elif choice=='1':
            tv.set_volume()

        #Изменение канала
           
        elif choice=='2':
            tv.set_channel()
        
        #Просмотр параметров
        elif choice=='3':
            tv.talk()

        else:
            print('Ты чё, выбери пункт из меню', choice)

main()
        

        