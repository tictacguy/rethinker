from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import ollama
import json
from datetime import datetime

@csrf_exempt 
def home(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('problem', '').strip()
            
            if not user_input:
                return JsonResponse({'error': 'Please describe your problem'}, status=400)
            
            response = ollama.generate(
                model='llama3.2:3b',
                prompt=f"Analyze this problem and provide detailed solutions by providing a single question that will make the user think about the problem he asked for:\n\n{user_input}",
                stream=False
            )
            
            return JsonResponse({
                'user_input': user_input,
                'ai_response': response['response']
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    from django.shortcuts import render
    return render(request, 'home.html')