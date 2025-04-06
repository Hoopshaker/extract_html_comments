# HTML Comments Extractor

This script extracts and displays all HTML comments from a given HTML file.

## Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)

## Setup

1. **Clone the repository** (if applicable) or navigate to the `extract_html_comments` directory:

   ```bash
   cd path/to/extract_html_comments
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To extract and display HTML comments from an HTML file, use the following command:

```bash
python3 extract_comments.py --filepath /path/to/your/htmlfile.html
```

Replace `/path/to/your/htmlfile.html` with the actual path to your HTML file.

### Example

```bash
python3 extract_comments.py --filepath ./example.html
```

## Output

The script will print all the HTML comments found in the specified file to the console. If no comments are found, it will indicate that no HTML comments were found.

## Dependencies

- `beautifulsoup4`: Used for parsing HTML and extracting comments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
