from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from SuperTeacher.accounts.models import TeacherProfile, StudentProfile

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_teacher:
            TeacherProfile.objects.create(user=instance)
        else:
            StudentProfile.objects.create(user=instance)
