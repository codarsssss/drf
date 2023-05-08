from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Data
from .serializers import DataSerializer


class GetListApiView(APIView):
    def get(self, request):
        lst = Data.objects.all().values()
        serializer = DataSerializer(lst, many=True)
        return Response({'versions': serializer.data})


class GetOneApiView(generics.RetrieveUpdateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"ошибка": "Метод DELETE не определён"})

        try:
            instance = Data.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({"ошибка": "Объект не сущеуствует"})

        return Response({"delete": "удалена версия " + str(pk)})

    # def get(self, request,  *args, **kwargs):
    #     pk = kwargs.get('id', None)
    #     try:
    #         instance = Data.objects.get(pk=pk)
    #     except:
    #         return Response({"ошибка": "Объект не сущеуствует"})
    #
    #
    #     return Response({'version': DataSerializer(instance).data})

    # def patch(self, request, *args, **kwargs):
    #     pk = kwargs.get('id', None)
    #     if not pk:
    #         return Response({"ошибка": "Метод PATCH не определён"})
    #
    #     try:
    #         instance = Data.objects.get(pk=pk)
    #         instance.delete()
    #         instance.save()
    #     except:
    #         return Response({"ошибка": "Объект не сущеуствует"})
    #
    #     serializer = DataSerializer(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({"update": serializer.data})




class PostApiView(APIView):

    def post(self, request):
        if request.data['id'] != '':
            serializer = DataSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({'post': serializer.data})
        return Response({"ошибка": "id не допустимо"})
