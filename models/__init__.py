#!/usr/bin/env python3
""" instantiates a storage engine """

from models.engine.file_storage import File_storage

Storage = File_storage()
Storage.reload()
