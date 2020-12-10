from tkinter import *
import tkinter.messagebox


class Survivor(Frame):
    def __init__(self, master):
        self.master = master
        self.master.title('SURVIVOR')

        text.insert(INSERT, "This game is called Survivor. Throughout this game, you will be given scenarios."
                            "Each scenario will have two options to choose from in order to survive. Pick the right"
                            " options to survive until help arrives.")
        text.pack()

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        Frame.__init__(self, master)
        self.pack()

        self.QUIT = Button(self)
        self.START = Button(self)

        self.top_frame.pack()
        self.bottom_frame.pack()

        self.create_widgets()

    def create_widgets(self):
        self.QUIT = tkinter.Button(self.bottom_frame, text='Quit', command=self.quit)
        self.QUIT["fg"] = "red"

        self.START = tkinter.Button(self.bottom_frame, text='Start', command=self.start)
        self.START["fg"] = "blue"

        self.QUIT.pack(side="left")
        self.START.pack(side="left")

    def start(self):
        SceneOne(self.master)


class SceneOne(Frame):
    def __init__(self, master):
        self.master = master
        self.scene_one = tkinter.Toplevel(master)
        self.scene_one.title('Scenario One')

        self.top_frame = tkinter.Frame(self.scene_one)
        self.middle_frame = tkinter.Frame(self.scene_one)
        self.bottom_frame = tkinter.Frame(self.scene_one)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(0)

        text.insert(INSERT, "\n \nYour Oxygen mask appears in front of you, your friend sitting next to you begins"
                            " struggling with their mask, what do you do?")

        self.option_one = tkinter.Radiobutton(self.top_frame, text='Help friend with their Oxygen mask',
                                              variable=self.radio_var, value=1)
        self.option_two = tkinter.Radiobutton(self.top_frame, text='Worry about yourself and place your Oxygen mask on',
                                              variable=self.radio_var, value=2)

        self.option_one.pack(anchor='w', padx=20)
        self.option_two.pack(anchor='w', padx=20)

        self.quit = tkinter.Button(self.bottom_frame, text='Quit', command=self.quit)
        self.quit["fg"] = "red"

        self.next = tkinter.Button(self.bottom_frame, text='Next', command=self.next)
        self.next["fg"] = "blue"

        self.quit.pack(side="left")
        self.next.pack(side="left")

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        Frame.__init__(self, master)
        self.pack()

        self.quit = Button(self)
        self.next = Button(self)

    def next(self):
        if self.radio_var.get() == 1:
            text.insert(INSERT, "\n \nYou help your friend successfully put their mask on, however, "
                                "\nyour mask is no where to be found when you turn back around.  "
                                "\nYou die due to lack of oxygen.")
            self.scene_one.destroy()
        elif self.radio_var.get() == 2:
            SceneTwo(self.master)
            self.scene_one.destroy()

    def quit(self):
        self.scene_one.destroy()


class SceneTwo(Frame):
    def __init__(self, master):
        self.master = master
        self.scene_two = tkinter.Toplevel(master)
        self.scene_two.title('Scenario Two')

        self.top_frame = tkinter.Frame(self.scene_two)
        self.middle_frame = tkinter.Frame(self.scene_two)
        self.bottom_frame = tkinter.Frame(self.scene_two)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(0)

        text.insert(INSERT, "\n \nThe plane crashes into the ocean waters which causes you to briefly lose "
                            "\nconsciousness. As you awake, you find yourself sinking into the ocean. "
                            "\nThe remaining passengers who have survived the crash are yelling to any other "
                            "\nsurvivors to get on the raft.  As you begin to unbuckle your seatbelt, "
                            "\nyou notice the paddle for the raft being brought down with the rest of the plane"
                            "\nWhat do you do?")

        self.option_one = tkinter.Radiobutton(self.top_frame, text='Swim after the paddle and retrieve it to help '
                                                                   'you and other survivors return to civilization',
                                              variable=self.radio_var, value=1)
        self.option_two = tkinter.Radiobutton(self.top_frame, text='Inflate your life-jacket and swim out to the raft.',
                                              variable=self.radio_var, value=2)

        self.option_one.pack(anchor='w', padx=20)
        self.option_two.pack(anchor='w', padx=20)

        self.quit = tkinter.Button(self.bottom_frame, text='Quit', command=self.quit)
        self.quit["fg"] = "red"

        self.next = tkinter.Button(self.bottom_frame, text='Next', command=self.next)
        self.next["fg"] = "blue"

        self.quit.pack(side="left")
        self.next.pack(side="left")

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        Frame.__init__(self, master)
        self.pack()

        self.quit = Button(self)
        self.next = Button(self)

    def next(self):
        if self.radio_var.get() == 1:
            text.insert(INSERT, "\n \nYou obtain the paddle but never resurface in time, causing you to drown.")
            self.scene_two.destroy()
        elif self.radio_var.get() == 2:
            SceneThree(self.master)
            self.scene_two.destroy()

    def quit(self):
        self.scene_two.destroy()


