This repo is mainely to generate coupan codes for brand and providing it to the logged in user and then update the same coupan code availablity in the system

Prerequisites:

Install Pip3 & Python3 -
Install python-3.9 Follow the steps from the below reference document based on your Operating System. Reference: https://docs.python-guide.org/starting/installation/

# Setup virtual environment- 
1. Install virtual environment
- `sudo pip3 install virtualenv`

2. Create virtual environment
- `virtualenv billogram`

3. Activate virtual environment
- `source bin/activate`

4. Install requirements.txt
- `pip3 install -r requirements.txt`

5. Run the server
- `python3 manage.py runserver 8000`

# your server is up on port 8000
Try opening http://localhost:8000 in the browser. Now you are good to go.

# Endpoints -
1. Coupan code generation: 
    http://localhost:8000/brand-discount
3. Retrive coupan code: 
    http://localhost:8000/brand-discount?user=shweta&brand=Zara


# API Specification

Allowed HTTPs requests:
POST    : Create X no of coupan codes for a given brand
GET     : When user request coupan code for a brand this request will give coupan code if available 


