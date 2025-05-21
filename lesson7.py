'''
def counter():

    yield 1
    yield 3
    yield 2
gen = counter()
print(next(gen))
print(next(gen))
print(next(gen))
'''

'''
def counter(start=1):
    while start >0:
        yield start
        start -= 1
for i in counter(5):
    print(i)
'''
'''
def counter(start=0):
    count = start
    def next_number(step=1):
        nonlocal count
        count += step
        return count
    return next_number()
counter = counter
print(counter(5))'''
import tkinter as tk
def counter(start):
    while start >=0:
        yield start
        start -= 1
start_time = 60
counter = counter(start_time)


'''def update():
    try:
        time_left = next(counter)
        label.config(text=f'Залишилось: {time_left}')
        root.after(1000, update)
    except StopIteration:
        label.config(text= 'Час вийшов!!!')


root = tk.Tk()
root.title('Timer')
label = tk.Label(root, font=('Helvetica', 24), fg='blue')
label.pack(padx =20, pady = 20)

update()
root.mainloop()
'''

#







def safe_input(func):
    