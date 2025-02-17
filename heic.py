import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import pillow_heif

# Initialize pillow_heif
pillow_heif.register_heif_opener()

# Set up Breeze Dark colors
breeze_dark_bg = "#232629"
breeze_dark_fg = "#eff0f1"
breeze_dark_button = "#3daee9"
breeze_dark_button_hover = "#5ec4f3"


class HEICConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HEIC to Image Converter")
        self.root.geometry("600x550")

        # Configure customtkinter appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Apply custom styles
        self.root.configure(bg=breeze_dark_bg)

        # File selection frame
        self.file_frame = ctk.CTkFrame(root, corner_radius=10)
        self.file_frame.pack(padx=10, pady=10, fill="x")

        self.file_label = ctk.CTkLabel(
            self.file_frame, text="Select HEIC Files", text_color=breeze_dark_fg)
        self.file_label.pack(pady=10)

        self.select_button = ctk.CTkButton(self.file_frame, text="Select Files", command=self.select_files,
                                           fg_color=breeze_dark_button, hover_color=breeze_dark_button_hover)
        self.select_button.pack(pady=10)

        self.file_listbox = ctk.CTkTextbox(self.file_frame, height=100)
        self.file_listbox.pack(pady=10, padx=10, fill="x")

        # Output directory selection frame
        self.output_frame = ctk.CTkFrame(root, corner_radius=10)
        self.output_frame.pack(padx=10, pady=10, fill="x")

        self.output_label = ctk.CTkLabel(
            self.output_frame, text="Select Output Directory", text_color=breeze_dark_fg)
        self.output_label.pack(pady=10)

        self.output_button = ctk.CTkButton(self.output_frame, text="Select Directory", command=self.select_output_directory,
                                           fg_color=breeze_dark_button, hover_color=breeze_dark_button_hover)
        self.output_button.pack(pady=10)

        self.output_dir_label = ctk.CTkLabel(
            self.output_frame, text="", text_color=breeze_dark_fg)
        self.output_dir_label.pack(pady=10)

        # File type selection and convert button frame
        self.convert_frame = ctk.CTkFrame(root, corner_radius=10)
        self.convert_frame.pack(padx=10, pady=10, fill="x")

        self.file_type_label = ctk.CTkLabel(
            self.convert_frame, text="Select Output File Type", text_color=breeze_dark_fg)
        self.file_type_label.grid(row=0, column=0, padx=5, pady=10)

        self.file_type_options = ["JPEG", "PNG", "BMP", "GIF", "TIFF"]
        self.file_type_var = ctk.StringVar(value="JPEG")
        self.file_type_menu = ctk.CTkOptionMenu(
            self.convert_frame, values=self.file_type_options, variable=self.file_type_var)
        self.file_type_menu.grid(row=0, column=1, padx=5, pady=10)

        self.convert_button = ctk.CTkButton(self.convert_frame, text="Convert", command=self.convert_files,
                                            fg_color=breeze_dark_button, hover_color=breeze_dark_button_hover)
        self.convert_button.grid(row=0, column=2, padx=5, pady=10)

        # Status bar
        self.status_bar = ctk.CTkLabel(
            root, text="", text_color=breeze_dark_fg)
        self.status_bar.pack(pady=10)

        self.files = []
        self.output_dir = ""

    def select_files(self):
        file_types = [("HEIC files", "*.heic"), ("All files", "*.*")]
        selected_files = filedialog.askopenfilenames(
            title="Select HEIC Files", filetypes=file_types)
        self.files = self.root.tk.splitlist(selected_files)

        self.file_listbox.delete("1.0", ctk.END)
        for file in self.files:
            self.file_listbox.insert(ctk.END, os.path.basename(file) + "\n")

    def select_output_directory(self):
        self.output_dir = filedialog.askdirectory(
            title="Select Output Directory")
        self.output_dir_label.configure(text=self.output_dir)

    def convert_files(self):
        if not self.files:
            messagebox.showwarning("No Files Selected",
                                   "Please select HEIC files to convert.")
            return

        if not self.output_dir:
            messagebox.showwarning("No Output Directory",
                                   "Please select an output directory.")
            return

        file_type = self.file_type_var.get().lower()

        total_files = len(self.files)
        for i, file in enumerate(self.files, start=1):
            try:
                image = Image.open(file)
                base_filename = os.path.splitext(os.path.basename(file))[0]
                output_file = os.path.join(
                    self.output_dir, f"{base_filename}.{file_type}")
                image.save(output_file, file_type.upper())

                self.status_bar.configure(text=f"Converting file {i} of {total_files}: {base_filename}.{file_type}")
                self.root.update_idletasks()
            except Exception as e:
                messagebox.showerror("Conversion Error",
                                     f"Failed to convert {file}: {e}")

        messagebox.showinfo("Conversion Complete",
                            "All files have been successfully converted.")
        self.status_bar.configure(text="")


if __name__ == "__main__":
    root = ctk.CTk()
    app = HEICConverterApp(root)
    root.mainloop()
