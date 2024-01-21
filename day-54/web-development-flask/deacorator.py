def greet(function):
    def call():
        print("This is my greeting")
        function()
    return call


# @greet
def hello():
    print("Say hello ):")


@greet
def hi():
    print("Say hi (:")


# hello()

greet(hi)()
