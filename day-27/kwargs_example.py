def foo(*a):
    print(sum(a))


foo(1, 2, 3)


def kwargs_fun(**kwargs):
    name = kwargs.get('name')
    age = kwargs.get('age')
    height = kwargs.get('height')
    print(kwargs)
    print(f'name -> {name}, age -> {age}, height -> {height}')


kwargs_fun(name='suraj', age=25, height=170)
