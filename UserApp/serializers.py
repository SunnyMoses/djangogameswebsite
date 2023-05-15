from rest_framework import serializers
from UserApp.models import AppUser
import json


class UserAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'

    def save(self, *args, **kwargs):
        data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
        }
        with open('user_data.json', 'a', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=2)
        return

