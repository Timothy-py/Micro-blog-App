from app import appInstance


@appInstance.route('/index')
def index():
    return "Hello, World!"
