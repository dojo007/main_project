from __future__ import unicode_literals
from django.db import models

class CommentManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData['content']) < 5:
            errors['content'] = "Comment must be at least 5 characters"
        return errors

class CourseManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData['course_name']) < 5:
            errors['course_name'] = "Course name must be at least 5 characters"
        if len(postData['desc']) < 15:
            errors['desc'] = "Course description must be at least 15 characters"
        return errors


class Description(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.OneToOneField(Description, related_name="course",null=True,on_delete=models.CASCADE)

    objects = CourseManager()

class Comment(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, related_name="has_comments",on_delete=models.CASCADE)

    objects = CommentManager()
