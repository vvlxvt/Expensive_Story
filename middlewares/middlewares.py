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
