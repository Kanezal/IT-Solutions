from rest_framework.response import Response
from rest_framework.views import APIView
from service.models import KeyModel
from .models import Advertisement
from .serializers import AdvertisementSerializer

class AdvertisementViewAPI(APIView):
    """
    API endpoint that allows to get an Advertisement by external_id.

    Чтобы получить один из рекламных объявлений, необходимо передать в GET-запросе параметр id рекламного объявления.

    Пример запроса:
    GET /api/advertisement/?id=103794726
    """
    def get(self, request):
        external_id = request.GET.get('id')
        api_key = request.GET.get('api_key')

        if request.user.is_authenticated:
            if not (key:=KeyModel.objects.filter(user=request.user).first()):
                return Response({"error": f"User does not have an api_key"}, status=400)
            api_key = key.api_key
        
        if not KeyModel.objects.filter(api_key=api_key).exists():
            return Response({"error": f"Invalid api_key"}, status=400)

        if not external_id:
            return Response({"error": f"ID of an Advertisement is required"}, status=400)
        
        if not (advertisements:=Advertisement.objects.filter(external_id=external_id)).exists():
            return Response({"error": f"Advertisement not found"}, status=400)
        
        advertisement = advertisements.first()

        serializer = AdvertisementSerializer(advertisement)
        return Response(serializer.data)