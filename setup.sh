
#!/bin/bash

# Install pre-requsite dependencies: python-dev, mysqld-dev, setuptools,
# apache, mod_wsgi etc.
echo "Installing pre-requisite dependencies.."
apt-get install -y python-dev python-setuptools apache2 libapache2-mod-wsgi
if [[ $? -ne 0 ]]; then
  echo "FATAL: Installing pre-requisite dependencies failed!"
  exit 1;
fi

echo "Enabling the mod WSGI on apache"
a2enmod wsgi
if [[ $? -ne 0 ]]; then
  echo "FATAL: Unable to enable mod wsgi!"
  exit 1;
fi

# Installing python dependencies
echo "Installing dependencies.."
python setup.py install
if [[ $? -ne 0 ]]; then
  echo "FATAL: Installation failed!"
  exit 1;
fi

exit 0
