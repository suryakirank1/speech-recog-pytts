mport speech_recognition as sr
import pyttsx3

class PronunciationNode:
    def __init__(self, pronunciation, next_node=None):
        self.pronunciation = pronunciation
        self.next_node = next_node

class PronunciationList:
    def __init__(self):
        self.head = None

    def add_pronunciation(self, pronunciation):
        new_node = PronunciationNode(pronunciation)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def display_pronunciations(self):
        pronunciations = []
        current = self.head
        while current:
            pronunciations.append(current.pronunciation)
            current = current.next_node
        return pronunciations

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next_node
            current.next_node = prev
            prev = current
            current = next_node
        self.head = prev

    def count_pronunciations(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_node
        return count

    def remove_duplicates(self):
        unique_pronunciations = set()
        current = self.head
        prev = None
        while current:
            if current.pronunciation in unique_pronunciations:
                prev.next_node = current.next_node
            else:
                unique_pronunciations.add(current.pronunciation)
                prev = current
            current = current.next_node

    def delete_pronunciation(self, pronunciation):
        current = self.head
        prev = None
        while current:
            if current.pronunciation == pronunciation:
                if prev:
                    prev.next_node = current.next_node
                else:
                    self.head = current.next_node
                return
            prev = current
            current = current.next_node

    def update_pronunciation(self, old_pronunciation, new_pronunciation):
        current = self.head
        while current:
            if current.pronunciation == old_pronunciation:
                current.pronunciation = new_pronunciation
                return
            current = current.next_node


def recognize_speech(audio):
    recognizer = sr.Recognizer()

    try:
        text = recognizer.recognize_google(audio)
        print(f"Recognized text: {text}")
        return text.split()  # Split the recognized text into words
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio")
        return []

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def practice_pronunciation(sentence):
    recognizer = sr.Recognizer()
    pronunciation_list = PronunciationList()
    words = sentence.split()

    for word in words:
        for i in range(1):  # Capture audio once for each word
            with sr.Microphone() as mic:
                print(f"\nAttempt {i + 1}: Say the word '{word}':")
                recognizer.adjust_for_ambient_noise(mic, duration=0.5)
                recognizer.timeout = 0.1
                audio = recognizer.listen(mic)
                pronunciations = recognize_speech(audio)

            for pronunciation in pronunciations:
                pronunciation_list.add_pronunciation(pronunciation)

    print("\nOriginal Pronunciations:")
    print(pronunciation_list.display_pronunciations())

    # Additional linked list functions
    pronunciation_list.reverse_list()
    print("\nReversed Pronunciations:")
    print(pronunciation_list.display_pronunciations())

    print(f"\nTotal Pronunciations: {pronunciation_list.count_pronunciations()}")

    pronunciation_list.remove_duplicates()
    print("\nPronunciations without Duplicates:")
    print(pronunciation_list.display_pronunciations())

    # Provide feedback using text-to-speech
    feedback_text = f"You pronounced the sentence: '{sentence}'. Try to pronounce it in reverse: {pronunciation_list.display_pronunciations()}"
    text_to_speech(feedback_text)

    # Delete a pronunciation
    pronunciation_to_delete = input("Enter the pronunciation to delete: ")
    pronunciation_list.delete_pronunciation(pronunciation_to_delete)
    print(f"\nPronunciations after deleting '{pronunciation_to_delete}':")
    print(pronunciation_list.display_pronunciations())

    # Update a pronunciation
    old_pronunciation = input("Enter the old pronunciation to update: ")
    new_pronunciation = input("Enter the new pronunciation: ")
    pronunciation_list.update_pronunciation(old_pronunciation, new_pronunciation)
    print(f"\nPronunciations after updating '{old_pronunciation}' to '{new_pronunciation}':")
    print(pronunciation_list.display_pronunciations())

if __name__ == "__main__":
    sentence_to_practice = input("Enter a sentence to practice pronunciation: ")
    practice_pronunciation(sentence_to_practice)
#STEP 1: download the latest version of python software from chrome --> install it 
#STEP 2:there are several libraries which has to be installed:gTTS,packaging, pipwin ,. PyAudio,. pyttsx3 ,pypiwin32,setuptools(update setuptools also),. SpeechRecognition 
#STEP 3: to download in vscode terminal use= pip install "your package name"    In my opinion vscode terminal is best to install all these python packages
#you need to watch many tutorials online this stuff is complex at first, needs good skills in command prompt(to install python libraries) 
#use pip list to check whatevs you have installed
