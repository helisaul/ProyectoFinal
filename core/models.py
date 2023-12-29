from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Course(models.Model):

    name = models.CharField(max_length = 90 , verbose_name ='Nombre')
    descripcion = models.TextField(blank = True,null = True,verbose_name ='Descripcion' )
    teacher = models.ForeignKey(User, on_delete =models.CASCADE,limit_choices_to = {'groups__name': 'profesor'},verbose_name ='Profesor')
    class_quantity = models.PositiveBigIntegerField(default = 0, verbose_name ='Cantidad de clases')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Curso'



class Registration(models.Model):

    course = models.ForeignKey(Course, on_delete = models.CASCADE, verbose_name = 'Curso')
    student = models.ForeignKey(User, on_delete =models.CASCADE,   related_name = 'students_registration',limit_choices_to = {'groups__name': 'estudiante'},verbose_name ='Estudiante')
    def __str__(self):
        return f'{self.student.username} - {self.course.name}'
    

    class Meta:
        verbose_name = 'Inscripcion'
        verbose_name_plural = 'Inscripciones'


class Mark(models.Model):
     course = models.ForeignKey(Course, on_delete = models.CASCADE, verbose_name = 'Curso')
     student = models.ForeignKey(User, on_delete =models.CASCADE,limit_choices_to = {'groups__name': 'estudiante'},verbose_name ='Estudiante')
     mark_1 = models.PositiveIntegerField(null = True, blank = True, verbose_name = 'Nota 1')
    
     average = models.DecimalField(max_digits = 3, decimal_places = 1, blank = True, verbose_name = 'Promedio')


     def __str__(self):
         return str(self.course)
     
     def calculate_average(self):
         

         marks = [self.mark_1 ]
         valid_marks = [ mark for mark in marks if mark is not None]

         if valid_marks:
             return sum(valid_marks)/ len(valid_marks)
         
         return  None

     def save(self, *args, **kwargs):
         
         if self.mark_1:
             self.average = self.calculate_average()

         super().save(*args, **kwargs)

     class Meta:
         
         verbose_name = 'Nota'
         verbose_name_plural = 'Notas'
         
