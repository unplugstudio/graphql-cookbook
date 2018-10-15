# Build a GraphQL API powered by Django

This repository contains the code samples to build your own GraphQL API using the Django web framework and the Graphene library for Python. It is intended to be accompanied by a presentation (originally prepared for DjangoCon US 2018).

## Slides

The slides are available here: https://keen-mayer-abfbee.netlify.com/

You can move across top-level sections using the left/right keys. On each top-level section you can use the up/down keys to drill into the content. Press `Esc` to go into overview mode.

## Using diffs to follow along

You can use the git's diff to see exactly what has changed from one step to the other (including which files have been modified and exactly which lines have been added or removed). GitHub includes an online diff viewer accessible right from the browser. To use it:

1. Go to the [**Releases**](https://github.com/unplugstudio/graphql-cookbook/releases) tab in the repository homepage.
1. Scroll to find the step you want to examine, for example `step-10`.
1. Right below the step you'll see the commit identifier (a string of letters and numbers like `67266fe`). Click it.
1. You should now be in GitHub's diff viewer. Lines of code with a green background indicate additions, and a red background indicates deletions.

At this point you can manually reproduce the steps in your local copy of the repository, or you can checkout each particular step with: `git checkout step-10` (and so forth). This command will apply the changes for a particular step on your codebase so you can be in sync with the slides.

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
