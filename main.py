import tkinter as tk
from tkinter import ttk, messagebox, font as tkfont
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use("TkAgg")


# ══════════════════════════════════════════════
#  TEMI
# ══════════════════════════════════════════════
THEMES = {
    "🌙 Dark": {
        "bg":        "#0f0f17",
        "bg2":       "#1a1a28",
        "bg3":       "#22223a",
        "card":      "#1e1e2e",
        "accent":    "#7c6af7",
        "accent_fg": "#ffffff",
        "text":      "#e8e4ff",
        "text2":     "#9490b8",
        "entry_bg":  "#252535",
        "entry_fg":  "#e8e4ff",
        "list_sel":  "#7c6af7",
        "green":     "#4ade80",
        "amber":     "#fbbf24",
        "red":       "#f87171",
        "border":    "#3a3a5c",
        "btn_bg":    "#7c6af7",
        "btn_fg":    "#ffffff",
        "btn_hover": "#6a59e0",
        "toggle_bg": "#2a2a3e",
        "toggle_fg": "#9490b8",
    },
    "🌊 Ocean": {
        "bg":        "#071a2e",
        "bg2":       "#0d2540",
        "bg3":       "#112f4e",
        "card":      "#0f2d4a",
        "accent":    "#38bdf8",
        "accent_fg": "#071a2e",
        "text":      "#e0f2fe",
        "text2":     "#7eb8d8",
        "entry_bg":  "#143459",
        "entry_fg":  "#e0f2fe",
        "list_sel":  "#38bdf8",
        "green":     "#34d399",
        "amber":     "#fbbf24",
        "red":       "#fb7185",
        "border":    "#1e4e78",
        "btn_bg":    "#38bdf8",
        "btn_fg":    "#071a2e",
        "btn_hover": "#29a8e0",
        "toggle_bg": "#0d2540",
        "toggle_fg": "#7eb8d8",
    },
    "🌿 Forest": {
        "bg":        "#0a1a0e",
        "bg2":       "#112516",
        "bg3":       "#17311e",
        "card":      "#132b18",
        "accent":    "#4ade80",
        "accent_fg": "#0a1a0e",
        "text":      "#f0fdf4",
        "text2":     "#86b895",
        "entry_bg":  "#193520",
        "entry_fg":  "#f0fdf4",
        "list_sel":  "#4ade80",
        "green":     "#4ade80",
        "amber":     "#fbbf24",
        "red":       "#f87171",
        "border":    "#2a5235",
        "btn_bg":    "#4ade80",
        "btn_fg":    "#0a1a0e",
        "btn_hover": "#3ac96e",
        "toggle_bg": "#112516",
        "toggle_fg": "#86b895",
    },
    "🌅 Sunset": {
        "bg":        "#1a0f0a",
        "bg2":       "#241510",
        "bg3":       "#2e1b14",
        "card":      "#28170f",
        "accent":    "#f97316",
        "accent_fg": "#ffffff",
        "text":      "#fff7ed",
        "text2":     "#c4896e",
        "entry_bg":  "#321d13",
        "entry_fg":  "#fff7ed",
        "list_sel":  "#f97316",
        "green":     "#4ade80",
        "amber":     "#fbbf24",
        "red":       "#f87171",
        "border":    "#5c3520",
        "btn_bg":    "#f97316",
        "btn_fg":    "#ffffff",
        "btn_hover": "#e06010",
        "toggle_bg": "#241510",
        "toggle_fg": "#c4896e",
    },
    "🌸 Rose": {
        "bg":        "#1a0a14",
        "bg2":       "#241018",
        "bg3":       "#2e151f",
        "card":      "#280f1a",
        "accent":    "#f472b6",
        "accent_fg": "#ffffff",
        "text":      "#fdf2f8",
        "text2":     "#c480a0",
        "entry_bg":  "#3a1528",
        "entry_fg":  "#fdf2f8",
        "list_sel":  "#f472b6",
        "green":     "#4ade80",
        "amber":     "#fbbf24",
        "red":       "#f87171",
        "border":    "#5c2040",
        "btn_bg":    "#f472b6",
        "btn_fg":    "#ffffff",
        "btn_hover": "#e060a8",
        "toggle_bg": "#241018",
        "toggle_fg": "#c480a0",
    },
    "☀️ Light": {
        "bg":        "#f8f7ff",
        "bg2":       "#ffffff",
        "bg3":       "#f0eeff",
        "card":      "#ffffff",
        "accent":    "#6c5ce7",
        "accent_fg": "#ffffff",
        "text":      "#1a1830",
        "text2":     "#6b647a",
        "entry_bg":  "#f0eeff",
        "entry_fg":  "#1a1830",
        "list_sel":  "#6c5ce7",
        "green":     "#16a34a",
        "amber":     "#d97706",
        "red":       "#dc2626",
        "border":    "#d8d4f0",
        "btn_bg":    "#6c5ce7",
        "btn_fg":    "#ffffff",
        "btn_hover": "#5a4bd4",
        "toggle_bg": "#f0eeff",
        "toggle_fg": "#6b647a",
    },
}

