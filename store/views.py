from django.shortcuts import render


def say_hello(request, num):

    a = 1
    b = a * 2
    return render(request, 'hello.html', {'b': b, 'num': num})