import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import matplotlib.pyplot as plt


# ================= TRANSLATOR =================
class Translator:
    def __init__(self):
        self.language = "it"

        self.texts = {
            "it": {
                "title": "Il contabile da taschino",

                "name_label": "Nome spesa",
                "name_placeholder": "es. Pizza / Benzina / Netflix",

                "amount_label": "Prezzo",
                "amount_placeholder": "0.00",
                "amount_hint": "solo numeri",

                "category": "Categoria",

                "add": "Aggiungi spesa",
                "total": "Totale",
                "advice": "Consiglio",

                "graph_btn": "📊 Mostra grafico delle spese mensili",
                "graph_hint": "Clicca per vedere l’andamento delle spese nel tempo",

                "toggle": "English",

                "empty": "Nessuna spesa",
                "error": "Dati non validi!",

                "low": "👍 Spese sotto controllo",
                "medium": "⚠️ Attenzione alle spese",
                "high": "🚨 Spese troppo alte",

                "chart_title": "Spese mensili",
                "x_axis": "Mese",
                "y_axis": "Euro"
            },

            "en": {
                "title": "The Pocket Accountant",

                "name_label": "Expense name",
                "name_placeholder": "e.g. Pizza / Gas / Netflix",

                "amount_label": "Price",
                "amount_placeholder": "0.00",
                "amount_hint": "numbers only",

                "category": "Category",

                "add": "Add expense",
                "total": "Total",
                "advice": "Advice",

                "graph_btn": "📊 Show monthly expense chart",
                "graph_hint": "Click to view spending over time",

                "toggle": "Italiano",

                "empty": "No expenses",
                "error": "Invalid data!",

                "low": "👍 Spending under control",
                "medium": "⚠️ Watch your spending",
                "high": "🚨 High spending",

                "chart_title": "Monthly expenses",
                "x_axis": "Month",
                "y_axis": "Euro"
            }
        }

    def t(self, key):
        return self.texts[self.language][key]

    def switch(self):
        self.language = "en" if self.language == "it" else "it"


