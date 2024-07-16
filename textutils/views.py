from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get("text", "default")
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get("newlineremover", "off")
    extraspaceremover = request.POST.get("extraspaceremover", "off")
    punctutaions = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    params = {}
    analyzed = ""
    if removepunc == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctutaions:
                analyzed = analyzed + char
        djtext = analyzed
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        djtext = analyzed
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == "  ":
                pass
            else:
                analyzed = analyzed + char
    params = {"purpose": "Removed new line", "analyzed_text": analyzed}
    if removepunc == "on" or fullcaps == "on" or newlineremover == "on" or extraspaceremover == "on":
        return render(request, "analyze.html", params)
    else:
        return HttpResponse("Error")
