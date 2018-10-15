# Build a GraphQL API powered by Django

This repository contains the code samples to build your own GraphQL API using the Django web framework and the Graphene library for Python. It is intended to be accompanied by a presentation (originally prepared for DjangoCon US 2018).

## Requirements

We assume you're comfortable with Python and Django. You should also be familiar with the usage of pip and how to install packages in your Python environment.

The code and all directions were written for Python 3. It may work with Python 2 but you may find unexpected errors.

## Quickstart

```bash
# Create a Python 3 virtual environment, then...
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata demo.json
python manage.py runserver
```

## Useful links

### General GraphQL
- [Introduction to GraphQL](https://graphql.org/learn/)
- [GraphQL technical specification](https://facebook.github.io/graphql/)
- [Relay specification](https://facebook.github.io/relay/docs/en/graphql-server-specification.html)

### Python / Django specific
- [Graphene Python documentation](http://docs.graphene-python.org/en/latest/)
- [Graphene Django documentation](https://docs.graphene-python.org/projects/django/en/latest/)
- [Graphene Django examples](https://github.com/graphql-python/graphene-django/tree/master/examples)
- [Migrating to graphene-django 2.0](https://github.com/graphql-python/graphene/blob/master/UPGRADE-v2.0.md)
- [Use DjangoObjectType (or something like it) as an Input class?](https://github.com/graphql-python/graphene-django/issues/121)

### Miscellaneous
- [A beginner's guide to GraphQL (using Node.js)](https://medium.freecodecamp.org/a-beginners-guide-to-graphql-60e43b0a41f5)
- [5 reasons you shouldn't be using GraphQL](https://blog.logrocket.com/5-reasons-you-shouldnt-be-using-graphql-61c7846e7ed3)
- [Collection of public GraphQL APIs](http://apis.guru/graphql-apis/)
- [Django Filter documentation](https://django-filter.readthedocs.io/en/master/index.html)

### Client-side
- [Apollo Client](https://www.apollographql.com/client)
