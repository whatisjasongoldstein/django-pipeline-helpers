import importlib
from django.conf import settings

# Assets with be cached the first 
# time module is imported.

_js = {}
_css = {}
cached = False


def _add_namespace(namespace, data):
    """
    Add namespace:key to each key in data.
    """
    # modifying the dict as you iterate over it 
    # would hit every key multiple times
    keys = data.keys()  
    
    for key in keys:
        data["%s:%s" % (namespace, key)] = data.pop(key)

def _assets_from_apps(js=False, css=False):
    """
    Search the INSTALLED_APPS for assets.py files,
    and fill the js/css with its contents. Namespace
    bundles with their app's name.
    """
    for app in settings.INSTALLED_APPS:
        try:
            assets = importlib.import_module("%s.assets"% app)
            js = getattr(assets, "PIPELINE_JS", {})
            css = getattr(assets, "PIPELINE_CSS", {})
            _add_namespace(app, js)
            _add_namespace(app, css)
            _js.update(getattr(assets, "PIPELINE_JS", {}))
            _css.update(getattr(assets, "PIPELINE_CSS", {}))
        except ImportError:
            continue
    if js:
        return _js
    if css:
        return _css

if not cached:
    _assets_from_apps()
    cached = True


def find_js():
    return _js

def find_css():
    return _css
