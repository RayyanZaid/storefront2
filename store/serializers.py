from rest_framework import serializers
from .models import Product


from decimal import Decimal
# Completely separate from the product class

# Using this, we can go from (Product Object) --> Python Dictionary
class ProductSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')

    # Add a custom serializer

    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

    def calculate_tax(self, product : Product):

                      # decimal           # float
        return round(product.unit_price * Decimal(1.1),2)