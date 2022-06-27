
# Logistics Management System (Odoo)
![](https://scontent.fuln6-1.fna.fbcdn.net/v/t39.30808-6/271411498_449003416828083_575926474610663720_n.png?_nc_cat=101&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeH4F9tdRFXxfToRD39VGE0jeQEo4jfuiyN5ASjiN-6LIxHfr6sx6PqVhduOs8HElokP4jw8HItt4iVR17uxp9IZ&_nc_ohc=mYUzxm-zHhAAX__CpXP&_nc_ht=scontent.fuln6-1.fna&oh=00_AT_qTspZAwNCPjyHx1n5WAZCcOw1MNkGl7BCBNxrDGi42Q&oe=62B96E35)

### Branches
1. MLTrucking
2. MLWorldWide
3. MLTransit
4. MLCargo
5. MLHolding


## Орчин бэлдэх заавар (Ubuntu):
1. Git -ээс эх код татах
```
git clone https://github.com/monlogistics-group/LMS.git
```
2. PostgreSQL суулгах
```
sudo apt install postgresql postgresql-client

sudo -u postgres createuser -s $USER

createdb $USER
```
3. Ubuntu сан суулгах

```
sudo apt install python3-dev libxml2-dev libxslt1-dev libldap2-devlibsasl2-dev \
    libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev libfreetype6-dev \
    liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev libxcb1-dev libpq-dev
```
4. Python орчин суулгах
```
pip3 install setuptools wheel

pip3 install -r requirements.txt
```
5. Odoo-г ажлуулах
```
python3 odoo-bin --addons-path=addons -d mydb
```