PYTHONPATH := $(LOCALPATH)/
TEST_SETTINGS := test
DJANGO_TEST_SETTINGS_MODULE = $(PROJECT).settings.$(TEST_SETTINGS)
DJANGO_TEST_POSTFIX := --settings=$(DJANGO_TEST_SETTINGS_MODULE) --pythonpath=$(PYTHONPATH)
PYTHON_BIN := $(VIRTUAL_ENV)/bin

test: clean virtual_env_set
	-$(PYTHON_BIN)/coverage run $(PYTHON_BIN)/django-admin.py test $(APP) $(DJANGO_TEST_POSTFIX)