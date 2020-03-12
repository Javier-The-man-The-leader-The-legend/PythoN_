from random import randint
from time import perf_counter
def random_decotator(func):
    def wrapper(*args):
        print(randint(0, 100))
        func(*args)
    return wrapper
@random_decotator
def say_hello():
    print("Hello!")
@random_decotator
def say_goodbye(name):
    print("Goodbye "+name)
# say_hello()
# say_goodbye("javi")

def timer(func):
    def wrapper(*args):
        satart_time = perf_counter()
        func(*args)
        end_time = perf_counter()
        print(f"Function took {end_time - satart_time}s")
    return wrapper
@timer
def quick_function():
    print("a")
quick_function()
@timer
def slow_function():
    print("This is a slow function")
    for _ in range(1000000):
        randint(0,1000000)
slow_function()