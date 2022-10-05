from django.db import models

class ResultLog(models.Model):
    total_students = models.TextField(default=1)
    address=models.TextField(null=True)
    school = models.TextField(null=True)
    type = models.TextField(null=True)
    grades = models.TextField(null=True)
    city=models.TextField(null=True)
    stud_t_ratio=models.TextField(null=True)
    review=models.TextField(null=True)
    district=models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.id}"

def isnumeric(self):
    review = self.name
    if review.isnumeric() is True:
        return True
    else:
        return False
