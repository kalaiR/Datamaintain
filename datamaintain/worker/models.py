from django.db import models

WorkerTaskStatus = (
  ('init', 'Initialized'),
  ('wait_for_approval', 'Wait for Approval'),
  ('scheduled', 'Scheduled'),
  ('started', 'Started'),
  ('failed', 'Failed'),
  ('completed', 'Completed'),
  ('canceled', 'Canceled')
)

class Worker(models.Model):

  id = models.CharField(max_length=128, unique=True, primary_key=True)
  name = models.CharField(max_length=128)
  cls_path = models.CharField(max_length=512)

  interval = models.BigIntegerField(default=60*5, help_text="interval in seconds")
  wait_for_approval = models.BigIntegerField(default=60*60*2, help_text="prepare the task and wait for approval")
  notify_for_approval = models.CharField(max_length=2048, blank=True, null=True, help_text="List email id to notify")
  notify_for_errors = models.CharField(max_length=2048, blank=True, null=True, help_text="List email id to notify")

  options = models.TextField(null=True, blank=True)
  active = models.BooleanField(default=True)

  @staticmethod
  def default_data():
    workers = Worker(id='attendance_notice_email')
    worker.name = 'Attendance Notice Email'
    worker.cls_path = 'worker.workers.AttendanceNotificationWorker'
    worker.save()

  def __unicode__(self):
    return self.id

class WorkerTask(models.Model):

  worker = models.ForeignKey(Worker)
  notes = models.TextField(null=True, blank=True)
  worker_options = models.TextField(null=True, blank=True)
  status = models.CharField(max_length=64, choices=WorkerTaskStatus, default='init')


  scheduled = models.DateTimeField(blank=True, null=True)
  started = models.DateTimeField(blank=True, null=True)
  completed = models.DateTimeField(blank=True, null=True)

  modified = models.DateTimeField(auto_now_add=True, auto_now=True)


