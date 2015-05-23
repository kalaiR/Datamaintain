from django.shortcuts import render_to_response
from django.template import RequestContext
from datamaintain.models import *
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy
from django.utils.encoding import smart_unicode, force_unicode
from django.utils import simplejson
import json as simplejson
from django.utils import formats
from django.contrib.auth import logout
from django.contrib.auth.models import User
# from rest_framework import viewsets
# from datamaintain.serializers import UserSerializer, AbsentListSerializer

# from django_cron import CronJobBase, Schedule

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class AbsentListViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = AbsentList.objects.all()
#     serializer_class = AbsentListSerializer

class JSONResponse(HttpResponse):
    def __init__(self, data):
        super(JSONResponse, self).__init__(
                simplejson.dumps(data), mimetype='application/json')
def get_absent_list(request):
    print "get_absent_list"
    if request.is_ajax() and request.GET and 'date' in request.GET:
        print request.GET['date'] 
#         print "format date"
#         date= request.GET['date'] 
# #         format_date = date.strftime('%Y-%m-%d')
#         format_date = formats.date_format(date,'%Y-%m-%d')
#         
#         print format_date
        
        objs1 = AbsentList.objects.filter(date=request.GET['date'])
        print objs1
        # print objs1.absent_name.split(",")
#         for obj in objs1:
#             print objs1.absent_name
        
        return JSONResponse([{'id': o1.id, 'name': o1.absent_name}
            for o1 in objs1])
    else:
        return JSONResponse({'error': 'Not Ajax or no GET'})
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

def home(request):
    return render_to_response('datamaintain/index.html',{}, context_instance=RequestContext(request))
   
def student_admission(request):    
    
   
    
    
    return render_to_response('datamaintain/student_admission.html', {}, context_instance=RequestContext(request))
def create_attendance(request):
     print "create_attendance"
     admission = Student_Admission.objects.all()
     
#      print student_admission.id
#      regno=student_admission.reg_no
     for regno in admission:
        print "regno", reg_no
     
     department=Department.objects.all()
     degree=Degree.objects.all()
     year=Year.objects.all()
     now = datetime.datetime.now()
     print now
 
     
     return render_to_response('datamaintain/create_attendance.html', {'admission':admission,'department':department,'degree':degree
                                                                       ,'year':year,'now':now}, context_instance=RequestContext(request))


def student_admission_det(request):
    success=False
    student_admission = Student_Admission()
    print "admission"
    student_admission.reg_no=request.POST.get('reg_no','')
    student_admission.name=request.POST.get('name','')
    student_admission.dob=request.POST.get('dob', '')
#     admission.father_name=request.POST.get('father_name','')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    student_admission.qualification=request.POST.get('qualification','')
#     admission.address=request.POST.get('address','')
    student_admission.telephone_no=request.POST.get('telephone_no','')
    student_admission.e_mail=request.POST.get('e_mail','')
    student_admission.department=request.POST.get('department','')
    student_admission.specialization=request.POST.get('specialization', '')
    student_admission.year=request.POST.get('year', '') 
    
       
    student_admission.save()
    success=True 
    return render_to_response('datamaintain/student_admission.html', {'success': success}, context_instance=RequestContext(request))
    
def create_excel(request):   
    print "create excel"
    print "enter else"
    
    selected_values = request.POST.getlist('checkbox')
    print "selected_values",selected_values    
    regno=request.POST.getlist('regno')
    name=request.POST.getlist('name')
    print regno
    print name
    absent_list=Create_Attendance_List()
    # regno_group=''
    # for obj in regno:
    #     regno_group= regno_group + ',' + obj
    # absent_list.absent_regno=regno_group
    # print absent_list.absent_regno
    
    absent_list.date= request.POST.get('date')
    print absent_list.date
    absent_list.department= Department.objects.get(id=request.POST.get('department'))
    absent_list.year= Year.objects.get(id=request.POST.get('year'))

    staff=Staff_Details.objects.filter(department=request.POST.get('department')).filter(year=request.POST.get('year')) 
    for staffs in staff:
        absent_list.staff=Staff_Details.objects.get(id=staffs.id)

    if request.POST.get('admin_checkbox') == None:
        absent_list.admin_status=0
    else:
        absent_list.admin_status=1
     
    absent_list.save()   
    
    for selected_value in selected_values:
        student=Student_Admission.objects.get(id=selected_value)
        print "student", student
        absent_list.student.add(student)

    

    date_for_staff=Create_Attendance_List.objects.filter(department=request.POST.get('department')).filter(year=request.POST.get('year'))
    print date_for_staff

    return HttpResponseRedirect('/admin/card/create_attendance/')  


#     if regnno and name:
#         book = xlwt.Workbook(encoding='utf8')
#         sheet = book.add_sheet('report')
#         sheet.col.width = int(13*380)
#             
#     for obj in regno:
#         sheet.write(1, column, obj, body_style)
#     for obj in name:
#         sheet.write(1, column, obj, body_style)
#     response = HttpResponse(mimetype='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename=report.xls'
#     response = render_to_response("facturas.html",context_instance=RequestContext(request), mimetype='application/vnd.ms-excel')
#     book.save(response)
#     return response
      
    # return render_to_response('card/create_attendance.html', context_instance=RequestContext(request))

def view_attendance(request):
    absentlist=AbsentList.objects.all()
    return render_to_response('datamaintain/view_attendance_list.html', {'absentlist':absentlist}, context_instance=RequestContext(request))

    
    



