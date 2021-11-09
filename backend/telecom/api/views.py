import os
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
import json
from api.services.statistics_service import StatisticsService


@csrf_exempt
def upload(request: HttpRequest):
    file_base64 = json.loads(request.body)['dataset_base64']
    file_path = _store_file(file_base64)
    statistics_service = StatisticsService(file_path)
    return JsonResponse({
        "market_cap": statistics_service.get_market_cap_info(),
        "stock_price": statistics_service.get_stock_price_info(),
        "daily_loss_gain": statistics_service.get_loss_gain_info()
    })
    

def _store_file(file_base64_string: str) -> str:
    current_folder = os.path.dirname(os.path.abspath(__file__))
    destination_file = os.path.join(current_folder, r'storage\dataset.csv')
    if (os.path.exists(destination_file)):
        os.remove(destination_file)
    binary_data = base64.b64decode(file_base64_string)
    with open(destination_file, 'wb+') as destination:
        destination.write(binary_data)
    return destination_file
    