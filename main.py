
import speech_recognition as sr
import openai

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)


try:
    
    print( r.recognize_google(audio,show_all=True)["alternative"][0]["transcript"])
   
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


openai.api_key = "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"
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=r.recognize_google(audio,show_all=True)["alternative"][0]["transcript"],
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
message = response.choices[0]["text"]

print(message)