class Temp:
    def __init__(self, a="default", b=0):
        self.a: str = a
        self.b: int = b


def f(a, b):
    print(a, b)


def f1(**kwargs):
    print(kwargs.get('a'), kwargs.get('b'))


d = {
    "a": "new value",
    "b": 123,
    "c": 0.5
}

if __name__ == "__main__":
    # f(**d)
    f1(**d)
    print(d)
    # print(tuple(**d))
    print(Temp())
    print(Temp(**d))
    print("a", Temp(**d).a)
    print("b", Temp(**d).b)
