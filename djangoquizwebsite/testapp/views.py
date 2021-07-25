from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, 'testapp/home.html')

def pythonquizpage(request):
    if request.method== 'POST':
        questions= QuestionsModel.objects.all()
        marksscored=0
        correctanswer=0
        wronganswer=0
        total=0
        for q in questions:
            total+=1
            if q.answer == request.POST.get(q.question):
                marksscored+=10
                correctanswer+=1
            else:
                wronganswer+=1
        percentage= marksscored/(total*10)*100
        default_values= {"MarksObtained" : percentage}
        obj, created = StudentScores.objects.update_or_create(
        StudentName=request.user , defaults= default_values)

        context={'marksscored': marksscored,
                'correctanswer': correctanswer,
                'wronganswer': wronganswer,
                'total': total,
                'percentage': percentage}
        return render(request,'testapp/result.html',context)
    else:
        questions= QuestionsModel.objects.all()
        context={'questions':questions}
        return render(request,'testapp/pythonquiz.html',context)

def loginuser(request):
    
    if request.user.is_authenticated:
        return redirect('pythonquizpage')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            
            return redirect('/')
    context={}
    return render(request,'testapp/login.html',context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form = createuserform()
        if request.method=='POST':
            form = createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'testapp/register.html',context)


def addQues(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'testapp/addQues.html',context)
    else: 
        return redirect('home') 

def viewScores(request):
    scores= StudentScores.objects.all()
    context={'scores':scores}
    return render(request,'testapp/scores.html',context)

def logoutuser(request):
    logout(request)
    return redirect('/')



