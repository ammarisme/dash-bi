class Url:
    """
    Url class that defined the path and the 
    relevant layout fot it
    """
    def __init__(self, path, layout):
        self.path = path
        self.layout = layout


def display_page(pathname, urlpatterns):
    """
    helper function to get the relevant layout
    """
    for url in urlpatterns:
        if pathname == url.path:
            return url.layout
    return '404'
