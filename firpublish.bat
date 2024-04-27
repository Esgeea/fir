cd /var/www/fir
git pull
systemctl restart fir_gunicorn.socket
systemctl restart fir_gunicorn.service
systemctl restart nginx.service



