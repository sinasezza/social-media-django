# social-media-django
a social media web application in django + some other things

## Required Software
- [Python 3.10](https://www.python.org/downloads/) or newer
<!-- - [Node.js 18.15 LTS](https://nodejs.org/) -->
- [Git](https://git-scm.com/)

## get started
1. clone the repository: `git clone https://github.com/sinasezza/social-media-django.git`
2. `cd social-media-django`

### configure environment
_macOS/Linux Users_
```bash
python3 manage.py -m venv venv
source ./venv/bin/activate
pip install uv
uv pip sync requirements.txt
```

_Windows Users_
```bash
python manage.py -m venv venv
venv\scripts\activate
pip install poetry
pip install uv
uv pip sync requirements.txt
```

### Run The Django Http Server
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```