CATEGORY_ICONS = {
    "Cibo":         "🍕",
    "Food":         "🍕",
    "Trasporti":    "🚗",
    "Transport":    "🚗",
    "Dispositivi":  "💻",
    "Devices":      "💻",
    "Casa":         "🏠",
    "Home":         "🏠",
    "Medicine":     "💊",
    "Medicines":    "💊",
    "Altro":        "📦",
    "Other":        "📦",
}


# ══════════════════════════════════════════════
#  TRADUTTORE
# ══════════════════════════════════════════════
class Translator:
    def __init__(self):
        self.language = "it"
        self.texts = {
            "it": {
                "title":           "Il Contabile da Taschino",
                "subtitle":        "Tieni traccia di ogni euro",
                "name_label":      "Nome spesa",
                "name_ph":         "es. Pizza, Benzina, Netflix…",
                "amount_label":    "Importo (€)",
                "amount_ph":       "0.00",
                "category_label":  "Categoria",
                "add":             "＋  Aggiungi",
                "delete":          "✕ Elimina",
                "clear_all":       "🗑  Svuota tutto",
                "graph_btn":       "📊  Grafico mensile",
                "total":           "Totale",
                "no_expenses":     "Nessuna spesa ancora.",
                "empty_warn":      "Nessuna spesa da mostrare.",
                "error":           "Compila tutti i campi correttamente.",
                "delete_warn":     "Seleziona una spesa da eliminare.",
                "confirm_clear":   "Eliminare tutte le spese?",
                "low":             "👍  Spese sotto controllo",
                "medium":          "⚠️  Attenzione alle spese",
                "high":            "🚨  Spese troppo alte!",
                "chart_title":     "Spese mensili",
                "x_axis":          "Mese",
                "y_axis":          "Euro (€)",
                "toggle_lang":     "🇬🇧  English",
                "theme_label":     "Tema",
                "categories": [
                    "🍕 Cibo", "🚗 Trasporti", "💻 Dispositivi",
                    "🏠 Casa", "💊 Medicine", "📦 Altro"
                ],
            },
            "en": {
                "title":           "The Pocket Accountant",
                "subtitle":        "Track every euro you spend",
                "name_label":      "Expense name",
                "name_ph":         "e.g. Pizza, Gas, Netflix…",
                "amount_label":    "Amount (€)",
                "amount_ph":       "0.00",
                "category_label":  "Category",
                "add":             "＋  Add",
                "delete":          "✕ Delete",
                "clear_all":       "🗑  Clear all",
                "graph_btn":       "📊  Monthly chart",
                "total":           "Total",
                "no_expenses":     "No expenses yet.",
                "empty_warn":      "No expenses to display.",
                "error":           "Please fill all fields correctly.",
                "delete_warn":     "Select an expense to delete.",
                "confirm_clear":   "Delete all expenses?",
                "low":             "👍  Spending under control",
                "medium":          "⚠️  Watch your spending",
                "high":            "🚨  High spending alert!",
                "chart_title":     "Monthly expenses",
                "x_axis":          "Month",
                "y_axis":          "Euro (€)",
                "toggle_lang":     "🇮🇹  Italiano",
                "theme_label":     "Theme",
                "categories": [
                    "🍕 Food", "🚗 Transport", "💻 Devices",
                    "🏠 Home", "💊 Medicines", "📦 Other"
                ],
            },
        }

    def t(self, key):
        return self.texts[self.language][key]

    def switch(self):
        self.language = "en" if self.language == "it" else "it"


