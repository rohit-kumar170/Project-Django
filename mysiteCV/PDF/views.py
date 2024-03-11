from django.shortcuts import render
from .models import Profile
from django.template import loader
from django.http import HttpResponse
import pdfkit
# Create your views here.
def accept(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        summary = request.POST.get('summary','')
        degree = request.POST.get('degree','')
        school = request.POST.get('school','')
        university = request.POST.get('university','')
        previous_work = request.POST.get('previous_work','')
        skills = request.POST.get('skills','')

        profile=Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,previous_work=previous_work,skills=skills)
        profile.save()

    return render(request,'PDF/accept.html')
def resume(request,id):
    user_profile=Profile.objects.get(pk=id)
    template=loader.get_template('PDF/resume.html')
    html=template.render({'user_profile':user_profile})
    options = {
    'page-size': 'Letter',   # Standard page size (8.5in x 11in)
    'encoding': 'UTF-8',    # UTF-8 encoding
    }
    pdf=pdfkit.from_string(html,False,options)
    response=HttpResponse(pdf,content_type="application/pdf")
    response['Content-Disposition']="attachment;filename=resume.pdf"
    
    return response
def list(request):
    profiles=Profile.objects.all()
    return render(request,'PDF/list.html',{'profiles':profiles})
