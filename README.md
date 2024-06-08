# SongQualities

How To Run
Download Repository

Create the table in the database: https://www.youtube.com/watch?v=wuyDrVqjC4w&ab_channel=BestTechLearn

Run Code
python manage.py makemigrations songs
python manage.py migrate 
python manage.py runserver
control + C to stop the server

Using the Application
Visit: http://127.0.0.1:8000/api/songs

Enter the following JSON in to the POST box to create DB entry
{
    "name": "Adolescents",
    "artist": "Incubus",
    "quality": "Meditative",
    "timestamp": "00:00"
}    

Review the data
http://127.0.0.1:8000/api/songs/?id=1

set ID in the URL in order to send that URL parameter to the API.
