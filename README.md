# Khwarizmi
Khwarizmi is an algorithm sharing and discussion platform. It's a web app I am building in Django.

![Screenshot of Khwarizmi](khwarizmi-screenshot.png)

The app is currently deployed using Heroku at [khwarizmiapp.herokuapp.com](https://khwarizmiapp.herokuapp.com). Since the app doesn't receive any traffic, it may take some time to load at first because the Heroku dyno is sleeping. From the Heroku [documentation](https://devcenter.heroku.com/articles/free-dyno-hours):
> If an app has a free web dyno and that dyno receives no web traffic in a 30-minute period, it will sleep.

## Current Features:
- Standard user authentication and authorization system (signup, login, logout, password reset, etc.)
- Create, update and delete algorithms (posts).
- Code highlighting in algorithms.
- Users can leave comments on algorithms.
- Edit profile bio, profile pic and display name.

## Technologies Used:
- **Python** and **Django** for the backend.
- **Heroku** for deployment (and **PostgreSQL** for the database).
- User file uploads (currently only profile pics) are handled by **AWS S3**.
- **Bootstrap 4** for the frontend.
- Code highlighting is handled by **[highlight.js](https://highlightjs.org/)**.
- **[ImageKit](https://github.com/matthewwithanm/django-imagekit)** is used to process images before sending them to S3.
- I use **[direnv](https://direnv.net/)** to automatically set and unset environment variables during development.

## Some of the Problems I Faced:
- I wanted to store sensitive configuration settings (e.g. AWS S3 keys) as environment variables on my machine during development. Instead of writing everything in ~/.profile (I use Linux), I used **[direnv](https://direnv.net/)** to handle exporting environment variables when I enter the project directory and automatically unsets them once I exit.
- Profile Pics need to be centered, cropped and resized before storing them on the file system (S3). I used **[ImageKit](https://github.com/matthewwithanm/django-imagekit)** to handle this part and only wrote a custom crop and center function instead of reinventing the wheel.