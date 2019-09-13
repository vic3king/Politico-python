import os

# local imports
from app import create_app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from flask_sqlalchemy import SQLAlchemy

app = create_app(os.getenv('APP_SETTINGS') or 'default')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0')
)

if __name__ == '__main__':
    manager.run()
