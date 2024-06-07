#!/bin/bash

echo "RUN Server by gunicron"
gunicorn cms_config.wsgi -b 0.0.0.0:8000