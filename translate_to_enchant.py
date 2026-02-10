import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk
import textwrap

def run_translator():
    sga_font = ImageFont.truetype("fonts/Minecraft_SGA_GG.ttf", 32)
    normal_font = ImageFont.truetype("arial.ttf", 20)

    root = tk.Tk()
    root.title("Minecraft Enchantment Translator")
    root.geometry("900x500")
    root.configure(bg="#0f172a")

    title = tk.Label(root, text="Minecraft Enchantment Translator",
                     font=("Arial", 20, "bold"), fg="white", bg="#0f172a")
    title.pack(pady=10)

    entry = tk.Text(root, height=4, font=("Arial", 14), bg="#111827", fg="white",
                    insertbackground="white", wrap="word")
    entry.pack(fill="x", padx=20, pady=10)

    canvas = tk.Canvas(root, bg="#020617", height=300, highlightthickness=0)
    canvas.pack(fill="both", padx=20, pady=10)

    def wrap_text(text, width=40):
        return "\n".join(textwrap.wrap(text, width))

    def update_text(event=None):
        text = entry.get("1.0", "end").strip()
        wrapped = wrap_text(text, 40)
        img = Image.new("RGB", (800, 300), "#020617")
        draw = ImageDraw.Draw(img)
       
        draw.text((10, 120), wrapped, font=sga_font, fill=(0, 255, 120))
        tk_img = ImageTk.PhotoImage(img)
        canvas.delete("all")
        canvas.create_image(0, 0, anchor="nw", image=tk_img)
        canvas.image = tk_img

    entry.bind("<KeyRelease>", update_text)
    root.mainloop()
