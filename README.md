# Blogging Platform with Personalized Recommendations

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python 3.x
Django 3.x
A database (e.g. PostgreSQL, MySQL, SqlLite)
Installing
Clone the repository to your local machine:
https://github.com/rjpatil885/Blog_Site.git

Navigate to the project directory:
cd Amazing-Blog-Site/BlogProject

Apply the migrations:
python manage.py makemigrations,

python manage.py migrate

Run the following command to start the development server:
python manage.py runserver

The server will be running on http://127.0.0.1:8000/

Username : admin,
Password : admin

# Features

User-friendly Interface: The application provides a clean and intuitive user interface for easy navigation and interaction with blog posts.

Post Search: Users can search for specific posts using keywords or phrases.

Detailed Post View: Users can view detailed information about each blog post, including the author, publication date, and content.

Comments: Users can comment on blog posts, enabling discussions and engagement with other users.

Likes and Dislikes: Users can express their opinion on posts by liking or disliking them.

User Registration and Authentication: The application includes a user registration system that allows new users to create an account. Registered users can log in and access additional features.

Exception Handling: The project incorporates error handling to provide a smooth user experience and handle potential exceptions.

User Profiles: Users have personalized profiles where they can update their information and manage their preferences.

Content-Based Recommendation System: The application includes a recommendation system that suggests posts to users based on their liked posts. The system utilizes the TF-IDF vectorization technique to calculate the similarity between posts and recommends a set of relevant posts to the user.
