`pip3 freeze` is how to see packages installed

Updating isn't always the best, breaks some depdendancies. We don't want projects to share libraries.

So, we want a clean installation using a virtual env. 

`pip 3 install virtualenv`

`virtualenv venv --python=python3` -- creates a fresh python install in the venv folder

`source venv/bin/activate`

Now, everything will run with Python 3 as default! 

`deactivate` will deactivate 


# JWT

encoding data as web token
encrpyt with user ids
client gets JWT, sends requests, tells us they have authenticated (loggin in)