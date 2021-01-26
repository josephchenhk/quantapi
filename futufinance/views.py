import ast
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from futufinance.models import Hk
from futufinance.serializers import HkSerializer


class HkView(generics.GenericAPIView):

    serializer_class = HkSerializer

    @swagger_auto_schema(
        operation_summary='获取财务数据',
        operation_description='获取香港公司财务数据',
        manual_parameters=[
            openapi.Parameter('code', openapi.IN_QUERY,
                              type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, format=None):
        # financials = Hk.objects.all()
        financials = Hk.objects.filter(code=request.query_params.get('code'))
        serializer = HkSerializer(financials, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary='更新财务数据',
        operation_description='更新香港公司财务数据',
    )
    def post(self, request, format=None):
        code = request.data.get('code')
        data = ast.literal_eval(request.data.get('data'))
        # serializer = HkSerializer(data=request.data)

        serializer = HkSerializer(data={"code": code, "data": data})
        records = Hk.objects.filter(code=code)
        if len(records)==0: # 如果数据库里面无记录，进行写入
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif len(records)==1: # 如果数据库里面已经存在记录，进行更新
            records[0].data = data
            try:
                records[0].save()
                return Response(data, status=status.HTTP_201_CREATED)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error": f"Existing record of {code} is {len(records)} (more than 1)"}, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework import generics
# from . import models
# from . import serializers
#
# class HkView(generics.ListAPIView):
#     queryset = models.Hk.objects.all()
#     serializer_class = serializers.HkSerializer

# {
#   "code": "01236",
#   "data": "{\"2021-01-01\": '6321', \"2020-01-01\": '63210'}"
# }