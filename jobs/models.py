from django.db import models
from abstract.base import BaseModel
from django.conf import settings

JOB_TYPES = (
    ('full-time', 'Full Time'),
    ('part-time', 'Part Time'),
    ('contract', 'Contract'),
    ('permanent', 'permanent')
)

JOB_STATUS = (
    ('active', 'active'),
    ('inactive', 'inactive')
)


class Category(BaseModel):
    title = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('-updated',)
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"{self.title}"


class Job(BaseModel):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=JOB_TYPES)
    descriptions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    requirements = models.TextField()
    application_count = models.IntegerField(default=0)
    contact_email = models.EmailField()
    status = models.CharField(max_length=9, choices=JOB_TYPES)
    featured_job = models.BooleanField(default=False)
    urgently_hiring = models.BooleanField(default=False)
    base_salary = models.FloatField(default=0.0)
    company_logo = models.ImageField(upload_to='company_logo')
    hiring_person = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-updated',)

    def __str__(self) -> str:
        return f"{self.title} - job has been created."
