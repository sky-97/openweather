
import model
def show_data(data):
    if  data["cod"] != "408":

        temp = data['main']['temp']
        wind_speed = data['wind']['speed']
        latitude = data['coord']['lat']
        longitude = data['coord']['lon']
        description = data['weather'][0]['description']
    #    date_time = data['sys']['dt_xt']
        print('Temperature : {} degree celcius'.format(temp))
        print('Wind Speed : {} m/s'.format(wind_speed))
        print('Latitude : {}'.format(latitude))
        print('Longitude : {}'.format(longitude))
        print('Description : {}'.format(description))
    #    print('Date and time : {}',format(date_time))
    else:
        print("please enter valid city name:")


def quit():
    return

def main():
    print('1. ENTER CITY NAME:')
    print('2. GO BACK')
    choice = input('Enter your choice : ')

    if choice == '1':
        data = model.by_city()
        show_data(data)
        #model.by_city()
    elif choice == '2':
        quit()

    else:
        print("enter valid choice")

if __name__ == '__main__':
    main()
