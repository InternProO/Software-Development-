import os
import spacy
from transformers import pipeline

# Initialize spaCy and transformers
nlp = spacy.load("en_core_web_sm")
summarizer = pipeline("summarization")

def extract_comments_from_code(file_path):
    """Extract comments from a source code file."""
    comments = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        inside_comment = False
        for line in lines:
            if line.strip().startswith('"""') or line.strip().startswith("'''"):
                inside_comment = not inside_comment
            elif inside_comment or line.strip().startswith('#'):
                comments.append(line.strip())
    return comments

def generate_documentation(comments):
    """Generate documentation from code comments."""
    full_text = " ".join(comments)
    doc = nlp(full_text)
    
    # Summarize comments to generate documentation
    summarized_text = summarizer(full_text, max_length=150, min_length=30, do_sample=False)
    return summarized_text[0]['summary_text']

def analyze_code_structure(file_path):
    """Analyze code structure for functions and classes."""
    with open(file_path, 'r') as file:
        code = file.read()
    functions = [line.split()[1].split('(')[0] for line in code.split('\n') if 'def ' in line]
    classes = [line.split()[1] for line in code.split('\n') if 'class ' in line]
    return functions, classes

def generate_code_documentation(file_path):
    """Generate code documentation from comments and structure."""
    comments = extract_comments_from_code(file_path)
    functions, classes = analyze_code_structure(file_path)
    documentation = generate_documentation(comments)
    
    # Combine documentation with code structure
    doc_structure = f"Functions: {', '.join(functions)}\nClasses: {', '.join(classes)}\n\n"
    full_documentation = doc_structure + documentation
    return full_documentation

if __name__ == "__main__":
    file_path = "example_code.py"  # Replace with your file path
    documentation = generate_code_documentation(file_path)
    print("Generated Documentation:\n")
    print(documentation)
