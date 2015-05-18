from celery.task.schedules import crontab
from celery.decorators import periodic_task
from datamaintain.models import *

# this will run every minute, see http://celeryproject.org/docs/reference/celery.task.schedules.html#celery.task.schedules.crontab
@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
def test():
    print "firing test task"
    create_attendance_list=Create_Attendance_List.objects.all()
    for create_attendance_lists in create_attendance_list:
    	if create_attendance_lists.staff_status == 1 and create_attendance_lists.admin_status == 1:
    		print "status activate for date", create_attendance_lists.date
    	else:
    		print "status inactivate for date", create_attendance_lists.date