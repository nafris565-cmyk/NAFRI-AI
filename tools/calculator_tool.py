def calculate(expression):
    try:
        expr = expression.strip()
        expr = expr.replace("calc", "").strip()
        allowed_chars = "0123456789+-*/().% "
        for ch in expr:
            if ch not in allowed_chars:
                return "Sorry, I can only calculate numbers and + - * /"
        result = eval(expr, {"__builtins__": {}}, {})
        return f"Result of {expr} is {result}"
    except Exception as e:
        return f"Calculation Error: {e}"