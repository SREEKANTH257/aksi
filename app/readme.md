
Aksi/
│
├── app/                      # Application 
│   ├── app.py                # Application code && #code to start the application
│   ├── tokengeneration.py    # JWT token generator
│   ├── tokenvalidation.py    # JWT token validation
│   ├── tokenapirequest.py    # tokenapirequestcheck
│   ├── testdb.py             # to see users list as Superadmin/admin/superuser or dev/user or trainee
│   ├── verifycurl.py         # verify curl
│   ├── viewdb.py             # test db connection
│   ├── users.db              # users database file
│   └── static/               # Static files (CSS)
│   └── templates/            # HTML templates
├── requirements.txt          # Python dependencies
├── nginx/(It's in EC2)
│   └── my-flask-app     # Nginx configuration file(my-flask-app.conf)
│
└── README.md                 # This file

Features:
Simple Flask application
Deployed on AWS EC2
Configured to handle HTTP traffic on port 80

Prerequisites:
AWS EC2 instance
Nginx installed on the EC2 instance
Flask application code
Python 3.x

Requirements:
Python
Flask
Flask-SQLAlchemy
Flask-JWT-Extended
Gunicorn


Local setup:

1. Unzip aksi folder

2. setup python environment 

3. pip install -r requirements.txt 

4. navigate to app folder cmd => python3 app.py

5. click link redirecting to http://localhost:5000

6. access the dashboard

8.For regestering curl -X POST http://localhost:5000/register -H "Content-Type: application/json" -d '{"username": "abcd", "password": "testpassword", "role": "developer"}'

9.For logging curl -X POST http://localhost:5000/login \ -H "Content-Type: application/json" \ -d '{"username": "zx", "password": "1234", "role": "developer"}'

10. Unfortunately my application cannot able to authorise after login so please if you wanna check manually entering please run "tokengeneration.py" copy generated output to clipboard. and generated token will be separate for role, the role you selected it'll fetch token of it, I commented on code where to change role.

11. run "tokenvalidation.py" to validate token

12. curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3RfdXNlciIsInJvbGUiOiJkZXZlbG9wZXIiLCJleHBpcmF0aW9uIjozNjAwMDAwMDAwMH0.XY_wCj2P3ocjch44UGk5P8kkkiPT5RzRuT0CTT9DWU" http://localhost:5000/api/dashboard

12. run testdb.py to view DB as superadmin/admin/superuser/user

13. static and template are css & html folders

14. you can see also database & tables using testdb.py




Setup: on EC2

1. ssh -i mykeypair.pem ec2-user@ec2-13-60-80-67.eu-north-1.compute.amazonaws.com

2.setup python environment (on ec2 "venv" yourwish)

3. pip install -r requirements.txt (if pip available)

4. run flask application

5. configure nginx 

6. start ngix

7. go to ec2 "http://ec2-13-60-80-67.eu-north-1.compute.amazonaws.com"



