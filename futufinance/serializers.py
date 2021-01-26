# -*- coding: utf-8 -*-
# @Time    : 22/1/2021 7:08 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: serializers.py
# @Software: PyCharm

from rest_framework import serializers
from futufinance.models import Hk

class HkSerializer(serializers.ModelSerializer):
     class Meta:
         model = Hk
         # fields = '__all__'
         fields = ('code', 'data')

