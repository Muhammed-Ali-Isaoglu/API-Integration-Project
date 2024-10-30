import requests

def get_weather(city):
    api_key="a4494e143f0b8c86e64559b2feb2be8a"
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response=requests.get(url)

    if response.status_code==200:
        data=response.json()
        main=data['main']
        weather=data['weather'][0]

        temperature=main['temp']
        feels_like=main['feels_like']
        weather_description=weather['description']


        print(f'{city}')
        print(f'Temperature is {temperature} C')
        print(f'Feels like {feels_like} C')
        print(f'weather description {weather_description.capitalize()}')
    else:
         print("City not found or API request failed")

    


if __name__=="__main__":
        city=input("inter city name: ")
        get_weather(city)
    

