# LectureOrg
"It's time to organize your studying process"<br>
A backend system designed to help students and professors organize lecture resources in an effective way.

## Overview
This backend system was made to solve the problem of unorganized lecture resources which could be a mess sometimes even if you use shared Google Drive Folder or something like that.<br>
Using the API, the resources can be organized in courses and lectures. The difference between using this backend system and Google Drive is that you can combine the professor resources alongside the students' notes all in one place. This makes studying or explaining the lecture easier than before. Also this API can be integrated with the faculty website easily.

## Features
The system contain 3 main roles for the users
- Admin
- Professor
- Student

Each role has its limitations in what he can do with the API. The `Professor` can add courses, edit the details of a specific course or even delete it. He can also create lectures, edit and delete them.
The `Student` can get the details of a specific course/lecture, but he can't edit or delete any course or lecture. The `Student` can add his own notes on a specific lecture and retrieve the details of a specific note anytime.

### Notes
- The `Professor` can add his own notes.
- `Professors`s can only show their own notes not any `Student` note.
- `Students` can only show their own notes and the `Professor` notes. They can't see any other `Student` notes.


## Technologies
- UV Project Manager
- Django
- Django REST Framework
- SQLite
- JWT Authentication

## Installation

Open you terminal and write these commands:

```
> git clone https://github.com/Backend-Committee/Backend-Workshop-Final-Projects.git
> cd Backend-Workshop-Final-Projects
> git switch moataz-mohamed
```
If you don't have `uv` install it from [here](https://docs.astral.sh/uv/getting-started/installation/)

Back to your terminal and write these commands:
```
> uv sync
> uv run manage.py runserver
```

Now you can test all the endpoints.

## API Documentation
You can find the API Documentation and an easy way to test the endpoints [here](https://2i6ijl8wt6.apidog.io/)

## Database and ERD
The Database Management System used in this project is `SQLite`. The database contains Course, Lecture, Note, Link and the User tables. 

For more details about the tables you can find the ERD [here](https://lucid.app/lucidchart/c7072ae2-93c8-472b-b7eb-92ac466690f1/edit?viewport_loc=13%2C-219%2C1680%2C833%2C0_0&invitationId=inv_00fe2421-0365-4fdc-a65d-b63464d6c116)
