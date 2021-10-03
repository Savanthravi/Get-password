from tkinter import *
App = Tk()
acc = Entry(App)
acc.pack()
def pass_find():
  dt = {
    'google':'1234',
    'insta':'3456',
    'facebook':'5678'
  }
  accont = acc.get()
  password = dt[account]
  ps = Label(App, text = password)
  ps.pack()
B = Button(
  App,
  text = 'get password',
  command = pass_find
  )
B.pack()
App.mainloop()