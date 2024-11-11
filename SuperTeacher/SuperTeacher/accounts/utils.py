from SuperTeacher.accounts.models import TeacherProfile, StudentProfile

def get_user_profile(user):
    try:
        return user.teacherprofile
    except TeacherProfile.DoesNotExist:
        try:
            return user.studentprofile
        except StudentProfile.DoesNotExist:
            return None
