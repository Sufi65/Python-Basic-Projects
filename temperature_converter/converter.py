class TemperatureConverter:

    def c_to_f(self, c):
        return (c * 9/5) + 32

    def f_to_c(self, f):
        return (f - 32) * 5/9

    def c_to_k(self, c):
        return c + 273.15

if __name__ == "__main__":
    converter = TemperatureConverter()
    print("=== Temperature Converter ===")
    print("Celsius to Fahrenheit:", converter.c_to_f(37))
    print("Fahrenheit to Celsius:", converter.f_to_c(98))
    print("Celsius to Kelvin:", converter.c_to_k(25))