import time
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from .serilaizer import ImageSerializer
from .models import Image as ImageModel


class Image (APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        serilaizer = ImageSerializer(data={**request.data, "image": file})
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data)
        return Response(serilaizer.errors)

    def get(self, request, *args, **kwargs):
        serilaizer = ImageSerializer(ImageModel.objects, many=True)
        time.sleep(10)
        return Response(serilaizer.data)
