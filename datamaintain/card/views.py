import os


from django.conf import settings

from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
# from core.config import COUNTRIES
from datamaintain.models import *
import datetime


def create_attendance(request):


    admission= Student_Admission.objects.all()
    print admission
    department=Department.objects.all()
    degree=Degree.objects.all()
    year=Year.objects.all()
    now = datetime.datetime.now()

    if request.user.is_superuser:
        if 'date' in request.REQUEST:
            date=Create_Attendance_List.objects.get(date=request.REQUEST['date'])
            student_list=date.student.filter(create_attendance_list=date.id)

            ctx={'admission':admission,'department':department,'degree':degree,'year':year,'now':now,'student_list':student_list}
        else:
            ctx={'admission':admission,'department':department,'degree':degree,'year':year,'now':now}
    else:
        if 'date' in request.REQUEST:
            print "enter if"

            staff=request.user
            print "staff", staff.id

            staffid=Staff_Details.objects.get(username=staff.id)
            print "staffid", staffid.id

            print "date", request.REQUEST['date']
            date=Create_Attendance_List.objects.get(date=request.REQUEST['date'], staff=staffid.id)
            print 'date id',date.id
            # student_list=date.student.filter(id=date.id)
            student_list=date.student.filter(create_attendance_list=date.id)
            # print "student_list", student_list

            # for student_lists in student_list:
            #     print student_lists.reg_no
            #     print student_lists.name
            ctx={'admission':admission,'department':department,'degree':degree,'year':year,'now':now,'student_list':student_list}
        else:
            print "enter else"
            ctx={'admission':admission,'department':department,'degree':degree,'year':year,'now':now}
    
    return render_to_response('card/create_attendance.html', ctx ,
        context_instance=RequestContext(request))

def staff_create_attendance(request):
    from datetime import date
    if request.user.is_superuser:
        dateid=Create_Attendance_List.objects.filter(date=request.REQUEST['date'])
        print "dateid", dateid  
        selected_values = request.POST.getlist('checkbox')
        print "selected_values",selected_values  

        absent_list=Create_Attendance_List()
        for selected_value in selected_values:
            for dateids in dateid:   
                studentid=Student_Admission.objects.get(id=selected_value)  
                dateids.student.remove(studentid.id)
    else:
        staff=request.user
        print "staff", staff.id

        staffid=Staff_Details.objects.get(username=staff.id)
        print "staffid", staffid.id

        # staffid_absentlist=Create_Attendance_List.objects.get(staff=staffid.id)
        # print staffid_absentlist.staff_id

        dateid=Create_Attendance_List.objects.filter(date=request.REQUEST['date']).filter(staff=staffid.id)
        print "dateid", dateid  
        selected_values = request.POST.getlist('checkbox')
        print "selected_values",selected_values  

        absent_list=Create_Attendance_List()
        for selected_value in selected_values:
            for dateids in dateid:   
                studentid=Student_Admission.objects.get(id=selected_value)  
                dateids.student.remove(studentid.id)
        
    date_for_status=Create_Attendance_List.objects.get(date=request.REQUEST['date'])
    print "date_for_status", date_for_status

    if request.user.is_superuser:
        if request.POST.get('admin_checkbox') == None:
            date_for_status.admin_status=0
            print "date_for_status.admin_status",date_for_status.admin_status
        else:
            date_for_status.admin_status=1
            print "date_for_status.admin_status", date_for_status.admin_status
    else:
        if request.POST.get('staff_checkbox') == None:
            date_for_status.staff_status=0
            print "date_for_status.staff_status",date_for_status.staff_status
        else:
            date_for_status.staff_status=1
            print "date_for_status.staff_status", date_for_status.staff_status
    date_for_status.save()


    
    # for selected_value in selected_values:
    #     for dateids in dateid:     
    #         Create_Attendance_List.objects.get(student__id=selected_value).delete()

    # for selected_value in selected_values:
    #     for dateids in dateid:            
    #         student=Student_Admission.objects.get(id=selected_value)
    #         print "student", student.id
    #         dateid_absentlist=dateids.student.filter(create_attendance_list=dateids.id).filter(id=student.id)
    #         print "dateid_absentlist", dateid_absentlist
    #         absent_list.student.remove(dateid_absentlist)


    # date=Create_Attendance_List.objects.get(date=request.REQUEST['date'])
    # print 'date id',date.id
    # # student_list=date.student.filter(id=date.id)
    # student_list=date.student.filter(create_attendance_list=date.id)
    

    # date_for_staff=Create_Attendance_List.objects.filter(department=request.POST.get('department')).filter(year=request.POST.get('year'))
    # print date_for_staff

    # return HttpResponseRedirect('/admin/card/create_attendance/') 

    return HttpResponseRedirect('/admin/')


def view_attendance(request):
    print "request.user", request.user.id
    if request.user.is_superuser:
        date_for_admin=Create_Attendance_List.objects.all()
        ctx={'date_for_admin':date_for_admin}
    else:
        staff=Staff_Details.objects.get(username=request.user.id)
        date_for_staff=Create_Attendance_List.objects.filter(staff=staff.id)
        print date_for_staff
        ctx={'date_for_staff':date_for_staff,'staff':staff}
        

    return render_to_response('card/view_attendance_list.html',ctx,
        context_instance=RequestContext(request))


