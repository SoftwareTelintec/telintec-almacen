from CTkTable import CTkTable
from PIL import Image
import customtkinter as ctk
from queries.data import Queries


class Orders(ctk.CTkFrame):
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

        ctk.CTkLabel(master=self.title_frame, text="Orders", font=("Arial Black", 25),
                     text_color="#04053A").pack(anchor="nw", side="left")

        ctk.CTkButton(master=self.title_frame,
                      text="+ New Order",
                      font=("Arial Black", 15),
                      text_color="#fff",
                      fg_color="#04053A",
                      hover_color="#07096b").pack(anchor="ne", side="right")

        self.metrics_frame = ctk.CTkFrame(
            master=self.main_view, fg_color="transparent")
        self.metrics_frame.pack(anchor="n", fill="x",  padx=27, pady=(36, 0))

        self.orders_metric = ctk.CTkFrame(master=self.metrics_frame,
                                          fg_color="#04053A", width=200, height=60)
        self.orders_metric.grid_propagate(0)
        self.orders_metric.pack(side="left")

        self.logitics_img_data = Image.open("./assets/logistics_icon.png")
        self.logistics_img = ctk.CTkImage(light_image=self.logitics_img_data,
                                          dark_image=self.logitics_img_data, size=(43, 43))

        ctk.CTkLabel(master=self.orders_metric, image=self.logistics_img, text="").grid(
            row=0, column=0, rowspan=2, padx=(12, 5), pady=10)

        ctk.CTkLabel(master=self.orders_metric, text="Orders", text_color="#fff",
                     font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
        ctk.CTkLabel(master=self.orders_metric, text="123", text_color="#fff", font=(
            "Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0, 10))

        self.shipped_metric = ctk.CTkFrame(master=self.metrics_frame,
                                           fg_color="#04053A", width=200, height=60)
        self.shipped_metric.grid_propagate(0)
        self.shipped_metric.pack(side="left", expand=True, anchor="center")

        self.shipping_img_data = Image.open("./assets/shipping_icon.png")
        self.shipping_img = ctk.CTkImage(light_image=self.shipping_img_data,
                                         dark_image=self.shipping_img_data, size=(43, 43))

        ctk.CTkLabel(master=self.shipped_metric, image=self.shipping_img, text="").grid(
            row=0, column=0, rowspan=2, padx=(12, 5), pady=10)

        ctk.CTkLabel(master=self.shipped_metric, text="Shipping", text_color="#fff",
                     font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
        ctk.CTkLabel(master=self.shipped_metric, text="91", text_color="#fff", font=(
            "Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0, 10))

        self.delivered_metric = ctk.CTkFrame(
            master=self.metrics_frame, fg_color="#04053A", width=200, height=60)
        self.delivered_metric.grid_propagate(0)
        self.delivered_metric.pack(side="right",)

        self.delivered_img_data = Image.open("./assets/delivered_icon.png")
        self.delivered_img = ctk.CTkImage(light_image=self.delivered_img_data,
                                          dark_image=self.delivered_img_data, size=(43, 43))

        ctk.CTkLabel(master=self.delivered_metric, image=self.delivered_img, text="").grid(
            row=0, column=0, rowspan=2, padx=(12, 5), pady=10)

        ctk.CTkLabel(master=self.delivered_metric, text="Delivered", text_color="#fff",
                     font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
        ctk.CTkLabel(master=self.delivered_metric, text="23", text_color="#fff", font=(
            "Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0, 10))

        self.search_container = ctk.CTkFrame(
            master=self.main_view, height=50, fg_color="#F0F0F0")
        self.search_container.pack(fill="x", pady=(45, 0), padx=27)

        ctk.CTkEntry(master=self.search_container,
                     width=305,
                     placeholder_text="Search Order",
                     border_color="#2A8C55",
                     border_width=2).pack(side="left", padx=(13, 0), pady=15)

        ctk.CTkComboBox(master=self.search_container,
                        width=125,
                        values=["Date", "Most Recent Order", "Least Recent Order"], button_color="#2A8C55",
                        border_color="#2A8C55",
                        border_width=2,
                        button_hover_color="#207244",
                        dropdown_hover_color="#207244",
                        dropdown_fg_color="#2A8C55",
                        dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)

        ctk.CTkComboBox(master=self.search_container,
                        width=125,
                        values=["Status", "Processing", "Confirmed",
                                "Packing", "Shipping", "Delivered", "Cancelled"],
                        button_color="#2A8C55", border_color="#2A8C55",
                        border_width=2,
                        button_hover_color="#207244",
                        dropdown_hover_color="#207244",
                        dropdown_fg_color="#2A8C55",
                        dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)

        table_data = self.fetching_data.get_all_products()

        table_data.insert(0, ["Product ID", "Name", "Description",
                          "Price", "Stock", "CategoryId"])

        table_frame = ctk.CTkScrollableFrame(
            master=self.main_view, fg_color="transparent")
        table_frame.pack(expand=True, fill="both", padx=10, pady=30)
        table = CTkTable(master=table_frame, values=table_data, colors=[
                         "#a8a7a5", "#858381"], header_color="#04053A", hover_color="#B4B4B4")
        table.edit_row(0, text_color="#fff", hover_color="#04053A")
        table.pack(expand=True)
