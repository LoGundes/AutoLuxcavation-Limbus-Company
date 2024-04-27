import os
import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
import configparser


class LauncherApp:
    def __init__(self, master):
        self.master = master
        master.title("AutoLuxcavation")
        master.geometry("800x600")
        master.resizable(False, False)

        self.ExpLuxNumber = ""
        self.ExpLuxValue = ""
        self.ExpLuxDamage = ""
        self.ThreadLuxNumber = ""
        self.ThreadLuxValue = ""
        self.ThreadLuxDamage = ""

        self.config = configparser.ConfigParser()

        self.logo_image = tk.PhotoImage(file="logo.png")
        self.logo_label = tk.Label(master, image=self.logo_image)
        self.logo_label.grid(row=0, column=0, columnspan=2, pady=50)

        self.ExpLux_label = ttk.Label(master, text="ExpLuxcavation:")
        self.ExpLux_label.grid(row=1, column=0, pady=10)
        self.ExpLux_values = ["Stage 01 - 8 LV", "Stage 02 - 18 LV", "Stage 03 - 28 LV", "Stage 04 - 33 LV",
                         "Stage 05 - 38 LV", "Stage 06 - 43 LV"]
        self.ExpLux_combobox = ttk.Combobox(master, values=self.ExpLux_values)
        self.ExpLux_combobox.grid(row=1, column=1)

        self.ExpLuxV_entry = ttk.Entry(master)
        self.ExpLuxV_entry.grid(row=1, column=3)

        self.ExpLuxD_var = tk.BooleanVar()
        self.ExpLuxD_label = ttk.Checkbutton(master, text="Damage", variable=self.ExpLuxD_var)
        self.ExpLuxD_label.grid(row=1, column=4, columnspan=2, pady=10)

        self.ThreadLux_label = ttk.Label(master, text="ThreadLuxcavation")
        self.ThreadLux_label.grid(row=2, column=0, pady=10)
        self.ThreadLux_values = ["Stage 01 - 20 LV", "Stage 02 - 30 LV", "Stage 03 - 40 LV"]
        self.ThreadLux_combobox = ttk.Combobox(master, values=self.ThreadLux_values)
        self.ThreadLux_combobox.grid(row=2, column=1)

        self.ThreadLuxV_entry = ttk.Entry(master)
        self.ThreadLuxV_entry.grid(row=2, column=3)

        self.ThreadLuxD_var = tk.BooleanVar()
        self.ThreadLuxD_label = ttk.Checkbutton(master, text="Damage", variable=self.ThreadLuxD_var)
        self.ThreadLuxD_label.grid(row=2, column=4, columnspan=2, pady=10)

        self.launch_button = tk.Button(master, text="Launch AutoLuxcavation", command=self.launch_file)
        self.launch_button.grid(row=3, column=4, columnspan=2, pady=10)

        master.protocol("WM_DELETE_WINDOW", self.save_settings)

    def save_settings(self):
        self.ExpLuxNumber = self.ExpLux_combobox.get()
        self.ExpLuxValue = self.ExpLuxV_entry.get()
        self.ThreadLuxNumber = self.ThreadLux_combobox.get()
        self.ThreadLuxValue = self.ThreadLuxV_entry.get()
        self.ExpLuxDamage = self.ExpLuxD_var.get()
        self.ThreadLuxDamage = self.ThreadLuxD_var.get()

        self.config['LuxParameters'] = {
            'ExpLuxcavationNumber': self.ExpLuxNumber,
            'ExpLuxcavationValue': self.ExpLuxValue,
            'ExpLuxcavationDamage': self.ExpLuxDamage,
            'ThreadLuxcavationNumber': self.ThreadLuxNumber,
            'ThreadLuxcavationValue': self.ThreadLuxValue,
            'ThreadLuxcavationDamage': self.ThreadLuxDamage
        }
        with open("config.ini", "w") as configfile:
            self.config.write(configfile)
        self.master.destroy()

    def launch_file(self):
        file_path = "../../GitHub/AutoLuxcavation-Limbus-Company/bin/Clickermann.exe"
        resources_dir = os.path.join(os.path.dirname(__file__), "../../GitHub/AutoLuxcavation-Limbus-Company/bin/projects")
        cms_file_path = os.path.join(resources_dir, "Mod_AutoLuxcavation.cms")
        try:
            subprocess.run([file_path, cms_file_path])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch file: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = LauncherApp(root)
    root.mainloop()
