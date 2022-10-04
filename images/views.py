from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from .serilaizer import ImageSerializer


class Image (APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        serilaizer = ImageSerializer(data={**request.data, "image": file})
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data)
        return Response(serilaizer.errors)
