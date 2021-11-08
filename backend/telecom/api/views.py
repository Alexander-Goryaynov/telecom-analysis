import os
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
import json


@csrf_exempt
def upload(request: HttpRequest):
    file_base64 = json.loads(request.body)['dataset_base64']
    _store_file(file_base64)
    return JsonResponse({
        'name': 'Snezhana',
        'age': 30
    })
    

def _store_file(file_base64_string: str):
    current_folder = os.path.dirname(os.path.abspath(__file__))
    destination_file = os.path.join(current_folder, r'storage\dataset.csv')
    if (os.path.exists(destination_file)):
        os.remove(destination_file)
    binary_data = base64.b64decode(file_base64_string)
    with open(destination_file, 'wb+') as destination:
        destination.write(binary_data)
    