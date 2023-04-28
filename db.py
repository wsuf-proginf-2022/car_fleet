from flask_sqlalchemy import SQLAlchemy
from typing import TYPE_CHECKING

db = SQLAlchemy()

# mypy hinting miatt
if TYPE_CHECKING:
  from flask_sqlalchemy.model import Model
  BasModel = db.make_declarative_base(Model)
else:
  BaseModel = db.Model
