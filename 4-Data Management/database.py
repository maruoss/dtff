# database.py

# create MySQL 
dialect = "mysql"
username = os.environ.get("DB_USERNAME")
password = os.environ.get("DB_PASSWORD")

db_name = "database"
host = "localhost"
port = 3306

eng = f"{dialect}://{username}:{password}@{host}:{port}/{db_name}"
