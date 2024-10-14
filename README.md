**Flask App**
To build and deploy a role-based user authentication system with a dashboard, follow these steps.
We'll use Flask for the backend API, SQLite for the database, HTML for frontend and deploy the application on an AWS EC2 Free Tier instance.
**1. setup**
Create a project directory with the following structure:
aksi/
├── app/
│   ├── app.py                        # Application code & code to start the application
│   ├── curls.txt                     # Curl commands to pass api reuests
│   ├── dupapp.py                     
│   ├── testdb.py                     # To see user list role wise
│   ├── tokenapirequest.py            # tokenapirequest
│   ├── tokengeneration.py            # JWT token generator
│   ├── tokenvalidation.py            # JWT token validation
│   ├── verifycurl.py                 # verify curl
│   ├── users.db                      # users database file
│   └── viewdb.py                     # Test DB connection
├── static/
│   ├── styles.css                    #styles
├── templates/
│   ├── index.html                    #UI/ Main page
│   └── dashboard.html                #dashboard page
├── instance/
│   └── myapp.conf                    #configuration file
├── requirements.txt                    # Python dependencies
└── README.md

Installation:
python3 -m venv yourenv
yourenv\Scripts\activate
pip install -r requirements.txt

Accessing application:
python3 app.py #main application file
application URL : http://127.0.0.1:5000 (Local Host)
application URL : http://16.16.68.195/ (Public URL) 
application URL : http://ec2-16-16-68-195.eu-north-1.compute.amazonaws.com (Public URL) 






