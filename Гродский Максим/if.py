class House():
    def __init__(self, planet, country, edge, street, house):
        self.planet = planet
        self.country = country
        self.edge = edge
        self.street = street
        self.house = house
        print(f'My house {planet}, {country}, {edge}, {street}, {house}')
House('Марс', 'Россия', 'Краснодарский край', 'Красная', '45')
House('Земля', 'Германия', 'Большой', 'Черноморская', '141')
House('Юпитер', 'США', 'Маленький', 'Мира', '251')