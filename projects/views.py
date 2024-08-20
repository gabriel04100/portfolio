from django.shortcuts import render

# Create your views here.
# projects/views.py

from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from .models_loader import predict_image
import os
import tempfile

def project_detail(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        temp_image_path = os.path.join(tempfile.gettempdir(), image.name)
        
        with open(temp_image_path, 'wb+') as f:
            for chunk in image.chunks():
                f.write(chunk)
        
        prediction = predict_image(temp_image_path)
        return JsonResponse({'prediction': prediction})
    
    return render(request, 'project_detail.html')

#def project_detail(request):
#    return render(request, 'project_detail.html')
