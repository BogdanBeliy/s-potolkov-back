from .models import Cards, Testimonials, NewClient
from .serializers import *
from rest_framework import generics, views, response, status
from rest_framework.decorators import api_view
from .telegram_bot import send_message


class TestimonialsView(views.APIView):
    def get(self, request):
        testimonials = Testimonials.objects.all()
        serializer = TestimonialSerializer(testimonials, many=True)
        return response.Response({'testimonials': serializer.data})


class CardView(views.APIView):
    def get(self, request):
        cards = Cards.objects.all()
        serializer = CardSerializer(cards, many=True)
        return response.Response({'cards': serializer.data})


class NewClientView(views.APIView):
    def get(self, request):
        new_clients = NewClient.objects.all()
        serializer = NewClientSerializer(new_clients, many=True)
        return response.Response({'new_clients': serializer.data})

    def post(self, request):
        serializer = NewClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            message = "Заявка с сайта: \n Тема заявки - {} \n Имя {}, \n Телефон: {}, \n Примерная площадь: {} м.кв, \n Точек освещения: {}".format(
                serializer.data["potolok"], serializer.data["name"], serializer.data["phone"], serializer.data["area"], serializer.data["dot_light"]).title()
            send_message(message)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewPotolok(views.APIView):
    def get(self, request):
        new_potolok_sale = NewSalePotolok.objects.all()
        serializer = NewSalePotolokSerializer(new_potolok_sale, many=True)
        return response.Response({'new_potolok': serializer.data})

    def post(self, request, format=None):
        serializer = NewSalePotolokSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            message = "Заявка на потолок: \n Тема заявки - {0} \n Имя {1}, \n Телефон: {2}, \n Тип потолка: {3}".format(
                serializer.data["type_sale"], serializer.data["name"], serializer.data["phone"], serializer.data["potolok"]).title()
            send_message(message)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
