from django.shortcuts import render
from .models import Project, Skill, Experience, Profile

def portfolio_view(request):
    profile = Profile.objects.first()
    
    projects = Project.objects.all().order_by('order')
    for project in projects:
        project.tech_list = [t.strip() for t in project.tech_stack.split(',')]
    
    experiences = Experience.objects.all().order_by('order')
    skills = Skill.objects.all()
    
    categorized_skills = {}
    for skill in skills:
        if skill.category not in categorized_skills:
            categorized_skills[skill.category] = []
        categorized_skills[skill.category].append(skill)

    context = {
        'profile': profile,
        'projects': projects,
        'experiences': experiences,
        'categorized_skills': categorized_skills,
    }
    return render(request, 'portfolio.html', context)
