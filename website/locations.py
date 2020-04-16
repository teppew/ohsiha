import geocoder
import pycountry


def location_verifier(location):
    loc = location.split(", ")

    countries = "Zimbabwe,Zhōnghuá Mínguó,Táiwān,Zhōngguó,Zambia,Yisra'el,Y Deyrnas Unedig,Xīnjiāpō,Wuliwya,Wallis-et-Futuna,Volívia,Viti,Việt Nam,Venezuela,Vanuatu,Uvea mo Futuna,Uruguay,Unitit Kinrick,United States Virgin Islands,United States,America,United Kingdom,uMzantsi Afrika,Ukraїna,Uganda,Uburundi,Tuvalu,Turks and Caicos Islands,Türkmenistan,Türkiye,Tūns,Tunes,Tšād,Trinidad and Tobago,Tonga,Tokelau,Tojikistan,Togo,Togo,Togo,Timor-Leste,Timor Lorosa'e,The Gambia,The Bahamas,Thai, Prathet Thai, Ratcha-anachak Thai,Tchad,Tanzania,Svizzera,Svizra,Sverige,Svalbard,Suriyah,Suriname,Suomi,Suisse,Suid-Afrika,Sudan Kusini,Sri Lankā,Srbija,South Sudan,South Africa,Soomaaliya,Solomon Islands,Solomon Aelan,Slovensko,Slovenija,Sint Maarten,Sint Maarten,Singapura,Singapur,Singapore,Sierra Leone,Shqipëria,Seychelles,Seychelles,Severna Makedonija,Sesel,Sénégal,Schweiz,São Tomé e Príncipe,San Marino,Sāmoa,Samoa,Sak'art'velo,Saint-Pierre et Miquelon,Saint-Martin,Saint-Barthélemy,Saint Vincent and the Grenadines,Saint Lucia,Saint Kitts and Nevis,Saint Helena, Ascension and Tristan da Cunha,Rwanda,Rossiya or Rossiâ,România,Rìoghachd Aonaichte,Ríocht Aontaithe,Réunion,République gabonaise,République du Congo,République démocratique du Congo,République Centrafricaine,République Arabe Sahraouie Démocratique,Republíki ya Kongó Demokratíki,Republíki ya Kongó,República Dominicana,República Árabe Saharaui Democrática,Qazaqstan,Qaṭar,Puerto Rico,Portugal,Polynésie française,Polska,Pitkern Ailen,Pitcairn Islands,Piruw,Pilipinas,Philippines,Perú,Paraguay,Paraguái,Papua Niugini,Papua Niugini,Papua New Guinea,Panamá,Pākistān,Paguot Thudän,Oumún,Österreich,O‘zbekiston,Nouvelle-Calédonie,Notte Mariånas,Northern Mariana Islands,Norge,Norfolk Island,Norf'k Ailen,Noreg,Niuē,Niue,Nippon,Nijeriya,Nihon,Nigeria,Niger,Nicaragua,Ngola,New Zealand,Nepāl,Nederland,Nederlân,Nauru,Naoero,Namibia,Namibia,Namibia,Namibia,Namibia,Namhan,Nàìjíríà,Naigeria,Myanma,Mūrītānyā,Muritan / Agawec,Múnegu,Moris,Montserrat,Mongol Uls,Monaco,Moldova,Moçambique,Misr or Masr,Mēxihco,México,Mayotte,Mauritius,Maurice,Martinique,Malta,Malta,Mali,Mali,Malēṣiyā,Malaysia,Malaŵi,Malawi,Mǎláixīyà,Magyarország,Madagasikara,Madagascar,Macau,Luxemburg,Luxembourg,Lubnān,Lietuva,Liechtenstein,Libya,Lībiyā,Liberia,Liban,Lëtzebuerg,Lesotho,Latvija,Lao,Kyrgyzstan,Kypros,Kuki Airani,Kosovo,Kosova,Kòrsou,Komori,Ködörösêse tî Bêafrîka,Kıbrıs,Kiribati,Kirgizija,Kenya,Kazakhstán,Kampuchea,Kalaallit Nunaat,Juzur al-Qamar,Jībūtī,Jersey,Jersey,Jèrri,Jamhuri ya Kidemokrasia ya Kongo,Jamaica,Ityop'ia,Italia,Israʼiyl,Isle of Man,Ísland,iSewula Afrika,Iritriya,Ireland,Îraq,Īrān,iNingizimu Afrika,iNingizimu Afrika,Indonesia,India,il-ikwet,Hrvatska,Hong Kong,Honduras,Heung Gong,Hellas,Hayastán,Hanguk as called in SK,Haïti,Guyane,Guyana,Guinée équatoriale,Guinée,Guinea Ecuatorial,Guiné-Bissau,Guiné Equatorial,Guernsey,Guatemala,Guam,Guåhån,Guadeloupe,Grønland,Grenada,Gine,Gine,Gibraltar,Ghana,Gana,Gana,Gaana,France,Føroyar,Finland,Filasṭīn,Fiji,Federated States of Micronesia,Falkland Islands,Færøerne,États-Unis,Eswatini,eSwatini,Estados Unidos,Espanya,Espanha,España,Espainia,Ertra,Ellan Vannin,El Salvador,Éire,Eesti,Ecuador,Dzayer,Druk Yul,Dominica,Djibouti,Dhivehi Raajje,Deutschland,Dawlat ul-Kuwayt,Danmark,Curaçao,Curaçao,Cuba,Crna Gora"
    countries = countries.split(",")

    #for country in pycountry.countries:
     #   countries.append(country.name)
    if len(loc) == 2 and loc[1] in countries:
        return True
    else:
        return False


def location_search(location):
    # [latitude, longitude]
    try:
        loc = geocoder.google(location, key="AIzaSyApdG_qanGoL47UuK-xtPzaou5__7qnVxc").latlng
    except:
        pass
    return loc


def main():
    location = "happy placeddedewf jrnbfjk34nfj"
    print(location_verifier(location))

main()
