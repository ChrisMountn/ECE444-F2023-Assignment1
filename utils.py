class Utils:
    @staticmethod
    def reversed(number):
        if not isinstance(number, int):
            raise ValueError("Input must be an integer")
        reversed_num = int(str(number)[::-1])
        return reversed_num

    @staticmethod
    def formatter(number):
        if not isinstance(number, int):
            raise ValueError("Input must be an integer")
        binary_format = bin(number)
        octal_format = oct(number)
        return binary_format, octal_format