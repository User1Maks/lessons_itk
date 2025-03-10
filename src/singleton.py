from config import logger


# Реализация Singleton с помощью метакласса
class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        """
        Вызывается при создании объекта класса, использующего этот
        метакласс.
        """
        if cls not in cls._instance:
            cls._instance[cls] = (
                super(Singleton, cls).__call__(*args, **kwargs)
            )
        return cls._instance[cls]


class Logger(metaclass=Singleton):
    pass


singleton1 = Logger()
singleton2 = Logger()

print(singleton1 is singleton2)


###############################################################################
# Реализация Singleton с помощью метода __new__ класса
class SingletonNew:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonNew, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        pass


class LoggerNew(SingletonNew):
    pass


singleton_new1 = LoggerNew()
singleton_new2 = LoggerNew()

print(singleton_new1 is singleton_new2)

###############################################################################
# Реализация Singleton через механизм импортов
logger.log("Приложение запущено")
