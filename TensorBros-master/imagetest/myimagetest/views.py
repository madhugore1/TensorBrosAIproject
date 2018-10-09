from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import VideoModel
from .forms import UploadVideoForm

@csrf_exempt 
def video_upload(request):
	form = UploadVideoForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return JsonResponse({"Status":"okay"})
	
	return JsonResponse({"Status":"Not Ok"})
