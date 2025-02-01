import re
import sys
import subprocess
from typing import List, Dict
from transformers import pipeline  # For Generative AI (e.g., Hugging Face Transformers)

class Compiler:
    def __init__(self):
        self.language = None
        self.ai_model = pipeline("text2text-generation", model="facebook/bart-large")  # Generative AI model

    def detect_language(self, code: str) -> str:
        """
        Detect the programming language (Python, Java, JavaScript, R, Kotlin, Jython) based on syntax.
        """
        python_patterns = [
            r'def\s+\w+\(',  # Function definitions
            r'print\s*\(',   # Print statements
            r'if\s+__name__\s*==\s*"__main__"',  # Main guard
            r'^\s*\w+\s*=\s*.+',  # Variable assignments
            r'import\s+\w+',  # Import statements
            r'for\s+\w+\s+in\s+.+',  # For loops
            r'while\s+.+:',  # While loops
            r'class\s+\w+:',  # Class definitions (note the colon at the end)
        ]
        java_patterns = [
            r'public\s+class\s+\w+',  # Class definitions
            r'System\.out\.println',  # Print statements
            r'void\s+main\s*\(',  # Main method
            r'import\s+java\.',  # Java imports
        ]
        javascript_patterns = [r'function\s+\w+\(', r'console\.log', r'let\s+\w+\s*=']
        r_patterns = [r'<-', r'print\(', r'function\s*\(']
        kotlin_patterns = [r'fun\s+\w+\(', r'println\(', r'class\s+\w+']
        jython_patterns = python_patterns  # Jython uses Python syntax

        # Debugging: Print which patterns are matched
        print("Python Patterns Matched:")
        for pattern in python_patterns:
            if re.search(pattern, code):
                print(f"Matched: {pattern}")

        print("Java Patterns Matched:")
        for pattern in java_patterns:
            if re.search(pattern, code):
                print(f"Matched: {pattern}")

        is_python = any(re.search(pattern, code) for pattern in python_patterns)
        is_java = any(re.search(pattern, code) for pattern in java_patterns)
        is_javascript = any(re.search(pattern, code) for pattern in javascript_patterns)
        is_r = any(re.search(pattern, code) for pattern in r_patterns)
        is_kotlin = any(re.search(pattern, code) for pattern in kotlin_patterns)
        is_jython = any(re.search(pattern, code) for pattern in jython_patterns)

        # Prioritize Java if Java patterns are matched
        if is_java:
            self.language = "Java"
        elif is_python:
            self.language = "Python"
        elif is_javascript:
            self.language = "JavaScript"
        elif is_r:
            self.language = "R"
        elif is_kotlin:
            self.language = "Kotlin"
        elif is_jython:
            self.language = "Jython"
        else:
            raise ValueError("Unable to determine the language or mixed patterns detected.")
        return self.language

    def lexical_analysis(self, code: str) -> List[str]:
        """
        Perform lexical analysis: Tokenize the input code.
        """
        tokens = re.findall(r'[\w]+|[{}()=;,.]', code)
        return tokens

    def syntax_analysis(self, tokens: List[str]) -> Dict:
        """
        Perform syntax analysis: Build a basic syntax tree.
        """
        # Placeholder for a syntax tree
        syntax_tree = {"tokens": tokens}
        return syntax_tree

    def semantic_analysis(self, syntax_tree: Dict):
        """
        Perform semantic analysis: Check for semantic correctness.
        """
        # Placeholder for semantic checks
        if "def" in syntax_tree["tokens"] and "(" not in syntax_tree["tokens"]:
            raise ValueError("Semantic Error: Function definition is incomplete.")

    def intermediate_code_generation(self, syntax_tree: Dict) -> str:
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
        elif self.language == "JavaScript":
            self._execute_javascript(code)
        elif self.language == "R":
            self._execute_r(code)
        elif self.language == "Kotlin":
            self._execute_kotlin(code)
        elif self.language == "Jython":
            self._execute_jython(code)

    def _execute_python(self, code: str):
        """
        Execute Python code directly.
        """
        # Try different Python commands in order
        python_commands = [ "python", "py"]
        for cmd in python_commands:
            try:
                print(f"Running Python code using {cmd}...")
                result = subprocess.run(
                    [cmd, "-c", code], capture_output=True, text=True
                )
                if result.returncode != 0:
                    print(f"Python Error ({cmd}):\n{result.stderr}")
                    self._recover_error(code, result.stderr)
                else:
                    print(f"Python Output ({cmd}):\n{result.stdout}")
                return  # Exit if successful
            except FileNotFoundError:
                continue  # Try the next command
            except Exception as e:
                print(f"Python Execution Error ({cmd}): {e}")
                return

        print("Python not found. Please ensure Python is installed and in PATH.")

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
                    self._recover_error(code, compile_result.stderr)
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

    def _execute_javascript(self, code: str):
        """
        Execute JavaScript code using Node.js.
        """
        try:
            print("Running JavaScript code...")
            result = subprocess.run(
                ["node", "-e", code], capture_output=True, text=True
            )
            if result.returncode != 0:
                print(f"JavaScript Error:\n{result.stderr}")
                self._recover_error(code, result.stderr)
            else:
                print(f"JavaScript Output:\n{result.stdout}")
        except FileNotFoundError as e:
            print("Node.js not found. Please ensure Node.js is installed and in PATH.")
        except Exception as e:
            print(f"JavaScript Execution Error: {e}")

    def _execute_r(self, code: str):
        """
        Execute R code using Rscript.
        """
        try:
            print("Running R code...")
            result = subprocess.run(
                ["Rscript", "-e", code], capture_output=True, text=True
            )
            if result.returncode != 0:
                print(f"R Error:\n{result.stderr}")
                self._recover_error(code, result.stderr)
            else:
                print(f"R Output:\n{result.stdout}")
        except FileNotFoundError as e:
            print("Rscript not found. Please ensure R is installed and in PATH.")
        except Exception as e:
            print(f"R Execution Error: {e}")

    def _execute_kotlin(self, code: str):
        """
        Execute Kotlin code using kotlinc and kotlin.
        """
        import os
        import tempfile

        try:
            # Create a temporary directory for the Kotlin file
            with tempfile.TemporaryDirectory() as tempdir:
                kotlin_file = os.path.join(tempdir, "TempProgram.kt")
                class_name = "TempProgramKt"

                # Write the Kotlin code to a file
                with open(kotlin_file, 'w') as f:
                    f.write(code)

                # Compile the Kotlin file
                compile_result = subprocess.run(
                    ["kotlinc", kotlin_file, "-d", tempdir], capture_output=True, text=True
                )
                if compile_result.returncode != 0:
                    print(f"Kotlin Compilation Error:\n{compile_result.stderr}")
                    self._recover_error(code, compile_result.stderr)
                    return

                # Run the compiled Kotlin class
                run_result = subprocess.run(
                    ["kotlin", "-cp", tempdir, class_name], capture_output=True, text=True
                )
                if run_result.returncode != 0:
                    print(f"Kotlin Runtime Error:\n{run_result.stderr}")
                else:
                    print(f"Kotlin Output:\n{run_result.stdout}")

        except FileNotFoundError as e:
            print("Kotlin tools (kotlinc/kotlin) not found. Please ensure Kotlin is installed and in PATH.")
        except Exception as e:
            print(f"Kotlin Execution Error: {e}")

    def _execute_jython(self, code: str):
        """
        Execute Jython code using jython.
        """
        try:
            print("Running Jython code...")
            result = subprocess.run(
                ["jython", "-c", code], capture_output=True, text=True
            )
            if result.returncode != 0:
                print(f"Jython Error:\n{result.stderr}")
                self._recover_error(code, result.stderr)
            else:
                print(f"Jython Output:\n{result.stdout}")
        except FileNotFoundError as e:
            print("Jython not found. Please ensure Jython is installed and in PATH.")
        except Exception as e:
            print(f"Jython Execution Error: {e}")

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