from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
import requests


class CustomJsonResponse(JsonResponse):
    def __init__(self, data, encoder=DjangoJSONEncoder, safe=True,
                 json_dumps_params=None, **kwargs):
        super().__init__(data, encoder, safe, json_dumps_params, **kwargs)

    @property
    def content(self):
        return super().content.decode('utf-8')

    def __str__(self):
        return self.content


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def add_poll(request):
    # Handle your poll addition logic here.
    pass


def get_data(request):
    if request.method == 'GET':
        data = request.GET.get('data')
        return CustomJsonResponse(data)
    else:
        return HttpResponse("Hello, world. You're at the polls index.")


# Note: You'll need to set up the routes in urls.py for the methods you mentioned (GET, POST, PUT, DELETE).

url = "https://services.nvd.nist.gov/rest/json/cves/2.0?cvssV3Severity=HIGH"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Extract the CVE items
    cve_items = data.get("result", {}).get("CVE_Items", [])

    # Loop through each CVE and display some information
    for item in cve_items:
        cve_data = item.get("cve", {})
        cve_meta = cve_data.get("CVE_data_meta", {})
        description_data = cve_data.get("description", {}).get("description_data", [{}])

        print(f"CVE ID: {cve_meta.get('ID')}")
        print(f"Description: {description_data[0].get('value')}")
        print("-" * 50)  # Print a separator

else:
    print("Failed to fetch data. Status code:", response.status_code)
