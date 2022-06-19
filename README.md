[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python 3.8.10](https://img.shields.io/badge/python-3.9.*-blue.svg)](https://www.python.org/downloads/release/python-3913/)

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)


# Yet-Another-Image-Scraper-API
A simple API that:
- Scrapes a link for images
- Allows "users" to fetch those images with minor downsizing if applicable for
an image.


## Getting Started
- This project assumes a that the host machine has a `Python 3.9.*` installation.
- Since this project is meant to be run locally only, we don't have to worry
about setting up a database.
- Run the entrypoint:
    - For *nix machines: `./entrypoint.sh`
    - For Windows machines: `./entrypoint.bat`
- Start the API server using: `python manage.py runserver`
- Start the the job runner using: `python manage.py scraping_jobs`
- Visit `/docs/swagger` for documentation.


## Considerations
- To make it easier to launch the project **very** quickly without any configurations
we're using a default SQLite database. However, it'll be easy to migrate to another
DB such as Postgres fairly easily.


## Assumptions
- I've tried to keep things simple so that it's easy to get started and test
things out without any complicated settings.
- While there aren't any "Users" yet for the API, I've left to leave in a
custom basic user model in case I decide to support users somewhere down the line.
- When a scraping request for a URL is made, all links on the site are fetched
and stored in the system. Later, through a scheduled job, the images are fetched
one at a time. This achieves two goals:
1. Prevents us from hitting any rate limits on a site, or spamming it with too
many requests.
2. Since fetching all the images is expected to take a while, this allows us to
complete a request-response cycle without forcing the user to wait for a long
time.


## References
- [This](https://github.com/saqibur/django-project-structure) structure was used
to organize files and directories for this project.
