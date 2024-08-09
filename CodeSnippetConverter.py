def python_to_js_converter(python_code):
    # Replace Python-specific syntax with JavaScript equivalents
    js_code = python_code.replace("print(", "console.log(")
    # Add more conversions as needed
    return js_code

# Example usage
python_code = "print('Hello, world!')"
js_code = python_to_js_converter(python_code)
print(js_code)
