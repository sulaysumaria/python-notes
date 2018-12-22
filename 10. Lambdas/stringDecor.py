def decorFun(fun):
    def inner(n):
        result = fun(n) + ' How are you?'
        return result

    return inner


@decorFun
def hello(name):
    return 'Hello ' + name


print(hello('John'))
