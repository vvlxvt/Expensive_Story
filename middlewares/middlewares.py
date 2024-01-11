from dataclasses import dataclass, astuple, asdict, field

# @dataclass(frozen=True)
@dataclass(order=True)
# Чтобы работали другие виды сравнения (__lt__ (меньше),
# __le__ (меньше или равно), __gt__ (больше) и __ge__ (больше или равно)),
# мы должны установить аргумент order в значение True
class Person:
    first_name: str = "Ahmed"
    last_name: str = "Besbes"
    age: int = 30
    job: str = "Data Scientist"
    full_name: str = field(init=False, repr=True)
    mylist: dict = field(default_factory=dict)
    def __post_init__(self):
    #  метод можно вызвать для инициализации внутреннего атрибута, который зависит от ранее заданных атрибутов
        self.full_name = self.first_name + " " + self.last_name
    def __repr__(self):
        return f"{self.full_name} ({self.mylist})"

a = Person()
print(a.__dict__)

first_tuple = (1, 2, 3, 4, 5)
second_tuple = (2, 4, 5)

contains_all = list(elem in first_tuple for elem in second_tuple)
print(contains_all) # True


class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value must be positive")
        self._value = new_value

x = MyClass(-12)
x.value = -17
print(x.__dict__)
