# utils/equation_extractor.py
import re

def extract_equations(text):
    # Simple LaTeX-style or math pattern detection
    equations = re.findall(r"\$.*?\$|\[.*?\]|\(.*?\)", text)
    return [eq for eq in equations if any(char.isdigit() or char in "+-=*/^" for char in eq)]
