# ✉️ Django Contact Form

A responsive contact form built with **Django 3.2**. Visitors fill in their details and message, and the app emails the submission to the site owner over SMTP.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-3.2-092E20?logo=django&logoColor=white)

## ✨ Features

- Collects first name, last name, email, phone, organization and message
- Sends each submission as an email using Django's `send_mail` over SMTP (Gmail by default)
- Separate desktop and mobile stylesheets for a responsive layout
- A single function-based view (`index`) handles both showing the form (`GET`) and processing it (`POST`)

## 🗂️ Project structure

```
contactform1/
├── settings.py        Django settings, including SMTP config
├── urls.py            Routes "/" to the form view
├── views.py           Handles form submission and sends the email
└── templates/
    └── index.html     The contact form
my_proj_static/css/    style.css, mobile.css
manage.py
```

## 🚀 Getting started

```bash
git clone https://github.com/AnjanRimal/Django-Contact-Form.git
cd Django-Contact-Form

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Configure email
Set your SMTP credentials as environment variables rather than hard-coding them. For Gmail, create an [App Password](https://support.google.com/accounts/answer/185833).

```bash
export DJANGO_SECRET_KEY="your-secret-key"
export EMAIL_HOST_USER="you@gmail.com"
export EMAIL_HOST_PASSWORD="your-app-password"
```

### Run
```bash
python manage.py migrate
python manage.py runserver
```

Open **http://127.0.0.1:8000** and submit the form.

## 🛣️ Roadmap
- [ ] Use a Django `Form` class for validation and CSRF-safe rendering
- [ ] Success and error messages after submitting
- [ ] Save submissions to the database and view them in the admin
- [ ] Deploy to Render or Railway

## 👤 Author
**Anjan Rimal** · [Portfolio](https://anjanrimal.com/) · [LinkedIn](https://www.linkedin.com/in/anjanrimal) · [GitHub](https://github.com/AnjanRimal)
