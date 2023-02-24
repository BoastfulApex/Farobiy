from academy.views import*
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'sliders', SliderView, basename='sliders')
router.register(r'categories', CategoryView, basename='categories')
router.register(r'courses', CourseView, basename='courses')
router.register(r'teachers', TeacherView, basename='teachers')
router.register(r'faqs', FAQView, basename='faqs')