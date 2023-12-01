import customtkinter as ctk


class Settings(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        self.pack_propagate(0)
        self.pack(fill="both", expand=True)
        self.main_view = ctk.CTkFrame(self, fg_color="#fff")
        self.main_view.pack_propagate(0)
        self.main_view.pack(fill="both", expand=True)

        # title frame
        self.title_frame = ctk.CTkFrame(
            master=self.main_view, fg_color="transparent")
        self.title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

        ctk.CTkLabel(master=self.title_frame, text="Settings", font=("Arial Black", 25),
                     text_color="#04053A").pack(anchor="nw", side="left")
