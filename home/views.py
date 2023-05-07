from django.http import HttpResponse
from django.shortcuts import render,redirect,HttpResponse
from django.template import loader
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login as auth_login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from home.models import Userdetails
from home.models import Productsdetails
from home.models import Productstatus
from home.models import Notice
from django.contrib import messages
from datetime import date
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.dateparse import parse_date 
from django.db import transaction, DatabaseError,IntegrityError
from django.views.generic.edit import FormView

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def registration(request):
  template = loader.get_template('registration.html')
  return HttpResponse(template.render())

def login(request):
  if(request.user.is_authenticated):
     return redirect('index')
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

@csrf_exempt
def saveUser(request):
    if request.method == "POST":
       name = request.POST.get('name')
       mobile = request.POST.get('mobile')
       email = request.POST.get('email')
       password = request.POST.get('password')
       designation = request.POST.get('designation')
       organization = request.POST.get('organization')
       user = User.objects.create_user(username=email, email=email,password=password)
       user.first_name = name
       user.is_active = 0
       user.is_staff = 0
       user.is_superuser = 0
       try:
          user.save()
       except (IntegrityError,DatabaseError) as e:
          return HttpResponse (e)
       id_u = User.objects.get(email=email).pk
       userdetails = Userdetails()
       userdetails.user_id = id_u
       userdetails.phone = mobile
       userdetails.designation = designation
       userdetails.organization = organization
       try:
          userdetails.save()
       except (DatabaseError, IntegrityError) as e:
          return HttpResponse (e)
    return render(request,'login.html',{'m':'Information provided to SHQTC Team, After approval you can login'})

@login_required(login_url='login')
def HomePage(request):
   list = []
   if request.user.is_staff:
      pr_ids = Productstatus.objects.filter(status='NEW')
      for pr in pr_ids:
         pr_details = Productsdetails.objects.filter(id=pr.product_id).values()
         list.append(pr_details)
   else:
      listu = findproductidbyuid(request.user.id)
      for pr in range(len(listu)):
         pr_details = Productsdetails.objects.filter(id=listu[pr]).values()
         list.append(pr_details)
   context = {
         'list': list,
         }
   return render(request,'home.html',context)

@csrf_exempt
def loginuser(request):
   email = request.POST.get('email')
   password = request.POST.get('password')
   user = authenticate(username=email, password=password)
   m = ''
   list = []
   if user is not None:
      auth_login(request,user)
      return redirect('index')
   else:
      return HttpResponse ('username and password not matched')
  # return render(request, "login.html",{'m':m})

def LogoutPage(request):
    logout(request)
    return redirect('login')

@user_passes_test(lambda u: u.is_superuser,login_url='login')
def userUpdate(request):
    if request.method == "POST":
       id = request.POST.get('id')
       staff = request.POST.get('staff_d')
       isactive = request.POST.get('active_d')
       staffornot = 0
       activeornot = 0
       if(staff == 'True'):
          staffornot = 1
       if(isactive == 'True'):
          activeornot = 1
       
       #print(staff)
       user = User.objects.get(id=id)
       user.is_active = activeornot
       user.is_staff = staffornot
       user.save()
    list = []
    users = User.objects.all()
    for user in users:
       if(user.username != 'admin'):
         user_info = User.objects.filter(username=user.username).values()
         list.append(user_info)
    context = {
            'list': list,
            }
    return render (request,'userupdate.html',context)

@user_passes_test(lambda u: u.is_superuser,login_url='login')
def userupdateadmin(request):
    if request.method == "POST":
       id = request.POST.get('id')
       staff = request.GET['staff_d']
       print(staff)
    return HttpResponse('got')

@login_required(login_url='login')
def updatewon(request):
   if request.user.is_authenticated:
         user = request.user
         user_info = User.objects.get(username=user)
         username = user_info.email
         name = user_info.get_full_name
         info = user_info.is_staff
         ids = user_info.pk
         userdetails = Userdetails.objects.filter(user_id=ids).values()
         context = {
            'userdetails': userdetails,
            'username': username,
            'name': name
            }
   return render (request,'updatewon.html', context)

@csrf_exempt
def updateeachuser(request):
   current_user = request.user
   if request.method == "POST":
      name = request.POST.get('name')
      mobile = request.POST.get('mobile')
      email = request.POST.get('email')
      password = request.POST.get('password')
      designation = request.POST.get('designation')
      organization = request.POST.get('organization')
      user = User.objects.get(id=current_user.id)
      user.first_name = name
      user.email = email
      if len(password) > 1 :
        user.set_password(password)
      user.save()
      Userdetails.objects.filter(user_id=current_user.id).update(designation=designation, organization = organization, phone = mobile)
      auth_login(request,user)
      messages.info(request, 'Your Profile has been updated')
   return redirect('index')

@staff_member_required
def addproduct(request):
   return render (request,'addproduct.html')

