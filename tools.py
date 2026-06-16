# tools.py

from datetime import datetime


def calculator(expression):

    try:
        result = eval(expression)
        return str(result)

    except Exception as e:
        return str(e)


def weather(city):

    weather_data = {

        "hyderabad": "34°C Sunny",
        "delhi": "38°C Hot",
        "mumbai": "31°C Humid",
        "bangalore": "27°C Cloudy"

    }

    return weather_data.get(
        city.lower(),
        "Weather data not available"
    )


def current_time():

    return datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

def unit_converter(query):

    query = query.lower().strip()

    try:

        parts = query.split()

        value = float(parts[0])

        from_unit = parts[1]

        to_unit = parts[-1]

        if from_unit == "km" and to_unit in ["meter", "meters"]:
            return str(value * 1000)

        if from_unit in ["meter", "meters"] and to_unit == "km":
            return str(value / 1000)

        if from_unit == "kg" and to_unit in ["gram", "grams"]:
            return str(value * 1000)

        if from_unit in ["gram", "grams"] and to_unit == "kg":
            return str(value / 1000)

        return "Conversion not supported"

    except Exception:

        return "Invalid conversion format"
    
def bmi_calculator(data):

    try:

        values = data.split(",")

        weight = float(values[0])

        height = float(values[1])

        bmi = weight / (height ** 2)

        if bmi < 18.5:

            category = "Underweight"

        elif bmi < 25:

            category = "Normal Weight"

        elif bmi < 30:

            category = "Overweight"

        else:

            category = "Obese"

        return f"BMI = {bmi:.2f}, Category = {category}"

    except Exception:

        return "Invalid BMI input"

AVAILABLE_TOOLS = {

    "calculator": calculator,

    "weather": weather,

    "current_time": current_time,

    "unit_converter": unit_converter,

    "bmi_calculator": bmi_calculator

}
