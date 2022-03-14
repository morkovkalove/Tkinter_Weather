from tkinter import *
import requests


root = Tk()


# Эта функция срабатывает при нажатии на кнопку "Посмотреть погоду"
def get_weather():
    # Получаем данные от пользователя
    city = cityField.get()

    # данные о погоде будем брать с сайта openweathermap.org
    key = 'dbb542714624b3d6d31350a48b5100b2'
    # ссылка, с которой мы получим все данные в формате JSON
    url = 'http://api.openweathermap.org/data/2.5/weather'
    # Дополнительные парамтеры в виде словаря :
    # (Ключ, город введенный пользователем и единицины измерения - metric означает Цельсий)
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    # Отправляем запрос по определенному URL
    result = requests.get(url, params=params)

    weather = result.json()
    # Полученные данные добавляем в текстовую надпись для отображения пользователю
    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'


#Настройка главного окна
root['bg'] = '#1E776D'
root.title('Твоя Погода')
root.geometry('300x250')
root.resizable(width=False, height=False)


#Создание фрейма

frame_top = Frame(root, bg='#FFB440', bd=5)

frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

# Все то-же самое, но для второго фрейма
frame_bottom = Frame(root, bg='#FFB440', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

#Текстовое поле для получения данных от пользователя
cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()

#Кнопка, при нажатии будет срабатывать метод "get_weather"
btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
btn.pack()

#Текстовая надпись будет выводить информацию о погоде
info = Label(frame_bottom, text='Погодная информация', bg='#ffb700', font=40)
info.pack()

root.mainloop()