import tkinter as tk
import calendar
from datetime import datetime


# ---------------- Calendar App ---------------- #
class DigitalCalendar:
    def __init__(self, root):
        self.root = root
        self.root.title("📅 Digital Calendar")
        self.root.geometry("420x420")
        self.root.config(bg="#1e1e2f")

        # Current Date Info
        now = datetime.now()
        self.year = now.year
        self.month = now.month

        # Header Label
        self.header = tk.Label(
            root,
            text="Digital Calendar",
            font=("Poppins", 20, "bold"),
            bg="#1e1e2f",
            fg="white"
        )
        self.header.pack(pady=10)

        # Month & Year Display
        self.month_year = tk.Label(
            root,
            text="",
            font=("Poppins", 16),
            bg="#1e1e2f",
            fg="#00ffcc"
        )
        self.month_year.pack()

        # Calendar Frame
        self.cal_frame = tk.Frame(root, bg="#1e1e2f")
        self.cal_frame.pack(pady=20)

        # Buttons Frame
        btn_frame = tk.Frame(root, bg="#1e1e2f")
        btn_frame.pack()

        tk.Button(
            btn_frame,
            text="⬅ Previous",
            command=self.prev_month,
            font=("Poppins", 10),
            bg="#333",
            fg="white",
            width=12
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            btn_frame,
            text="Next ➡",
            command=self.next_month,
            font=("Poppins", 10),
            bg="#333",
            fg="white",
            width=12
        ).grid(row=0, column=1, padx=10)

        # Draw Calendar
        self.show_calendar()

    # ---------------- Show Calendar ---------------- #
    def show_calendar(self):
        # Clear old widgets
        for widget in self.cal_frame.winfo_children():
            widget.destroy()

        # Update Month-Year Title
        month_name = calendar.month_name[self.month]
        self.month_year.config(text=f"{month_name} {self.year}")

        # Weekday Headers
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            tk.Label(
                self.cal_frame,
                text=day,
                font=("Poppins", 10, "bold"),
                bg="#1e1e2f",
                fg="white",
                width=5
            ).grid(row=0, column=i)

        # Month Calendar Data
        month_days = calendar.monthcalendar(self.year, self.month)

        # Current day highlight
        today = datetime.now()

        for r, week in enumerate(month_days, start=1):
            for c, day in enumerate(week):
                if day == 0:
                    text = ""
                else:
                    text = str(day)

                # Highlight today
                if (day == today.day and
                        self.month == today.month and
                        self.year == today.year):
                    bg_color = "#00ffcc"
                    fg_color = "black"
                else:
                    bg_color = "#2a2a3d"
                    fg_color = "white"

                tk.Label(
                    self.cal_frame,
                    text=text,
                    font=("Poppins", 10),
                    bg=bg_color,
                    fg=fg_color,
                    width=5,
                    height=2
                ).grid(row=r, column=c, padx=2, pady=2)

    # ---------------- Navigation ---------------- #
    def prev_month(self):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.show_calendar()

    def next_month(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.show_calendar()


# ---------------- Run App ---------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalCalendar(root)
    root.mainloop()
