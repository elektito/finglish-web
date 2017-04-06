This package provides a very simple Web UI for the
[Finglish-to-Persian converter][1] library. You can launch the UI
using the following instructions:

    $ virtualenv venv -p python3
    $ . venv/bin/activate
    $ pip install -r requirements.txt
    $ gunicorn web:app

You can also use the provided Dockerfile to build a docker image.

[1]: https://github.com/elektito/finglish
