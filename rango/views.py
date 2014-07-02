# ****** Rango Views.py ***********

from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.

def index(request):
	# Request the context of the request.
	# The context contains information such as the client's 
	# machine details, for example.
    context = RequestContext(request)
	
	# Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}
	
	# Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
	
	# return HttpResponse("Rango says hello world! <a href='/rango/about/'>About</a>")
    return render_to_response('rango/index.html', context_dict, context)
	
def about(request):
    context = RequestContext(request)
    context_dict = {'welcome': "WELCOME _____!"}
    return render_to_response('rango/about.html', context_dict, context)
	# return HttpResponse("Rango Says: Here is the about page. <a href='/rango/'>Home</a>")