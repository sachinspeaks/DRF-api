from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CompanySerializer
from .models import *
# Create your views here.


@api_view(['GET','POST'])
def home(request):
    return Response({'message':'Hello World'})


@api_view(['GET'])
def productList(request):
    products=Product.objects.all()
    serializer=CompanySerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productDetail(request,pk):

    product=Product.objects.get(id=pk)
    serializer=CompanySerializer(product,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def productCreate(request):
    products=request.data
    serializer=CompanySerializer(data=products)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Created Successfully","data": serializer.data})
    return Response({'message':'Product not created'})

@api_view(['POST'])
def productUpdate(request,pk):
    product=Product.objects.get(id=pk)
    serializer=CompanySerializer(instance=product,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Created Successfully","data": serializer.data})
    return Response({'message':'Product not created'})

@api_view(['DELETE'])
def productDelete(request,pk):
    product=Product.objects.get(id=pk)
    product.delete()
    return Response({'message':'Product Deleted'})