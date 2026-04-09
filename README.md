# AI Medical Image-to-Speech
A Python-based multimodal AI tool using Salesforce BLIP that uses computer vision to "see" medical objects and interprets them aloud. This project demonstrates the local inferencce of Multimodal Large Language Models (MLLMs). The project also implements the 'transformers' library to build a vision-to-text pipeline. It takes a local medical image file as input and processes it through a pre-trained transformer model to output a human-readable description, further reading the description aloud after the text-to-speech engine integration. 

**Tech Stack:**
- Language: Python
- Framework: Hugging Face Transformer
- Model: Salesforce BLIP
- Libraries: PIL (pillow), PyTorch, pyttsx3

**Features:**
- Vision engine: uses Salesforce BLIP to generate descriptive captions from provided images
- Medical logic: special lexicon filter that distinguishes between regular objects and medical objects
- Error handling: robust image verificating and exception handling
- Voice output: integerated with 'pyttsx3' library to generate text-to-speech feedback

**Future Improvements:**
- Integrate SQL Database for larger and more robust medical knowledge base.
- Generation of more elaborate descriptions based on relavant properties of the medical object (eg. function, usage, diseases associated with it etc.)
- Integrate confidence scoring and "Uncertainty Flags" to prevent the spread of medical misinformation.
- Domain-Specific Fine-Tuning by optimizing the MLLM on specialized medical datasets to improve accuracy for local pharmaceutical brands and equipment.
