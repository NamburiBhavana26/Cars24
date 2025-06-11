class CarInfo:
    def __init__(self, carId, carName, carType, city):
        self.__carId = carId
        self.__carName = carName
        self.__carType = carType
        self.__city = city

    # Getters
    def getCarId(self):
        return self.__carId

    def getCarName(self):
        return self.__carName

    def getCarType(self):
        return self.__carType

    def getCity(self):
        return self.__city

    # Setters
    def setCarId(self, carId):
        self.__carId = carId

    def setCarName(self, carName):
        self.__carName = carName

    def setCarType(self, carType):
        self.__carType = carType

    def setCity(self, city):
        self.__city = city

    # Method to check availability
    def checkAvailability(self):
        car_name = self.__carName.lower()
        car_type = self.__carType.lower()
        city = self.__city.lower()

        valid_cars = {
            "nissan": {
                "sedan": ("Kicks", 8400.0),
                "suv": ("Magnite", 10800.0),
                "muv": ("Terrano", 14400.0)
            },
            "ford": {
                "sedan": ("Figo", 4802.0),
                "suv": ("Eco Sport", 9605.0),
                "muv": ("Endeavour", 21600.0)
            }
        }

        valid_cities = ["new york", "denver", "losangels"]

        if car_name not in valid_cars:
            return "Not Available"
        if car_type not in valid_cars[car_name]:
            return "Not Available"
        if city not in [c.replace(" ", "").lower() for c in valid_cities]:
            return "Not Available"

        available_car, price = valid_cars[car_name][car_type]
        return f"{available_car} and ${price}"
