from django.db import models

# Create your models here.

# Create your models here.
PRIORITY = (
        ('HIGH', 'HIGH'),
        ('MEDIUM', 'MEDIUM'),
        ('LOW', 'LOW'),
    )
PHASE = (
        ('US', 'US'),
        ('ISSUE', 'ISSUE'),
        ('OTHER', 'OTHER'),
    )
STATUS = (
        ('NOTSTARTED', 'NOT-STARTED'),
        ('INPROGRESS', 'IN-PROGRESS'),
        ('FIXED', 'FIXED'),
        ('HOLD', 'HOLD'),

    )
STATUS1 = (
        ('WEBSITE', 'WEBSITE'),
        ('MOBILEAPP', 'MOBILEAPP'),
        ('BUSINESS', 'BUSINESS'),
        ('TOOLS', 'TOOLS'),
    )
ADMIN_PEOPLE = (
        ('DEEPAK', 'DEEPAK'),
)

class Bug(models.Model):
    bug_phase = models.CharField(max_length=10, blank=True, null=True, choices=PHASE)
    bug_title = models.CharField(max_length=80,blank=True, null=True)
    bug_detail = models.CharField(max_length=200,blank=True, null=True)
    priority = models.CharField(max_length=10, blank=True, null=True, choices=PRIORITY)
    status = models.CharField(max_length=100, blank=True, null=True, choices=STATUS)
    category = models.CharField(max_length=100, blank=True, null=True, choices=STATUS1)
    issue_pic = models.ImageField(upload_to = 'bugissue/', default = 'bugissue/default/no-img.jpg')
    assgined_to = models.CharField(max_length=10, blank=True, null=True, choices=ADMIN_PEOPLE)



