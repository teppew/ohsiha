import geocoder
import pycountry


def location_verifier(location):
    loc = location.split(", ")
    countries = []
    for country in pycountry.countries:
        countries.append(country.name)

    if len(loc) == 2 and loc[1] in countries:
        return True
    else:
        return False


def location_search(location):
    # [latitude, longitude]
    loc = geocoder.google(location, key="AIzaSyApdG_qanGoL47UuK-xtPzaou5__7qnVxc").latlng
    return loc


def main():
    a = [1,2,3,4,5]
    b = {'1': ['aasi', 'kissa'],
        '2': ['koira', 'kissa']
         }
    print(len(a))
    print(len(b))


main()
