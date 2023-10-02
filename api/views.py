from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.settings import *
from app.models import *
from .permissions import *
from .serializers import *

@api_view(['GET', 'POST'])
@permission_classes([StudyCenterPermission])
def studycenter(request):
    if request.method == "GET":
        studycenter = StudyCenter.objects.all()
        serializer = StudyCenterSerializers(studycenter, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudyCenterSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = HTTP_201_CREATED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
@permission_classes([StudyCenterDetailPermissions])
def studycenter_detail(request, pk):
    studycenter = StudyCenter.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = StudyCenterSerializers(studycenter)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = StudyCenterSerializers(studycenter,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        studycenter.delete()
        return Response(status=HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([TeacherPermissions])
def teacher(request):
    if request.method == "GET":
        teacher = Teacher.objects.all()
        serializer = TeacherSerializers(teacher, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TeacherSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = HTTP_201_CREATED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
@permission_classes([TeacherDetailPermissions])
def teacher_detail(request, pk):
    teacher = Teacher.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = TeacherSerializers(teacher)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = TeacherSerializers(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        teacher.delete()
        return Response(status=HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([StudentPermissions])
def student(request):
    if request.method == "GET":
        student = Student.objects.all()
        serializer = StudentSerializers(student, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = HTTP_201_CREATED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
@permission_classes([StudentDetailPermissions])
def student_detail(request, pk):
    student = Student.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = StudentSerializers(student)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = StudentSerializers(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=HTTP_204_NO_CONTENT)

