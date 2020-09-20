class Tv:

    def __init__(self, channel, volume):
        self.channel=channel
        self.volume=volume

    def set_volume(self, volume):
        volume=int(input('Введите какую громкость вы хотите поставить'))
        self.volume=volume
        if volume>100:
            volume=100
        elif volume<0:
            volume=0


    def set_channel(self, channel):
        channel=int(input('Введите какой канал вы хотите включить'))
        self.channel=channel
        if channel>225:
            print('Такого канала не существует')
            channel=0
        elif channel<0:
            print('Такого канала не существует')
            channel=0
    
    def talk(self):
        print('Вы смотрите', self.channel, 'на громкости', self.volume)

def main():
    tv=Tv()
    choice=None
    while choice!='0':
        print \
        ('''
        Меню

        0-выключить телевизор
        1-изменить громкость
        2-изменить канал

        ''')
        choice=input('Ваш выбор: ')
        print()

        #Выход

        if choice=='0':
            print('*Агрессивно выключается*')

        #Изменение звука

        elif choice=='1':
            tv.set_volume

        #Изменение канала
           
        elif choice=='2':
            tv.set_channel

        else:
            print('Ты чё, выбери пункт из меню', choice)

main()
        

        