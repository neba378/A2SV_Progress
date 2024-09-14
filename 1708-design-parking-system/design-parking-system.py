class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.type = [big,medium,small]

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            
            if self.type[0] >0:
                self.type[0]-=1
                return True
            else:
                return False
        elif carType == 2:
            if self.type[1] >0:
                self.type[1]-=1
                return True
            else:
                return False
        else:
            if self.type[2] >0:
                self.type[2]-=1
                return True
            else:
                return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)