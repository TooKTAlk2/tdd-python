class Dollor:
    def __init__(self, amount) -> None:
        self.__amount = amount

    def times(self, multiplier):
        return Dollor(self.__amount * multiplier)

    def __eq__(self, __o: object) -> bool:
        return self.__amount == __o.__amount
