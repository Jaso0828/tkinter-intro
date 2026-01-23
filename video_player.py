import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Modern Video Player")
root.geometry("900x650")

# Gornji menu bar
menu_frame = ctk.CTkFrame(root, height=40, fg_color="#1a1a2e")
menu_frame.pack(fill="x", padx=10, pady=(10,0))

btn_file = ctk.CTkButton(menu_frame, text="📁 Open", width=80, height=30, fg_color="transparent", hover_color="#2d2d44")
btn_file.pack(side="left", padx=5, pady=5)

btn_playlist = ctk.CTkButton(menu_frame, text="📋 Playlist", width=80, height=30, fg_color="transparent", hover_color="#2d2d44")
btn_playlist.pack(side="left", padx=5, pady=5)

# Video područje
video_frame = ctk.CTkFrame(root, fg_color="#0f0f1a", corner_radius=15)
video_frame.pack(fill="both", expand=True, padx=10, pady=10)

video_label = ctk.CTkLabel(video_frame, text="🎬\n\nDrag & Drop Video Here\nor click Open", 
                           font=("Arial", 20), text_color="#4a4a6a")
video_label.pack(expand=True)

# Progress bar
progress_frame = ctk.CTkFrame(root, fg_color="transparent", height=50)
progress_frame.pack(fill="x", padx=20)

time_left = ctk.CTkLabel(progress_frame, text="0:00", font=("Courier", 12), width=50)
time_left.pack(side="left")

progress_bar = ctk.CTkSlider(progress_frame, from_=0, to=100, height=8, 
                              button_color="#6c5ce7", button_hover_color="#a29bfe",
                              progress_color="#6c5ce7", fg_color="#2d2d44")
progress_bar.pack(side="left", fill="x", expand=True, padx=10)
progress_bar.set(35)

time_right = ctk.CTkLabel(progress_frame, text="3:45", font=("Courier", 12), width=50)
time_right.pack(side="right")

# Kontrole
controls_frame = ctk.CTkFrame(root, fg_color="transparent", height=80)
controls_frame.pack(fill="x", padx=10, pady=(0,15))

# Lijeva strana - volume
left_controls = ctk.CTkFrame(controls_frame, fg_color="transparent")
left_controls.pack(side="left", padx=20)

btn_volume = ctk.CTkButton(left_controls, text="🔊", width=40, height=40, 
                           fg_color="transparent", hover_color="#2d2d44", font=("Arial", 18))
btn_volume.pack(side="left")

volume_slider = ctk.CTkSlider(left_controls, from_=0, to=100, width=100, height=8,
                               button_color="#6c5ce7", progress_color="#6c5ce7")
volume_slider.pack(side="left", padx=5)
volume_slider.set(70)

# Sredina - playback kontrole
center_controls = ctk.CTkFrame(controls_frame, fg_color="transparent")
center_controls.pack(expand=True)

btn_prev = ctk.CTkButton(center_controls, text="⏮", width=50, height=50, 
                         fg_color="#2d2d44", hover_color="#3d3d54", font=("Arial", 20), corner_radius=25)
btn_prev.pack(side="left", padx=5)

btn_rewind = ctk.CTkButton(center_controls, text="⏪", width=50, height=50, 
                           fg_color="#2d2d44", hover_color="#3d3d54", font=("Arial", 20), corner_radius=25)
btn_rewind.pack(side="left", padx=5)

btn_play = ctk.CTkButton(center_controls, text="▶", width=70, height=70, 
                         fg_color="#6c5ce7", hover_color="#a29bfe", font=("Arial", 28), corner_radius=35)
btn_play.pack(side="left", padx=10)

btn_forward = ctk.CTkButton(center_controls, text="⏩", width=50, height=50, 
                            fg_color="#2d2d44", hover_color="#3d3d54", font=("Arial", 20), corner_radius=25)
btn_forward.pack(side="left", padx=5)

btn_next = ctk.CTkButton(center_controls, text="⏭", width=50, height=50, 
                         fg_color="#2d2d44", hover_color="#3d3d54", font=("Arial", 20), corner_radius=25)
btn_next.pack(side="left", padx=5)

# Desna strana - settings
right_controls = ctk.CTkFrame(controls_frame, fg_color="transparent")
right_controls.pack(side="right", padx=20)

btn_speed = ctk.CTkButton(right_controls, text="1x", width=40, height=40, 
                          fg_color="transparent", hover_color="#2d2d44", font=("Arial", 14))
btn_speed.pack(side="left", padx=5)

btn_fullscreen = ctk.CTkButton(right_controls, text="⛶", width=40, height=40, 
                               fg_color="transparent", hover_color="#2d2d44", font=("Arial", 18))
btn_fullscreen.pack(side="left", padx=5)

root.mainloop()