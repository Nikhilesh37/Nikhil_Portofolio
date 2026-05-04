# Nikhil Gogineni Portfolio

A minimalist, high-contrast portfolio website built with Django and Vanilla JavaScript.

## Features
- Dark Mode support (automatic & toggle)
- Responsive design
- Minimalist UI with a single primary color (#6366F1)
- Project showcase with tech stack tags
- Experience timeline
- Skills categorized by domain

## Tech Stack
- **Backend:** Django
- **Frontend:** HTML5, CSS3 (Vanilla), JavaScript (Vanilla)
- **Database:** MongoDB (via MongoDB Atlas)

## Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # venv\Scripts\activate on Windows
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Populate data:
   ```bash
   python manage.py populate_data
   ```
4. Start the server:
   ```bash
   python manage.py runserver
   ```

## Render Deployment
1. **Environment Variables:**
   - `MONGODB_URI`: Your MongoDB Atlas connection string.
   - `MONGODB_NAME`: The name of your database (e.g., `portfolio_db`).
   - `SECRET_KEY`: A secure key for Django.
   - `DEBUG`: Set to `False` in production.
2. **IP Access:** Ensure `0.0.0.0/0` is whitelisted in MongoDB Atlas Network Access.
3. **Shell Command:** After first deployment, use the Render Shell to run `python manage.py populate_data`.

## Design Choices
- **Color Palette:** Strictly uses Indigo (#6366F1) as the primary accent color to avoid the "AI-generated" rainbow look.
- **Typography:** Uses clean sans-serif fonts with high hierarchy.
- **Animations:** Subtle fade-in on scroll using Intersection Observer.
