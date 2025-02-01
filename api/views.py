from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from . serializers import agentSerializer
from . utils import code_converter,code_explainer

class CodeConverterView(APIView):

    def post(self,request):

        serializer = agentSerializer(data = request.data)

        if serializer.is_valid():
            source_code = serializer.validated_data['source_code']
            source_language = serializer.validated_data['source_language']
            target_language = serializer.validated_data['target_language']

            converted_code = code_converter(source_code,source_language,target_language)

            explaination_code = code_explainer(converted_code,target_language)
            response_data = {
                "converted_code" : converted_code,
                "explaination_code" : explaination_code
            }

            return Response(response_data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

