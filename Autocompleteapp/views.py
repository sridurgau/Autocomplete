import json
from django.shortcuts import render, redirect
from .Autocomplete import searchwords, sortwords
from django.http import JsonResponse, HttpResponse


#renders the search page.
def view(request):
    return render(request, 'Autocomplete/base.html', {})


# Returns the autocomplete options while typing the particular word
def autocomplete(request):
    if request.is_ajax():
        query = request.GET.get('term','')
        results = sortwords(searchwords(query.lower()), query.lower())
        data = json.dumps(results)
    else:
        data = 'fail'
    type = 'application/json'
    return HttpResponse(data, type)


#Returns a json format response for particular word
def results(request):
    if request.method == 'GET':
        query = request.GET.get('term')
        if query:
            result = sortwords(searchwords(query.lower()), query.lower())
            if len(result) == 0:
                return JsonResponse({'Result': "Word not found."})
            else:
                return JsonResponse({'Result': result})
        else:
            return redirect('/')