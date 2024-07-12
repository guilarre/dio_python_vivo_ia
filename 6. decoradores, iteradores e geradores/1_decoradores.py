import functools

def duplicate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@duplicate
def learn(technology):
    print(f"I'm learning {technology}!")

learn("Python")
print(learn.__name__)