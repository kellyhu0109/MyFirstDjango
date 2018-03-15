# from django.http import HttpResponse

# def root(request, n1, n2):
#     # w = request.GET.get('w')
#     # s = '<h1>Hello World</h1>'
#     return HttpResponse(n1+n2)

from django.shortcuts import render

def root(request, n1, n2):
    s = n1 + n2
    return render(request, 'hi.html',{
        's':s,
    })

def r(request, start, end):
    if start > end:
        start, end = end, start
       
    rr = range(start, end+1)

    rr=reversed(rr)

    return render(request, 'r.html', {
        'rr':rr,
    })