#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from flask_script import Manager
import settings
from koswift import app

app.config.from_object(settings)
manager = Manager(app)

if __name__ == "__main__":
    manager.run()

