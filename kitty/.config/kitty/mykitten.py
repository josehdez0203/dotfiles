from typing import List
from kitty.boss import Boss

def main(args: List[str]) -> str:
    def mostrar_menu(lista):
        for i, opcion in enumerate(lista):
            print(f"{i+1}. {opcion}")

    # Lista de opciones para el menú
    opciones = ["Perrona", "github", "odoo", "odoo2"]
    passwords = [
        'TRhd"L]s{Kk<,7!,4cHT6Q.6k(v$KWqg',
        "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",
        "s5&zh5jT",
        ".Fedrojesa11235813",
    ]

    # Mostrar el menú
    mostrar_menu(opciones)

    # Pedir al usuario que seleccione una opción
    opcion_seleccionada = int(input("Selecciona una opción: "))
    # this is the main entry point of the kitten, it will be executed in
    # the overlay window when the kitten is launched
        # whatever this function returns will be available in the
    # handle_result() function
    opcion_seleccionada=opcion_seleccionada-1
    if opcion_seleccionada>=0 and opcion_seleccionada<=3:
        return passwords[opcion_seleccionada]
    else:
        return opcion_seleccionada

def handle_result(args: List[str], answer: str, target_window_id: int, boss: Boss) -> None:
    # get the kitty window into which to paste answer
    w = boss.window_id_map.get(target_window_id)
    if w is not None:
        w.paste_text(answer)
