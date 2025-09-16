Open Project Folder: Launch Visual Studio Code and open your project directory (e.g., my-streamlit-app).

Open Terminal: Open the integrated terminal in VS Code using the menu (Terminal > New Terminal) or the shortcut `.

Activate Virtual Environment: In the terminal, type the command for your shell:

If using PowerShell:

PowerShell

.venv\Scripts\Activate.ps1
If using Command Prompt:

DOS

.venv\Scripts\activate.bat
Run Streamlit App: Once (.venv) appears in your terminal prompt, start the application with:

Bash

streamlit run app.py