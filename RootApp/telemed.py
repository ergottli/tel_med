from app import app, db
<<<<<<< HEAD
from app.models import User#, Post
=======
from app.models import User, Post
>>>>>>> cfebcc893638e5eabc57ea920b01d2bd9a73ff66


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
