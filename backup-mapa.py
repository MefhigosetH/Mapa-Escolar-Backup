"""
Rutina Python para realizar backup de la info publicada en Mapa Escolar
"""
import json

def obtener_capas(base_url: str) -> dict:
    """ Descarga la informacion de capas disponibles en la plataforma y la devuelve en forma de objeto. """

    try:
        # El servidor se comunica con SSLv3 y esto dispara una excepcion al hacer el request.
        #req = requests.get(f"{base_url}/capas")
        #return req.json()

        with open('res/capas_mock.json', 'r') as f:
            data = json.load(f)

        return data

    except Exception as e:
        raise Exception("Error en obtener_capas():", e)



if __name__ == "__main__":
    base_url = "https://mapaescolar.abc.gob.ar"

    try:
        data = obtener_capas(base_url)

        for categoria in data:
            print(categoria["titulo"])

            for capa in categoria["children"]:
                print("|___", capa["name"])

                for parametro in capa["parametros"]:
                    print("|    |___", parametro["titulo"])

    except Exception as e:
        print("Error:", e)