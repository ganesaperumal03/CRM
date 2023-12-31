from django.db import models

class Deals(models.Model):
    deal_id = models.AutoField(primary_key=True)
    deal_name = models.CharField(max_length=255, default='Default Name')
    stage = models.CharField(max_length=255, default='Default Stage')
    activity = models.CharField(max_length=255, default='Default Activity')
    client = models.CharField(max_length=255, default='Default Client')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    responsible = models.CharField(max_length=255, default='Default Responsible')
    created = models.DateTimeField(auto_now_add=True)
    customer_journey = models.CharField(max_length=255, default='Default Journey')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Leads(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    status = models.CharField(max_length=20)
    source = models.CharField(max_length=50)
    assigned_to = models.CharField(max_length=50)
    lead_quality = models.CharField(max_length=10)
    lead_score = models.IntegerField()
    notes = models.TextField()
    created_date = models.DateField()
    last_contacted = models.DateField()
    next_followup_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"