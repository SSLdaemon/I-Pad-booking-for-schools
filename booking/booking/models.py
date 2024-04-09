from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)

class Period(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.start_time.strftime("%I:%M %p")} - {self.end_time.strftime("%I:%M %p")}'


class IPad(models.Model):
    identifier = models.CharField(max_length=200)

class Booking(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    periods = models.ManyToManyField(Period)
    date = models.DateField()
    num_ipads = models.IntegerField()
