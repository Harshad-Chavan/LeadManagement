from django.shortcuts import render
from .models import Lead,Followup


# Create your views here.
def Index(request):
    objects = Lead.objects.values()
    print(objects)
    return render(request,"Info/Index.html",{'objects':objects})

def Result(request):
    if request.method == "POST":
        id = request.POST.get("id")
        print(id)
        leadobj = Lead.objects.get(ContactPersonName = id)
        Leadname = leadobj.ContactPersonName
        followupobj = Followup.objects.filter(Lead_id = leadobj.id)
        followups = [ (val["Response"],val["DateOfFollowup"]) for val in followupobj.values()]
        return render(request,"Info/result.html",{'Leadname':Leadname, "Followups":followups})
    else:
        return render(request,"Info/Index.html",{'objects':objects})