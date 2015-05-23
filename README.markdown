[Django Pipeline](https://github.com/cyberdelia/django-pipeline/) expects you
to keep the list of your static assets in `settings.py`. That seems like it 
violates the separation of concerns.

Instead, I'm going to borrow an idea from [Django Assets](https://github.com/miracle2k/django-assets)
and keep them in the `assets.py` inside the apps.

## Usage

In `settings.py`

```
import pipeline_helpers
PIPELINE_CSS = pipeline_helpers.find_css()
PIPELINE_JS = pipeline_helpers.find_js()
```

And then put asset configs in `assets.py` modules within the apps.