class SceneThree(Frame):
    def __init__(self, master):
        self.master = master
        self.scene_three = tkinter.Toplevel(master)
        self.scene_three.title('Scenario Three')

        self.top_frame = tkinter.Frame(self.scene_three)
        self.middle_frame = tkinter.Frame(self.scene_three)
        self.bottom_frame = tkinter.Frame(self.scene_three)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(0)

        text.insert(INSERT, "\n \n12 hours later, your raft manages to be carried by the ocean currents to, "
                            "\nwhat appears to be, a nearby deserted island.  Storm clouds are approaching,"
                            "\nwhat is your first priority while reaching land?")

        self.option_one = tkinter.Radiobutton(self.top_frame, text='Find shelter',
                                              variable=self.radio_var, value=1)
        self.option_two = tkinter.Radiobutton(self.top_frame, text='Find source of water and food.',
                                              variable=self.radio_var, value=2)

        self.option_one.pack(anchor='w', padx=20)
        self.option_two.pack(anchor='w', padx=20)

        self.quit = tkinter.Button(self.bottom_frame, text='Quit', command=self.quit)
        self.quit["fg"] = "red"

        self.next = tkinter.Button(self.bottom_frame, text='Next', command=self.next)
        self.next["fg"] = "blue"

        self.quit.pack(side="left")
        self.next.pack(side="left")

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        Frame.__init__(self, master)
        self.pack()

        self.quit = Button(self)
        self.next = Button(self)

    def next(self):
        if self.radio_var.get() == 1:
            SceneFour(self.master)
            self.scene_three.destroy()
        elif self.radio_var.get() == 2:
            text.insert(INSERT, "\n \nWinds grow stronger, heavy rainfall suddenly appears,"
                                "\nyou and everyone else develop hypothermia and do not survive.")
            self.scene_three.destroy()

    def quit(self):
        self.scene_three.destroy()


class SceneFour(Frame):
    def __init__(self, master):
        self.master = master
        self.scene_four = tkinter.Toplevel(master)
        self.scene_four.title('Scenario Four')

        self.top_frame = tkinter.Frame(self.scene_four)
        self.middle_frame = tkinter.Frame(self.scene_four)
        self.bottom_frame = tkinter.Frame(self.scene_four)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(0)

        text.insert(INSERT, "\n \nYou make it through the first night on the island with the other survivors. "
                            "\nThe weather has cleared up and now you are able to search for food and water. "
                            "\nYou and another survivor decide to go fishing for the rest of the survivors.")

        self.option_one = tkinter.Radiobutton(self.top_frame, text='You happen to find a crab along the beach and'
                                                                   'decide to keep it for food.',
                                              variable=self.radio_var, value=1)
        self.option_two = tkinter.Radiobutton(self.top_frame, text='You find a stick with a sharp end to use as a'
                                                                   'harpoon.',
                                              variable=self.radio_var, value=2)

        self.option_one.pack(anchor='w', padx=20)
        self.option_two.pack(anchor='w', padx=20)

        self.quit = tkinter.Button(self.bottom_frame, text='Quit', command=self.quit)
        self.quit["fg"] = "red"

        self.next = tkinter.Button(self.bottom_frame, text='Next', command=self.next)
        self.next["fg"] = "blue"

        self.quit.pack(side="left")
        self.next.pack(side="left")

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        Frame.__init__(self, master)
        self.pack()

        self.quit = Button(self)
        self.next = Button(self)

    def next(self):
        if self.radio_var.get() == 1:
            text.insert(INSERT, "\n \nUnfortunately, the crab you found was poisonous and you do not survive.")
            self.scene_four.destroy()
        elif self.radio_var.get() == 2:
            SceneFive(self.master)
            self.scene_four.destroy()

    def quit(self):
        self.scene_four.destroy()


class SceneFive(Frame):
    def __init__(self, master):
        self.master = master
        self.scene_five = tkinter.Toplevel(master)
        self.scene_five.title('Scenario Five')

        self.top_frame = tkinter.Frame(self.scene_five)
        self.middle_frame = tkinter.Frame(self.scene_five)
        self.bottom_frame = tkinter.Frame(self.scene_five)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(0)

        text.insert(INSERT, "\n \nHarpooning fish was not as easy as you thought it would be, but after many hours of"
                            "\nfishing, you and your fellow fisher manage to get enough fish for the rest of the camp."
                            "\nWhile away, the others have found a clean water source and have managed to build a fire."
                            "\nOne of them tells you they heard some noises in the jungle as they were looking for"
                            "\nwater.")

        self.option_one = tkinter.Radiobutton(self.top_frame, text='You decide to ignore them and tell them it was'
                                                                   'just their imagination.',
                                              variable=self.radio_var, value=1)
        self.option_two = tkinter.Radiobutton(self.top_frame, text='You decide to investigate what the noise could be.',
                                              variable=self.radio_var, value=2)

        self.option_one.pack(anchor='w', padx=20)
        self.option_two.pack(anchor='w', padx=20)

        self.quit = tkinter.Button(self.bottom_frame, text='Quit', command=self.quit)
        self.quit["fg"] = "red"

        self.next = tkinter.Button(self.bottom_frame, text='Next', command=self.next)
        self.next["fg"] = "blue"

        self.quit.pack(side="left")
        self.next.pack(side="left")

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        Frame.__init__(self, master)
        self.pack()

        self.quit = Button(self)
        self.next = Button(self)

    def next(self):
        if self.radio_var.get() == 1:
            text.insert(INSERT, "\n \nWhile relaxing from your long day of fishing, "
                                "\nyou were bitten by a poisonous spider and do not survive.")
            self.scene_five.destroy()
        elif self.radio_var.get() == 2:
            text.insert(INSERT, "\n \nAfter investigation, you find tourists and hear loud music playing."
                                "\nYou realize that the island isn't deserted and you're actually on the island "
                                "\nthat's part of Hawaii, called Maui.  Congratulations, you survived!"
                                "\n#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#"
                                "\n%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%"
                                "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

    def quit(self):
        self.scene_five.destroy()


root = tkinter.Tk()
text = Text(root)
app = Survivor(master=root)
app.mainloop()
root.destroy()
