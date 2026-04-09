import sys
from transformers import pipeline
from PIL import Image
import pyttsx3 

engine=pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

captioner= pipeline("image-text-to-text", model="Salesforce/blip-image-captioning-base")

def genMedCaption(image_path):
    try:
        img=Image.open(image_path).convert('RGB')
        print("Analysing Medical Content...")
        
        result=captioner(img, text="")
        caption= result[0]['generated_text']
        
        med_Arr=[
            "medicine", "medical", "doctor", "physician", "hospital", "clinic", "patient",
            "healthcare", "treatment", "diagnosis", "prescription", "pharmacy",
            
            "pill", "tablet", "capsule", "syrup", "injection", "vaccine", "ointment", "dose",
            "medication", "antibiotic", "vial", "bottle", "drug",
            
            "stethoscope", "thermometer", "syringe", "bandage", "gauze", "mask", "gloves",
            "scalpel", "iv", "monitor", "x-ray", "mri", "scan", "microscope", "lab",
            
            "fever", "cough", "pain", "blood", "heart", "lungs", "brain", "injury", "wound"
        ]
        
        if any(word in caption.lower() for word in med_Arr):
            final= f"Verified: MEDICAL OBJECT DETECTED. It is {caption}."
        else:
            final=f"Observation: {caption}. Note that this does not appear to be a medical item."
        return final
        
    except Exception as e:
        return f"Error: {e}"
    
if __name__=="__main__":
    image_file="mri machine.jpg"
    description=genMedCaption(image_file)
    print(f"\nResult: {description}")
    speak(description)
    