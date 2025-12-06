import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")

COUNTRY_MAP = {
    "AFGHANISTAN": "AF", "ALBANIA": "AL", "ALGERIA": "DZ", "ANDORRA": "AD",
    "ANGOLA": "AO", "ANTIGUA": "AG", "ARGENTINA": "AR", "ARMENIA": "AM",
    "AUSTRALIA": "AU", "AUSTRIA": "AT", "AZERBAIJAN": "AZ", "BAHAMAS": "BS",
    "BAHRAIN": "BH", "BANGLADESH": "BD", "BARBADOS": "BB", "BELARUS": "BY",
    "BELGIUM": "BE", "BELIZE": "BZ", "BENIN": "BJ", "BHUTAN": "BT",
    "BOLIVIA": "BO", "BOSNIA": "BA", "BOTSWANA": "BW", "BRAZIL": "BR",
    "BRUNEI": "BN", "BULGARIA": "BG", "BURKINA FASO": "BF", "BURUNDI": "BI",
    "CAMBODIA": "KH", "CAMEROON": "CM", "CANADA": "CA", "CAPE VERDE": "CV",
    "CENTRAL AFRICAN REPUBLIC": "CF", "CHAD": "TD", "CHILE": "CL", "CHINA": "CN",
    "COLOMBIA": "CO", "COMOROS": "KM", "CONGO": "CG", "DEMOCRATIC CONGO": "CD",
    "COSTA RICA": "CR", "CROATIA": "HR", "CUBA": "CU", "CYPRUS": "CY",
    "CZECHIA": "CZ", "DENMARK": "DK", "DJIBOUTI": "DJ", "DOMINICA": "DM",
    "DOMINICAN REPUBLIC": "DO", "ECUADOR": "EC", "EGYPT": "EG", "EL SALVADOR": "SV",
    "EQUATORIAL GUINEA": "GQ", "ERITREA": "ER", "ESTONIA": "EE", "ESWATINI": "SZ",
    "ETHIOPIA": "ET", "FIJI": "FJ", "FINLAND": "FI", "FRANCE": "FR",
    "GABON": "GA", "GAMBIA": "GM", "GEORGIA": "GE", "GERMANY": "DE",
    "GHANA": "GH", "GREECE": "GR", "GRENADA": "GD", "GUATEMALA": "GT",
    "GUINEA": "GN", "GUINEA-BISSAU": "GW", "GUYANA": "GY", "HAITI": "HT",
    "HONDURAS": "HN", "HUNGARY": "HU", "ICELAND": "IS", "INDIA": "IN",
    "INDONESIA": "ID", "IRAN": "IR", "IRAQ": "IQ", "IRELAND": "IE",
    "ISRAEL": "IL", "ITALY": "IT", "JAMAICA": "JM", "JAPAN": "JP",
    "JORDAN": "JO", "KAZAKHSTAN": "KZ", "KENYA": "KE", "KIRIBATI": "KI",
    "KUWAIT": "KW", "KYRGYZSTAN": "KG", "LAOS": "LA", "LATVIA": "LV",
    "LEBANON": "LB", "LESOTHO": "LS", "LIBERIA": "LR", "LIBYA": "LY",
    "LIECHTENSTEIN": "LI", "LITHUANIA": "LT", "LUXEMBOURG": "LU", "MADAGASCAR": "MG",
    "MALAWI": "MW", "MALAYSIA": "MY", "MALDIVES": "MV", "MALI": "ML",
    "MALTA": "MT", "MARSHALL ISLANDS": "MH", "MAURITANIA": "MR", "MAURITIUS": "MU",
    "MEXICO": "MX", "MICRONESIA": "FM", "MOLDOVA": "MD", "MONACO": "MC",
    "MONGOLIA": "MN", "MONTENEGRO": "ME", "MOROCCO": "MA", "MOZAMBIQUE": "MZ",
    "MYANMAR": "MM", "NAMIBIA": "NA", "NAURU": "NR", "NEPAL": "NP",
    "NETHERLANDS": "NL", "NEW ZEALAND": "NZ", "NICARAGUA": "NI", "NIGER": "NE",
    "NIGERIA": "NG", "NORTH KOREA": "KP", "NORTH MACEDONIA": "MK", "NORWAY": "NO",
    "OMAN": "OM", "PAKISTAN": "PK", "PALAU": "PW", "PALESTINE": "PS",
    "PANAMA": "PA", "PAPUA NEW GUINEA": "PG", "PARAGUAY": "PY", "PERU": "PE",
    "PHILIPPINES": "PH", "POLAND": "PL", "PORTUGAL": "PT", "QATAR": "QA",
    "ROMANIA": "RO", "RUSSIA": "RU", "RWANDA": "RW", "SAINT KITTS & NEVIS": "KN",
    "SAINT LUCIA": "LC", "SAINT VINCENT & GRENADINES": "VC", "SAMOA": "WS",
    "SAN MARINO": "SM", "SAO TOME & PRINCIPE": "ST", "SAUDI ARABIA": "SA",
    "SENEGAL": "SN", "SERBIA": "RS", "SEYCHELLES": "SC", "SIERRA LEONE": "SL",
    "SINGAPORE": "SG", "SLOVAKIA": "SK", "SLOVENIA": "SI", "SOLOMON ISLANDS": "SB",
    "SOMALIA": "SO", "SOUTH AFRICA": "ZA", "SOUTH KOREA": "KR", "SOUTH SUDAN": "SS",
    "SPAIN": "ES", "SRI LANKA": "LK", "SUDAN": "SD", "SURINAME": "SR",
    "SWEDEN": "SE", "SWITZERLAND": "CH", "SYRIA": "SY", "TAIWAN": "TW",
    "TAJIKISTAN": "TJ", "TANZANIA": "TZ", "THAILAND": "TH", "TIMOR-LESTE": "TL",
    "TOGO": "TG", "TONGA": "TO", "TRINIDAD & TOBAGO": "TT", "TUNISIA": "TN",
    "TURKEY": "TR", "TURKMENISTAN": "TM", "TUVALU": "TV", "UGANDA": "UG",
    "UKRAINE": "UA", "UNITED ARAB EMIRATES": "AE", "UNITED KINGDOM": "GB",
    "UNITED STATES": "US", "URUGUAY": "UY", "UZBEKISTAN": "UZ", "VANUATU": "VU",
    "VATICAN CITY": "VA", "VENEZUELA": "VE", "VIETNAM": "VN", "YEMEN": "YE",
    "ZAMBIA": "ZM", "ZIMBABWE": "ZW",
}

