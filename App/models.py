from django.db import models


class House(models.Model):
    HOUSENAMES = (
        ('GH', 'Gryffindor'),
        ('HH', 'Hufflepuff'),
        ('RH', 'Ravenclaw'),
        ('SH', 'Slytherin'),
    )
    name = models.CharField(db_column="House", max_length=2, choices=HOUSENAMES)


class Student(models.Model):
    name = models.CharField(db_column="Name", max_length=32)
    surname = models.CharField(db_column="Surname", max_length=32)
    gender = models.BooleanField(db_column="Gender", default=True)  # True male, False female
    age = models.IntegerField(db_column="Age", default=1)
    photo = models.ImageField(db_column="Photo", upload_to="student_photos")
    s_house = models.ForeignKey(House, on_delete=models.PROTECT)


class MistakeRecord(models.Model):
    record = models.TextField(db_column="Record", max_length=2000, blank=True)
    m_student = models.ForeignKey(Student, on_delete=models.PROTECT)


class Wand(models.Model):
    name = models.CharField(db_column="Name", max_length=32)
    w_student = models.ForeignKey(Student, on_delete=models.PROTECT)


class Magic(models.Model):
    TYPES = (
        ('N', 'Normal'),
        ('F', 'Forbidden'),
    )
    type = models.CharField(db_column="Type", max_length=12, choices=TYPES)
    name = models.CharField(db_column="Name", max_length=32)
    m_wand = models.ForeignKey(Wand, on_delete=models.PROTECT)