from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Course
from .serializers import CourseSerializer


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/course-list/',
		'Detail View':'/course-detail/<str:pk>/',
		'Create':'/course-create/',
		'Update':'/course-update/<str:pk>/',
		'Delete':'/course-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
@permission_classes([AllowAny])
def courseList(request):
	courses = Course.objects.all().order_by('-id')
	serializer = CourseSerializer(courses, many=True)
	return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def courseDetail(request, pk):
	courses = Course.objects.get(id=pk)
	serializer = CourseSerializer(courses, many=False)
	return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def courseCreate(request):
  data = request.data.copy()
  data['instructor'] = request.user.id
  serializer = CourseSerializer(data=data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  else:
    return Response({'error': 'Invalid data', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def courseUpdate(request, pk):
    course = get_object_or_404(Course, id=pk)
    # 檢查 instructor 是否等於 request.user
    if course.instructor != request.user:
        return Response({'error': 'You do not have permission to update this course.'}, status=403)
    data = request.data.copy()
    data['instructor'] = request.user.id
    serializer = CourseSerializer(instance=course, data=data)

    if serializer.is_valid():
        serializer.save()
    else:
      return Response({'error': 'Invalid data', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def courseDelete(request, pk):
    course = get_object_or_404(Course, id=pk)
    # 檢查 instructor 是否等於 request.user
    if course.instructor != request.user:
      return Response({'error': 'You do not have permission to delete this course.'}, status=403)

    course.delete()

    return Response('Item succsesfully delete!')