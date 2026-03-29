import requests

city=str(input("Město:"))
api_key = "api_key=e30e661abb45d2d33275ed289e9a8216"
def main(city, api_key):
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={None}&lon={None}&exclude={city}&appid={api_key}"
    try:
        response=requests.get(url)
        response.raise_for_status()

        data = response.json

        weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temp = data["main"]["temp"]

        print(f"V městě {city}",
              f"teplota: {temp} °C",
              f"stav: {description}.")
        
        if weather == "Rain":
            return True
        else:
            return False
    
    except Exception as e:
        print(f"Nastala chyba: {e}")
        return False
    
if __name__ == "__main__":
    main(city, api_key)


