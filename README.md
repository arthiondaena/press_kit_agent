# Project: Press Kit Automatic Generation and Quality Review AI Agent
This project is designed to automatically generate and review high-quality press kits for companies, leveraging AI. 
It processes company information, press kit topics, and preferred tone to draft press content tailored to specific contexts.

---
## Features
- **Automated Press Kit Generation**: Generate polished press kits with essential information such as company details, 
flagship product services, and major accomplishments.
- **Configurable Tone**: Customize the tone of the press kit to fit your needs (e.g., Professional, Formal, Casual).
- **Custom Topics**: Optionally specify personalized press kit topics for detailed customization.

---
## Prerequisites
1. **Python**: Ensure Python 3.8+ is installed.
2. **Dependencies**: Install required packages by running:

``` bash
   pip install -r requirements.txt
```

3. **Environment Variables**: Use a `.env` file to manage sensitive data such as Hugging Face tokens (HF_TOKEN).

---
## Setting Up the `.env` File
The `.env` file is crucial for securely managing the Hugging Face API Token (HF_TOKEN). Follow these steps:
1. In the project directory, create a `.env` file or ensure it is present.
2. Add the `HF_TOKEN` key with your token value in the format:

``` env
   HF_TOKEN="your_hugging_face_token"
```
The application automatically loads the `.env` file using `python-dotenv`.

---
## Running the Script
The script accepts command-line arguments for generating press kits. Use the following options with Python's `argparse` module.

### Basic Usage
Run the project using the `main.py` script:

``` bash
python main.py "Company information and achievements" [-t "Topic description"] [--tone "Preferred tone"]
```

### Arguments
- **`company_info`** _(required)_: Provide company details like name, flagship products, achievements, and other brand-specific information.
**Format**: `"Company name; Flagship product/service; Major achievements; Other details"`

- **`-t` or `--topic`**: Specify the topic of the press kit if you want to focus on a specific event or announcement.

**Example**:
``` bash
   python main.py "Tesla, Inc.; Flagship product: Electric vehicles; Achievements: Leading innovation in renewable energy." -t "Launch of a new AI-driven analysis platform targeting global markets"
```

- **`--tone`** _(optional)_: Set the tone for the press kit content (e.g., Professional, Formal, Informal).
**Default**: `"Professional"`

**Example**:
``` bash
   python main.py "Tesla, Inc.; Flagship product: Electric vehicles; Achievements: Leading innovation in renewable energy." --tone "Casual"
```

---
## Project Files
1. **`main.py` **: Entry point for the application. It processes command-line arguments and initiates the workflow.
2. **`.env` **: Stores environment variables like API tokens.
3. **`agents/`**: Contains the `ManagerAgent` class implementation for managing AI generation processes.
4. **`workflows/`**: Includes `press_kit_workflow`, orchestrating the press kit generation.