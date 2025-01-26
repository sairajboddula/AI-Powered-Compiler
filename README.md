# AI-Powered Compiler

This project is an AI-powered compiler capable of detecting programming languages (Python or Java), analyzing the code, generating intermediate and optimized code representations, and executing or simulating the code.

## Prerequisites

1. **Python Installation**: Ensure Python 3.8 or later is installed on your system.
2. **Java Installation** (for running Java code):
   - Install the Java Development Kit (JDK).
   - Add the JDK `bin` directory to your system PATH.
3. **Libraries**:
   - `transformers` (Hugging Face Transformers for Generative AI).
   Install using pip:
   ```bash
   pip install transformers
   ```
4. **Environment Setup**:
   - Ensure both `python` and `java` commands are accessible from the terminal.

## Features

1. **Language Detection**:
   - Automatically detects whether the input code is Python or Java.
2. **Compiler Phases**:
   - Lexical Analysis: Tokenizes the input code.
   - Syntax Analysis: Constructs a basic syntax tree.
   - Semantic Analysis: Checks for semantic correctness.
   - Intermediate Code Generation.
   - Code Optimization.
   - Target Code Generation.
3. **Execution**:
   - Executes Python code directly.
   - Compiles and executes Java code using `javac` and `java`.
4. **Error Recovery**:
   - Uses Generative AI to suggest fixes for syntax or runtime errors in Python code.

## How to Run the Compiler

1. Save your Python or Java code to a file. For example:

   - Python file: `program.py`
     ```python
     print("Hello, world!")
     ```
   - Java file: `program.java`
     ```java
     public class TempProgram {
         public static void main(String[] args) {
             for (int i = 0; i < 5; i++) {
                 System.out.println(i);
             }
         }
     }
     ```

2. Run the compiler with the file as an argument:

   ```bash
   python compiler.py <source_file>
   ```

   Example:

   ```bash
   python compiler.py program.py
   ```

3. The compiler will:

   - Detect the language.
   - Compile and execute the code.

## Pros and Cons

### Pros:

- **Language Detection**: Automatically identifies Python and Java code.
- **AI-Powered Error Recovery**: Suggests fixes for Python errors using Generative AI.
- **Complete Compilation Pipeline**: Implements all major compiler phases.
- **Cross-Language Support**: Supports both Python and Java.

### Cons:

- **Limited Java Execution**: Requires a functioning JDK and assumes the presence of `javac` and `java` in PATH.
- **Generative AI Dependency**: Error recovery relies on Hugging Face Transformers, which requires internet access and model downloads.
- **Security**: The use of `exec` for Python execution poses potential security risks.

## Repository Structure

- `compiler.py`: Main compiler script.
- Example files:
  - `program.py`: Example Python script.
  - `program.java`: Example Java script.

## Troubleshooting

1. **Java Not Detected**:
   - Ensure the JDK is installed.
   - Check if `javac` and `java` commands work in your terminal.
2. **Library Issues**:
   - Run `pip install transformers` to install missing libraries.
3. **Permission Errors**:
   - Ensure you have read/write permissions for the directory where the scripts are stored.

## Future Improvements

- Add support for more programming languages.
- Implement real-time debugging features.
- Expand AI-based recovery to Java and other languages.

## License

This project is open-source and available under the MIT License.

