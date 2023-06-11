import speech_recognition as sr
import pyttsx3
import tkinter as tk
import PySimpleGUI as sg


from tkinter import messagebox

from autocorrect import Speller
# Initialize speech recognition and synthesis
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def print_to_window(window, text):
    # This is the normal print that comes with simple GUI
    sg.Print('', do_not_reroute_stdout=False)

    # this is clobbering the print command, and replacing it with sg's Print()
    print = sg.Print

    # this will now output to the sg display.
    print(text)
    # # Create a canvas to draw on the window
    # canvas = tk.Canvas(window, width=window.winfo_width(), height=window.winfo_height(), bg="light blue",
    #                    highlightthickness=0)
    # canvas.pack()
    # canvas.create_text(window.winfo_width() / 2, window.winfo_height() / 2, text=text, font=("Arial", 12), fill="black")


# def print_to_window(window, text):
#     canvas = tk.Canvas(window, width=window.winfo_width(), height=window.winfo_height(), bg="light blue", highlightthickness=0)
#     canvas.pack()
#     canvas.create_text(window.winfo_width() / 2, window.winfo_height() / 2, text=text, font=("Arial", 12), fill="black")

# def print_to_window(window,text):
#     label=tk.Label(window,text=text)
#     label.configure(text=text)
#     label.pack()
# def print_to_label(label_widget, text):
#     label_widget.configure(text=text)




# Function to convert text to speech
def speak(window,text):
    print_to_window(window,text)
    engine.setProperty('rate', 150)  # Adjust the speech rate as needed
    engine.say(text)
    engine.runAndWait()


# Function to listen for user input
# def listen():
#     try:
#         with sr.Microphone() as source:
#             recognizer.adjust_for_ambient_noise(source, duration=0.2)
#             audio = recognizer.listen(source)
#             text = recognizer.recognize_google(audio)
#             text =text.lower()
#             words = text.split()
#             corrected_text = []
#             for word in words:
#                 corrected_word = spell.correction(word)
#                 corrected_text.append(corrected_word)
#             corrected_text = " ".join(corrected_text)
#             return corrected_text
#
#     except sr.UnknownValueError:
#         print("Speech recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))
#         return None
def listen():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Listening...")


            audio = r.listen(source, timeout=None)

        recognized_text = r.recognize_google(audio)
        print("Recognized Text:", recognized_text)

        # Perform autocorrection on recognized text
        spell = Speller(lang='en')
        corrected_text = spell(recognized_text).split()

        if corrected_text:
            return " ".join(corrected_text)
        else:
            return None
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio, try again")
        return listen()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None
    except KeyboardInterrupt:
        print("Program interrupted by user")
        return None



def asthma(window,concius):
    speak(window,"any improvement?")
    text = listen()
    if "yes" in text:
        if concius == "danger":
            speak(window,"During the evacuation, give repeated inhalations of Ventolin + Irovant")
            return
        if concius == "severe" or "easy":
            speak(window,"Continue monitoring and treatment while being evacuated to the hospital")
    else:
        if "no" in text:
            if concius == "danger":
                speak(window,"Consider respiratory support using CPAP")
            if concius == "severe":
                speak(window,
                    "During the evacuation, give repeated inhalations of Ventolin + Irovant. Consider giving magnesium sulfate")
            if concius == "easy":
                speak(window,
                    "During evacuation, give another ventolin inhalation. Give IV solomedrol if were not already given")

    return


def start_body_check(window,):
    speak(window,"perform body check: provide number of Breaths in a minute, tachycardia, Storation...")
    text = listen()
    condition=None
    if ("shortness of breath at rest" or ("storation" or "91")) in text:
        speak(window,"this is severe Asthma attack")
        speak(window,"Give Ventolin inhalation + Irovant. give IV solomedrol. Consider giving adrenaline")
        condition = "severe"

    if (("shortness of breath" or "cant breath") and "exertion") and "storation is 95" in text:
        speak(window,"easy/medium Asthma attack")
        condition = "easy"
        speak(window,"Give Ventolin inhalation + Irovant. Consider giving IV solomedrol")

    if "cant talk" in text:
        speak(window,"danger! a threatening cessation of breathing")
        condition = "danger"
        speak(window,"Give Ventolin inhalation + Irovant. give IV solomedrol. give adrenaline")
    asthma(condition,condition)


# Function to handle emergency instructions
def handle_emergency(window):
    # Gather information from the user
    speak(window,"give details about the event, ")
    emergency = listen()
    print(emergency)
    concius = "conscious"

    # the patient is unconsios, he was coughing and experianced Difficulty breathing

    if "unconscious" in emergency:
        concius = "unconscious"
    if ("cough" or "coughing") in emergency:
        Suspected_foreign_body_suffocation(window,concius)

    if "breath" in emergency:
        start_body_check(window)


# Call the function to start the resuscitation guidance
def Suspected_foreign_body_suffocation(window, concius):
    speak(window,"it is possible that the patient is suffocating")
    if "unconscious" in concius:
        speak(window,"perform 30 chest compressions and 2 breaths")
    else:
        speak(window,"encourage cough")
        speak(window,"is there any improvement?")
        ans = listen()
        if "yes" in ans:
            speak(window,
                "keep the patient sitting while evacuating to the nearest hospital and continue to monitor and treat during the evacuation. Consider transferring a report to the hotline/hospital")
            return
        else:
            if "no" in ans:
                speak(window,"perform Heimlich maneuver or abdominal presses")
    speak(window,"any improvement?")
    ans = listen()
    if "yes" in ans:
        speak(window,
            "keep the patient sitting while evacuating to the nearest hospital and continue to monitor and treat during the evacuation. Consider transferring a report to the hotline/hospital")
        return
    speak(window,
        "Continue performing the Heimlich maneuver/abdominal presses. Consider performing a laryngoscopy. Continue monitoring")
    return


# Main function
def main(window):
    # Start the app and listen for voice command
    # Create a text widget to display the chatbot responses
    # text_widget = tk.Text(window, width=50, height=20, font=("Arial", 12))
    # text_widget.pack()
    handle_emergency(window)


if __name__ == '__main__':
    main()
