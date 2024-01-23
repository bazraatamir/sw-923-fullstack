from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterSerializer,CategorySerializer,ProductSerializer,ImageSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from rest_framework.views import APIView
from .models import CostumUser,Category,Product,ProductImages
from rest_framework.exceptions import AuthenticationFailed
import datetime,jwt
from rest_framework.response import Response
from django.contrib.auth.models import User
from  rest_framework.renderers import TemplateHTMLRenderer

 
# Create your views here.
class CategoryView(generics.ListCreateAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
        
class ProductView(generics.ListCreateAPIView):
        queryset = Product.objects.all()
        serializer_class =ProductSerializer
        renderer_classes = [TemplateHTMLRenderer]
        template_class = 'index.html'
        def get(self,request):
             response = super().get(request)
             return response.render()
        
class ProductImagesView(generics.ListCreateAPIView):
    queryset = ProductImages.objects.all()
    serializer_class = ImageSerializer
   
class UserRegister(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    

class LoginView(APIView):
 
    
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        print(email)

        user = User.objects.filter(email = email).first()
        
        if user is None:
            raise AuthenticationFailed('хэрглэгчийн майл буруу байна')
        
        if not user.check_password(password):
            raise AuthenticationFailed('нууц үг буруу байна')


        payload = {
            'id':user.id,
            'exp':datetime.datetime.utcnow()+ datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
            }
        token = jwt.encode(payload, 'secret',algorithm='HS256' )
        response = Response()
        response.set_cookie('jwtoken',token)
        response.data={
            "token":token
        }
        return response