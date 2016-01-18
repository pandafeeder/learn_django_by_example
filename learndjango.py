#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from django.conf import settings
from django.conf.urls import url


BASE_DIR = os.path.dirname(__file__)

settings.configure(
	DEBUG = True,
	ROOT_URLCONF = __file__,
	INSTALLED_APPS = (
		'learnmodel',
		#'learnview',
		#'learnform',
	),
	DATABASES = {
		'default': {
            		'ENGINE': 'django.db.backends.sqlite3',
            		'NAME': 'learnmodel.db',
            		'USER': '',
            		'PASSWORD': '',
            		'HOST': '',
            		'PORT': '',
		},
	},
)

urlpatterns = (
	#url(r'^learnmodel/', include('learnmodel.urls', namespace='learnmodel')),
	#url(r'^learnview/',  include('learnview.urls',  namespace='learnview')),
	#url(r'^learnform',   include('learnform.urls',  namespace='learnform')),
)



if __name__ == '__main__':
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
	import sys
	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)
