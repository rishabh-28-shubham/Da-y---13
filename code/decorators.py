import time

def calculateTime(func):
    def wrapper(*args,**kwargs):
        st = time.time()
        func(*args,**kwargs)
        end = time.time()
        return end-st
    return wrapper

@calculateTime
def greet(x):
    print(f"Hello Class! {x}")


func_val = greet("34-502")

print(f"function execution time is, {func_val}")