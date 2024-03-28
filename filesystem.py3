class Container:
    """
    A container of integers that should support
    addition, removal, and search for the median integer
    """
    def __init__(self):
        self.data = []

    def add(self, value: int) -> None:
        """
        Adds the specified value to the container

        :param value: int
        """
        # TODO: implement this method
        self.data.append(value)
        self.data.sort()

    def delete(self, value: int) -> bool:
        """
        Attempts to delete one item of the specified value from the container

        :param value: int
        :return: True, if the value has been deleted, or
                 False, otherwise.
        """
        # TODO: implement this method
        try:
            self.data.remove(value)
            return True 
        except ValueError:
            return False

    def get_median(self) -> int:
        """
        Finds the container's median integer value, which is
        the middle integer when the all integers are sorted in order.
        If the sorted array has an even length,
        the leftmost integer between the two middle 
        integers should be considered as the median.

        :return: The median if the array is not empty, or
        :raise:  a runtime exception, otherwise.
        """
        # TODO: implement this method
        if not self.data:
            raise Exception("Container is empty")
        n = len(self.data)
        mid = n // 2
        if n % 2 == 0:
            return self.data[mid - 1]
        else:
            return self.data[mid]
