import os
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
import json
from api.services.statistics_service import StatisticsService


@csrf_exempt
def upload(request: HttpRequest):
    file_base64 = json.loads(request.body)['datasetBase64']
    file_base64 = file_base64.split(',')[1]
    file_path = _store_file(file_base64)
    statistics_service = StatisticsService(file_path)
    return JsonResponse({
        "marketCap": statistics_service.get_market_cap_info(),
        "stockPrice": statistics_service.get_stock_price_info(),
        "dailyLossGain": statistics_service.get_loss_gain_info(),
        "totalCapByCountry": statistics_service.get_companies_total_cap_by_country(),
        "companiesCountByCountry": statistics_service.get_companies_count_by_country(),
        "clusterizationResult": statistics_service.get_companies_clusters()
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
    