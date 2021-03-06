from tkinter import (
    Entry, Tk, Frame, Button, BOTH, Label
)
import controller
import util

root = Tk()
root.title("Scraping Apartment Prices")
root_width = root.winfo_screenwidth() - 15
root_height = root.winfo_screenheight() - 70
root.geometry("400x220")
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=True, pady=10)

label_head = Label(main_frame, text="Compute Price Changes")
label_head.grid(row=1, column=0, columnspan=2, pady=10, padx=20)
label_head.config(font=("helvetica", 16), fg="dark blue")

old_text = Label(main_frame, text="Old Filename")
old_text.grid(row=2, column=0, pady=10, padx=20)
old_text.config(font=("Arial", 14), fg="dark blue")
entry_old = Entry(main_frame, width=20, font=("Arial", 12))
entry_old.grid(row=2, column=1, pady=10, padx=20)

new_text = Label(main_frame, text="New Filename")
new_text.grid(row=3, column=0, pady=10, padx=20)
new_text.config(font=("Arial", 14), fg="dark blue")
entry_new = Entry(main_frame, width=20, font=("Arial", 12))
entry_new.grid(row=3, column=1, pady=10, padx=20)

button_compute = Button(
    main_frame, text="Calculate Inflation", width=25, bg='#3DC70D', fg='black',
    command=lambda: util.calculate_difference(entry_old.get(), entry_new.get()))
button_compute.grid(row=4, column=0, columnspan=2, pady=10, padx=20)
button_compute.bind("<Enter>", util.on_enter)
button_compute.bind("<Leave>", util.on_leave)
button_compute.configure(font=("arial", 12))

util.main()
controller.main()
root.mainloop()
