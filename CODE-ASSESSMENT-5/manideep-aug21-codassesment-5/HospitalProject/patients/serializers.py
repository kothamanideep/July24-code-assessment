from rest_framework import serializers
from patients.models import Patient

class patientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=('patientcode','name','address','disease','admitstatus')