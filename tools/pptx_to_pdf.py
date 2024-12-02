import subprocess
from tkinter import filedialog, Tk, messagebox

def convert():
    # Hide the root Tk window
    root = Tk()
    root.withdraw()

    # Select multiple files
    input_paths = filedialog.askopenfilenames(
        title="Select PPTX files",
        filetypes=[("PowerPoint files", "*.pptx;*.ppt")],
    )
    if not input_paths:
        return  # User canceled

    # Output directory
    output_dir = filedialog.askdirectory(
        title="Select output directory"
    )
    if not output_dir:
        return  # User canceled

    for input_path in input_paths:
        output_path = f"{output_dir}/{input_path.split('/')[-1].replace('.pptx', '.pdf')}"
        try:
            subprocess.run(
                ["soffice", "--headless", "--convert-to", "pdf", "--outdir", output_dir, input_path],
                check=True,
            )
        except Exception as e:
            terminate = messagebox.askyesno("Error", f"An error occurred: {e}\n\nDo you want to terminate?")
            if terminate:
                messagebox.showinfo("Terminating", "Conversion process terminated.")
                return  # Exit the function, stopping the conversion
            else:
                messagebox.showinfo("Continuing", "Continuing with the next file.")
                continue  # Continue with the next file

    messagebox.showinfo("Success", f"Converted {input_path} to {output_path}")

