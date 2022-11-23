from django.shortcuts import render

def bosses(request):
    bossesFile = open('./bosses.txt', 'r')
    data = bossesFile.read()
    list = data.split('\n')
    print(list)
    bossesFile.close()
    return render(request, 'bosses.html', {'list': list})