def parse_location(location: str) -> str:
    """Turn user input into city,country format for OpenWeatherMap."""
    location = location.strip()

    # Space-separated (like "London UK" or "New York USA")
    if " " in location and "," not in location:
        *city_parts, country_part = location.split()
        country_corrected = COUNTRY_MAP.get(country_part.upper(), country_part)
        city_name = " ".join(city_parts)
        return f"{city_name},{country_corrected}"

    # Comma-separated (like "London,UK")
    elif "," in location:
        city_name, country_part = map(str.strip, location.split(",", 1))
        country_corrected = COUNTRY_MAP.get(country_part.upper(), country_part)
        return f"{city_name},{country_corrected}"

    # Only city provided, no country
    return location

def get_weather(city_country: str) -> str:
    if not API_KEY:
        return "Weather service is not configured. Please set the API key."

    # Parse/normalize location
    location = parse_location(city_country)

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        city_name = data.get("name")
        country = data.get("sys", {}).get("country")
        temp = data.get("main", {}).get("temp")
        weather_desc = data.get("weather", [{}])[0].get("description", "unknown")
        humidity = data.get("main", {}).get("humidity")
        wind_speed = data.get("wind", {}).get("speed")

        return (f"🌤 Weather for **{city_name}, {country}**:\n"
                f"Temperature: {temp}°C\n"
                f"Condition: {weather_desc.title()}\n"
                f"Humidity: {humidity}%\n"
                f"Wind speed: {wind_speed} m/s")

    except requests.HTTPError as http_err:
        if response.status_code == 404:
            return f"City '{location}' not found. Please check the spelling."
        return f"HTTP error occurred: {http_err}"
    except Exception as e:
        return f"Error fetching weather: {e}"
