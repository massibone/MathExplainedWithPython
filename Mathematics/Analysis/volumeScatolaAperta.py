'''
con un quadrato di lato a è stata costruita
una scatolas rettangolare aperta di altezza x. il volume V della scatola è V=x(a-2x)^2
'''
def calcola_volume(a, x):
    # Calcolo del volume della scatola rettangolare aperta
    V = x * (a - 2 * x) ** 2
    return V