# ══════════════════════════════════════════════
#  APP
# ══════════════════════════════════════════════
class PocketAccountantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Il Contabile da Taschino")
        self.root.geometry("860x640")
        self.root.minsize(800, 580)
        self.root.resizable(True, True)

        self.tr = Translator()
        self.expenses = []
        self.current_theme_name = "🌙 Dark"
        self.theme = THEMES[self.current_theme_name]

        self._build_ui()
        self._apply_theme()
        self._refresh_ui()

    # ────────────────────────────────────────
    #  COSTRUZIONE UI
    # ────────────────────────────────────────
    def _build_ui(self):
        th = self.theme

        # ── ROOT CONFIG ──
        self.root.configure(bg=th["bg"])

        # ── FRAME PRINCIPALE ──
        self.main = tk.Frame(self.root, bg=th["bg"])
        self.main.pack(fill="both", expand=True)

        # ── SIDEBAR ──
        self.sidebar = tk.Frame(self.main, bg=th["bg2"], width=220)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Logo / titolo nella sidebar
        self.logo_frame = tk.Frame(self.sidebar, bg=th["bg2"])
        self.logo_frame.pack(fill="x", pady=(24, 4), padx=16)

        self.emoji_lbl = tk.Label(self.logo_frame, text="💰", font=("Segoe UI Emoji", 28),
                                   bg=th["bg2"], fg=th["accent"])
        self.emoji_lbl.pack(anchor="w")

        self.title_lbl = tk.Label(self.logo_frame, font=("Segoe UI", 13, "bold"),
                                   bg=th["bg2"], fg=th["text"], wraplength=180, justify="left")
        self.title_lbl.pack(anchor="w", pady=(4, 0))

        self.subtitle_lbl = tk.Label(self.logo_frame, font=("Segoe UI", 9),
                                      bg=th["bg2"], fg=th["text2"], wraplength=180, justify="left")
        self.subtitle_lbl.pack(anchor="w", pady=(2, 0))

        # Separatore
        tk.Frame(self.sidebar, bg=th["border"], height=1).pack(fill="x", padx=16, pady=14)

        # ── TEMA ──
        theme_section = tk.Frame(self.sidebar, bg=th["bg2"])
        theme_section.pack(fill="x", padx=16, pady=(0, 8))

        self.theme_lbl = tk.Label(theme_section, font=("Segoe UI", 9, "bold"),
                                   bg=th["bg2"], fg=th["text2"])
        self.theme_lbl.pack(anchor="w", pady=(0, 6))

        self.theme_var = tk.StringVar(value=self.current_theme_name)
        self.theme_menu = tk.OptionMenu(theme_section, self.theme_var,
                                         *THEMES.keys(), command=self._change_theme)
        self.theme_menu.config(font=("Segoe UI", 10), bd=0, relief="flat",
                                bg=th["bg3"], fg=th["text"], activebackground=th["bg3"],
                                activeforeground=th["accent"], highlightthickness=0,
                                indicatoron=True, width=16)
        self.theme_menu["menu"].config(bg=th["bg3"], fg=th["text"], font=("Segoe UI", 10),
                                        activebackground=th["accent"], activeforeground=th["accent_fg"])
        self.theme_menu.pack(fill="x")

        tk.Frame(self.sidebar, bg=th["border"], height=1).pack(fill="x", padx=16, pady=14)

        # ── TOGGLE LINGUA ──
        self.lang_btn = tk.Button(self.sidebar, font=("Segoe UI", 10, "bold"),
                                   bd=0, cursor="hand2", relief="flat",
                                   command=self._toggle_language)
        self.lang_btn.pack(fill="x", padx=16, pady=(0, 8), ipady=8)

        tk.Frame(self.sidebar, bg=th["border"], height=1).pack(fill="x", padx=16, pady=6)

        # ── TOTALE nella sidebar ──
        total_frame = tk.Frame(self.sidebar, bg=th["bg3"])
        total_frame.pack(fill="x", padx=16, pady=14, ipady=12)

        tk.Frame(total_frame, bg=th["bg3"]).pack(fill="x")  # spacer top

        self.total_lbl = tk.Label(total_frame, font=("Segoe UI", 22, "bold"),
                                   bg=th["bg3"], fg=th["accent"])
        self.total_lbl.pack()

        self.total_sub_lbl = tk.Label(total_frame, font=("Segoe UI", 9),
                                       bg=th["bg3"], fg=th["text2"])
        self.total_sub_lbl.pack(pady=(2, 0))

        self.advice_lbl = tk.Label(total_frame, font=("Segoe UI", 10),
                                    bg=th["bg3"], fg=th["text"], wraplength=180)
        self.advice_lbl.pack(pady=(10, 4))

        # ── PULSANTE GRAFICO ──
        self.graph_btn = tk.Button(self.sidebar, font=("Segoe UI", 10, "bold"),
                                    bd=0, relief="flat", cursor="hand2",
                                    command=self._show_chart)
        self.graph_btn.pack(fill="x", padx=16, pady=(8, 4), ipady=8)

        # ── CLEAR ALL ──
        self.clear_btn = tk.Button(self.sidebar, font=("Segoe UI", 9),
                                    bd=0, relief="flat", cursor="hand2",
                                    command=self._clear_all)
        self.clear_btn.pack(fill="x", padx=16, pady=(0, 8), ipady=6)

        # ═══════════════════════════════════
        # CONTENUTO PRINCIPALE (destra)
        # ═══════════════════════════════════
        self.content = tk.Frame(self.main, bg=th["bg"])
        self.content.pack(side="left", fill="both", expand=True, padx=0, pady=0)

        # ── INPUT CARD ──
        self.input_card = tk.Frame(self.content, bg=th["card"],
                                    highlightbackground=th["border"], highlightthickness=1)
        self.input_card.pack(fill="x", padx=20, pady=(20, 10))

        input_inner = tk.Frame(self.input_card, bg=th["card"])
        input_inner.pack(fill="x", padx=20, pady=16)

        # Row 1: Nome + Importo + Categoria
        row1 = tk.Frame(input_inner, bg=th["card"])
        row1.pack(fill="x", pady=(0, 10))

        # Nome
        col_name = tk.Frame(row1, bg=th["card"])
        col_name.pack(side="left", expand=True, fill="x", padx=(0, 10))

        self.name_lbl = tk.Label(col_name, font=("Segoe UI", 9, "bold"),
                                  bg=th["card"], fg=th["text2"])
        self.name_lbl.pack(anchor="w", pady=(0, 4))

        self.name_entry = tk.Entry(col_name, font=("Segoe UI", 11),
                                    bg=th["entry_bg"], fg=th["entry_fg"],
                                    insertbackground=th["text"], relief="flat",
                                    bd=0, highlightthickness=1,
                                    highlightbackground=th["border"],
                                    highlightcolor=th["accent"])
        self.name_entry.pack(fill="x", ipady=8)

        # Importo
        col_amt = tk.Frame(row1, bg=th["card"])
        col_amt.pack(side="left", expand=True, fill="x", padx=(0, 10))

        self.amount_lbl = tk.Label(col_amt, font=("Segoe UI", 9, "bold"),
                                    bg=th["card"], fg=th["text2"])
        self.amount_lbl.pack(anchor="w", pady=(0, 4))

        self.amount_entry = tk.Entry(col_amt, font=("Segoe UI", 11),
                                      bg=th["entry_bg"], fg=th["entry_fg"],
                                      insertbackground=th["text"], relief="flat",
                                      bd=0, highlightthickness=1,
                                      highlightbackground=th["border"],
                                      highlightcolor=th["accent"])
        self.amount_entry.pack(fill="x", ipady=8)

        # Categoria
        col_cat = tk.Frame(row1, bg=th["card"])
        col_cat.pack(side="left", expand=True, fill="x")

        self.cat_lbl = tk.Label(col_cat, font=("Segoe UI", 9, "bold"),
                                 bg=th["card"], fg=th["text2"])
        self.cat_lbl.pack(anchor="w", pady=(0, 4))

        self.cat_var = tk.StringVar()
        self.cat_menu = tk.OptionMenu(col_cat, self.cat_var, "")
        self.cat_menu.config(font=("Segoe UI", 10), bd=0, relief="flat",
                              bg=th["entry_bg"], fg=th["entry_fg"],
                              activebackground=th["bg3"],
                              activeforeground=th["accent"],
                              highlightthickness=1,
                              highlightbackground=th["border"],
                              highlightcolor=th["accent"],
                              width=18, anchor="w")
        self.cat_menu.pack(fill="x", ipady=4)

        # Bottone aggiungi
        self.add_btn = tk.Button(input_inner, font=("Segoe UI", 11, "bold"),
                                  bd=0, relief="flat", cursor="hand2",
                                  command=self._add_expense)
        self.add_btn.pack(fill="x", ipady=10, pady=(4, 0))

        # Hover effects bottone aggiungi
        self.add_btn.bind("<Enter>", lambda e: self.add_btn.config(bg=self.theme["btn_hover"]))
        self.add_btn.bind("<Leave>", lambda e: self.add_btn.config(bg=self.theme["btn_bg"]))

        # ── LISTA SPESE ──
        list_header = tk.Frame(self.content, bg=th["bg"])
        list_header.pack(fill="x", padx=20, pady=(4, 6))

        self.list_title_lbl = tk.Label(list_header, font=("Segoe UI", 11, "bold"),
                                        bg=th["bg"], fg=th["text"])
        self.list_title_lbl.pack(side="left")

        self.delete_btn = tk.Button(list_header, font=("Segoe UI", 9),
                                     bd=0, relief="flat", cursor="hand2",
                                     command=self._delete_selected)
        self.delete_btn.pack(side="right", padx=(4, 0), ipadx=8, ipady=4)

        list_frame = tk.Frame(self.content, bg=th["card"],
                               highlightbackground=th["border"], highlightthickness=1)
        list_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        scrollbar = tk.Scrollbar(list_frame, bg=th["bg2"], troughcolor=th["bg"],
                                  relief="flat", width=8)
        scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(list_frame,
                                   font=("Segoe UI", 11),
                                   bg=th["card"], fg=th["text"],
                                   selectbackground=th["list_sel"],
                                   selectforeground=th["accent_fg"],
                                   activestyle="none",
                                   relief="flat", bd=0,
                                   yscrollcommand=scrollbar.set,
                                   highlightthickness=0)
        self.listbox.pack(fill="both", expand=True, padx=4, pady=4)
        scrollbar.config(command=self.listbox.yview)

    # ────────────────────────────────────────
    #  APPLICA TEMA (ricrea colori su tutti i widget)
    # ────────────────────────────────────────
    def _apply_theme(self):
        th = self.theme

        self.root.configure(bg=th["bg"])
        self.main.configure(bg=th["bg"])
        self.sidebar.configure(bg=th["bg2"])
        self.logo_frame.configure(bg=th["bg2"])
        self.emoji_lbl.configure(bg=th["bg2"], fg=th["accent"])
        self.title_lbl.configure(bg=th["bg2"], fg=th["text"])
        self.subtitle_lbl.configure(bg=th["bg2"], fg=th["text2"])
        self.theme_lbl.configure(bg=th["bg2"], fg=th["text2"])
        self.theme_menu.configure(bg=th["bg3"], fg=th["text"],
                                   activebackground=th["bg3"],
                                   activeforeground=th["accent"])
        self.theme_menu["menu"].configure(bg=th["bg3"], fg=th["text"],
                                           activebackground=th["accent"],
                                           activeforeground=th["accent_fg"])
        self.lang_btn.configure(bg=th["toggle_bg"], fg=th["accent"],
                                 activebackground=th["bg3"],
                                 activeforeground=th["accent"])
        self.total_lbl.configure(bg=th["bg3"], fg=th["accent"])
        self.total_sub_lbl.configure(bg=th["bg3"], fg=th["text2"])
        self.advice_lbl.configure(bg=th["bg3"], fg=th["text"])

        # Aggiorna frame totale
        for child in self.sidebar.winfo_children():
            if isinstance(child, tk.Frame) and child.cget("bg") == th["bg3"]:
                child.configure(bg=th["bg3"])

        self.graph_btn.configure(bg=th["accent"], fg=th["accent_fg"],
                                  activebackground=th["btn_hover"],
                                  activeforeground=th["accent_fg"])
        self.clear_btn.configure(bg=th["bg3"], fg=th["text2"],
                                  activebackground=th["bg3"],
                                  activeforeground=th["red"])

        # Separatori
        for child in self.sidebar.winfo_children():
            if isinstance(child, tk.Frame) and child.cget("height") == 1:
                child.configure(bg=th["border"])

        self.content.configure(bg=th["bg"])
        self.input_card.configure(bg=th["card"],
                                   highlightbackground=th["border"])

        for child in self.input_card.winfo_children():
            self._style_frame_children(child, th)

        self.add_btn.configure(bg=th["btn_bg"], fg=th["btn_fg"],
                                activebackground=th["btn_hover"],
                                activeforeground=th["btn_fg"])

        self.list_title_lbl.configure(bg=th["bg"], fg=th["text"])
        self.delete_btn.configure(bg=th["bg3"], fg=th["text2"],
                                   activebackground=th["bg3"],
                                   activeforeground=th["red"])

        self.listbox.configure(bg=th["card"], fg=th["text"],
                                selectbackground=th["list_sel"],
                                selectforeground=th["accent_fg"])

    def _style_frame_children(self, widget, th):
        """Ricorsivamente applica stili ai figli del frame di input."""
        try:
            cls = widget.winfo_class()
            if cls == "Frame":
                widget.configure(bg=th["card"])
                for child in widget.winfo_children():
                    self._style_frame_children(child, th)
            elif cls == "Label":
                widget.configure(bg=th["card"], fg=th["text2"])
            elif cls == "Entry":
                widget.configure(bg=th["entry_bg"], fg=th["entry_fg"],
                                  insertbackground=th["text"],
                                  highlightbackground=th["border"],
                                  highlightcolor=th["accent"])
            elif cls == "Menubutton":
                widget.configure(bg=th["entry_bg"], fg=th["entry_fg"],
                                  activebackground=th["bg3"],
                                  activeforeground=th["accent"],
                                  highlightbackground=th["border"],
                                  highlightcolor=th["accent"])
                widget["menu"].configure(bg=th["bg3"], fg=th["text"],
                                          activebackground=th["accent"],
                                          activeforeground=th["accent_fg"])
        except Exception:
            pass

    # ────────────────────────────────────────
    #  REFRESH UI (lingue + dati)
    # ────────────────────────────────────────
    def _refresh_ui(self):
        t = self.tr
        th = self.theme

        self.root.title(t.t("title"))
        self.title_lbl.config(text=t.t("title"))
        self.subtitle_lbl.config(text=t.t("subtitle"))
        self.theme_lbl.config(text=t.t("theme_label"))
        self.lang_btn.config(text=t.t("toggle_lang"))
        self.graph_btn.config(text=t.t("graph_btn"))
        self.clear_btn.config(text=t.t("clear_all"))

        self.name_lbl.config(text=t.t("name_label"))
        self.amount_lbl.config(text=t.t("amount_label"))
        self.cat_lbl.config(text=t.t("category_label"))
        self.add_btn.config(text=t.t("add"))
        self.delete_btn.config(text=t.t("delete"))

        # Placeholder nome
        if not self.name_entry.get() or self.name_entry.get() in (
            self.tr.texts["it"]["name_ph"], self.tr.texts["en"]["name_ph"]
        ):
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, t.t("name_ph"))
            self.name_entry.config(fg=th["text2"])

        # Placeholder importo
        if not self.amount_entry.get() or self.amount_entry.get() in (
            self.tr.texts["it"]["amount_ph"], self.tr.texts["en"]["amount_ph"]
        ):
            self.amount_entry.delete(0, tk.END)
            self.amount_entry.insert(0, t.t("amount_ph"))
            self.amount_entry.config(fg=th["text2"])

        # Categorie dropdown
        cats = t.t("categories")
        menu = self.cat_menu["menu"]
        menu.delete(0, "end")
        for c in cats:
            menu.add_command(label=c, command=lambda v=c: self.cat_var.set(v))
        if not self.cat_var.get() or self.cat_var.get() not in cats:
            self.cat_var.set(cats[0])

        # Aggiorna lista
        self.listbox.delete(0, tk.END)
        if not self.expenses:
            self.listbox.insert(tk.END, f"  {t.t('no_expenses')}")
            self.listbox.itemconfig(0, fg=th["text2"])
        else:
            for i, e in enumerate(self.expenses):
                line = f"  {e['icon']}  {e['name']:<20}  €{e['amount']:>8.2f}   {e['category']:<20}  {e['date']}"
                self.listbox.insert(tk.END, line)
                # Colore alternato
                row_bg = th["card"] if i % 2 == 0 else th["bg2"]
                self.listbox.itemconfig(i, bg=row_bg)

        # Totale e consiglio
        total = sum(e["amount"] for e in self.expenses)
        self.total_lbl.config(text=f"€ {total:,.2f}")
        self.total_sub_lbl.config(text=t.t("total"))
        self.advice_lbl.config(text=self._get_advice(total))

        # Titolo lista
        n = len(self.expenses)
        self.list_title_lbl.config(text=f"📋  Spese  ({n})" if self.tr.language == "it"
                                    else f"📋  Expenses  ({n})")

    # ────────────────────────────────────────
    #  LOGICA
    # ────────────────────────────────────────
    def _add_expense(self):
        name = self.name_entry.get().strip()
        amount_str = self.amount_entry.get().strip()
        category = self.cat_var.get().strip()

        # Ignora placeholders
        if name == self.tr.t("name_ph"):
            name = ""
        if amount_str == self.tr.t("amount_ph"):
            amount_str = ""

        try:
            if not name or not category:
                raise ValueError
            amount = float(amount_str.replace(",", "."))
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("⚠️", self.tr.t("error"))
            return

        # Icona categoria
        icon = "📦"
        for k, v in CATEGORY_ICONS.items():
            if k in category:
                icon = v
                break

        self.expenses.append({
            "name": name,
            "amount": amount,
            "category": category,
            "icon": icon,
            "date": datetime.now().strftime("%Y-%m"),
        })

        # Pulisci campi
        self.name_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

        self._refresh_ui()

    def _delete_selected(self):
        sel = self.listbox.curselection()
        if not sel or not self.expenses:
            messagebox.showwarning("⚠️", self.tr.t("delete_warn"))
            return
        idx = sel[0]
        if idx < len(self.expenses):
            self.expenses.pop(idx)
        self._refresh_ui()

    def _clear_all(self):
        if not self.expenses:
            return
        if messagebox.askyesno("🗑", self.tr.t("confirm_clear")):
            self.expenses.clear()
            self._refresh_ui()

    def _get_advice(self, total):
        t = self.tr
        if total < 100:
            return t.t("low")
        elif total < 500:
            return t.t("medium")
        return t.t("high")

    # ────────────────────────────────────────
    #  GRAFICO
    # ────────────────────────────────────────
    def _show_chart(self):
        if not self.expenses:
            messagebox.showinfo("ℹ️", self.tr.t("empty_warn"))
            return

        data = {}
        cat_data = {}
        for e in self.expenses:
            m = e["date"]
            data[m] = data.get(m, 0) + e["amount"]
            c = e["category"]
            cat_data[c] = cat_data.get(c, 0) + e["amount"]

        th = self.theme
        t = self.tr

        # Colori matplotlib dal tema
        plt.rcParams.update({
            "figure.facecolor":  th["bg"],
            "axes.facecolor":    th["bg2"],
            "axes.edgecolor":    th["border"],
            "axes.labelcolor":   th["text2"],
            "text.color":        th["text"],
            "xtick.color":       th["text2"],
            "ytick.color":       th["text2"],
            "grid.color":        th["border"],
            "grid.alpha":        0.4,
        })

        win = tk.Toplevel(self.root)
        win.title(t.t("chart_title"))
        win.geometry("800x480")
        win.configure(bg=th["bg"])

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))
        fig.patch.set_facecolor(th["bg"])

        # Grafico a barre - mensile
        months = list(data.keys())
        values = list(data.values())
        bars = ax1.bar(months, values, color=th["accent"], edgecolor=th["bg"], linewidth=1.5)
        for bar, val in zip(bars, values):
            ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max(values) * 0.02,
                     f"€{val:.0f}", ha="center", va="bottom",
                     fontsize=9, color=th["text"], fontweight="bold")
        ax1.set_title(t.t("chart_title"), fontsize=12, color=th["text"], fontweight="bold", pad=12)
        ax1.set_xlabel(t.t("x_axis"), color=th["text2"], fontsize=9)
        ax1.set_ylabel(t.t("y_axis"), color=th["text2"], fontsize=9)
        ax1.set_facecolor(th["bg2"])
        ax1.tick_params(axis="x", rotation=30)
        ax1.grid(axis="y", alpha=0.3)
        ax1.spines["top"].set_visible(False)
        ax1.spines["right"].set_visible(False)

        # Grafico a torta - categorie
        cat_palette = [th["accent"], th["green"], th["amber"], th["red"],
                       "#a78bfa", "#60a5fa", "#34d399", "#fb923c"]
        wedges, texts, autotexts = ax2.pie(
            cat_data.values(),
            labels=cat_data.keys(),
            autopct="%1.0f%%",
            startangle=90,
            colors=cat_palette[:len(cat_data)],
            wedgeprops=dict(edgecolor=th["bg"], linewidth=2),
            textprops=dict(color=th["text"], fontsize=9),
        )
        for at in autotexts:
            at.set_color(th["bg"])
            at.set_fontweight("bold")
            at.set_fontsize(8)
        ax2.set_title("Categorie" if self.tr.language == "it" else "Categories",
                      fontsize=12, color=th["text"], fontweight="bold", pad=12)
        ax2.set_facecolor(th["bg"])

        fig.tight_layout(pad=2)

        canvas = FigureCanvasTkAgg(fig, master=win)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

        close_btn = tk.Button(win, text="✕  Chiudi" if self.tr.language == "it" else "✕  Close",
                               font=("Segoe UI", 10, "bold"),
                               bg=th["btn_bg"], fg=th["btn_fg"],
                               bd=0, relief="flat", cursor="hand2",
                               command=win.destroy)
        close_btn.pack(pady=(0, 12), ipadx=20, ipady=6)

    # ────────────────────────────────────────
    #  CAMBIO TEMA / LINGUA
    # ────────────────────────────────────────
    def _change_theme(self, name):
        self.current_theme_name = name
        self.theme = THEMES[name]
        self._apply_theme()
        self._refresh_ui()

    def _toggle_language(self):
        self.tr.switch()
        self._refresh_ui()


# ══════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════
if __name__ == "__main__":
    root = tk.Tk()
    try:
        root.tk.call("tk", "scaling", 1.2)
    except Exception:
        pass
    app = PocketAccountantApp(root)
    root.mainloop()