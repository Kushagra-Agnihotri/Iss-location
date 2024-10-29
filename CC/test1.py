import requests
import time
from datetime import datetime

def get_iss_location():
    response = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
    data = response.json()
    print(f"Latitude: {data['latitude']}, Longitude: {data['longitude']}")

def get_country_code():
    response_for_location = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
    data_for_location = response_for_location.json()
    latitude = data_for_location['latitude']
    longitude = data_for_location['longitude']
    response = requests.get(f"https://api.wheretheiss.at/v1/coordinates/{latitude},{longitude}")
    data = response.json()
    print(f"Country Code: {data['country_code']}, Time Zone: {data['timezone_id']}")

def get_iss_at_time(date, time):
    #converting the date time string to a unix timestamp
    date_string = f"{date} {time}"
    date_time_obj = datetime.strptime(date_string, "%d/%m/%Y %H:%M:%S")
    timestamp = date_time_obj.timestamp()

    response = requests.get(f"https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps={timestamp}")
    data = response.json()[0]

    print(f"Latitude: {data['latitude']}, Longitude: {data['longitude']}")

def main():

    print(('What would you like to fetch?'
            '\n--------------------------------'
            '\n 1: ISS Location' 
            '\n 2: ISS Country Code' 
            '\n 3: Location of ISS at specified time'
            '\n--------------------------------'
            '\nEnter 1/2/3 to continue'
            '\nEnter anything else to Exit"'))
    option = input()
    if(option == '1'):
        print("Processing Results...")
        get_iss_location()
    elif(option == '2'):
        print("Processing Results...")
        get_country_code()
    elif(option =='3'):
        print("Enter desired date in DD/MM/YYYY format")
        date = input()
        print("Enter desired time in HH:MM:SS format")
        time= input()
        print("Processing Results...")
        get_iss_at_time(date,time)
    else:
        return
   


if __name__ == "__main__":
    main()
