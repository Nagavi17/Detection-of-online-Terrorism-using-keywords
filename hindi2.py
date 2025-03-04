# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 20:53:29 2023

@author: nagavi
"""

import json
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle

class MyApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        menu = tk.Menu(container)

        ex = tk.Menu(menu, tearoff=0)
        menu.add_cascade(menu=ex, label="Exit")
        ex.add_command(label="Exit",
                   command=self.destroy)

      
        
        tk.Tk.config(self, menu=menu)

        for F in (Startpage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Startpage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



class Startpage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Detection of Online Terrorism",font=("Simplifica",22))         # page heading
        label.pack(pady=5, padx=5)

        ttk.Label(self,text="").pack()

        button1 = ttk.Button(self, text="Detect",                           
                        command=lambda: controller.show_frame(PageOne))     # got to detect page
        button1.pack()

        ttk.Label(self,text="").pack()

        button2 = ttk.Button(self, text="About",
                        command=lambda: controller.show_frame(PageTwo))     # got to about page
        button2.pack()

        ttk.Label(self,text="").pack()

        img=ImageTk.PhotoImage(Image.open(r'C:/Users/PC/engg proj/wallpaper.jpg').resize((1200,700)))   # set the home page image
        img.image = img
        ttk.Label(self,image=img).pack()
        # ... (rest of the code)

class PageOne(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Detect",font=("Simplifica",22))       # page heading
        label.pack(pady=5, padx=5)

        ttk.Label(self,text="\n").pack()

        ttk.Label(self,text="Enter a webpage",font=(18)).pack()     
        text = tk.Entry(self,font=(26),width=70,bg="lightgray")             # textbox to enter a website
        text.pack()

        ttk.Label(self,text="").pack()

        # ... (rest of the code)

        # load the file containing Hindi keywords
        j = []
        f = open(r'C:/Users/PC/engg proj/keywords2.txt', encoding='utf-8')
        for line in f:
            j.append(line.strip())
        f.close()
        d = dict.fromkeys(j, 0)

        # ... (rest of the code)
        def scan():
            count=0
            url = text.get()
            text.delete(0,"end")
            result = requests.get(url.strip())
            soup = BeautifulSoup(result.content, 'lxml')
            for i in soup.get_text().split():
                if(i.lower()in j):
                    count+=1
                    if i.lower() in d:
                        d[i.lower()] +=1
            l3.config(state=tk.NORMAL)
            l3.delete('1.0',"end")
            di = dict(sorted(d.items(),reverse=True, key=lambda item: item[1]))
            lis = [(k,v) for k,v in di.items() if v >= 1]
            output_text = f"{url.strip()} = {count}\n\n keywords matched\n"
            for keyword, keyword_count in lis:
                output_text += f"{keyword} = {keyword_count}\n"
            l3.insert(tk.END, output_text)
                


        b2=ttk.Button(self,text="Scan",command= scan)
        b2.pack()

        def open_n_scan():
            files = askopenfile(mode='r', filetypes=[("Text File", "*.txt")])
            l3.config(state=tk.NORMAL)
            l3.delete('1.0', "end")
            for url in files:
                count = 0
                result = requests.get(url.strip())
                soup = BeautifulSoup(result.content, 'lxml')
                for i in soup.get_text().split():
                    if(i.lower()in j):
                        count+=1
                l3.insert(tk.END,url.strip()+" = "+str(count)+"\n")
            l3.config(state=tk.DISABLED)

        ttk.Label(self,text="Select your text file containing urls",font=(18)).pack()

        b1=ttk.Button(self,text="Open and Scan",command= open_n_scan)
        b1.pack()

        ttk.Label(self,text="").pack()

        l3=scrolledtext.ScrolledText(self,font=(18),height=10,width=70,bg="lightgray",state=tk.DISABLED)       # multiline textbox
        l3.pack()

        ttk.Label(self,text="").pack()

        button1 = ttk.Button(self, text="Back to Home",
                        command=lambda: controller.show_frame(Startpage))                           # go to home page
        button1.pack()

        ttk.Label(self,text="").pack()

        button2 = ttk.Button(self, text="About",
                        command=lambda: controller.show_frame(PageTwo))                             # got to about page
        button2.pack()


        # ... (rest of the code)

class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="About",font=("Simplifica",22))                    # page heading
        label.pack(pady=5, padx=5)

        ttk.Label(self,text="").pack()

        button1 = ttk.Button(self, text="Back to Home",
                        command=lambda: controller.show_frame(Startpage))               # got to home page
        button1.pack()

        ttk.Label(self,text="").pack()

        button2 = ttk.Button(self, text="Detect",
                        command=lambda: controller.show_frame(PageOne))                 # got to detect page
        button2.pack()

        ttk.Label(self,text="").pack()

        tk.Message(self,relief="sunken",bd=4,font=(20),width=1100,text="Terrorism is, in the broadest sense, the use of intentional violence for political or religious purposes. It is used in this regard primarily to refer to violence during peacetime or in the context of war against non-combatants (mostly civilians and neutral military personnel). The terms terrorist and terrorism originated during the French Revolution of the late 18th century but gained mainstream popularity in the 1970s during the conflicts of Northern Ireland, the Basque Country and Palestine. The increased use of suicide attacks from the 1980s onwards was typified by the September 11 attacks in New York City and Washington, D.C. in 2001.").pack()
                                                                                        # Info on terrorism
        ttk.Label(self,text="").pack()

        tk.Message(self,relief="sunken",bd=4,font=(20),width=1100,text="Cyberterrorism is the use of the Internet to conduct violent acts that result in, or threaten, loss of life or significant bodily harm, in order to achieve political or ideological gains through threat or intimidation. It is also sometimes considered an act of Internet terrorism where terrorist activities, including acts of deliberate, large-scale disruption of computer networks, especially of personal computers attached to the Internet by means of tools such as computer viruses, computer worms, phishing, and other malicious software and hardware methods and programming scripts. Cyberterrorism is a controversial term.").pack()
                                                                                        # Info on cyberterrorism
        ttk.Label(self,text="").pack()

        tk.Message(self,relief="sunken",bd=4,font=(20),width=1100,text="We use web mining algorithms to mine textual information on web pages and detect their relevancy to terrorism. This system will check web pages whether a webpage is promoting terrorism. Data mining is a technique used to mine out patterns of useful data from large data sets and make the most use of obtained results. Web mining also consists of text mining methodologies that allow us to scan and extract useful content from unstructured data.").pack()
                                                                                        # About
        ttk.Label(self,text="").pack()

        ttk.Label(self,text="© Sushma , Nagavi , ShreeGanesha & Yashwanth",font=(20)).pack()                        # copyright


app = MyApp()

# set default app theme
style = ThemedStyle(app)
style.set_theme("plastik")

# set app icon
icon = ImageTk.PhotoImage(Image.open(r'C:/Users/PC/engg proj/icon.jpg'))
app.iconphoto(True,icon)

app.resizable(0,0)
app.title("Detect Terrorism")                                                           # app title
app.state('zoomed')                                                                     # maximized app by default
app.mainloop()

        # ... (rest of the code)
