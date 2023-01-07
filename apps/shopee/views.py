from django.shortcuts import render


api_urls = {
    "success": True,
    "data": {
        "list": [
    {
        "id": 5,
        "avatar": {
            "id": 43,
            "imagefile": "https://antapi.pythonanywhere.com/media/upload_pics/2509_SDg7PyR.png"
        },
        "name": "100 Plus",
        "price": "RM4.53",
        "category": "Beverages",
        "cartadded": false,
        "ordered": false,
        "order_id": ""
    },
    {
        "id": 3,
        "avatar": {
            "id": 41,
            "imagefile": "https://antapi.pythonanywhere.com/media/upload_pics/1003_4Htt9rm.png"
        },
        "name": "Double Cheeseburger",
        "price": "RM10.37",
        "category": "Burgers",
        "cartadded": false,
        "ordered": false,
        "order_id": ""
    },
    {
        "id": 2,
        "avatar": {
            "id": 39,
            "imagefile": "https://antapi.pythonanywhere.com/media/upload_pics/2100_03CcJBm.png"
        },
        "name": "Coca-Cola",
        "price": "RM4.53",
        "category": "Beverages",
        "cartadded": false,
        "ordered": false,
        "order_id": ""
    },
    {
        "id": 1,
        "avatar": {
            "id": 40,
            "imagefile": "https://antapi.pythonanywhere.com/media/upload_pics/1028_IwVvaDb.png"
        },
        "name": "McChicken",
        "price": "RM8.49",
        "category": "Burgers",
        "cartadded": false,
        "ordered": false,
        "order_id": ""
    }
]
    },
    "errorCode": 0
}



@api_view(['GET'])
def apiOverview(request):
	
	return Response(api_urls)