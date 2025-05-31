import datetime
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = '__all__'
        
    def get_days_since_created(self, obj):
        now = datetime.now(datetime.timezone.utc)
        delta = now - obj.created_at
        return delta