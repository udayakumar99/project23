from django.db import models

# Create your models here.
class department(models.Model):
    deptno=models.IntegerField(primary_key=True)
    deptno=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

class employee(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    mgr=models.CharField(max_length=100)
    hiredate=models.DateField()
    salary=models.IntegerField()
    comm=models.IntegerField()
    deptno=models.ForeignKey(department,on_delete=models.CASCADE)

class bonus(models.Model):
    ename=models.ForeignKey(employee,on_delete=models.CASCADE)
    job=models.CharField(max_length=100,primary_key=True)
    sal=models.IntegerField()
    comm=models.IntegerField()

class salgrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    lowsal=models.IntegerField()
    highsal=models.IntegerField()