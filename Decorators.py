def announce(f):
    def wrapper():
        print("Function about to run")
        f()
        print("Done with function")
    return wrapper

@announce
def hello():
    print("Hello hope")



hello()