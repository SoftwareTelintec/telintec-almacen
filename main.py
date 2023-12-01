import customtkinter as ctk
from PIL import Image
from screens.Dashboard import Dashboard
from screens.Orders import Orders
from screens.Inventory import Inventory
from screens.Returns import Returns
from screens.Settings import Settings


class MainApp(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        self.after(0, lambda: self.state('zoomed'))
        self.title("Telintec Almacen")
        self._frame = None
        self.new_frame = None
        self._dashboard = Dashboard
        self._orders = Orders
        self._inventory = Inventory
        self._returns = Returns
        self._settings = Settings
        self.create_sidebar_frame(self)
        self.switch_frame(self._dashboard)

    def switch_frame(self, frame_class):
        print("Switching to", frame_class)
        print("Current frame:", self._frame)
        new_frame = frame_class(self)

        # If the new frame is the same as the current frame, do nothing
        if self._frame == new_frame:
            return

        # If there is no current frame, set the new frame as the current frame
        if self._frame is None:
            self._frame = new_frame
            return

        # If the current frame is different from the new frame, destroy the current frame and replace it with the new frame
        print("frame destroy?:", self._frame)
        print("New frame:", new_frame)
        self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def create_sidebar_frame(self, master):
        self.sidebar_frame = ctk.CTkFrame(master=self, fg_color="#04053A",
                                          width=220, height=650, corner_radius=0)
        self.sidebar_frame.pack_propagate(0)
        self.sidebar_frame.pack(fill="y", anchor="w", side="left")

        # logo icon
        self.logo_img_data = Image.open("./assets/logo.webp")
        self.logo_img = ctk.CTkImage(dark_image=self.logo_img_data,
                                     light_image=self.logo_img_data, size=(120, 75))

        ctk.CTkLabel(master=self.sidebar_frame, text="", image=self.logo_img).pack(
            pady=(40, 0), anchor="center")

        # analytics icon and Dashboard button
        self.analytics_img_data = Image.open("./assets/analytics_icon.png")
        self.analytics_img = ctk.CTkImage(dark_image=self.analytics_img_data,
                                          light_image=self.analytics_img_data)

        ctk.CTkButton(master=self.sidebar_frame,
                      image=self.analytics_img,
                      text="Dashboard",
                      font=(
                          "Arial Bold", 14),
                      fg_color="transparent",
                      text_color="#fff",
                      hover_color="#07096b",
                      anchor="w",
                      command=lambda:
                      master.switch_frame(self._dashboard)).pack(anchor="center", ipady=5, pady=(60, 0))

        # package icon and Orders button
        self.package_img_data = Image.open("./assets/package_icon.png")
        self.package_img = ctk.CTkImage(dark_image=self.package_img_data,
                                        light_image=self.package_img_data)

        ctk.CTkButton(master=self.sidebar_frame,
                      image=self.package_img,
                      text="Orders",
                      font=("Arial Bold", 14),
                      fg_color="transparent",
                      text_color="#fff",
                      hover_color="#07096b",
                      anchor="w",
                      command=lambda:
                      master.switch_frame(self._orders)).pack(anchor="center", ipady=5, pady=(16, 0))

        # list icon and Inventory button
        self.list_img_data = Image.open("./assets/list_icon.png")
        self.list_img = ctk.CTkImage(dark_image=self.list_img_data,
                                     light_image=self.list_img_data)
        ctk.CTkButton(master=self.sidebar_frame,
                      image=self.list_img,
                      text="Inventory",
                      font=(
                          "Arial Bold", 14),
                      fg_color="transparent",
                      text_color="#fff",
                      hover_color="#07096b",
                      anchor="w",
                      command=lambda:
                      master.switch_frame(self._inventory)).pack(anchor="center", ipady=5, pady=(16, 0))

        # returns icon and Returns button
        self.returns_img_data = Image.open("./assets/returns_icon.png")
        self.returns_img = ctk.CTkImage(dark_image=self.returns_img_data,
                                        light_image=self.returns_img_data)
        ctk.CTkButton(master=self.sidebar_frame,
                      image=self.returns_img,
                      text="Returns",
                      font=(
                          "Arial Bold", 14),
                      fg_color="transparent",
                      text_color="#fff",
                      hover_color="#07096b",
                      anchor="w",
                      command=lambda:
                      master.switch_frame(self._returns)).pack(anchor="center", ipady=5, pady=(16, 0))

        self.settings_img_data = Image.open("./assets/settings_icon.png")
        self.settings_img = ctk.CTkImage(dark_image=self.settings_img_data,
                                         light_image=self.settings_img_data)
        ctk.CTkButton(master=self.sidebar_frame,
                      image=self.settings_img,
                      text="Settings",
                      font=(
                          "Arial Bold", 14),
                      fg_color="transparent",
                      text_color="#fff",
                      hover_color="#07096b",
                      anchor="w",
                      command=lambda:
                      master.switch_frame(self._settings)).pack(anchor="center", ipady=5, pady=(16, 0))


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
