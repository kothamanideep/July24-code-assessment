from rest_framework import serializers
from Donar.models import Donar

class donarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donar
        fields=('id','bloodgroup','donarname','address','mobilenumber','username','password')