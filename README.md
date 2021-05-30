# Designing RESTful APIs

## Introduction

This is my project code and solutions for the lectures and exercises in
Udacity's
[Designing RESTful APIs course](https://www.udacity.com/course/designing-restful-apis--ud388)
. There is a directory for each section of the course, and each section is
listed below with a description. The lessons that utilize each have a file
named `app.py`. This is the file the Docker image looks for in its `/app`
directory. Each app can be run with the same Docker configuration by changing
the [mount point](https://github.com/fitzystrikesagain/designing-restful-apis/blob/main/docker-compose.yml#L12)
in the Docker compose file.

### Project structure

```
├── accessing_published_apis
│   ├── find_a_restaurant.py
│   ├── geocoding.py
│   └── restaurant_search.py
├── create_endpoints
│   ├── making
│   │   ├── app.py
│   │   └── endpoints_tester.py
│   └── responding
│       ├── app.py
│       └── endpoints_tester2.py
└── whats_and_whys
    └── app.py
    └── sending_requests.py
```

## 1. Whats and Whys of APIs
    Learn about the basics of APIs and why they are important.
    How to choose the appropriate technologies for implementing a modern web API.
This section sets up a very basic webserver with API endpoints to 
demonstrate the four HTTP methods: `GET`, `POST`, `PUT`, and `DELETE`.
## 2. Accessing Published APIs

    Explore published APIs from Foursquare and Google Maps.
    See how these companies implement their API endpoints.
    Now leverage some of this information for our own use!
Utilizes the Google Maps and Foursquare APIs to get the latitude and 
longitude from a city and search for venues of interest there.
## 3. Creating your own API Endpoints

    Use Flask to build your own web server.
    Setup API endpoints that follow the constraints to qualify as a RESTful API.

## 4. Securing your API

    Learn about API security.
    How to add OAuth login and token-based authentication.
    Learn to Rate limit your API endpoints.

## 5. Writing Developer-Friendly APIs

    Learn some API best practices using real-world examples.
    Take on the final project!