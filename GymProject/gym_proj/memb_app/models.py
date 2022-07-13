from django.db import models

class Role(models.Model):
    name =models.CharField(max_length=100, null = False)

    def __str__(self):
        return self.name
    
class Fees_plan(models.Model):
    plan = models.CharField(max_length=100, null = False)
    duration = models.IntegerField(default = 0, null = False)
    fees = models.IntegerField(default = 0, null = False)

    def __str__(self):
        return "%s %s %s" %(self.plan,self.duration,self.fees)
    
class Member(models.Model):
    first_name = models.CharField(max_length=100, null = False)
    last_name = models.CharField(max_length=100)
    role = models.ForeignKey(Role,on_delete = models.CASCADE)
    entry_id = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    fees_plan = models.ForeignKey(Fees_plan,max_length=100, on_delete = models.CASCADE,null=True)
    
        
    def __str__(self):
        return "%s %s %s %s" %(self.role,self.entry_id,self.first_name, self.last_name)
