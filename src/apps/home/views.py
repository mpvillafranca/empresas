# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Bussiness,Student

# Create your views here.
def index(request):
	"""
	Vista correspondiente a la página principal de la aplicación empresas.
		En esta vista listamos las empresas almacenadas en la base de datos, así como 
		los alumnos que están trabajando en ella. A continuación, se muestra también 
		un ranking de las empresas según su nota media.
	"""
	template = loader.get_template('home/index.html')
	asociados=dict()
	notas=dict()
	for bussiness in Bussiness.objects.all():
		students = []
		average=0
		cont=0
		for student in Student.objects.all():
			if student.bussiness == bussiness:
				students.append(student.alias)
				average=average+student.mark
				cont=cont+1
		asociados[bussiness]=students
		average=average/cont
		notas[bussiness]=average
	context = RequestContext(request,{'asociados':asociados,'notas':notas,})
	return HttpResponse(template.render(context))
