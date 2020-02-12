from . import routes


@routes.route('/')
def wtf():
    return "foobar"

@routes.route('/test')
def test():
    return "This is a new test"