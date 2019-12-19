'''this is doc string for the module'''
s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]

def foo(arg):
    '''docstring'''
    print(f'arg = {arg}')

class Foo:
    '''docstring'''
    pass

# When a .py file is imported as a module, Python sets the special dunder variable __name__ to the name of the module. However, if a file is run as a standalone script, __name__ is (creatively) set to the string '__main__'. Using this fact, you can discern which is the case at run-time and alter behavior accordingly:

if (__name__ == '__main__'):
    print('Executing as standalone script')
    print(s)
    print(a)
    foo('quux')
    x = Foo()
    print(x)