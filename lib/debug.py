# lib/debug.py
#!/usr/bin/env python3

from models import get_session, Base, engine
import ipdb

# Example: create tables if not exist
Base.metadata.create_all(bind=engine)

with get_session() as session:
    ipdb.set_trace()
