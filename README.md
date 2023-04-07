# API Practice with Django

## How to start this project.
1. Clone from github. 

2. Create a virtual environment.
- `python -m venv /path/to/new/virtual/environment` (https://docs.python.org/3/library/venv.html)
3. Activate virtual environment
- Gitbash: `source venv/Scripts/activate` (Refer to link in point 2)
4. Install requirement.txt
- `pip install -r requirements.txt`
5. Run migrations
6. Run server.
- Navigate into 'codecademy_django' directory and run the following in the command line: `python manage.py runserver`

# API GUIDE
### Base URL: "http://127.0.0.1:8000/"

## Getting Started
1. REGISTER
  - POST - api/register/
2. LOGIN
  - POST - api/login/
  - Login to receive API Authorization token.

## Venue
1. Retrieve all venues
  - GET - api/venues
2. Retrieve a venue with a primary key
  - GET - api/venues/:pk
3. Add a venue
  - POST - api/venues/
4. Update a venue
  - PATCH - api/venues/:pk/
5. Delete a venue
  - DELETE - api/venues/:pk/

## Photo
1. Retrieve all photos
  - GET - api/photos
2. Retrieve a photo with a primary key
  - GET - api/photos/:pk
3. Add a photo
  - POST - api/photos/
4. Update a photo
  - PATCH - api/photos/:pk/
5. Delete a photo
  - DELETE - api/photos/:pk/
  
