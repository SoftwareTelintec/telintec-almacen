from CTkTable import CTkTable
import customtkinter as ctk
from queries.data import Queries


class Inventory(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        self.fetching_data = Queries()
        self.pack_propagate(0)
        self.pack(fill="both", expand=True)
        self.main_view = ctk.CTkFrame(self, fg_color="#fff")
        self.main_view.pack_propagate(0)
        self.main_view.pack(fill="both", expand=True)

        # title frame
        self.title_frame = ctk.CTkFrame(
            master=self.main_view, fg_color="transparent")
        self.title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

        ctk.CTkLabel(master=self.title_frame, text="Inventory", font=("Arial Black", 25),
                     text_color="#04053A").pack(anchor="nw", side="left")

        ctk.CTkButton(master=self.title_frame,
                      text="+ New Product",
                      font=("Arial Black", 15),
                      text_color="#fff",
                      fg_color="#04053A",
                      hover_color="#07096b").pack(anchor="ne", side="right")

        self.search_container = ctk.CTkFrame(
            master=self.main_view, height=70, fg_color="#F0F0F0")
        self.search_container.pack(fill="x", pady=(45, 0), padx=30)

        ctk.CTkEntry(master=self.search_container,
                     width=305,
                     placeholder_text="Search Product",
                     border_color="#04053A",
                     border_width=2).pack(side="left", padx=(15, 0), pady=20)
        table_data = self.fetching_data.get_all_products()

        table_data.insert(0, ["Product ID", "Name", "Description",
                          "Price", "Stock", "CategoryId"])

        table_frame = ctk.CTkScrollableFrame(
            master=self.main_view, fg_color="transparent")
        table_frame.pack(expand=True, fill="both", padx=10, pady=50)
        table = CTkTable(master=table_frame, values=table_data, colors=[
                         "#a8a7a5", "#858381"], header_color="#04053A", hover_color="#B4B4B4")
        table.edit_row(0, text_color="#fff", hover_color="#04053A")
        table.pack(expand=True)
