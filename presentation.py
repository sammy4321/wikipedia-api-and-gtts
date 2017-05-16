import Tkinter
import wikipedia
from gtts import gTTS
import os
def button_clicked():
	entered_string=search_box.get()
	result=wikipedia.summary(entered_string,sentences=2)
	tts=gTTS(text=result,lang="en")
	tts.save("result.mp3")
	os.system("mpg321 result.mp3")


window=Tkinter.Tk()
window.geometry('%dx%d+%d+%d'%(300,60,600,350))
window.wm_title("Wikipedia API & STT")

find_button=Tkinter.Button(window,text="Find",command=button_clicked)
find_button.place(x=240,y=15)
search_box=Tkinter.Entry(window,width=25)
search_box.place(x=10,y=18)



window.mainloop()
