from django.shortcuts import render, HttpResponse , redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import InMemoryUploadedFile
from myApp.models import *
from PIL import Image
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home_page(request):
    posts = Post.objects.order_by('?')
    if request.user.is_authenticated:
        profile_model = Profile.objects.get(user=request.user)
        return render(request, "index.html", {'posts': posts, 'profile_model':profile_model})
    return render(request, "index.html", {'posts': posts})

@csrf_exempt
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pass")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request,"login.html",{'error_message_IL': 'Invalid Credentials'})
    return render(request, "login.html")
@csrf_exempt
def register_page(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pass")
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error_message_username': 'Username already exists'})
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error_message_email': 'Email already exists'})
        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        user_login = authenticate(request, username=username, password=password)
        login(request, user_login)

        user_model = User.objects.get(username=username)
        new_profile = Profile(user=user_model)
        new_profile.save()
        profile_model = Profile.objects.get(user=user_model)
        # messages.success(request, 'Account created successfully!')
        # return redirect("login")
        return render(request,"firstsetting.html",{'profile_model':profile_model})
    return render(request, "register.html")

def logoutuser(request):
    if not request.user.is_authenticated:
        return redirect("login")
    logout(request)
    return redirect("/")  

def hero_page(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "hero.html")

def profile(request, pk):
    user = User.objects.get(username=pk)
    posts = Post.objects.filter(user=user).order_by('-date_created')
    profile_model = Profile.objects.get(user=user)
    return render(request, "profiletest.html", {"posts": posts , "profile_model": profile_model, "pk": pk})

def post(request):
    post_id = request.GET.get("post_id")
    post = Post.objects.get(id=post_id)
    return render(request, "post.html", {"post": post})

def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(tech_stack__icontains=query))
    profiles = Profile.objects.filter(Q(user__username__icontains=query) | Q(location__icontains=query))

    context = {
        'query': query,
        'posts': posts,
        'profiles': profiles
    }
    return HttpResponse("<h2>Search Results</h2><br><a href='/'>Home</a>")

@login_required(login_url='login')
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.user == post.user:
        post.delete()
        messages.success(request, 'Your post has been deleted.')
    else:
        messages.error(request, 'You are not authorized to delete this post.')
    return redirect('dashboard')

@login_required(login_url="login")
def upload(request):
    if request.method == "POST":
        user=request.user
        user_profile=Profile.objects.get(user=user)
        title = request.POST.get("title")
        description = request.POST.get("description")
        date_started = request.POST.get("date_started")
        tech_stack = request.POST.get("tech_stack")
        github_link = request.POST.get("github_link")
        website_link = request.POST.get("website_link")
        image_1 = request.FILES.get("image_1")
        image_2 = request.FILES.get("image_2")
        image_3 = request.FILES.get("image_3")
        post_thumbnail=image_1
        # Resize the images
        if post_thumbnail:
            post_thumbnail_file = BytesIO(post_thumbnail.read())
            post_thumbnail_image = Image.open(post_thumbnail_file)
            post_thumbnail_image.thumbnail((450, 338))
            post_thumbnail_file = BytesIO()
            post_thumbnail_image.save(post_thumbnail_file, post_thumbnail_image.format)
            post_thumbnail_file.seek(0)
            post_thumbnail = InMemoryUploadedFile(post_thumbnail_file, 'ImageField', post_thumbnail.name, post_thumbnail.content_type, None, None)

        new_post=Post(user=user,user_profile=user_profile,title=title,description=description,date_started=date_started,tech_stack=tech_stack,github_link=github_link,website_link=website_link,image_1=image_1,image_2=image_2,image_3=image_3,post_thumbnail=post_thumbnail)
        new_post.save()
        return HttpResponse("<h2>Post Updated</h2><br><a href='/'>Home</a>")
    return render(request, "upload.html")

@login_required(login_url="login")
def dashboard(request):
    posts = Post.objects.filter(user=request.user).order_by('-date_created')
    profile_model = Profile.objects.get(user=request.user)
    return render(request, "dashboardtest.html", {"posts": posts , "profile_model":profile_model})

@csrf_exempt
@login_required(login_url="login")
def settings_page(request):
    profile_model = Profile.objects.get(user=request.user)
    user_model=User.objects.get(username=request.user.username)
    if request.method == "POST":
        profession=request.POST.get("profession")
        mobilenumber=request.POST.get("mobilenumber")
        if profile_model.firstsetting == True:
            fname=request.POST.get("fname")
            lname=request.POST.get("lname")
            email=request.POST.get("email")
            user_model.first_name = fname
            if email:
                user_model.email = email
            user_model.last_name = lname
        bio = request.POST.get("bio")
        linkedin = request.POST.get("linkedin")
        github = request.POST.get("github")
        website = request.POST.get("website")
        twitter = request.POST.get("twitter")
        acadmicyear = request.POST.get("acadmicyear")
        branch = request.POST.get("branch")
        location = request.POST.get("location")
        profileimg = request.FILES.get("profileimg")
        # user_model = User.objects.get(username=request.user.username)
        # profile_model = Profile.objects.get(user=user_model)
        
        
        profile_model.profession = profession
        profile_model.mobilenumber = mobilenumber
        if linkedin:
            profile_model.linkedin = linkedin
        profile_model.bio = bio
        if github:
            profile_model.github = github
        if website:
            profile_model.website = website
        if twitter:
            profile_model.twitter = twitter
        profile_model.acadmicyear = acadmicyear
        profile_model.branch = branch
        profile_model.location = location
        if profileimg:
            print("Testing")
            print(profile_model.profileimg.url) 
            if profile_model.profileimg.url != "/media/profile_images/default-user.png":
                profile_model.profileimg.delete(save=False)
            profile_model.profileimg = profileimg
        if profile_model.firstsetting == False:
            profile_model.firstsetting = True
        profile_model.save()
        user_model.save()
        return HttpResponse("<h2>Settings Updated</h2><br><a href='/settings'>Settigns</a>")
    return render(request, "usersetting.html",{ 'profile_model': profile_model})