class CustomException(Exception):

    def __init__(self, message="예외가 발생했어요", value=None) -> None:
        Exception.__init__(self)
        self.__message__ = message
        self.__value__ = value

    def __str__(self):
        return self.get_message()

    def get_message(self):
        return self.__message__

    def get_value(self):
        return self.__value__

    def print(self):
        print('#### 오류 정보 ####')
        print('메시지', self.get_message())
        print('값:', self.get_value())


try:
    raise CustomException(message="딱히 이유 없음", value=273)
except CustomException as e:
    e.print()
