import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import configparser


def launch_program():
    ExpLuxNumber = ExpLux_combobox.get()
    ExpLuxValue = ExpLuxV_entry.get()
    ThreadLuxNumber = ThreadLux_combobox.get()
    ThreadLuxValue = ThreadLuxV_entry.get()
    ExpLuxDamage = ExpLuxD_var.get()
    ThreadLuxDamage = ThreadLuxD_var.get()

    config = configparser.ConfigParser()
    config['LuxParameters'] = {
        'ExpLuxcavationNumber': ExpLuxNumber,
        'ExpLuxcavationValue': ExpLuxValue,
        'ExpLuxcavationDamage': ExpLuxDamage,
        'ThreadLuxcavationNumber': ThreadLuxNumber,
        'ThreadLuxcavationValue': ThreadLuxValue,
        'ThreadLuxcavationDamage': ThreadLuxDamage
    }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    # Относительный путь к исполняемому файлу
    exe_path = "./your_program.exe"

    # Формируем команду для запуска программы с дополнительными параметрами
    command = f"{exe_path} {ExpLuxNumber} {ExpLuxValue} {ThreadLuxNumber} {ThreadLuxValue}"

    # Запускаем программу
    messagebox.showinfo("Launch", "Program launched with the selected parameters.")
    # subprocess.Popen(command, shell=True)


# Создание основного окна
root = tk.Tk()
root.title("Launcher")
root.geometry("640x360")
root.resizable(False, False)
root.attributes("-toolwindow", True)

#logo_image = tk.PhotoImage(file="logo.png")
#logo_label = tk.Label(master, image=self.logo_image)
#logo_label.pack(pady=50)


ExpLux_label = ttk.Label(root, text="ExpLuxcavation:")
ExpLux_label.grid(row=0, column=0, pady=10)
ExpLux_values = ["Stage 01 - 8 LV", "Stage 02 - 18 LV", "Stage 03 - 28 LV", "Stage 04 - 33 LV", "Stage 05 - 38 LV", "Stage 06 - 43 LV"]
ExpLux_combobox = ttk.Combobox(root, values=ExpLux_values)
ExpLux_combobox.grid(row=0, column=1)

ExpLuxV_entry = ttk.Entry(root)
ExpLuxV_entry.grid(row=0, column=3)

ExpLuxD_var = tk.BooleanVar()
ExpLuxD_label = ttk.Checkbutton(root, text="Damage", variable=ExpLuxD_var)
ExpLuxD_label.grid(row=0, column=4, columnspan=2, pady=10)

ThreadLux_label = ttk.Label(root, text="ThreadLuxcavation")
ThreadLux_label.grid(row=1, column=0, pady=10)
ThreadLux_values = ["Stage 01 - 20 LV", "Stage 02 - 30 LV", "Stage 03 - 40 LV"]  # Здесь должны быть ваши варианты значений
ThreadLux_combobox = ttk.Combobox(root, values=ThreadLux_values)
ThreadLux_combobox.grid(row=1, column=1)

ThreadLuxV_entry = ttk.Entry(root)
ThreadLuxV_entry.grid(row=1, column=3)

ThreadLuxD_var = tk.BooleanVar()
ThreadLuxD_label = ttk.Checkbutton(root, text="Damage", variable=ThreadLuxD_var)
ThreadLuxD_label.grid(row=1, column=4, columnspan=2, pady=10)




# Кнопка для запуска программы с выбранными параметрами
launch_button = ttk.Button(root, text="Launch", command=launch_program)
launch_button.grid(row=4, columnspan=2, pady=20)

# Запуск основного цикла обработки событий
root.mainloop()
