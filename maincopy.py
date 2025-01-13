# GROUP 2 MEMBERS#
# DAVID PAUL MWITA            22100533590058
# NICHOLAUS NUNGU WAROBI      22100533590017
# MBAGA   MBAGA KAJEMBULA     22100533590040
# LAZARO LANGOI LEKINDERAKI   22100533590012
# FEDELIKA MAXMUS NG'OLO      22100533590038
from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import pillow_heif 

pillow_heif.register_heif_opener()

def select_images():
    global input_files, image_list_frame
    input_files = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("All Files", "*.*")]
    )
    if input_files:
        for widget in image_list_frame.winfo_children():
            widget.destroy()
        for file in input_files:
            try:
                img = Image.open(file)
                img = img.resize((100, 100))
                img_tk = ImageTk.PhotoImage(img)
                lbl = tk.Label(image_list_frame, image=img_tk)
                lbl.image = img_tk
                lbl.pack(side=tk.LEFT, padx=5, pady=5)
            except Exception as e:
                messagebox.showerror("Error", f"Cannot load image: {file}\n{e}")
        messagebox.showinfo("Images Selected", f"{len(input_files)} images selected.")
    else:
        messagebox.showwarning("No Selection", "No images were selected.")

def select_output_folder():
    global output_folder
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if output_folder:
        messagebox.showinfo("Output Folder Selected", f"Images will be saved in: {output_folder}")
    else:
        messagebox.showwarning("No Selection", "No output folder was selected.")

def process_images():
    if not input_files or not output_folder:
        messagebox.showerror("Missing Selection", "Please select both images and an output folder before proceeding.")
        return

    output_format = format_var.get().strip('.').lower()
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Dimensions", "Please enter valid width and height values.")
        return

    for file_path in input_files:
        try:
            img = Image.open(file_path)
            img = img.resize((width, height))

            base_name = os.path.splitext(os.path.basename(file_path))[0]
            output_file = os.path.join(output_folder, f"{base_name}.{output_format}")

            img.save(output_file, format=output_format.upper())
        except Exception as e:
            messagebox.showerror("Processing Error", f"Error processing {file_path}: {e}")
            return

    messagebox.showinfo("Success", "All images processed successfully!")

input_files = []
output_folder = ""

root = tk.Tk()
root.title("Image Resizer and Converter")
root.geometry("600x700")
root.configure(bg="#f5f5f5")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 12), padding=5)
style.configure("TEntry", font=("Arial", 12))

main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

header_label = tk.Label(
    main_frame, text="Image Resizer and Converter", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white"
)
header_label.pack(fill=tk.X, pady=10)

btn_select_images = ttk.Button(main_frame, text="Select Images", command=select_images)
btn_select_images.pack(pady=10)

image_list_frame = tk.Frame(main_frame, bg="#e0e0e0", height=120)
image_list_frame.pack(fill=tk.X, pady=10)

btn_select_output_folder = ttk.Button(main_frame, text="Select Output Folder", command=select_output_folder)
btn_select_output_folder.pack(pady=10)

format_label = ttk.Label(main_frame, text="Select Output Format:")
format_label.pack(pady=5)

format_var = tk.StringVar(value="jpg")
format_dropdown = ttk.Combobox(main_frame, textvariable=format_var, state="readonly", values=['png', 'jpeg', 'bmp', 'gif', 'tiff', 'webp', 'jpg', 'heic'])
format_dropdown.pack(pady=5)

size_label = ttk.Label(main_frame, text="Enter Dimensions (Width x Height):")
size_label.pack(pady=5)

size_frame = ttk.Frame(main_frame)
size_frame.pack(pady=5)

width_label = ttk.Label(size_frame, text="Width:")
width_label.pack(side=tk.LEFT, padx=5)
width_entry = ttk.Entry(size_frame, width=10)
width_entry.pack(side=tk.LEFT, padx=5)
width_entry.insert(0, "900")

height_label = ttk.Label(size_frame, text="Height:")
height_label.pack(side=tk.LEFT, padx=5)
height_entry = ttk.Entry(size_frame, width=10)
height_entry.pack(side=tk.LEFT, padx=5)
height_entry.insert(0, "600")

btn_process_images = ttk.Button(main_frame, text="Process Images", command=process_images)
btn_process_images.pack(pady=20)

footer_label = tk.Label(
    main_frame, text="Developed for All Devices", font=("Arial", 10), bg="#4CAF50", fg="white"
)
footer_label.pack(fill=tk.X, pady=10)

root.mainloop()



