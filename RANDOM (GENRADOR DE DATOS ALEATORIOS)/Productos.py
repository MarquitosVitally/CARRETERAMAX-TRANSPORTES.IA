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
    "Pan integral": "50,000kg",
    "Refresco cola": "2,083L",
    "Yogur natural": "8,333L",
    "Paracetamol 500 mg": "500,000Kg",
    "Alcohol etílico": "1,388L",
    "Guantes de látex": "83,333Kg",
    "Playera de algodón": "125,000Kg",
    "Pantalón de mezclilla": "41,666Kg",
    "Sudadera deportiva": "31,250Kg",
    "Laptop 15”": "8,333Kg",
    "Smartphone gama media": "83,333Kg",
    "Audífonos inalámbricos": "100,000Kg",
    "Filtro de aceite": "16,666L",
    "Llanta rin 15": "2,777Kg",
    "Batería automotriz": "1,388Kg",
    "Cemento gris": "500Kg",
    "Varilla de 3/8": "500Kg",
    "Arena fina": "15Kg",
    "Solvente industrial": "1,388L",
    "Resinas plásticas": "1,000Kg",
    "Combustible ligero": "3L",
    "Cobre refinado": "1,000Kg",
    "Mineral de hierro": "25Kg",
    "Zinc procesado": "1,000Kg",
    "Maíz grano": "500Kg",
    "Fertilizante NPK": "500Kg",
    "Alimento para ganado": "500Kg",
    "Cajas chicas": "5,000Kg",
    "Sobres acolchados": "25,000Kg",
    "Etiquetas adhesivas": "50,000Kg",
    "Refrigerador 14 pies": "312Kg",
    "Escritorio MDF": "625Kg",
    "Silla acolchonada": "1,666Kg",
    "Películas Blu-ray": "5,000Kg",
    "Consolas de videojuegos": "6,250Kg",
    "Tarjetas de regalo": "12,500",
    "Toallas blancas": "2,500Kg",
    "Juego de sábanas": "8,333Kg",
    "Amenidades de baño": "3,125Kg",
    "Cartón corrugado": "31Kg",
    "Papel bond": "25Kg",
    "Cintas de embalaje": "125Kg",
    "Contenedores de reciclaje": "714Kg",
    "Bolsas industriales": "1,000Kg",
    "Compactadores pequeños": "41Kg"
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
