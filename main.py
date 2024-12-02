import tkinter as tk
from tkinter import messagebox, font
import tools.pptx_to_pdf as pptx_to_pdf
import tools.download_youtube_video as download_video

# Color Palette
COLORS = {
    "background": "#f0f0f0",
    "primary": "#4a4a4a",
    "secondary": "#007bff",
    "hover": "#0056b3",
    "text": "#ffffff"
}

TOOLS = {
    "Convert PPTX to PDF": pptx_to_pdf.convert,
    "Download a YouTube video": download_video.run_in_thread,
    # Add more tools here
}


class FacilitiesApp:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        # Configure window
        self.root.title("Facilities Toolbox")
        self.root.geometry("400x500")
        self.root.configure(bg=COLORS["background"])

        # Disable window resizing
        self.root.resizable(False, False)

    def create_widgets(self):
        # Create a main frame
        main_frame = tk.Frame(self.root, bg=COLORS["background"])
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Title Label with custom styling
        title_font = font.Font(family="Helvetica", size=18, weight="bold")
        title_label = tk.Label(
            main_frame,
            text="Facilities Toolbox",
            font=title_font,
            bg=COLORS["background"],
            fg=COLORS["primary"]
        )
        title_label.pack(pady=(0, 20))

        # Subtitle
        subtitle_font = font.Font(family="Helvetica", size=10)
        subtitle_label = tk.Label(
            main_frame,
            text="Select a tool to get started",
            font=subtitle_font,
            bg=COLORS["background"],
            fg=COLORS["primary"]
        )
        subtitle_label.pack(pady=(0, 10))

        for tool_name, tool_func in TOOLS.items():
            self.create_tool_button(main_frame, tool_name, tool_func)

        footer_font = font.Font(family="Helvetica", size=8)
        footer_label = tk.Label(
            main_frame,
            text="© 2024 Facilities Toolbox",
            font=footer_font,
            bg=COLORS["background"],
            fg=COLORS["primary"]
        )
        footer_label.pack(side=tk.BOTTOM, pady=(20, 0))

    def create_tool_button(self, parent, tool_name, tool_func):
        button = tk.Button(
            parent,
            text=tool_name,
            font=("Helvetica", 10, "bold"),
            bg=COLORS["secondary"],
            fg=COLORS["text"],
            activebackground=COLORS["hover"],
            activeforeground=COLORS["text"],
            width=30,
            height=2,
            relief=tk.FLAT,
            command=lambda func=tool_func: self.launch_tool(func)
        )
        button.pack(pady=5)

        # Add hover effects
        button.bind("<Enter>", lambda e, btn=button: self.on_enter(btn))
        button.bind("<Leave>", lambda e, btn=button: self.on_leave(btn))

    def on_enter(self, button):
        button.configure(bg=COLORS["hover"])

    def on_leave(self, button):
        button.configure(bg=COLORS["secondary"])

    def launch_tool(self, tool_func):
        try:
            tool_func()  # Call the tool's function
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


def main():
    root = tk.Tk()
    app = FacilitiesApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()