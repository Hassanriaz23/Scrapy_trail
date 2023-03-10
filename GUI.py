import tkinter as tk
from tkinter import ttk
import os
import csv

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Clash of Clans Spider")
        self.root.geometry("600x400")

        self.clan_tag_label = tk.Label(self.root, text="Enter clan tag:")
        self.clan_tag_label.pack(pady=10)

        self.clan_tag_entry = tk.Entry(self.root, width=40)
        self.clan_tag_entry.pack(pady=10)

        self.run_button = tk.Button(self.root, text="Run", command=self.run_spider)
        self.run_button.pack(pady=10)

        self.tree_frame = tk.Frame(self.root)
        self.tree_frame.pack(padx=20, pady=10)

        self.tree_scrollbar = ttk.Scrollbar(self.tree_frame)
        self.tree_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scrollbar.set)
        self.tree["columns"] = ("1", "2", "3", "4", "5")
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("1", width=100, anchor=tk.W)
        self.tree.column("2", width=100, anchor=tk.W)
        self.tree.column("3", width=100, anchor=tk.W)
        self.tree.column("4", width=100, anchor=tk.W)
        self.tree.column("5", width=100, anchor=tk.W)
        self.tree.heading("1", text="Townhall Level", anchor=tk.W)
        self.tree.heading("2", text="XP Level", anchor=tk.W)
        self.tree.heading("3", text="Current League", anchor=tk.W)
        self.tree.heading("4", text="Current Rank", anchor=tk.W)
        self.tree.heading("5", text="Trophies", anchor=tk.W)
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.tree_scrollbar.config(command=self.tree.yview)

        self.root.bind("<Return>", self.run_spider_event)

    def run_spider(self):
        clan_tag = self.clan_tag_entry.get()

        if clan_tag != "":
            with open("clan_tag.txt", "w") as f:
                f.write(clan_tag)

            os.system("python run_spider.py")

            for row in self.tree.get_children():
                self.tree.delete(row)

            # Display the scraped data in the treeview widget
            with open("data.csv", "r") as f:
                reader = csv.reader(f)
                next(reader)  # Skip the header row
                for row in reader:
                    self.tree.insert("", tk.END, values=row)

        else:
            self.tree.delete(*self.tree.get_children())
            self.tree.insert("", "end", text="Please enter a valid clan tag.")

    def run_spider_event(self, event):
        self.run_spider()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
