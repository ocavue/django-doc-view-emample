# django-doc-view example

A runable example for [django_doc_view](https://github.com/ocavue/django-doc-view)

## requirements

1. Django version >= 1.8, or you can't user `-f --format` [argument](https://stackoverflow.com/questions/30230490/django-custom-command-error-unrecognized-arguments)

## run server

```
pip3 install -r requirements.txt
python3 manage.py runserver
```

## document views

```
$ python3 manage.py doc_view

## ^$
    None (An example of undocmented view)

## polls/

    An example of Function-based view

    method
        get
    request
        None
    response:
        type: html


## polls/user

    An example of Class-based view

    method
        get
    request:
        none
    respones:
        type: json
        example:

            ```
            {
                "data": {
                    "user": {
                        "id": "123",
                        "name": "qwertyuiop",
                        "create_date": "1970-01-01"
                    }
                },
                "error": false
            }
            {
                "msg": "error message",
                "error": true
            }
            ```

    more info:
        add login authentication in future

```