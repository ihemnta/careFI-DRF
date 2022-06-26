from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import response, status
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


from django.http import HttpResponse
import requests
from datetime import datetime
from pytz import timezone

from bitcoin_api.models import Bitcoin
from bitcoin_api.serializers import BitcoinSerializer



class ping(APIView):
    def get(self, request):
        return HttpResponse("Pong using get!")
    def post(self, request):
        return HttpResponse("Pong using post!")


class BitcoinListAPIView(ListAPIView):
    queryset = Bitcoin.objects.all().order_by('-created_at')
    serializer_class = BitcoinSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ("timestamp",)
    ordering_fields = ("price",)



@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def fetchPrice(request):
    try:
        base_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        result = requests.get(base_url)
        time_stamp = result.headers['Date']
        date_format = "%a, %d %b %Y %H:%M:%S %Z"
        time_stamp_utc = datetime.strptime(time_stamp, date_format)
        time_stamp_asia = time_stamp_utc.astimezone(timezone('Asia/Kolkata'))
        timestamp = time_stamp_asia.strftime("%Y-%m-%d %H:%M:%S")

        data = result.json()
        coin_name = data['symbol']
        current_price = data['price']
        description = "Sucess"

        try:
            bitcoin_obj = Bitcoin()
            bitcoin_obj.timestamp = timestamp
            bitcoin_obj.price = current_price
            if description:
                bitcoin_obj.description = description
            bitcoin_obj.save()
        except exception as e:
            print("e: ",e)
            return response.Response({"message":"Unable to save data in database"},status=502)

        final_response = {
            "name":coin_name,
            "price":current_price,
            "timestamp":timestamp
        }
        return response.Response(final_response,status=status.HTTP_200_OK)
    except:
        return response.Response({"message":"Unable to fetch data form Binance API"},status=424)
