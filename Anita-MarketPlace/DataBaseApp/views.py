from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Category, Brand, Product, Order, OrderItem


@login_required(login_url='signIn')
def index(request):
    popular_products = Product.objects.filter(status='POPULAR')
    category = Category.objects.filter(parent_category__isnull=False)
    ctx = {
        'popular_products': popular_products,
        'category': category
    }
    return render(request, 'DataBaseApp/index.html', ctx)


def new_product(request):
    products = Product.objects.filter(status='NEW')
    category = Category.objects.filter(parent_category__isnull=False)
    ctx = {
        'products': products,
        'category': category
    }
    return render(request, 'DataBaseApp/new.html', ctx)


def discount_product(request):
    products = Product.objects.filter(status='DISCOUNT')
    category = Category.objects.filter(parent_category__isnull=False)
    print(category)
    ctx = {
        'products': products,
        'category': category
    }
    return render(request, 'DataBaseApp/discount.html', ctx)


def category_page(request, cat_id):
    category = Category.objects.get(id=cat_id)
    products = category.products.all()
    ctx = {
        'products': products,
        'category': category
    }
    return render(request, 'DataBaseApp/category.html', ctx)


def add_product_to_session(request, product_id):
    product = Product.objects.get(id=product_id)
    last_product = request.session.get('product', [])
    reformat_product = {
        'id': product.id,
        'name': product.name,
        'price': str(product.price),
        'image': product.image.url}
    last_product.append(reformat_product)
    request.session['product'] = last_product
    print(request.session.get('product'))
    return redirect('category-page', cat_id=product.category.id)


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    products = request.session.get('product', [])
    products = list(filter(lambda x: x['id'] != product.id, products))
    request.session['product'] = products
    return redirect('basket-page')


def order_page(request):
    del request.session['product']
    return render(request, 'DataBaseApp/order_page.html')


def basket_page(request):
    products = request.session.get('product', [])
    ctx = {
        'products': products
    }
    return render(request, 'DataBaseApp/basket.html', ctx)


@login_required(login_url='signIn')
def admin_page(request):
    return render(request, 'DataBaseApp/admin.html')