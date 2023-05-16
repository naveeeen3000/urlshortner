# Django URL Shortener

A simple URL shortener built using Django.

## Features

- Allows users to shorten long URLs.
- Keeps track of the number of times a shortened URL has been visited.
- Customizable URLs.

## Installation

1. Clone the repository:

   ```shell
    git clone https://github.com/your-username/django-url-shortener.git
    cd django-url-shortener
    
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
Visit http://localhost:8000 in your web browser.

