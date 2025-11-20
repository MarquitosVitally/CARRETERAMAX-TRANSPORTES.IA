import random

# Diccionario completo: Industria → Empresa
empresas = {
    "Alimentos y Bebidas": "DeliciaMax Foods",
    "Farmacéutica y Salud": "FarmaNova Global",
    "Textil y Moda": "UrbanLine Clothing",
    "Tecnología y Electrónica": "TechFound Systems",
    "Automotriz": "Titan Motors Co.",
    "Construcción": "Constructora Ápex",
    "Química y Petroquímica": "PetroChem Solutions",
    "Minería y Metalurgia": "DeepRock Mining",
    "Agricultura y Ganadería": "AgroTerra Group",
    "E-commerce y Paquetería": "FastRoute Express",
    "Muebles y Línea Blanca": "HomeLine Furnishings",
    "Industria del Entretenimiento": "Stellar Media Group",
    "Hotelería y Turismo": "Horizon Grand Hotels",
    "Papel, Cartón y Empaques": "EcoPack Solutions",
    "Logística de Residuos": "GreenCycle Systems"
}

# Productos por industria
productos = {
    "Alimentos y Bebidas": ["Pan integral", "Refresco cola", "Yogur natural"],
    "Farmacéutica y Salud": ["Paracetamol 500 mg", "Alcohol etílico", "Guantes de látex"],
    "Textil y Moda": ["Playera de algodón", "Pantalón de mezclilla", "Sudadera deportiva"],
    "Tecnología y Electrónica": ["Laptop 15”", "Smartphone gama media", "Audífonos inalámbricos"],
    "Automotriz": ["Filtro de aceite", "Llanta rin 15", "Batería automotriz"],
    "Construcción": ["Cemento gris", "Varilla de 3/8", "Arena fina"],
    "Química y Petroquímica": ["Solvente industrial", "Resinas plásticas", "Combustible ligero"],
    "Minería y Metalurgia": ["Cobre refinado", "Mineral de hierro", "Zinc procesado"],
    "Agricultura y Ganadería": ["Maíz grano", "Fertilizante NPK", "Alimento para ganado"],
    "E-commerce y Paquetería": ["Cajas chicas", "Sobres acolchados", "Etiquetas adhesivas"],
    "Muebles y Línea Blanca": ["Refrigerador 14 pies", "Escritorio MDF", "Silla acolchonada"],
    "Industria del Entretenimiento": ["Películas Blu-ray", "Consolas de videojuegos", "Tarjetas de regalo"],
    "Hotelería y Turismo": ["Toallas blancas", "Juego de sábanas", "Amenidades de baño"],
    "Papel, Cartón y Empaques": ["Cartón corrugado", "Papel bond", "Cintas de embalaje"],
    "Logística de Residuos": ["Contenedores de reciclaje", "Bolsas industriales", "Compactadores pequeños"]
}

# Cantidades por producto
cantidades = {
    "Pan integral": "50,000",
    "Refresco cola": "2,083",
    "Yogur natural": "8,333",
    "Paracetamol 500 mg": "500,000",
    "Alcohol etílico": "1,388",
    "Guantes de látex": "83,333",
    "Playera de algodón": "125,000",
    "Pantalón de mezclilla": "41,666",
    "Sudadera deportiva": "31,250",
    "Laptop 15”": "8,333",
    "Smartphone gama media": "83,333",
    "Audífonos inalámbricos": "100,000",
    "Filtro de aceite": "16,666",
    "Llanta rin 15": "2,777",
    "Batería automotriz": "1,388",
    "Cemento gris": "500",
    "Varilla de 3/8": "500",
    "Arena fina": "15",
    "Solvente industrial": "1,388",
    "Resinas plásticas": "1,000",
    "Combustible ligero": "3",
    "Cobre refinado": "1,000",
    "Mineral de hierro": "25",
    "Zinc procesado": "1,000",
    "Maíz grano": "500",
    "Fertilizante NPK": "500",
    "Alimento para ganado": "500",
    "Cajas chicas": "5,000",
    "Sobres acolchados": "25,000",
    "Etiquetas adhesivas": "50,000",
    "Refrigerador 14 pies": "312",
    "Escritorio MDF": "625",
    "Silla acolchonada": "1,666",
    "Películas Blu-ray": "5,000",
    "Consolas de videojuegos": "6,250",
    "Tarjetas de regalo": "12,500",
    "Toallas blancas": "2,500",
    "Juego de sábanas": "8,333",
    "Amenidades de baño": "3,125",
    "Cartón corrugado": "31",
    "Papel bond": "25",
    "Cintas de embalaje": "125",
    "Contenedores de reciclaje": "714",
    "Bolsas industriales": "1,000",
    "Compactadores pequeños": "41"
}

# Selección aleatoria
industria = random.choice(list(empresas.keys()))
empresa = empresas[industria]
producto = random.choice(productos[industria])
cantidad = cantidades[producto]


# RESULTADO FINAL
print(f"Empresa: {empresa}")
print(f"Industria: {industria}")
print(f"Producto a transportar: {producto}")
print(f"Cantidad a transportar: {cantidad}")
