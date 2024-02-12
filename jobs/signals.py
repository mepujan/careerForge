from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import JobApplication
from django.template.loader import get_template
from asgiref.sync import sync_to_async


@receiver(post_save, sender=JobApplication)
@sync_to_async
def send_email_to_user(sender, instance, created, **kwargs):
    sender_ = 'gautampujan10@gmail.com'
    receiver_ = [instance.applicant.email]
    if created:
        job_title = instance.job.title
        subject = "Job Applied Successfully"
        message = "Email Body"
        body = get_template('job_applied_mail.html')
        html_content = body.render({
            'title': job_title
        })
        send_mail(
            subject,
            message,
            sender_,
            receiver_,
            fail_silently=False,
            html_message=html_content,
        )
