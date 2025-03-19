import json
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Product, Category
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class ProductListView(View):
    def get(self, request):
        products = Product.objects.all().values(
            "id", "name", "price", "description", "count", "is_active", "category__name"
        )
        return JsonResponse(list(products), safe=False)

    def post(self, request):
        data = json.loads(request.body)
        category = get_object_or_404(Category, id=data["category_id"])
        product = Product.objects.create(
            name=data["name"],
            price=data["price"],
            description=data["description"],
            count=data["count"],
            is_active=data.get("is_active", True),  # исправлено
            category=category
        )
        return JsonResponse({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "count": product.count,
            "is_active": product.is_active,
            "category": product.category.name
        }, status=201)


class ProductDetailView(View):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        return JsonResponse({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "count": product.count,
            "is_active": product.is_active,
            "category": product.category.name
        })


class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all().values("id", "name")
        return JsonResponse(list(categories), safe=False)

    def post(self, request):
        data = json.loads(request.body)
        category = Category.objects.create(name=data["name"])
        return JsonResponse({"id": category.id, "name": category.name}, status=201)


class CategoryDetailView(View):
    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        return JsonResponse({"id": category.id, "name": category.name})


class CategoryProductsView(View):
    def get(self, request, id):
        products = Product.objects.filter(category_id=id).values(
            "id", "name", "price", "description", "count", "is_active"
        )
        return JsonResponse(list(products), safe=False)
