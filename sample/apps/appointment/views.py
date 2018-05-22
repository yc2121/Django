from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *
import os, random, datetime

def index(request):
  return render(request,'appointment/index.html')
def logout(request):
  # clean up the session here
  return render(request,'appointment/index.html')

def register (request):

  print '\n',"*"*10,' def register\n'
  errors = User.objects.basic_validator(request.POST,'register')
  print errors

  if errors:
      for tag, error in errors.iteritems():
          messages.error(request, error, extra_tags=tag)
      return redirect('/')
  else:
    u=User.objects.create(
      name = request.POST['name'],
      email = request.POST['email'],
      password = bcrypt.hashpw( request.POST['password'].encode(), bcrypt.gensalt() ),
      dob = request.POST['dob'],
      )
    u=User.objects.get(email=request.POST['email'])
    context = u
    
  context ={ 'where':'def register'}

  return render(request,'appointment/appointment',context)

def login(request):  
  print '\n',"*"*10,' def login\n'

  if User.objects.filter(email=request.POST['email']).exists():
    request.session['userID'] = User.objects.get(email=request.POST['email']).id
    return redirect ('/show')
  else:
    errors={}; errors['userID']='User has not yet registered'
    return redirect('appointment/')

def show(request):
  thisone=request.session['userID']
  allappointments = User.objects.get(id=thisone).has_appointments.all()
  print '****** allappointments=',allappointments
  context = { 
    'name':User.objects.get(id=request.session['userID']).name,
    'appts':allappointments 
    }
  return render(request, 'appointment/dashboard.html', context)
  
def update_appointment(request):
  print '\n',"*"*10,' def update_appointment\n'

  # Successfully tested it in shell
  # User.objects.get(id=1).has_appointments.create(task='Me and Ms. Jones',
  # status='Missed', thedate='09/30/2018', thetime='09:30')
  u = User.objects.get(email=request.POST['email'])
  u.has_appointments.create(
    task=request.POST['task'],
      status=request.POST['status'],
      thedate=request.POST['appdate'],
      time=request.POST['apptime']
      )
  context = User.objects.get(id=request.POST['email'])
  context ={ 'where':'def register'}
  return render(request,'appointment/body.html',context)

def dashboard(request):
  print '\n',"*"*10,' def dashboard\n'
  Appointment.objects.all()
  return redirect('/appointment_detail.html')

  return redirect('/appointment_detail.html')

def user_review(request):
  print '\n',"*"*10,' def user_review\n'
  return redirect('/user_review.html')

def users(request):
  print '\n',"*"*10,' def users\n'
  
  if 'activities' not in request.session:
    request.session['activities']=[]

  if request.method=='POST':
    # print request.POST
    if request.POST['submit']=='register':
      return redirect('/register')
    else:
      return redirect('/bookreview')

def users_details(request, userid):
  print '\n',"*"*10,' def users_details\n'
  print 'userid=',userid
  context = {
    'user' : User.objects.get(id=userid)
  }
  print '\n CONTEXT \n',context

  return render(request, "bookreview/details.html", context)

# def update(request):
#     errors = Blog.objects.basic_validator(request.POST)
#         if len(errors):
#             for tag, error in errors.iteritems():
#                 messages.error(request, error, extra_tags=tag)
#             return redirect('/blog/edit/'+id)
#         else:
#             blog = Blog.objects.get(id = id)
#             blog.name = request.POST['name']
#             blog.desc = request.POST['desc']
#             blog.save()
#             return redirect('/blogs')

  # for author in Author.objects.all():
  #   context = {
  #     "authors": author,
  #     "books": Author.books.all(),   
  #   }
  # print '\n', context

  # if 'yourgold' not in request.session:
  #   request.session['yourgold']=0
  # if 'activities' not in request.session:
  #   request.session['activities']=[]
  # if request.method=='POST':
  #   # print request.POST
  #   if request.POST['loc']=='farm':
  #     return redirect('/farm')
  #   elif request.POST['loc']=='cove':
  #     return redirect('/cove') 
  #   elif request.POST['loc']=='house':
  #     return redirect('/house') 
  #   else:
  #     return redirect('/casino') 
