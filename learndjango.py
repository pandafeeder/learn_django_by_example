#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from django.conf import settings


BASE_DIR = os.path.dirname(__file__)

settings.configure(
	DEBUG = True,
	ROOT_URLCONF = 'urls_conf',
	INSTALLED_APPS = (
		'learnmodel.apps.LearnmodelConfig',
		#'learnview',
		#'learnform',
	),
	DATABASES = {
		'default': {
        		'ENGINE': 'django.db.backends.sqlite3',
        		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    		}
	},
)



if __name__ == '__main__':
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
	import sys
	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)
