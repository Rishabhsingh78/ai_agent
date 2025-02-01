from rest_framework import serializers

class agentSerializer(serializers.Serializer):
    source_code = serializers.CharField(help_text = "Enter the source Code")
    source_language = serializers.CharField(help_text = "Language of the sourse code")
    target_language = serializers.CharField(help_text = "Langugae to convert the source code")
