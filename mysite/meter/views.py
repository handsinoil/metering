from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import UnitValue, Rate, Meter, UsersSNT, News


def index(request):
	listing = News.objects.all()
	out = ", ".join([q.title for q in listing])
	template = loader.get_template('meter/index.html')
	context = {
		"listing": listing,
	}
	#return HttpResponse(template.render(context, request))
	return render(request, 'meter/index.html', context)

