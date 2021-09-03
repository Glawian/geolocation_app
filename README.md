# Geolocation app
Application is developed with Django framework.

Authenticated user can list IP addresses with their geolocation and add new IP addresses.

## Setup application
Before running any commands update variable **API_TOKEN** with your API Access Key in **docker-compose.yml** file which will be used by **[ipstack](https://ipstack.com/)** to find geolocation of an IP address.

Next run following commands (Linux):

```
docker-compose build - to build image
docker-compose up - start the container (use -d if necessary)
docker-compose run geolocation-app python manage.py createsuperuser (if needed)
docker-compose run geolocation-app python manage.py migrate
```

Migration will create auth0 user needed for authentication. To use other authentication APIs change AUTH0_DOMAIN and API_IDENTIFIER in settings.py of the project.

**Django** project will be available under [localhost:80](http://localhost:80)
