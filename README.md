**Flask App**
To build and deploy a role-based user authentication system with a dashboard as outlined, follow these steps.
We'll use Flask for the backend API, SQLite for the database, HTML for frontend and deploy the application on an AWS EC2 Free Tier instance.
**1. setup**
Create a project directory with the following structure:
aksi/
├── app/
│   ├── app.py
│   ├── curls.txt
│   ├── dupapp.py
│   ├── testdb.py
│   ├── tokenapirequest.py
│   ├── tokengeneration.py
│   ├── tokenvalidation.py
│   ├── verifycurl.py
│   └── viewdb.py
├── instance/
│   └── myapp.config
├── requirements.txt
└── README.md

