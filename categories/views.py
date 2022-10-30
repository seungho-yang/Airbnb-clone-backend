from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer


class categories(APIView):
    def get(self, request):
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            return Response(
                CategorySerializer(new_category).data,
            )
        else:
            return Response(serializer.errors)    


class CategotyDetail(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound
    def get(self, request, pk):
        serializer = CategorySerializer(self.get_object(pk))
        return Response(serializer.data)
    def put(self, request, pk):
        serializer = CategorySerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)
    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)



/

# @api_view(['GET', 'POST'])
# def categories(request):
#     if request.method == 'GET':
#         all_categories = Category.objects.all()
#         serializer = CategorySerializer(all_categories, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         # Category.objects.create(
#         #     name = request.data["name"],
#         #     kind = request.data["kind"]
#         # )
#         serializers = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             new_category = serializers.save()
#             return Response(CategorySerializer(new_category).data)
#         else:
#             return Response(serializers.error)

#         return Response({'created': True})

# @api_view()
# def category(request, pk):
#     category = Category,object.get(pk=pk)
#     serializer = CategorySerializer(Category)
#     return Response(serializer.data)

