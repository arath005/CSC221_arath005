def city_country(city, country, population=500000):
    """Return a string representing a city-country pair."""

    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f" - population {population}"
    return output_string