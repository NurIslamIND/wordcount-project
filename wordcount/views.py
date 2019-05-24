from django.http import HttpResponse

from django.shortcuts import render
import operator


def home(request):
    return render(request,'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddidctionary = {}

    for word in wordlist:
        if word in worddidctionary:
            worddidctionary[word] +=1
        else:
            worddidctionary[word] =1

    sortedwords = sorted(worddidctionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords })

def about(request):
    return render (request,'about.html')