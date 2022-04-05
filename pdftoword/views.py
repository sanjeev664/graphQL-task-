from fileinput import filename
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
# from celery import shared_task
import time
from django.shortcuts import render






# Create your views here.
# def index(request):
#     if request.method=="POST":
#         try:
#             x=request.FILES.get('filename')
#             if x:
#                 doc = aw.Document(x.name)
#                 doc.save("word.docx")
#         except:
#             messages.error(request, 'Something went wrong.')
#             return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

#         return doc
        # doc = aw.Document(x)
        # doc.save("pdf-to-word.docx")       
        
        
    
    # return render(request,"index.html")


def index(request):
    return render(request,"pdfword_index.html")

# @celery_app.task(ignore_result=False)
# def send_email_run_task():
#     """ celery taks send email """
#     print("Task is runing.")
  
#     return "Done"