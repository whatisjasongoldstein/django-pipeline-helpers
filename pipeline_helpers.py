import importlib
from django.conf import settings

_js = {}
_css = {}
_cached = False

def _assets_from_apps(js=False, css=False):
    if not _cached:
        for app in settings.INSTALLED_APPS:
            try:
                assets = importlib.import_module("%s.assets"% app)
            except ImportError:
                continue
            _js.update(getattr(assets, "PIPELINE_JS", {}))
            _css.update(getattr(assets, "PIPELINE_CSS", {}))
    if js:
        return _js
    if css:
        return _css

def find_js():
    return _assets_from_apps(js=True)


def find_css():
    return _assets_from_apps(css=True)