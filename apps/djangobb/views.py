from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# Create your views here.
def fake_data_01(request):
	api_urls = {
    "salesData": [
        {
            "x": "Jan",
            "y": 1
        },
    ],
}

	return JsonResponse(api_urls, safe=False)