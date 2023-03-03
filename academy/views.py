from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)

        return super(LoginView, self).post(request, format=None)


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    

class SubCategoryView(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def list(self, request, *args, **kwargs):
        category_id = request.GET.get('category_id')
        if category_id:
            datas = SubCategory.objects.values().filter(category__id=category_id).first()
            return Response(datas)            
        else:
            datas = SubCategory.objects.all().values()
            return Response(datas)
    

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    
    def list(self, request, *args, **kwargs):
        category_id = request.GET.get('subcategory_id')
        if category_id:
            datas = Course.objects.values().filter(sub_category__id=category_id).first()
            return Response(datas)            
        else:
            datas = Course.objects.all().values()
            return Response(datas)
    
    def retrieve(self, request, *args, **kwargs):
        course_id = kwargs['pk']
        course = Course.objects.values().filter(id=course_id).first()
        if course:
            descriptions = CourseDescription.objects.values().filter(course__id=course_id).all()
            print(course)
            course["descriptions"]=descriptions
            return Response(course)
        else:
            return Response({"detail": "not found"})
        return super().retrieve(request, *args, **kwargs)

class CourseDescriptionView(viewsets.ModelViewSet):
    queryset = CourseDescription.objects.all()
    serializer_class = CourseDescriptionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    

class SliderView(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    
    def list(self, request, *args, **kwargs):
        sliders = self.queryset   
        data = []
        for slider in sliders:
            file = []
            if slider.image:
                file = {
                    "id": slider.image.id,
                    "file": slider.image.fileUrl
                }
            else:
                file = []
            d = {
                "id": slider.id,
                "name_uz": slider.name_uz,
                "name_en": slider.name_en,
                "name_ru": slider.name_ru,
                "description_uz": slider.description_uz,
                "description_en": slider.description_en,
                "description_ru": slider.description_ru,
                "image": file
            }
            data.append(d)
                 
        return Response(data)
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    

class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    

class FAQView(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    

class FileView(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
