# Importa la biblioteca 'phonenumbers' que se utiliza para trabajar con números de teléfono
import phonenumbers

# Importa los módulos necesarios para obtener información sobre el número de teléfono
from phonenumbers import geocoder, carrier, timezone

# Define el número de teléfono que deseas analizar
number = "+000 000000000"

# Parsea el número de teléfono para su posterior análisis
parsed_number = phonenumbers.parse(number)

# Obtiene y muestra el país del número de teléfono en español
location = geocoder.description_for_number(parsed_number, "es")
print("Country:", location)

# Parsea nuevamente el número de teléfono para obtener información sobre el operador
service_provider = phonenumbers.parse(number)

# Obtiene y muestra el operador del número de teléfono en español
print("Operator:", carrier.name_for_number(service_provider, "es"))

# Obtiene y muestra la zona horaria asociada al número de teléfono
time_zone = timezone.time_zones_for_number(parsed_number)
print("Time Zone:", time_zone)
