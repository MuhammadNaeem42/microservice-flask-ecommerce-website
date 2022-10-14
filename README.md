# Mastering Microservices with Python, Flask, and Docker
## Microservices Setup and Configuration
To launch the end-to-end microservices application perform the following:

### Step 1.
Navigate into the [frontend](https://github.com/cloudacademy/python-flask-microservices/tree/master/frontend) directory, and confirm the presence of the ```docker-compose.deploy.yml``` file:
```
cd frontend
ls -la
```

### Step 1.
Create a new Docker network and name it ```micro_network```:
```
docker network create micro_network
```

### Step 2.
Build each of the microservice Docker container images:
```
docker-compose -f docker-compose.deploy.yml build
docker images
```

### Step 3.
Launch the microservice environment:
```
docker-compose -f docker-compose.deploy.yml build
docker ps -a
```

### Step 4.
Prepare each microservice mysql database:
```
for service in corder-service cproduct-service cuser-service;
do 
 docker exec -it $service flask db init
 docker exec -it $service flask db migrate
 docker exec -it $service flask db upgrade
done
```

### Step 5.
Populate the product database:
```
curl -i -d "name=prod1&slug=prod1&image=product1.jpg&price=100" -X POST localhost:5002/api/product/create
curl -i -d "name=prod2&slug=prod2&image=product2.jpg&price=200" -X POST localhost:5002/api/product/create
```

### Step 6.
Using your workstations browser - navigate to the following URL and register:
```
http://localhost:5000/register
```

### Step 7.
Back within your terminal, use a mysql client to confirm that a new user registration record was created:
```
mysql --host=127.0.0.1 --port=32000 --user=cloudacademy --password=pfm_2020
mysql> show databases;
mysql> use user;
mysql> show tables;
mysql> select * from user;
mysql> exit
```

### Step 8.
Using your workstations browser - login, and add products into your cart, and then finally click the checkout option
```
http://localhost:5000/login
```

### Step 9.
Back within your terminal, use a mysql client to confirm that a new order has been created:
```
mysql --host=127.0.0.1 --port=32002 --user=cloudacademy --password=pfm_2020
mysql> show databases;
mysql> use order;
mysql> show tables;
mysql> select * from order.order;
mysql> select * from order.order_item;
mysql> exit
```

## Microservices Teardown
Perform the following steps to teardown the microservices environment:

### Step 1.
Create a new Docker network and name it ```micro_network```:
```
for container in cuser-service cproduct-service corder-service cproduct_dbase cfrontend-app cuser_dbase corder_dbase;
do
 docker stop $container
 docker rm $container
done
```

### Step 2.
Remove the container volumes
```
for vol in frontend_orderdb_vol frontend_productdb_vol frontend_userdb_vol;
do
 docker volume rm $vol
done
```

### Step 3.
Remove the container network
```
docker network rm micro_network
```

## Python extensions reference
The following Python extensions were used:

* Flask-SQLAlchemy: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
* Flask-Login: https://flask-login.readthedocs.io/en/latest/
* Flask-Migrate: https://github.com/miguelgrinberg/flask-migrate/
* Requests: https://requests.readthedocs.io/en/master/
"# microservice-flask-ecommerce-website" 
