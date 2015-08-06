# django-csrftoken
Here is my Confused about django csrftoken

When I test django csrftoken, I found this problem

pls download this project and run it

    python manage.py runserver

And then open localhost:8000 in your browser

The defalut page dose not have csrf_token which means I didn't add `{% csrf_token %}` in the page

When you click post test button , it will show 403

When you click set cookie button , it will run this command `document.cookie = "csrftoken=bbbbbb";`

Then you click post test button , it will be success!

Why does django did NOT verify the csrftoken ???? 
