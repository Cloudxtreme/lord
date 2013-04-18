import game

def version(request):
    return {'version': game.__version__, 'copyright': game.__copyright__}