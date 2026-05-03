from django.core.management.base import BaseCommand
from main.models import Project, Skill, Experience, Profile

class Command(BaseCommand):
    help = 'Populate initial portfolio data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Project.objects.all().delete()
        Skill.objects.all().delete()
        Experience.objects.all().delete()
        Profile.objects.all().delete()

        # Profile
        Profile.objects.create(
            name='Nikhil Gogineni',
            title='B.Tech Data Science student & Backend Developer',
            bio='I am a Data Science student with a strong foundation in backend development and machine learning. I specialize in building end-to-end systems using Python, Django, and Java. My passion lies in solving real-world engineering problems with clean and functional code.',
            email='nikhilgogineni.22@gmail.com',
            linkedin_url='https://www.linkedin.com/in/nikhil-gogineni-350254212',
            github_url='https://github.com/Nikhilesh37'
        )

        # Experiences
        Experience.objects.create(
            company='UVXYZ Labs Pvt Ltd, Hyderabad',
            role='Software Engineer Intern',
            period='Jul 2025 – Dec 2025',
            description='Built and maintained web applications using Python and Django (MVT architecture) for production backend services. Tracked and resolved bugs across the codebase, improving overall application stability and test coverage.',
            order=1
        )
        Experience.objects.create(
            company='Jala Academy, Hyderabad',
            role='Student Intern',
            period='Jun 2024 – Jul 2024',
            description='Completed an intensive Java training program focused on OOP principles and practical application development. Built a fully functional Java Calculator from scratch.',
            order=2
        )

        # Projects
        Project.objects.create(
            title='IP102 Pest Identification Web App',
            description='Deep learning pest classification project using a ResNet-50 model trained on IP102 (102 classes), with a Django web app for drag-and-drop image inference. Achieved Top-1 73.6% accuracy.',
            tech_stack='PyTorch, Django, ResNet-50, OpenCV, Albumentations',
            github_link='https://github.com/Nikhilesh37/IP102-Pest-Identification-Web-App',
            order=1
        )
        Project.objects.create(
            title='Smart Inventory Demand Forecaster',
            description='End-to-end demand forecasting system built on Rossmann Store Sales dataset (~1M rows). Uses XGBoost and Random Forest models with an interactive Streamlit dashboard.',
            tech_stack='Django, XGBoost, Celery, Redis, MongoDB, PostgreSQL, Streamlit',
            github_link='https://github.com/Nikhilesh37/inventory-forcaster',
            order=2
        )
        Project.objects.create(
            title='Dynamic Blogging Platform',
            description='Relational database models for posts, comments, and authors using Django ORM with full CRUD support via DRF. Includes a session-based "Read Later" feature.',
            tech_stack='Python, Django, Django REST Framework, SQLite',
            github_link='https://github.com/Nikhilesh37/BlogPage',
            order=3
        )
        Project.objects.create(
            title='Movie Recommendation System',
            description='Recommender system using MovieLens dataset and SVD algorithm. Includes TF-IDF for content-based filtering and IMDb metadata merging.',
            tech_stack='Python, Surprise, Pandas, TF-IDF, IMDb Data',
            github_link='https://github.com/Nikhilesh37/Movie-Recommendation',
            order=4
        )
        Project.objects.create(
            title='X Auto Liker Bot',
            description='Automation bot for X (Twitter) using Selenium to automatically like posts based on configuration.',
            tech_stack='Python, Selenium, Automation',
            github_link='https://github.com/Nikhilesh37/X-Auto-Liker-Bot',
            order=5
        )

        # Skills
        skills_data = [
            ('Python', 'Languages'), ('Java', 'Languages'), ('HTML5', 'Languages'),
            ('MySQL', 'Databases'), ('MongoDB', 'Databases'), ('PostgreSQL', 'Databases'),
            ('Django', 'Frameworks'), ('REST API Development', 'Frameworks'), ('Django REST Framework', 'Frameworks'),
            ('AWS', 'ML'), ('NumPy', 'ML'), ('Pandas', 'ML'), ('Matplotlib', 'ML'), ('PyTorch', 'ML'), ('XGBoost', 'ML'),
            ('Git', 'Tools'), ('Celery', 'Tools'), ('Redis', 'Tools'), ('Docker', 'Tools'), ('Selenium', 'Tools'),
        ]

        for name, cat in skills_data:
            Skill.objects.create(name=name, category=cat)

        self.stdout.write(self.style.SUCCESS('Successfully populated portfolio data'))
