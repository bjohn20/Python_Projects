

class Protected:
    def __init__(self):
        # Set a protected var in _getNumber 
        self._getNumber = 0
        # Set a private var in __getPrivateNum
        self.__getPrivateNum = 23

    # Added a method that prints the private var
    def privateNum(self):
        print(self.__getPrivateNum)


if __name__ == "__main__":
    # Set the class to obj var
    obj = Protected()
    # print the protected var
    print(obj._getNumber)
    # print the private var
    print(obj.privateNum())
