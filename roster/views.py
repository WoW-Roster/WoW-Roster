from django.shortcuts import render

def bosses(request):
    bossesFile = open('./bosses.txt', 'r')
    data = bossesFile.read()
    list = data.split('\n')
    bossesFile.close()
    return render(request, 'bosses.html', {'list': list})

def bosses2(request):
    bossesFile = open('./bosses.txt', 'r')
    data = bossesFile.read()
    list = data.split('\n')
    bossesFile.close()
    return render(request, 'bosses2.html', {'list': list})
