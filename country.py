class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.population > 250*10*6 or self.are > 3*10**6

    def compare_pd(self, other_country):
        if self.population/self.area > other_country.population/other_country.area:
            print(
                f"{self.name} has larger population density than {other_country.name}")
        if self.population/self.area < other_country.population/other_country.area:
            print(
                f"{self.name} has smaller population density than {other_country.name}")


australia = Country('australia', 23545500, 7692024)
andorra = Country('andorra', 76098, 468)
print(australia.is_big)
print(andorra.is_big)

andorra.compare_pd(australia)
australia.compare_pd(andorra)
