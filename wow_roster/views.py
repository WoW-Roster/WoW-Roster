from django.shortcuts import render

def Bosses(request):
    bossesFile = open('./bosses.txt', 'r')
    data = bossesFile.read()
    list = data.split('\n')
    print(list)
    return render(request, 'blog/Bosses.html', {'list': list})