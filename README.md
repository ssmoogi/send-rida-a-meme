# send-rida-a-meme
a surprise 💖✨

### overview
This is a simple web app built using Flask and the [Twilio API](https://www.twilio.com/docs/usage/api) to send random memes by text to someone, in this case, Rida :)

### how to run
1. fork and clone this repo
2. install dependencies using poetry into a virtual env
3. create a .env file and set the following variables
  * ENTER_KEY = (your desired password)
  * SENDER_PHONE = (twilio phone number)
  * RIDA_PHONE = (phone number to send memes to)
  * ACCOUNT_SID = (twilio account sid)
  * AUTH_TOKEN = (twilio auth token)
4. set environment variable FLASK_APP to main.py
5. change the memes in static/images/memes and the items in meme_list in main.py
6. in the send function, change the link to your own github repo or somewhere where your images can be found online since the twilio api requires a http or https link
7. run using the terminal or host it somewhere (ex. repl.it)
8. have a good laugh 😁💖✨