# ================= APP =================
class PocketAccountantApp:
    def __init__(self, root):
        self.root = root
        self.tr = Translator()
        self.expenses = []

        self.categories = ["Cibo/Food", "Trasporti/Transport", "Dispositivi/Devices", "Casa/Home", "Medicine/Medicines", "Altro/Other"]

        self.build_ui()
        self.refresh_ui()

    # ---------------- UI ----------------
    def build_ui(self):
        self.root.geometry("750x550")
        self.root.configure(bg="white")

        self.main = tk.Frame(self.root, bg="white")
        self.main.pack(fill="both", expand=True, padx=10, pady=10)

        # TITLE
        self.title_label = tk.Label(
            self.main,
            font=("Arial", 16, "bold"),
            fg="black",
            bg="white"
        )
        self.title_label.pack(pady=5)

        # ================= INPUT =================
        input_frame = tk.Frame(self.main, bg="white")
        input_frame.pack(pady=10)

        # ---- NAME ----
        name_container = tk.Frame(input_frame, bg="white")
        name_container.grid(row=0, column=0, padx=10)

        self.name_label = tk.Label(
            name_container,
            fg="black",
            bg="white",
            font=("Arial", 9, "bold")
        )
        self.name_label.pack(anchor="w")

        self.name_entry = ttk.Entry(name_container, width=25)
        self.name_entry.pack()

        # ---- AMOUNT ----
        amount_container = tk.Frame(input_frame, bg="white")
        amount_container.grid(row=0, column=1, padx=10)

        self.amount_label = tk.Label(
            amount_container,
            fg="black",
            bg="white",
            font=("Arial", 9, "bold")
        )
        self.amount_label.pack(anchor="w")

        row = tk.Frame(amount_container, bg="white")
        row.pack()

        self.amount_entry = ttk.Entry(row, width=10)
        self.amount_entry.pack(side="left")

        tk.Label(row, text="€", fg="black", bg="white").pack(side="left")

        self.amount_hint = tk.Label(
            row,
            fg="black",
            bg="white",
            font=("Arial", 8)
        )
        self.amount_hint.pack(side="left")

        # ---- CATEGORY ----
        cat_container = tk.Frame(input_frame, bg="white")
        cat_container.grid(row=0, column=2, padx=10)

        self.category_label = tk.Label(
            cat_container,
            fg="black",
            bg="white",
            font=("Arial", 9, "bold")
        )
        self.category_label.pack(anchor="w")

        self.category_box = ttk.Combobox(
            cat_container,
            values=self.categories,
            state="readonly",
            width=15
        )
        self.category_box.pack()

        # ADD BUTTON
        self.add_btn = ttk.Button(input_frame, command=self.add_expense)
        self.add_btn.grid(row=0, column=3, padx=10)

        # ================= LIST =================
        self.listbox = tk.Listbox(self.main, fg="black")
        self.listbox.pack(fill="both", expand=True, pady=10)

        # ================= SUMMARY =================
        self.total_label = tk.Label(
            self.main,
            fg="black",
            bg="white",
            font=("Arial", 12, "bold")
        )
        self.total_label.pack()

        self.advice_label = tk.Label(
            self.main,
            fg="black",
            bg="white"
        )
        self.advice_label.pack()

        # ================= GRAPH =================
        self.graph_btn = ttk.Button(self.main, command=self.show_chart)
        self.graph_btn.pack(pady=5)

        self.graph_hint = tk.Label(
            self.main,
            fg="black",
            bg="white",
            font=("Arial", 9)
        )
        self.graph_hint.pack()

        # ================= TOGGLE =================
        self.toggle_btn = tk.Button(
            self.main,
            command=self.toggle_language,
            fg="black",
            bg="white"
        )
        self.toggle_btn.pack(pady=10)

    # ---------------- LOGIC ----------------
    def add_expense(self):
        name = self.name_entry.get()
        amount = self.amount_entry.get()
        category = self.category_box.get()

        try:
            amount = float(amount)
            if not name or not category:
                raise ValueError

            self.expenses.append({
                "name": name,
                "amount": amount,
                "category": category,
                "date": datetime.now().strftime("%Y-%m")
            })

            self.refresh_ui()

        except ValueError:
            messagebox.showerror("Error", self.tr.t("error"))

    # ---------------- REFRESH UI ----------------
    def refresh_ui(self):
        t = self.tr

        self.root.title(t.t("title"))
        self.title_label.config(text=t.t("title"))

        # labels
        self.name_label.config(text=t.t("name_label"))
        self.amount_label.config(text=t.t("amount_label"))
        self.amount_hint.config(text=t.t("amount_hint"))
        self.category_label.config(text=t.t("category"))

        # buttons
        self.add_btn.config(text=t.t("add"))
        self.toggle_btn.config(text=t.t("toggle"))
        self.graph_btn.config(text=t.t("graph_btn"))
        self.graph_hint.config(text=t.t("graph_hint"))

        # placeholders (IMPORTANT)
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, t.t("name_placeholder"))

        self.amount_entry.delete(0, tk.END)
        self.amount_entry.insert(0, t.t("amount_placeholder"))

        # list
        self.listbox.delete(0, tk.END)

        for e in self.expenses:
            self.listbox.insert(
                tk.END,
                f"{e['name']} | {e['category']} | €{e['amount']:.2f}"
            )

        total = sum(e["amount"] for e in self.expenses)

        self.total_label.config(text=f"{t.t('total')}: €{total:.2f}")
        self.advice_label.config(text=self.get_advice(total))

    # ---------------- CONSIGLI ----------------
    def get_advice(self, total):
        t = self.tr

        if total < 100:
            return t.t("low")
        elif total < 500:
            return t.t("medium")
        return t.t("high")

    # ---------------- GRAFICO ----------------
    def show_chart(self):
        if not self.expenses:
            messagebox.showinfo("Info", self.tr.t("empty"))
            return

        data = {}
        for e in self.expenses:
            m = e["date"]
            data[m] = data.get(m, 0) + e["amount"]

        t = self.tr

        plt.bar(data.keys(), data.values())
        plt.title(t.t("chart_title"))
        plt.xlabel(t.t("x_axis"))
        plt.ylabel(t.t("y_axis"))
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # ---------------- LANGUAGE ----------------
    def toggle_language(self):
        self.tr.switch()
        self.refresh_ui()


# ================= RUN =================
if __name__ == "__main__":
    root = tk.Tk()
    app = PocketAccountantApp(root)
    root.mainloop()