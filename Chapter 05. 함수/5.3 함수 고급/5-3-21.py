def global_variable_change():
    global a
    a += 10
    print('a 10 증가')


a = 10
print('a = ',a)
global_variable_change()
print('a = ',a)
global_variable_change()
print('a = ',a)
