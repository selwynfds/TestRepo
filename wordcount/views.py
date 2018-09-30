from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    # print(request.GET)
    print(request.POST)
    return render(request, 'home.html',{'chosada':'asad'})

def about(request):
    return render(request, 'about.html', {})

def count(request):
    # print(request.GET)
    print(request.POST)
    fulltext = request.POST['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    context = {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords}
    return render(request, 'count.html', context)
