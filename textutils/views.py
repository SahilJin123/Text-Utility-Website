#I have created this file :- Sahil

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # a='''Home <br><button><a href="removepunc/">Remove Punctuations</a></button>
    # <button><a href="capitalizefirst/">Capitalize First</a></button>'''
    # return HttpResponse(a)

    #Third argument of render
    # params = {'name':'Sahil','place':'Patiala'}
    return render(request,'index.html')


def analyze(request):
    #get the text
    djtext=request.GET.get('text','default')
    #checkbox value
    djrempunc=request.GET.get('removepunc','off ')
    djcapfirst = request.GET.get('capfirst','off')
    djnewlineremover = request.GET.get('newlineremover','off')
    djextraspaceremover = request.GET.get('extraspaceremover','off')
    djcharcount = request.GET.get('charcount','off')
    #Analyze the text
    for char in djtext:
            print(char)
    punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    analyzed=""
    if djrempunc=='on' and djcapfirst=='off':
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif (djcapfirst=='on' and djrempunc=='off'):
        djtext=djtext.upper()
        params={'purpose':'Capitalize','analyzed_text':djtext}
        return render(request,'analyze.html',params)
    elif (djrempunc=='on' and djcapfirst=='on'):
        djtext=djtext.upper()
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuations and Capitalize','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(djnewlineremover=='on'):
        analyzed=""
        for char in djtext:
            if char != "\n":
                analyzed=analyzed+char
        params={'purpose':'Remove New Line','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(djextraspaceremover=='on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params={'purpose':'Extra Space Remove','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(djcharcount=='on'):
        count = 0
        for char in djtext:
            print(char)
            count+=1
        params={'purpose':'Character Count','analyzed_text':f'Number of Character in this document is {count}'}
        return render(request,'analyze.html',params)
    else:
        params={'purpose':'','analyzed_text':djtext}
        return render(request,'analyze.html',params)



def about(request):
    return render(request,'aboutus.html')

def contact(request):
    return render(request,'contactus.html')


# def capfirst(request):
#     return HttpResponse("Capitalize First")

# def newlineremove(request):
#     return HttpResponse("new line remove")

# def spaceremove(request):
#     return HttpResponse("space remove") 

# def charcount(request):
#     return HttpResponse("char count") 


# def read_file(request):
#     f = open('one.txt', 'r')
#     file_content = f.read()
#     f.close()
#     return HttpResponse(file_content, content_type="text/plain") 

# def personal_navigator(request):
#     return HttpResponse('''<a href="https://www.geeksforgeeks.org/">GFG</a> <br>
#     <a href="https://www.thecodehelp.in/course/web-development-bootcamp">Code Help</a>''')  