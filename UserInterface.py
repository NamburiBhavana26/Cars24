from CarInfo import CarInfo

class UserInterface:
    @staticmethod
    def extractDetails(carDetails):
        try:
            carId, carName, carType, city = carDetails.strip().split(":")
            car_info = CarInfo(carId, carName, carType, city)
            return car_info
        except:
            return None
