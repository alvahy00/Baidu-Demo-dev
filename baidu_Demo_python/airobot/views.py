from django.shortcuts import render
from .models import Post
from . import templates
from .api import get_ernie_response # Ensure this function is defined to call ERNIE Bot
from django.http import JsonResponse
import json

def home(request):
    if request.method == "POST":
        user_message = request.body.decode('utf-8')
        message_data = json.loads(user_message)
        prompt = message_data.get('message', '')
        
        # Get response from ERNIE Bot
        bot_response = get_ernie_response(prompt)
        print("HI")
        return JsonResponse({'response': bot_response},'airobot/home.html')
    return render(request, 'airobot/home.html')


'''
def index(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        response = get_ernie_response(prompt)
        return render(request, "ernie/index.html", {"response": response})
    return render(request, "ernie/index.html")
'''




def chat(request):
    if request.method == "POST":
        user_message = request.body.decode('utf-8')
        message_data = json.loads(user_message)
        prompt = message_data.get('message', '')
        
        # Get response from ERNIE Bot
        bot_response = get_ernie_response(prompt)
        print("HI")
        return JsonResponse({'response': bot_response})