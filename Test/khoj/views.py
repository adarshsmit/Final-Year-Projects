from django.shortcuts import render_to_response, get_object_or_404
#from django.http import Http404,HttpResponse, HttpResponseRedirect
#from google import search
from django.template import RequestContext
from pygoogle import pygoogle
import requests
from grin import POST
#from google import search
# Create your views here.

infereddic = {}

def khoj(request):
    if request.POST:
        s_term = request.POST['term']
        if s_term in infereddic.keys():
            return render_to_response('khoj.html',{'result': infereddic[s_term]},context_instance=RequestContext(request))
        else :
            infereddic.setdefault(s_term, [])
            res = pygoogle(s_term)
            res.pages = 2
            return render_to_response('khoj.html',{'result': res.search()}, context_instance=RequestContext(request))
            if request.GET:
                if 'clicked' in request.GET:
                    urls = request.GET.get('url')
                    infereddic[s_term].append(urls)
            return render_to_response('khoj.html', context_instance=RequestContext(request))  
            # return HttpResponseRedirect("/")
    else :
        return render_to_response('khoj.html', context_instance=RequestContext(request))