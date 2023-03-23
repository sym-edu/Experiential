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
course_data = {
    "course_name": "Python Basics",
    "course_code": "PYB101",
    "course_description": "Learn the basics of Python programming",
    "duration": "6 weeks",
    "cost": "$100",
    "ages": "18+",
    "video_lesson" : 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    'presentation':'https://www.canva.com/design/DAFPHNW7IqY/saS1gdkdzIwF8la29JyfOw/edit?utm_content=DAFPHNW7IqY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton',
    "written_assessment":'temp',
    "oral_assessment"   :'https://github.com/sym-edu/XP-Core-API',
    "quiz_questions": [
  {
    "question_text": "What is the capital of France?",
    "options": [
      {
        "answer_text": "Paris",
        "is_correct": True
      },
      {
        "answer_text": "London",
        "is_correct": False
      },
      {
        "answer_text": "Madrid",
        "is_correct": False
      },
      {
        "answer_text": "Berlin",
        "is_correct": False
      }
    ]
  }
]

}




course_response = session.post('http://127.0.0.1:8000/authentication/add_course/', json=course_data, headers={
    'X-CSRFToken': csrftoken,
    'Content-Type': 'application/json'
})


# print(course_response.json())
# print(course_response.status_code)

course_data = {
    "course_name": "Python Basics",
    "course_code": "PYB101",
    "course_description": "Learn the basics of Python programming",
    "duration": "6 weeks",
    "cost": "$100",
    "ages": "18+",
    "video_lesson" : 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    'presentation':'https://www.canva.com/design/DAFPHNW7IqY/saS1gdkdzIwF8la29JyfOw/edit?utm_content=DAFPHNW7IqY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton',
    "quiz_questions": [
        {
            "question_text": "What is the output of print(2 + 3 * 4 - 1)?",
            "options": [
                {"answer_text": "9", "is_correct": False},
                {"answer_text": "14", "is_correct": True},
                {"answer_text": "15", "is_correct": False},
                {"answer_text": "19", "is_correct": False}
            ]
        },
        {
            "question_text": "Which of the following is NOT a Python data type?",
            "options": [
                {"answer_text": "int", "is_correct": False},
                {"answer_text": "str", "is_correct": False},
                {"answer_text": "bool", "is_correct": False},
                {"answer_text": "char", "is_correct": True}
            ]
        }
    ],
    "written_assessment":'temp',
    "oral_assessment"   :'https://github.com/sym-edu/XP-Core-API'
}


course_response = session.post('http://127.0.0.1:8000/authentication/add_course/', data=course_data, headers={
    'X-CSRFToken': csrftoken
})
print(course_response.json())
print(course_response.status_code)
