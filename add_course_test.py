import requests

# set up session for login
session = requests.Session()

# login
login_data = {
    'username': 'bbb',
    'password': 'mypassword'
}

login_response = session.post('http://127.0.0.1:8000/authentication/login/', data=login_data, headers={'Referer': 'http://127.0.0.1:8000/authentication/login/'})

csrftoken = login_response.cookies['csrftoken']
# login_response = session.post(, data=login_data)
print(login_response.json())
# add course

url = 'http://127.0.0.1:8000/authentication/add_course/'

course_data = {
    "course_name": "Sample Course",
    "course_code": "SC001",
    "course_description": "This is a sample course",
    "duration": "2 weeks",
    "cost": "Free",
    "ages": "18+",
    "video_lesson": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "presentation": "https://www.canva.com/sample-presentation-link",
    "quiz_questions": [
        {
            "question_text": "What is the capital of India?",
            "answer_options": [
                {"answer_text": "New Delhi", "is_correct": True},
                {"answer_text": "Mumbai", "is_correct": False},
                {"answer_text": "Chennai", "is_correct": False},
                {"answer_text": "Kolkata", "is_correct": False}
            ]
        },
        {
            "question_text": "What is the largest mammal in the world?",
            "answer_options": [
                {"answer_text": "Blue whale", "is_correct": True},
                {"answer_text": "Elephant", "is_correct": False},
                {"answer_text": "Giraffe", "is_correct": False},
                {"answer_text": "Hippopotamus", "is_correct": False}
            ]
        },
        {
            "question_text": "Who is the founder of Microsoft?",
            "answer_options": [
                {"answer_text": "Steve Jobs", "is_correct": False},
                {"answer_text": "Bill Gates", "is_correct": True},
                {"answer_text": "Elon Musk", "is_correct": False},
                {"answer_text": "Jeff Bezos", "is_correct": False}
            ]
        },
        {
            "question_text": "What is the largest organ in the human body?",
            "answer_options": [
                {"answer_text": "Skin", "is_correct": True},
                {"answer_text": "Liver", "is_correct": False},
                {"answer_text": "Heart", "is_correct": False},
                {"answer_text": "Brain", "is_correct": False}
            ]
        },
        {
            "question_text": "What is the formula for water?",
            "answer_options": [
                {"answer_text": "H2O2", "is_correct": False},
                {"answer_text": "HO2", "is_correct": False},
                {"answer_text": "H2O", "is_correct": True},
                {"answer_text": "H3O", "is_correct": False}
            ]
        }
    ],
    "written_assessment": "This is a sample written assessment",
    "oral_assessment": "https://drive.google.com/sample-audio-link"
}

response = requests.post(url, data=course_data, headers={'Referer': url})

print(response.json())
