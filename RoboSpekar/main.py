import pyttsx3                                    # # import module to recognize as speech 

if  __name__ == "__main__":

    print("welcome to speech recognize system through input  created by J")

    while True:

        speech = input('enter the sppech you want to speak :')
        if speech.lower() == "q":
            engine.say("bye bye friend to everyone")
            engine.runAndWait()
            break

        engine =pyttsx3.init()                  # initilize object for it

        engine.say(speech)

        # Wait for the speech to finish
        engine.runAndWait()








#
#
#     # engine.setProperty('rate', 125)  # Speed to speech speed it is optional
#
#     # Speak the given text
#     engine.say(text_to_speak)
#
#     # Wait for the speech to finish
#     engine.runAndWait()
