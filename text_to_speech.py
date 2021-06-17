# THIS CODE BY THUNDERBOLT

# HERE IS IMPORT PART
from gtts import gTTS
import os

# HERE WE START THE CODE
theText = "Hello World" 

# HERE IS THE SUPPORTED LANGUGE
language = 'en'

# HERE IS THE OUTPUT
output = gTTS(text=(theText), lang=(language), slow=False)
output.save("helloworld.mp3")
os.system("start helloworld.mp3")
