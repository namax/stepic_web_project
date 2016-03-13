sudo pip3 install django
sudo pip3 install gunicorn
sudo apt-get -y update
sudo apt-get -y install python3-dev libmysqlclient-dev
sudo pip3 install mysqlclient
sudo service mysql restart
mysql -u root < /home/box/web/etc/db.sql