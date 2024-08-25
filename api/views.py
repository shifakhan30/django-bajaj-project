from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json





def home(request):
    return HttpResponse("Welcome to the Django REST API!")

# @csrf_exempt
# def bfhl(request):
#     # print('hello')
#     if request.method == 'GET':
#         # Handle GET request
#         return JsonResponse({"operation_code"}, status=200)

#     elif request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             response = process_post_request(data)
#             return JsonResponse(response, status=200)
#         except Exception as e:
#             return JsonResponse({"is_success": False, "error": str(e)}, status=400)
@csrf_exempt
def bfhl(request):
    if request.method == 'GET':
        # Handle GET request
        return JsonResponse({"operation_code": 1}, status=200)

    elif request.method == 'POST':
        try:
            # Load JSON data from the request body
            data = json.loads(request.body)

            # Process the data
            response = process_post_request(data)

            # Return the JSON response
            return JsonResponse(response, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"is_success": False, "error": "Invalid JSON format."}, status=400)
        except Exception as e:
            return JsonResponse({"is_success": False, "error": str(e)}, status=400)

def process_post_request(data):
    # Dummy data for user_id, email, and roll_number
    user_id = "john_doe_17091999"
    email = "john@xyz.com"
    roll_number = "ABCD123"

    numbers = []
    alphabets = []
    highest_lowercase = []

    # Process data
    for item in data.get("data", []):
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
            if item.islower():
                highest_lowercase.append(item)

    # Determine the highest lowercase letter
    highest_lowercase.sort(reverse=True)
    highest_lowercase_alphabet = [highest_lowercase[0]] if highest_lowercase else []

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }

    return response
