from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Profile,Order
from .forms import ContactForm, SignUpForm, LoginForm, ProfieForm, ProductSearchForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
import uuid
import hmac
import hashlib
import base64

def home(request):
    all_prods = Product.objects.all()
    product_category = Product.objects.values_list('product_category', flat=True).distinct()
    category_images = {}
    
    for category in product_category:
        product = Product.objects.filter(product_category=category).first()
        if product:
            category_images[category] = product.product_img.url
    
    context = {
        'products': all_prods,
        'category_images': category_images
    }

    return render(request, 'pasal/home.html', context)


def category_items(request, my_category):
    cat_items = Product.objects.filter(product_category=my_category)
    return render(request, 'pasal/categories.html',{'category_items':cat_items,'category':my_category})


def about(request):
    return render(request, 'pasal/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['name'].isalnum() or len(form.cleaned_data['name'])>20:
                messages.warning(request, "Invalid  Credentials")
                return redirect("/contact")
            form.save()
            messages.success(request,"Submitted Successfully")
    else:
        form = ContactForm()
    return render(request, 'pasal/contact.html',{"form":form})

    
def firm(request):
    return render(request, 'pasal/firm.html')

def product(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'pasal/product.html',{'product':product})

def collection(request):
    collections = Product.objects.all()
    return render(request,'pasal/more_items.html',{"collections":collections})

def site_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['user_name']
            email = form.cleaned_data['your_email']
            password1 = form.cleaned_data['your_password']
            password2 = form.cleaned_data['your_password_confirm']
            f_name = form.cleaned_data["first_name"]
            l_name = form.cleaned_data["last_name"]
            if password1 != password2:
                messages.warning(request,"Password didn't match")
                return redirect("/register")
            if len(f_name.split()) > 1:
                messages.warning(request,f"{f_name} cannot be the first name")
                return redirect("/register")
            if len(l_name.split()) > 1:
                messages.warning(request,f"{l_name} cannot be the last name")
                return redirect("/register")
            myuser = User.objects.create_user(username,email,password1)
            myuser.first_name = f_name
            myuser.last_name = l_name
            myuser.save()
            messages.success(request,"Account has been created! You can now Login")
            return redirect("/login")
        else:
            messages.error(request,"Invalid Credentials")
    else:
        form = SignUpForm()
    
    return render(request,"pasal/register.html",{"form":form})

def site_login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Successfully Logged In")
                return redirect("/")
            else:
                messages.warning(request,"Account with this username and password doesnt exist")
                return redirect("/login")
            
        else:
            messages.warning(request, "Invalid Credentials.")
    else:
        form=LoginForm()

    return render(request,"pasal/login.html",{"form":form})

@login_required
def user_account(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)

    except Profile.DoesNotExist:
        profile = Profile(user=user)
        profile.save()
    first_name = user.first_name
    last_name = user.last_name
    if request.method == 'POST':
        form = ProfieForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = ProfieForm(instance = profile)
    return render(request, "pasal/profile.html", {"profile": profile, "form": form, "f_name": first_name, "l_name": last_name, "profile_image": profile.profile_image})


def user_logout(request):
    logout(request)
    messages.success(request,"Youv'e been logged out!")
    return redirect("/")

def remove_pic(request):
    user= request.user
    obj = Profile.objects.get(user=user)
    obj.profile_image = None
    obj.save()

    return redirect("/account")

def search(request):
    products = []
    query = request.GET.get('query')
    user = request.user
    if user.is_authenticated:
        try:
            user_profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            user_profile = Profile(user=user)
            user_profile.save()
        user_profile.searched = query
        user_profile.save()
    products = Product.objects.filter(
    Q(product_name__icontains=query) | Q(product_desc__icontains=query) | Q(product_category__icontains=query) | Q(product_subcategory__icontains=query)
                                          )
    return render(request, 'pasal/search.html',{"products":products,"query":query})



def genSha256(key, message):
    key = key.encode('utf-8')
    message = message.encode('utf-8')

    hmac_sha256 = hmac.new(key, message, hashlib.sha256)
    digest = hmac_sha256.digest()
    signature = base64.b64encode(digest).decode('utf-8')
    return signature

def purchase(request):
    order_items = []  # Define order_items outside the block
    total_price = 0   # Define total_price outside the block
    transaction_uuid = None
    result = None
    user = request.user
    print(f"User: {user}")
    cart_data = request.POST.get('cart_data')
    if cart_data:
        print(f"Cart data: {cart_data}")
        if user.is_authenticated:
            items = json.loads(cart_data)

            for item in items:
                product_id = item['id']
                product_name = item['product_name']
                quantity = item['quantity']
                item_price = item['item_price']
                order_item = Order(
                            user=user,
                            product_name=product_name,
                            product_price=item_price,
                            product_quantity=quantity,
                            product_id=product_id)
                order_item.save()
                print(order_item)
                order_items.append(order_item)
                total_price += item_price*quantity

            secret_key = "8gBm/:&EnhH.1/q"
            transaction_uuid = uuid.uuid4()
            data_to_sign = f"{total_price},{transaction_uuid},EPAYTEST"
            print(data_to_sign)
            result = genSha256(secret_key, data_to_sign)
            print(result)
        else:
            return HttpResponse("404 Error")

    return render(request, "pasal/purchase.html", {"items": order_items, "total": total_price, "uuid": transaction_uuid, "signature": result})










            



