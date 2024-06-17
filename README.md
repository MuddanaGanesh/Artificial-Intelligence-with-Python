# Artificial-Intelligence-with-Python
Welcome to the "AI Assistant" repository, featuring a voice-controlled AI assistant built with Python. This versatile assistant can handle various tasks, including telling the current time and date, searching Wikipedia, taking screenshots, sending emails, playing YouTube videos, sending WhatsApp messages, and much more. The following sections provide a detailed breakdown of each function in the code to enhance your understanding of its functionality.
The primary file in this repository is ai.py, which implements the core functionality of the AI Assistant. Below is an overview of the functions and their purposes:

Main Loop
The main loop continuously listens for voice commands and executes the corresponding actions. It can provide the current time and date, search Wikipedia for information, capture screenshots, send emails, play YouTube videos, send WhatsApp messages, perform web searches, remember information, control music playback, shut down or restart the computer, and handle unrecognized commands by querying an AI model for responses.

Functions
The speak(audio) function uses the pyttsx3 library to convert text to speech. It takes a string audio and vocalizes it.
The time() function announces the current time by using the datetime library to fetch the time and the speak function to read it out loud.
The date() function announces the current date by using the datetime library to fetch the date and the speak function to read it out loud.
The youtube(ele) function plays a YouTube video using the pywhatkit library to search and play the specified video.
The chrome(ele) function performs a web search using Chrome with the pywhatkit library.
The whatsapp(t, msg) function sends a WhatsApp message using the pywhatkit library to the specified number t with the message msg.
The sendmail(to, msg) function sends an email using SMTP. It logs into a Gmail account and sends an email to the recipient to with the message msg.
The wish() function greets the user based on the time of day. It uses the datetime library to determine the appropriate greeting and the speak function to deliver it.  
The inp() function listens for voice input using the speech_recognition library, capturing and recognizing speech, and returning the recognized text.
The screenshot() function takes a screenshot using the pyscreeze library to capture and save the screen image.
The talktoai(query) function sends a query to an AI model for a response. It uses the requests library to send a request to an AI service and then speaks the response using the speak function.

Additional Components
The authorization header, stored in the headers variable, contains an authorization token for accessing the AI service. The AI service URL is specified by the url variable, which indicates the endpoint used in talktoai. The wikipedia library is utilized to search for and summarize articles. The sample module includes functions to play and control music, which are invoked in the main loop.

Requirements
This project requires Python 3.x and the following libraries: pyttsx3, datetime, speech_recognition, wikipedia, pyautogui, pyscreeze, json, requests, openai, pywhatkit, smtplib, sample, and os.

