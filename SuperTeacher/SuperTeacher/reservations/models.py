

from django.db import models
from django.utils import timezone

from SuperTeacher.accounts.models import StudentProfile, TeacherProfile


class Reservation(models.Model):

    class Meta:
        ordering = ['reservation_time']
        unique_together = (
        'student', 'reservation_time')

    student = models.ForeignKey(
        to=StudentProfile,
        on_delete=models.CASCADE,
        related_name='student_reservations',
    )

    teacher = models.ForeignKey(
        to=TeacherProfile,
        on_delete=models.CASCADE,
        related_name='teacher_reservations',
    )

    reserved_at = models.DateTimeField(
        default=timezone.now,
        help_text="The date and time the reservation is made",
    )

    reservation_time = models.DateTimeField(
        help_text="The date and time the reservation is for",
    )

    status = models.CharField(
        max_length=20,
        choices=(
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('cancelled', 'Cancelled'),
            ('completed', 'Completed'),
        ),
        default='pending',
    )

    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Optional notes or special instructions for the reservation",
    )

    def __str__(self):
        return f"Reservation by {self.student} with {self.teacher} at {self.reservation_time}"

