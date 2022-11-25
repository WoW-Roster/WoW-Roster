from django.shortcuts import render

def bosses_selection(request):
    bosses_file = open('./bosses.txt', 'r')
    data = bosses_file.read()
    list = data.split('\n')
    bosses_file.close()
    return render(request, 'bosses_selection.html', {'list': list})

def players_selection(request):
    return render(request, 'players_selection.html')
