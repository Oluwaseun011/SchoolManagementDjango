from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
import uuid


# Create your models here.


class Person(AbstractBaseUser):
    id = models.UUIDField("Person unique id", primary_key=True, default=uuid.uuid4(), null=False)
    first_name = models.CharField("Person first name", max_length=50, null=True, blank=True)
    last_name = models.CharField("Person last name", max_length=50, null=False, blank=False)
    email = models.EmailField("Person email", null=False, unique=True, blank=False)
    password = models.CharField("Person password", max_length=150, null=False, blank=False)
    address = models.CharField("Person address", max_length=150, null=False, blank=False)
    gender = models.CharField("Person gender", max_length=150, null=False, blank=False)
    telephone = models.CharField("Person phone number", max_length=20, null=True, blank=True)
    date_of_birth = models.DateTimeField("Person dob", auto_now=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    role = models.ManyToManyField("Role")
    permission = models.ManyToManyField("Permission")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["email", "password"]


class Role(models.Model):
    id = models.UUIDField("Role id", primary_key=True, default=uuid.uuid4(), null=False)
    name = models.CharField("Role name", max_length=20, null=False, blank=False, unique=True)
    description = models.CharField("Role description", max_length=500, null=True, blank=True)
    permission = models.ManyToManyField("Permission")


class Permission(models.Model):
    id = models.UUIDField("Permission id", primary_key=True, default=uuid.uuid4(), null=False)
    name = models.CharField("Permission name", unique=True, null=False, blank=False, max_length=20)
    description = models.CharField("Permission description", null=False, blank=False, max_length=500)


class Application(models.Model):
    id = models.UUIDField("Application id", primary_key=True, default=uuid.uuid4(), null=False)
    application_no = models.CharField('Application number', unique=True, max_length=20, null=True, blank=False)
    email = models.CharField("Applicant email", unique=True, null=False, blank=False, max_length=20)
    first_name = models.CharField("Applicant first name", unique=True, null=False, blank=False, max_length=20)
    last_name = models.CharField("Applicant last name", unique=True, null=False, blank=False, max_length=20)
    passport = models.ImageField(upload_to='images/')
    basic = models.ForeignKey("Basic", on_delete=models.RESTRICT)
    application_score = models.IntegerField("Application Score", null=False, blank=False)
    status = models.CharField("Application status", null=False, blank=False, max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Student(models.Model):
    id = models.UUIDField("Role id", primary_key=True, default=uuid.uuid4(), null=False)
    admin_number = models.CharField("Admission Number", max_length=500, null=True, blank=True)
    admin_year = models.CharField("Admission Year", max_length=10, null=True, blank=True)
    person = models.ForeignKey('Person', on_delete=models.RESTRICT)
    basic = models.ManyToManyField('Basic')


class Employee(models.Model):
    id = models.UUIDField("Role id", primary_key=True, default=uuid.uuid4(), null=False)
    person = models.ForeignKey('Person', on_delete=models.RESTRICT)
    staff_number = models.CharField("Staff Number", max_length=500, null=True, blank=True)
    employment_date = models.DateTimeField("Employment date", auto_now=False)
    employment_status = models.CharField("Staff Number", max_length=500, null=True, blank=True)


class Session(models.Model):
    id = models.UUIDField("Session id", primary_key=True, default=uuid.uuid4(), null=False)
    session_name = models.CharField("Session name", unique=True, null=False, blank=False, max_length=20)
    session_start = models.DateTimeField('Session Start', auto_now=False)
    session_end = models.DateTimeField('Session Start', auto_now=False)
    session_status = models.CharField("Session status", null=False, blank=False, max_length=20)


class Term(models.Model):
    id = models.UUIDField("Term id", primary_key=True, default=uuid.uuid4(), null=False)
    session = models.ForeignKey('Session', on_delete=models.RESTRICT)
    term_name = models.CharField("Term name", unique=True, null=False, blank=False, max_length=20)
    term_status = models.CharField("Term status", null=False, blank=False, max_length=20)


class Basic(models.Model):
    id = models.UUIDField("Basic id", primary_key=True, default=uuid.uuid4(), null=False)
    basic_name = models.CharField("Basic name", unique=True, null=False, blank=False, max_length=20)
    subject = models.ManyToManyField('Subject')


class Arm(models.Model):
    id = models.UUIDField("Arm id", primary_key=True, default=uuid.uuid4(), null=False)
    basic = models.ForeignKey('Basic', on_delete=models.RESTRICT)
    arm_name = models.CharField("Arm name", unique=True, null=False, blank=False, max_length=20)
    basic_teacher = models.ForeignKey("Person", null=True, on_delete=models.RESTRICT)


class Subject(models.Model):
    id = models.UUIDField("Subject id", primary_key=True, default=uuid.uuid4(), null=False)
    subject_name = models.CharField("Subject name", unique=True, null=False, blank=False, max_length=20)


class Attendance(models.Model):
    id = models.UUIDField("Attendance id", primary_key=True, default=uuid.uuid4(), null=False)
    status = models.BooleanField()
    date = models.DateTimeField(auto_now=False)
    student = models.ForeignKey('Student', on_delete=models.RESTRICT)
