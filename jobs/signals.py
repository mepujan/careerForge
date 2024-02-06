from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import JobApplication


@receiver(post_save, sender=JobApplication)
def send_email_to_user(sender, instance, created, **kwargs):
    sender_ = 'gautampujan10@gmail.com'
    receiver_ = [instance.applicant.email]
    if created:
        subject = "Job Applied Successfully"
        body = render_to_string('job_applied_mail.html')
        plain_msg = strip_tags(body)
        send_mail(subject, plain_msg, sender_, receiver_)
    else:
        subject = "Job Status Updated"
        body = render_to_string('job_status_updated_mail.html')
        send_mail(subject, 'Job Updated Successfully',
                  sender_, receiver_)
