This package provides a very simple Web UI for the
[Finglish-to-Persian converter][1] library. You can launch the UI
using the following instructions:

    $ virtualenv venv -p python3
    $ . venv/bin/activate
    $ pip install -r requirements.txt
    $ gunicorn web:app

You can also use the provided Dockerfile to build a docker image. You
can build the image by running something like this:

    $ docker build -t elektito/finglish-web .

Or you can download it from Docker Hub:

    $ docker pull elektito/finglish-web

Then run the container:

    $ docker run -it -p 8000:8000 --rm finglish-web

[1]: https://github.com/elektito/finglish
