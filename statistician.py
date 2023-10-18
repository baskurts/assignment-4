class statistician:
    """The statistician class may be given a sequence of float numbers and it will
    obtain the sum of the numbers and a count of the numbers its been given.
    """
    def __init__(self):
        """Construct a statistician with all instance variables initialized to zero.
        :ivar __nextNum: next float number given to the calling statistician
        :ivar __count: count of float numbers given to the calling statistician
        :ivar __sum: sum of the float numbers given to the calling statistician
        """
        self.__nextNum = 0.0
        self.__count = 0
        self.__sum = 0.0

    def giveNextNum(self, number: float):
        """Sets __nextNum to the specified number, increases __count by 1, and
        calls __computeSum
        Args:
        number (float): specified number
        Raises:
        ValueError: indicates specified number is not a float
        """
        if not isinstance(number, float):
                raise ValueError("Number is not a float")
        self.__nextNum = number
        self.__count += 1
        self.__computeSum()

    def __computeSum(self):
        """Computes the sum of the float numbers that have been
        given to the calling statistician.
        """
        self.__sum += self.__nextNum

    def __str__(self):
        """Returns string representation of the calling statistician.
        Returns:
        2
        str: string representation of the calling statistician
        """
        return f"nextNum: {self.__nextNum}, Count: {self.__count}, Sum: {self.__sum}"

    def __eq__(self, other):
        """Tests if the calling statistician is equal to the specified object.
        Args:
        other: the specified object
        Returns:
        Boolean: True if the calling statistician is equal to the specified
        object, else False
        """
        if not isinstance(other, statistician):
                return False
        return self.__count == other.__count and self.__sum == other.__sum