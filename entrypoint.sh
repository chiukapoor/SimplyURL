#!/bin/bash
gunicorn -b 0.0.0.0:5000 api.wsgi:app --timeout=3600 --workers=2 --reload