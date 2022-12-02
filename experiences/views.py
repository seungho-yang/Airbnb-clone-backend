from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.experiences import NotFound
from rest_framework.response import Response
from .models import Perk
from .serializers import PerkSerializer
    
# Create your views here.

class Perks(APIView):
    def get(self, request):
        all_perks = Perk.objects.all()
        serializers = PerkSerializer(all_perks, many=True)
        return Response(serializers.data)
    
    def post(self, request):
        serializers = PerkSerializer(data=request.data)
        if serializers.is_valid():
            perk = serializers.save()
            return Response(PerkSerializer(perk).data)
        else:
            return Response(serializers.errors)
    
    
class PerkDetails(APIView):
    def get_object(self, pk):
        try:
            return Perk.objects.get(pk=pk)
        except Perk.DoesNotExist:
            raise NotFound
        
    def get(self, request, pk):
        perk = self.get_object(pk=pk)
        serializers = PerkSerializer(perk)
        return Response(serializers.data)
    
    def put(self, request, pk):
        perk = self.get_object(pk)
        serializers = PerkSerializer(perk, data=request.data, partial=True)
        if serializers.is_valid():
            updated_perk = serializers.save()
            return Response(
                PerkSerializer(updated_perk).data,
            )
        else:
            return Response(serializers.errors)
    
    def delete(self, request, pk):
        park = self.get_object(pk)
        perk.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