@csrf_exempt
def saveproduct(request):
   if request.method == "POST":
       name = request.POST.get('product_name')
       organization = request.POST.get('organization')
       vendor = request.POST.get('vendor')
       ptype = request.POST.get('p_type')
       issue_date = request.POST.get('issue_date')
       product = Productsdetails()
       product.product_name = name
       product.organization_name = organization
       product.vendors_name = vendor
       product.p_type = ptype
       product.issue_date = parse_date(issue_date)
       try:
          product.save()
       except DatabaseError as e:
          return render(request, "home.html",{'m':e})
       id = Productsdetails.objects.get(product_name=name).pk
       
       productstatus = Productstatus()
       productstatus.product_id = id
       productstatus.status = 'NEW'
       productstatus.update_user = request.user
       productstatus.update_date =  date.today()
       try:
          productstatus.save()
       except DatabaseError as e:
          return render(request, "home.html",{'m':e})
       return render(request, "home.html",{'m':'Product added to database'})
@staff_member_required  
def productupdate(request,item):
   if request.method == "GET":
      pass
   else:
      return redirect('index')
   pr_details = Productsdetails.objects.filter(id=item)
   pr_status = Productstatus.objects.filter(product_id=item)
   P_name = ''
   status = ''
   users_id = ''
   update_user = ''
   update_date = ''
   for pr in pr_details:
      p_id = pr.pk
      P_name = pr.product_name
      users_id = pr.users_id
   user_list = []
   if(len(users_id)>1):
      user_array = users_id.split('|')
      for i in range(len(user_array)-1):
         user_e = User.objects.filter(id=user_array[i])
         for e in user_e:
            user_list.append(e.username)
   print(user_list)
   
   for pr in pr_status:
      status = pr.status
      update_user = pr.update_user
      update_date = pr.update_date
   users = User.objects.filter(is_active=True,is_staff=False)
   context = {
            'p_id': p_id,
            'p_name': P_name,
            'status': status,
            'update_user': update_user,
            'update_date': update_date,
            'users':users,
            'users_list':user_list,
            }
   return render(request, "productupdate.html",context)

@csrf_exempt
def updateproduct(request):
   user = request.user.username
   if request.method == 'POST':
      id = request.POST.get('id')
      status = request.POST.get('status')
      productstatus = Productstatus.objects.get(product_id=id)
      productstatus.product_id = id
      productstatus.status = status
      productstatus.update_user = user
      productstatus.update_date =  date.today()
      try:
          productstatus.save()
      except DatabaseError as e:
         return HttpResponse('not updated')
      print(status)
      users = request.POST.getlist('users')
      users_id = ''
      pr_details = Productsdetails.objects.get(id=id)
      for user_name in users:
         user_id = User.objects.get(username=user_name).pk
         users_id = users_id+str(user_id)+'|'
      pr_details.users_id = users_id
      try:
          pr_details.save()
      except DatabaseError as e:
         return HttpResponse('not updated')
   return redirect('productupdate',item=id)

def findproductidbyuid(id):
   listu = []
   pr_details = Productsdetails.objects.all() 
   for pr in pr_details:
      users_l = pr.users_id.split('|')
      for i in range(len(users_l)-1):
         if id == int(users_l[i]):
            listu.append(pr.pk)
   return listu
@login_required
def viewproduct(request,item):
   if request.method == "GET":
      if idinproduct(request.user.id,item):
         pass
      else:
         return redirect('index')
   else:
      return redirect('index')
   pr_details = Productsdetails.objects.filter(id=item)
   pr_status = Productstatus.objects.filter(product_id=item)
   P_name = ''
   status = ''
   users_id = ''
   update_user = ''
   update_date = ''
   for pr in pr_details:
      p_id = pr.pk
      P_name = pr.product_name
      users_id = pr.users_id
   user_list = []
   if(len(users_id)>1):
      user_array = users_id.split('|')
      for i in range(len(user_array)-1):
         user_e = User.objects.filter(id=user_array[i])
         for e in user_e:
            user_list.append(e.username)
   print(user_list)
   
   for pr in pr_status:
      status = pr.status
      update_user = pr.update_user
      update_date = pr.update_date
   users = User.objects.filter(is_active=True,is_staff=False)
   context = {
            'p_id': p_id,
            'p_name': P_name,
            'status': status,
            'update_user': update_user,
            'update_date': update_date,
            'users':users,
            'users_list':user_list,
            }
   return render(request, "viewproduct.html",context)

def idinproduct(id,p_id):
   found = False
   pr_details = Productsdetails.objects.filter(id=p_id)
   for pr in pr_details:
      users_l = pr.users_id.split('|')
      for i in range(len(users_l)-1):
         if id == int(users_l[i]):
            found=True
   return found

def about(request):
   return render(request,'about.html')
def price(request):
   return render(request,'price.html')

@user_passes_test(lambda u: u.is_superuser,login_url='login')
def addnotice(request):
   return render(request,'addnotice.html')

@csrf_exempt
def savenotice(request):
   if request.method == 'POST':
      #print(request.FILES)
      handle_uploaded_file(request.FILES['docfile'])  
      notice_name = request.POST.get('notice_name')
      notice = Notice()
      notice.notice_name = notice_name
      notice.file = request.FILES['docfile']
      notice.upload_date = date.today()
      try:
         notice.save()
      except DatabaseError as e:
         return HttpResponse(e)
     
   return render(request,'addnotice.html',{'m':'Notice added to database'})
   
def handle_uploaded_file(f):  
    with open('home/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)

def notice(request):
   notice = Notice.objects.all().order_by('-id')
   for nots in notice:
      print(nots.notice_name)
      print(nots.file.url)
   context={
      'notice':notice
   }
   return render(request,'notice.html',context)

def services(request):
   return render(request,'services.html')