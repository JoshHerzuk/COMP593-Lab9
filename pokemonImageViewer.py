from tkinter import *
from tkinter import ttk
from pokeAPI import get_pokemon_names, get_pokemon_image_url
from library import download_image_from_url, set_desktop_background
import os
import sys
import ctypes

def main():

    script_dir = sys.path[0]
    image_dir = os.path.join(script_dir, 'images')
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    #creates the window
    root = Tk()
    root.title('Pokemon Image Viewer')
    app_id = 'pokemon.image.viewer'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    root.iconbitmap(os.path.join(script_dir, 'pokeball.ico'))
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.minsize(500, 600)

    #creates a frame inside the window
    frm = ttk.Frame(root)
    frm.grid(sticky = (N,S,E,W))
    frm.rowconfigure(0, weight=9)
    frm.columnconfigure(0, weight=1)

    img_poke = PhotoImage(file = os.path.join(script_dir, 'pokeball.png'))
    lbl_img = ttk.Label(frm, image = img_poke)
    lbl_img.grid(row=0, column=0, padx=10, pady=10)

    pokemon_list = get_pokemon_names(limit=2000)
    pokemon_list.sort()
    pokemon_list = [p.capitalize() for p in pokemon_list]

    #created the combobox with the list of pokemon
    cbo_pokemon = ttk.Combobox(frm, values = pokemon_list, state = 'readonly')
    cbo_pokemon.set('Select a Pokemon')
    cbo_pokemon.grid(row=1, column=0, padx=10, pady=10)


    def handle_poke_select(event):
        """
        Defines what happens when the user selects a Pokemon
        :returns: NONE
        """

        selection = cbo_pokemon.get()#gets the name of the pokemon that was selected
        image_url = get_pokemon_image_url(selection)
        image_path = os.path.join(image_dir, selection + '.png')#sets the path where the image is downloaded
        download_image_from_url(image_url, image_path)
        img_poke['file'] = image_path#changes the shown Pokemon to the selected one
        btn_desktop.state(['!disabled'])#enables the "set image as desktop" button


    cbo_pokemon.bind('<<ComboboxSelected>>', handle_poke_select)

    def handle_btn_press():
        """
        Defines what happens when the "Set Image as Desktop" button is pressed
        :returns: NONE
        """
        selection = cbo_pokemon.get()
        image_path = os.path.join(image_dir, selection + '.png')
        set_desktop_background(image_path)

    #creates the button
    btn_desktop = ttk.Button(frm, text = 'Set Image as Desktop', command=handle_btn_press)
    btn_desktop.state(['disabled'])
    btn_desktop.grid(row=2, column=0, padx=10, pady=10)

    root.mainloop()


main()
