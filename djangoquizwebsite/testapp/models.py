from django.db import models

# Create your models here.


class QuestionsModel(models.Model):
    question= models.CharField(max_length= 300, null=True)
    choice1= models.CharField(max_length= 300, null=True)
    choice2= models.CharField(max_length= 300, null=True)
    choice3= models.CharField(max_length= 300, null=True,blank=True)
    choice4= models.CharField(max_length= 300, null=True,blank=True)
    answer= models.CharField(max_length= 300, null=True)

    def __str__(self):
        return self.question
        

class StudentScores(models.Model):
    StudentName= models.CharField(max_length= 100, null=True)
    MarksObtained= models.IntegerField()

    def __str__(self):
        return self.StudentName
    
