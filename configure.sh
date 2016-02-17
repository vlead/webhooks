
#!/bin/bash
# Configure the application in the deployment environment
# 1. Update the apache config to server via WSGI


if [[ `id -u` -ne 0 ]]; then
  echo "You have to execute this script as super user!"
  exit 1;
fi


update_apache_config() {
  PROC_NAME="webhooks"
  WSGI_SCRIPT="webhooks.wsgi"
  APACHE_VHOST_FILE="/etc/apache2/sites-available/default"

  sed -i "/<\/VirtualHost>/i \
    WSGIScriptAlias / $ABS_PATH_DS/$WSGI_SCRIPT
  " $APACHE_VHOST_FILE
}

update_apache_config
if [[ $? -ne 0 ]]; then
  echo "FATAL: Failed to update apache config"
  exit 1;
fi

service apache2 restart

exit 0;
