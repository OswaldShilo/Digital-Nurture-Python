# Exercise 43: Configuration Manager
# Objective: Classes + inheritance + configparser for DB settings

import configparser
import os

FILE = "db.ini"

def create_sample_config():
    cfg = configparser.ConfigParser()
    cfg["database"] = {"host": "localhost", "port": "5432",
                       "name": "app_db", "user": "admin", "password": "secret"}
    with open(FILE, "w") as f:
        cfg.write(f)

class Config:
    def __init__(self, filepath):
        self.filepath = filepath
        self._cfg     = configparser.ConfigParser()

    def load(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Config file '{self.filepath}' not found.")
        self._cfg.read(self.filepath)

class DatabaseConfig(Config):
    REQUIRED = ["host", "port", "name", "user", "password"]

    def validate(self):
        if "database" not in self._cfg:
            raise KeyError("Missing [database] section.")
        for key in self.REQUIRED:
            if key not in self._cfg["database"]:
                raise KeyError(f"Missing required key: '{key}'")

    def display(self):
        db = self._cfg["database"]
        print("Database Configuration:")
        for key in self.REQUIRED:
            val = "****" if key == "password" else db[key]
            print(f"  {key:<10}: {val}")

create_sample_config()
cfg = DatabaseConfig(FILE)
cfg.load()
cfg.validate()
cfg.display()
