import re
import sys
from typing import Union
import subprocess
from transformers import pipeline  # For Generative AI (e.g., Hugging Face Transformers)

class Compiler:
    def __init__(self):
        self.language = None
        self.ai_model = pipeline("text2text-generation", model="facebook/bart-large")  # Generative AI model

    def detect_language(self, code: str) -> str:
        """
        Detect the programming language (Python or Java) based on syntax.
        """
        python_patterns = [r'def\s+\w+\(', r'print\s*\(', r'if\s+__name__\s*==\s*"__main__"']
        java_patterns = [r'public\s+class\s+\w+', r'System\.out\.println', r'void\s+main\s*\(']

        is_python = any(re.search(pattern, code) for pattern in python_patterns)
        is_java = any(re.search(pattern, code) for pattern in java_patterns)

        if is_python and not is_java:
            self.language = "Python"
        elif is_java and not is_python:
            self.language = "Java"
        else:
            raise ValueError("Unable to determine the language or mixed patterns detected.")
        return self.language

    def lexical_analysis(self, code: str) -> list:
        """
        Perform lexical analysis: Tokenize the input code.
        """
        tokens = re.findall(r'[\w]+|[{}()=;,.]', code)
        return tokens

    def syntax_analysis(self, tokens: list):
        """
        Perform syntax analysis: Build a basic syntax tree.
        """
        # Placeholder for a syntax tree
        syntax_tree = {"tokens": tokens}
        return syntax_tree

    def semantic_analysis(self, syntax_tree):
        """
        Perform semantic analysis: Check for semantic correctness.
        """
        # Placeholder for semantic checks
        if "def" in syntax_tree["tokens"] and "(" not in syntax_tree["tokens"]:
            raise ValueError("Semantic Error: Function definition is incomplete.")

    def intermediate_code_generation(self, syntax_tree):
        """
        Generate intermediate representation (IR) from syntax tree.
        """
        ir = "INTERMEDIATE_CODE_REPRESENTATION"  # Placeholder IR
        return ir

    def code_optimization(self, ir: str) -> str:
        """
        Optimize the intermediate representation.
        """
        optimized_ir = ir.replace("INTERMEDIATE", "OPTIMIZED_INTERMEDIATE")
        return optimized_ir

    def target_code_generation(self, optimized_ir: str) -> str:
        """
        Generate target code from optimized intermediate representation.
        """
        target_code = optimized_ir.replace("OPTIMIZED_INTERMEDIATE", "MACHINE_CODE")
        return target_code

    def compile(self, code: str) -> None:
        """
        Compile the code based on the detected language, performing all phases.
        """
        tokens = self.lexical_analysis(code)
        syntax_tree = self.syntax_analysis(tokens)
        self.semantic_analysis(syntax_tree)
        ir = self.intermediate_code_generation(syntax_tree)
        optimized_ir = self.code_optimization(ir)
        target_code = self.target_code_generation(optimized_ir)

        if self.language == "Python":
            self._execute_python(code)
        elif self.language == "Java":
            self._execute_java(code)

    def _execute_python(self, code: str):
        """
        Execute Python code directly.
        """
        try:
            print("Running Python code...")
            exec(code)  # Warning: Use with caution; for demo purposes only.
        except Exception as e:
            print(f"Python Error: {e}")
            self._recover_error(code, str(e))

    def _execute_java(self, code: str):
        """
        Execute Java code by compiling and running it.
        """
        import os
        import tempfile

        try:
            # Create a temporary directory for the Java file
            with tempfile.TemporaryDirectory() as tempdir:
                java_file = os.path.join(tempdir, "TempProgram.java")
                class_name = "TempProgram"

                # Write the Java code to a file
                with open(java_file, 'w') as f:
                    f.write(code)

                # Compile the Java file
                compile_result = subprocess.run(
                    ["javac", java_file], capture_output=True, text=True
                )
                if compile_result.returncode != 0:
                    print(f"Java Compilation Error:\n{compile_result.stderr}")
                    return

                # Run the compiled Java class
                run_result = subprocess.run(
                    ["java", "-cp", tempdir, class_name], capture_output=True, text=True
                )
                if run_result.returncode != 0:
                    print(f"Java Runtime Error:\n{run_result.stderr}")
                else:
                    print(f"Java Output:\n{run_result.stdout}")

        except FileNotFoundError as e:
            print("Java tools (javac/java) not found. Please ensure JDK is installed and in PATH.")
        except Exception as e:
            print(f"Java Execution Error: {e}")



    def _recover_error(self, code: str, error_message: str):
        """
        Use Generative AI to suggest fixes for errors.
        """
        prompt = f"The following code has an error:\n{code}\nError message:\n{error_message}\nPlease suggest a corrected version of the code."
        try:
            suggestion = self.ai_model(prompt, max_length=512, truncation=True)[0]['generated_text']
            print("AI Suggestion for Fix:\n", suggestion)
        except Exception as e:
            print(f"Error in AI-based recovery: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python compiler.py <source_file>")
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        code = f.read()

    compiler = Compiler()
    try:
        language = compiler.detect_language(code)
        print(f"Detected language: {language}")
        compiler.compile(code)
    except ValueError as e:
        print(e)
