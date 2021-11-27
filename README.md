This repo is mainely to generate coupan codes for brand and providing it to the logged in user and then update the same coupan code availablity in the system

Prerequisites:

Install Pip3 & Python3 -
Install python-3.9 Follow the steps from the below reference document based on your Operating System. Reference: https://docs.python-guide.org/starting/installation/

Setup virtual environment- 
# Install virtual environment
sudo pip3 install virtualenv

# Create virtual environment
virtualenv thanos

cd thanos

# Activate virtual environment
source bin/activate

cd billogram_discount_code/discount_code

# install requirements.txt
pip3 install -r requirements.txt

# Run the server
python3 manage.py runserver 8000

# your server is up on port 8000
Try opening http://localhost:8000 in the browser. Now you are good to go.

Endpoint -
Coupan code generation: http://localhost:8000/brand-discount
Retrive coupan code: http://localhost:8000/brand-discount?user=shweta&brand=Zara


API Specification - 

Allowed HTTPs requests:
POST    : Create coupan codes for a given brand
GET     : When user request coupan code for a brand this request will give coupan code if available 


