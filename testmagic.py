import ascii_magic
url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/491.png"

poke_img = ascii_magic.from_url(url, columns = 100)
ascii_magic.to_terminal(poke_img)