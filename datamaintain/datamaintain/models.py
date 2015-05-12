from django.db import models
from django.template.defaultfilters import date
from django.contrib.auth.models import User
from datetime import date


from django.forms import ModelForm


class Degree(models.Model): 
    degree = models.CharField(max_length=5,null=True) 
     
    def __unicode__(self):
        return self.degree

class Specialization(models.Model):
    specialization=models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.specialization

class Department(models.Model):
    degree = models.ForeignKey(Degree) 
    department = models.CharField(max_length=50,null=True)
    specialization = models.ForeignKey(Specialization)
    
    def __unicode__(self):
        return self.department

class Year(models.Model):
    year = models.CharField(max_length=5,null=True) 
     
    def __unicode__(self):
        return self.year

class Student_Admission(models.Model):    
    reg_no = models.CharField(max_length=20,null=True, unique =True)
    name = models.CharField(max_length=50,null=True)
#     father_name = models.CharField(max_length=50,null=True)
    dob=models.CharField(max_length=50,null=True)
    qualification = models.CharField(max_length=50,null=True)
#     address = models.CharField(max_length=50,null=True)
    telephone_no = models.CharField(max_length=20,null=True)
    e_mail = models.CharField(max_length=30,null=True)
    department = models.ForeignKey(Department)
    specialization = models.ForeignKey(Specialization)
    year = models.ForeignKey(Year)
    
    
    def __unicode__(self):
        return self.name

class Staff_Details(models.Model):
     # username = models.CharField(max_length=50,null=True) 
     username = models.ForeignKey(User)
     department = models.ForeignKey(Department)
     specialization = models.ForeignKey(Specialization)
     year = models.ForeignKey(Year)  
        
class Create_Attendance_List(models.Model):    
    date = models.DateField()
    department=models.ForeignKey(Department)
    year = models.ForeignKey(Year)
    staff=models.ForeignKey(Staff_Details)
    staff_status=models.BooleanField(default=False)
    admin_status=models.BooleanField(default=False)
    student=models.ManyToManyField(Student_Admission, null=True,blank=True)
    
    # def __unicode__(self):
    #     return self.datetime.strftime(date,"%Y/%m/%d")

    # def __unicode__(self):
    #     return self.date.strftime("%Y-%m-%d")
    
    def __unicode__(self):
        return str(self.id)
    
class AbsentList_Details(models.Model):   
    absent_regno=models.CharField(max_length=200)
    absent_name=models.CharField(max_length=200)

class AbsentList(models.Model):
    date=models.DateField()
    absent = models.OneToOneField(AbsentList_Details)
    staff=models.ForeignKey(User)  
    @property
    def lifespan(self):
        return '%s - present' % date(self.date, "d/m/y")

class Parent_Details(models.Model):  
       fathername = models.CharField(max_length=50,null=True)
       mothername = models.CharField(max_length=50,null=True)
       Address = models.CharField(max_length=50,null=True)
       email = models.CharField(max_length=50,null=True)
       phone_no = models.CharField(max_length=50,null=True)
       student_id = models.ForeignKey(Year)  
       
       def __unicode__(self):
        return self.fathername



    
        
        

        

      
