from django.shortcuts import render
from django.http import JsonResponse
from .jira_tools import interact_with_jira_agent
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from .jira_tools import agent
def index(request):
    return HttpResponse("Welcome to the Jira Toolkit App!")


@csrf_exempt
def jira_query(request):
    print("Received request:", request)
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Parse JSON input
            query = data.get("query")
            if query:
                print("Query:", query)
                response = interact_with_jira_agent(query)
                return JsonResponse({"response": response})
            return JsonResponse({"error": "Query field is required"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    """"elif request.method == "GET":
        try:
            data = json.loads(request.body)  # Parse JSON input
            query = data.get("query")
            if query:
                response = interact_with_jira_agent(query)
                return JsonResponse({"response": response})
            return JsonResponse({"error": "Query field is required"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)"""
    return JsonResponse({"error": "Only POST method is allowed"}, status=405)


# Create your views here.
