from django.shortcuts import render, HttpResponse
from .models import Member, Role, Fees_plan
from django.db.models import Q

def index(request):
    return render(request, 'index.html')

def all_memb(request):
    memb = Member.objects.all
    context = {
        'memb': memb
    }
    return render(request, 'all_memb.html',context)

def add_memb(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        entry_id = int(request.POST['entry_id'])
        fees_plan = int(request.POST['fees_plan'])
        new_memb = Member(first_name= first_name, last_name=last_name, role_id=role, phone=phone, entry_id = entry_id, fees_plan_id = fees_plan)
        new_memb.save()
        return HttpResponse("<h1>Member added Successfully</h1>")
        return render(request, 'remove_memb.html')
        
    elif request.method =='GET':
        return render(request, 'add_memb.html')
    
    else:
        return HttpResponse("An Exception Occured! Member Has Not Been Added")

def remove_memb(request, mem_id =0 ):
    if mem_id:
        try:
            member_to_be_removed = Member.objects.get(id=mem_id)
            member_to_be_removed.delete()
            return HttpResponse("Member Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid Member ID")
    memb = Member.objects.all()
    context = {
        'memb': memb
    }
    return render(request, 'remove_memb.html',context)



def filter_memb(request):
    if request.method == 'POST':
        name = request.POST['name']
        entry_id = request.POST['entry_id']
        role = request.POST['role']
        memb = Member.objects.all()
        if name:
            memb = memb.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if entry_id:
            memb = memb.filter(entry_id__icontains = entry_id)
        if role:
            memb = memb.filter(role__name__icontains = role)

        context = {
            'memb': memb
        }
        return render(request, 'all_memb.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_memb.html')



def facilities(request):
    return render(request, 'facilities.html')
   