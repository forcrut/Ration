from django.shortcuts import render
from .models import Norm, Nutrition
from settings import CALCULATOR_FIELDS_NAMES
from django.http import JsonResponse

# Create your views here.

def calculator(request):
	return render(request, 'calculator.html', {'norms': Norm.objects.all(), 'fields': CALCULATOR_FIELDS_NAMES, 'fields_len': len(CALCULATOR_FIELDS_NAMES),
		'nutrs': Nutrition.objects.all()})

def get_norm(request, ind=None):
	if ind is None:
		norm = [0]*len(CALCULATOR_FIELDS_NAMES)
	else:
		try:
			norm = Norm.objects.get(id=ind).to_list()
		except Norm.DoesNotExist:
			norm = [0]*len(CALCULATOR_FIELDS_NAMES)
	return JsonResponse({'norm': norm})

def get_nutr(request, ind=None):
	if ind is None:
		nutr = [0]*len(CALCULATOR_FIELDS_NAMES)
	else:
		try:
			nutr = Nutrition.objects.get(id=ind).to_list()
		except Norm.DoesNotExist:
			nutr = [0]*len(CALCULATOR_FIELDS_NAMES)
	return JsonResponse({'nutr': nutr})
