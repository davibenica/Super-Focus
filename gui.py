
import customtkinter as tk
import eyeDetector
import threading


tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")


class App(tk.CTk):
    def __init__(self):

        # Main setup
        super().__init__()
        self.title('Super Focus')
        self.geometry("500x350")
        
        # Main Menu
        self.menu = Menu(self)



        # Main loop
        self.mainloop()


class Menu(tk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        tk.CTkLabel(self, text ="Super Focus", font=("Roboto",24)).pack(pady=13, padx=10)
        
        

        self.PhoneNumberEntry = tk.CTkEntry(self, placeholder_text="Enter Phone Number")
        self.PhoneNumberEntry.pack(pady=12, padx=10)

        self.button = tk.CTkButton(self, text="Submit", command = self.displayNextFrame)
        self.button.pack(pady=13, padx=10)

        

        # Displays the frame
        self.pack(pady=20, padx=60, fill= "both",expand = True)


    # After user inputing the Phone Number this frame will apper
    def displayNextFrame(self):

        phoneNumber = self.PhoneNumberEntry.get()
        self.button.destroy()
        self.PhoneNumberEntry.destroy()
        tk.CTkLabel(self, text = "Currently Texting Number: " + phoneNumber, font=("Roboto",12)).pack(pady=13, padx=10)
        self.button = tk.CTkButton(self, text="Start Focus", command = lambda: self.start_detector(phoneNumber))
        self.button.pack(pady=13, padx=10)

        self.Stop_button = tk.CTkButton(self, text="Stop", command = lambda: self.stop_detector(),state = tk.DISABLED)
        self.Stop_button.pack(pady=13, padx=10)

    # Function to start the eyes detector
    def start_detector(self, phoneNumber):
        self.detector = eyeDetector.EyeDetector()
        self.detector_thread = threading.Thread(target=self.detector.StartDetector, args=(phoneNumber,))
        self.detector_thread.start()
        self.button.configure(state = tk.DISABLED)
        self.Stop_button.configure(state = tk.NORMAL)

    # Funtion to stop the eye detector
    def stop_detector(self):
        if self.detector_thread and self.detector_thread.is_alive() and self.detector:
            self.detector.turnDetectorOff()
            self.detector_thread.join()
            self.button.configure(state = tk.NORMAL)
            self.Stop_button.configure(state = tk.DISABLED)


            

App()
