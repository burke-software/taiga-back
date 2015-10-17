#!/bin/bash
celery -A taiga worker -l info -E& python manage.py runserver 0.0.0.0:8000
