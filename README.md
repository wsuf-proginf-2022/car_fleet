
# Car fleet api

## How to setup dev environment

1. cd into the project directory and run:
```
python -m venv venv
```

2. activate the virtualenv, (on windows):

```
.\venv\Scripts\activate
```

If you are on linux/macOs:

```
source venv/bin/activate
```

3. install the dependencies from requirements.txt

```
pip install -r requirements.txt
```

4. Run the app:

```
flask run
```


# For DB migrations
```
pip install alembic;
alembic init alembic;
```

Then fill out the `sqlalchemy.url` in `alembic.ini`.

After this, edit alembic/env.py:

```
from db import BaseModel

# EACH MODEL NEEDS TO BE IMPORTED HERE IF YOU WANT TO INCLUDE THEM TO YOUR MIGRATIONS
from models.user import UserModel
from models.user import UserModel
from models.project import ProjectModel
from models.supply import SupplyModel

target_metadata = BaseModel.metadata
```

Initialize the alembic table in the database:

```
alembic upgrade head
```

Then, when db changes, generate the migrations automatically:

```
alembic revision --autogenerate -m "Added paypaltransactionid to subscription table"
```

If for some reason you want to create the migration code manually, this will only give you empty functions:

```
alembic revision -m "create basic user and related tables"
```

To delete the migration just delete the file from alembic/versions and if it is
already applied, it will also be included in the alembic_version table in your
db

To apply a migration:

```
alembic upgrade head
```

read more https://alembic.sqlalchemy.org/en/latest/tutorial.html#running-our-first-migration

