from rest_framework.response import Response
from rest_framework import status

def return_response(status, message, data, status_code):
    return Response(data={
        'status': status,
        'message': message,
        'data': data if data else []
    }, status=status_code)