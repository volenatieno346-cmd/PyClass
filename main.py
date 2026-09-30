import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MULTIPLICATION TABLE")
        self.geometry("1000x1000")

        self.label = ctk.CTkLabel(
            self,
            text="MULTIPLICATION TABLE",
            font=ctk.CTkFont(size=22, weight="bold")
        )
        self.label.pack(padx=20, pady=20)

        self.entry = ctk.CTkEntry(self, placeholder_text="Enter a number...")
        self.entry.pack(padx=20, pady=10)

        self.button = ctk.CTkButton(self, text="Show Table", command=self.btn_click)
        self.button.pack(padx=20, pady=10)

        self.table = ctk.CTkTextbox(self, width=800, height=800, wrap="word")
        self.table.pack(padx=20, pady=10)
        self.table.insert("0.0", "Enter a number and click Show Table.")
        self.table.configure(state="disabled")

    def generate_table(self, number):
        try:
            n = int(number)
        except ValueError:
            return "Please enter a valid whole number."

        if n <= 0:
            return "Please enter a positive number."

        lines = []
        for i in range(n,0,-1):
            row = "\t".join(f"{i * j:>3}" for j in range(n, 0, -1))
            lines.append(row)
        return "\n\n".join(lines)

    def btn_click(self):
        user_text = self.entry.get().strip()
        result = self.generate_table(user_text)

        self.table.configure(state="normal")
        self.table.delete("0.0", "end")
        self.table.insert("0.0", result)
        self.table.configure(state="disabled")


if __name__ == "__main__":
    app = App()
    app.mainloop()