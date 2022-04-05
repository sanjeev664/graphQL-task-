
from django.contrib import messages
from django.shortcuts import redirect, render
import requests
# Create your views here.
def HomeView(request):
    if request.method =="POST":
        image_file = request.FILES.get('image_file')
        files = {
        'operations': (None, '{"query": "mutation ($file: Upload) { myUpload(fileIn: $file) { ok }}", "variables": { "file": null }}'),
        'map': (None, '{ "0": ["variables.file"]}'),
        '0': ('news.txt', open(image_file.name, 'rb')),
        }
        response = requests.post('http://localhost:8000/graphql', files=files)  
        messages.success(request,"Uploaded Successfully!")    
        return redirect('graphtask:homepage')  
    return render(request, 'graphql_index.html')