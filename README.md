# Agriculture Vertical
## Introduction
This is an IoT platform based on FANIoT for specific vertical.
The back-end is based on Django(python).

## Up and Running
1. Create `pyvenv` environment and install the requirements.

```sh
python3 -mvenv .
pip3 install -r requirements.txt
```

2. Check system configuration in `agri_platform/settings.py`.
This project requires a Postgresql database, and you can instantiate it with docker by the following command:

```sh
docker run --name agri-postgres -p 5432:5432 -e POSTGRES_PASSWORD=adminpass -e POSTGRES_USER=admin -e POSTGRES_DB=agri -d postgres
```

3. Apply the migration(s).

```sh
python3 manage.py migrate
```

4. Run and Enjoy :yum:

```sh
python3 manage.py runserver
```

5. Create an admin user

```sh
python3 manage.py createsuperuser
```
