
```markdown
# CV Analyzer

## Project Overview
This project, created by **Ibrahim Nuri**, is a Python-based tool designed to extract and analyze key information from CVs. The tool can detect important details like personal information, skills, and experiences. It is particularly useful for parsing CVs written in **Azerbaijani** and **English**, and provides insights based on this extracted data.

## Features
- Extracts personal details, skills, and experience from CVs.
- Supports PDF files for CV analysis.
- Detects language (Azerbaijani or English) and processes accordingly.
- Provides feedback on missing or key CV components (e.g., email, phone, skills).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/username/cv-analyzer.git
    ```

2. Navigate to the project directory:
    ```bash
    cd cv-analyzer
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Upload a CV in PDF format via the interface.
2. The script will automatically detect the language and extract relevant data such as name, email, phone number, and skills.
3. The extracted data will be displayed in the Streamlit interface.

To run the project locally:

```bash
streamlit run cv.py
```

### Example Usage:

```bash
python cv.py --input "data/sample_cv.pdf"
```

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt` (e.g., `pdfplumber`, `spacy`, `streamlit`).

## Contributing

Feel free to contribute by submitting issues or pull requests. Any feedback or improvements are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
**Ibrahim Nuri**

If you have any questions, feel free to reach out!
```
