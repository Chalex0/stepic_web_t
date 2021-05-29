sudo apt update
sudo apt install python3.5 -y
sudo apt install python3.5-dev -y
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo python3 -m pip install gunicorn
sudo python3 -m pip install django==2.0
sudo python3 -m pip install mysqlclient

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE stepic_web;"
mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'box'@'localhost' WITH GRANT OPTION;"
mysql -uroot -e "FLUSH PRIVILEGES;"
sudo /etc/init.d/mysql restart
python /home/box/web/ask/manage.py collectstatic
python /home/box/web/ask/manage.py syncdb
sudo /etc/init.d/nginx restart

cd ask
python3 manage.py makemigrations qa
python3 manage.py migrate

gunicorn --bind=0.0.0.0:8000 --workers=2 --timeout=15 --log-level=debug ask.wsgi:application
