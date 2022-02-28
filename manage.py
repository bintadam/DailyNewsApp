# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

