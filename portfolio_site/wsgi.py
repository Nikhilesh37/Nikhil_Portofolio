"""
WSGI config for portfolio_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import pymongo
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')

# --- DIAGNOSTIC PING ---
try:
    from django.conf import settings
    uri = os.environ.get('MONGODB_URI', 'localhost')
    print(f"DEBUG: Attempting to connect to MongoDB...")
    client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=5000)
    client.server_info()
    print("DEBUG: MongoDB Connection SUCCESS!")
except Exception as e:
    print(f"DEBUG: MongoDB Connection FAILED: {e}")
# -----------------------

application = get_wsgi_application()
