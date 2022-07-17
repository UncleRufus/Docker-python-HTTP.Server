#!/bin/bash
echo "
from django.contrib.auth import get_user_model;
user = get_user_model();
user.objects.filter(username="$ADMIN_NAME").exists() or user.objects.create_superuser("$ADMIN_NAME", "$ADMIN_EMAIL", "$ADMIN_PASSWORD")
" | python web_core/manage.py shell
