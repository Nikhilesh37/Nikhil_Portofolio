from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    email = models.EmailField()
    linkedin_url = models.URLField()
    github_url = models.URLField()
    resume_file = models.FileField(upload_to='resumes/', blank=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=[
        ('Languages', 'Languages'),
        ('Databases', 'Databases'),
        ('Frameworks', 'Frameworks'),
        ('Tools', 'Tools'),
        ('ML', 'Machine Learning'),
    ])

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    period = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.role} at {self.company}"
