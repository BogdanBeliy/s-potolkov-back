from rest_framework import serializers
from .models import *


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ('id', 'name', 'descr', 'imgUrl')


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['img', 'title']


class NewClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewClient
        fields = ['name', 'phone', 'area', 'dot_light', 'potolok']


class NewSalePotolokSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewSalePotolok
        fields = ['type_sale', 'name', 'phone', 'potolok']
