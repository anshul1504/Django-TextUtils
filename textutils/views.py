#I had created this file - Anshul
from django.http.response import HttpResponse
from  django.shortcuts import render

def index(request):
    return render(request, 'index.htm')

def analyze(request):
    #get the text 
    djtext = (request.POST.get('text','default'))
    
    #checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    
    #check which checkbox is on
    if removepunc == "on":
        punctuaions = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for char in djtext:
            if char not in punctuaions:
                analyzed = analyzed + char
        parms = {'purpose': 'Remove Punctuations', 'analyze_text': analyzed}
        djtext = analyzed
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        parms = {'purpose': 'Change to UPPERCASE', 'analyze_text': analyzed}
        djtext = analyzed
    if(extraspaceremover == "on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index + 1]==" "):    
                analyzed = analyzed + char
        parms = {'purpose': 'Extra Space Remover', 'analyze_text': analyzed}
        djtext = analyzed               
    if(newlineremover == "on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        parms = {'purpose': 'Remove New lines', 'analyze_text': analyzed}
    if(removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select the opretion")               
    
    return render(request, 'analyze.htm', parms) 

