from sqlalchemy import Column, String, create_engine, Integer, SmallInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
from sqlalchemy import text
from sqlalchemy.sql import and_, asc, desc, or_
import model

if __name__ == '__main__':
