from CarInfo import CarInfo
from UserInterface import UserInterface


if __name__ == "__main__":
    car_input = input("Enter the Car Details\n")
    car_info = UserInterface.extractDetails(car_input)

    if car_info:
        availability = car_info.checkAvailability()
        if availability == "Not Available":
            print("Invalid Details")
        else:
            print(f"Car Id : {car_info.getCarId()}")
            print(f"Car Name : {car_info.getCarName()}")
            print(f"Car Type : {car_info.getCarType()}")
            print(f"City : {car_info.getCity()}")
            print(f"Available car and price is: {availability}")
    else:
        print("Invalid Details")
