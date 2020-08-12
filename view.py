from django.http imoprt HttpResponse

def index(requset):
	return HttpResponse('index')