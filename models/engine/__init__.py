#!/usr/bin/python3
"""Initializing a Unique fileStorage Instance on Importation of the Package
Uses the __init__ magic method.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()