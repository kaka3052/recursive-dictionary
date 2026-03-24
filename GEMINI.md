# Recursive Word Dictionary (Gemini CLI)

## Project Overview
This project is an automated system for generating English word study notes in Markdown format. It monitors a specific directory (determined by a configurable `root.md` path) for Obsidian-style internal links (`[[word]]`) and automatically creates corresponding explanation files in the same directory.

### Core Objectives
- **Configurable Root**: Specify the path to `root.md`, which serves as the starting point (Level 0).
- **Directory Co-location**: All automatically generated word files are created in the same directory as the specified `root.md`.
- **Automatic Creation**: Detect new `[[word]]` links in `.md` files within the target directory.
- **Data Enrichment**: Fetch authentic **Collins Dictionary** definitions and **IPA (International Phonetic Alphabet)**.
- **Recursive Leveling**: Track the depth of the word relative to the root file.

## Technical Architecture
- **Language**: Python 3.x
- **File Monitoring**: `watchdog` library to track real-time changes.
- **Web Scraping**: `requests` + `BeautifulSoup` to extract data from `https://www.collinsdictionary.com/dictionary/english/{word}`.
- **State Management**: `levels.json` maps filenames to their recursive level.
- **Parser**: Regex-based extraction of `[[word]]` or `[[word|alias]]` syntax.

## Project Structure
- `main.py`: Entry point for the monitoring service.
- `src/`: Core logic package.
    - `monitor.py`: Event handling for file creation/modification.
    - `dictionary.py`: Scraper for Collins definitions and IPA.
    - `parser.py`: Logic to find `[[word]]` links.
    - `generator.py`: Markdown file template and creation logic.
    - `state.py`: JSON state persistence for word levels.
- `requirements.txt`: Project dependencies (`watchdog`, `requests`, `beautifulsoup4`).
- `levels.json`: Auto-generated mapping of `file -> Level n`.

## Usage and Startup

To manually start and operate this project, follow these steps:

### 1. Environment Setup
Ensure you have Python 3.10+ installed. Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

### 2. Configuration
Before starting, verify the `config.json` file in the root directory. It defines which file is the "Root" (Level 0) and consequently which directory will be monitored:
```json
{
    "root_file": "notes/root.md"
}
```
*Note: All word files will be created in the same folder as the `root_file`.*

### 3. Starting the Service
Run the main script from the project root:
```bash
python main.py
```
The program will:
1. Scan the `root_file` for existing `[[word]]` links and generate files for them.
2. Enter a "Watch" mode, monitoring the directory for any new `.md` files or modifications.

### 4. How to Use
- Open your `root.md` or any other `.md` file in the monitored directory.
- Type a link like `[[obvious]]`.
- Save the file.
- The system will automatically create `obvious.md` with its IPA and Collins definition.

### 5. Stopping the Service
To stop the automatic generator, press `Ctrl+C` in the terminal where the script is running.

## Guidelines for Future Agents
1. **Scraping Robustness**: The site structure of Collins Dictionary may change. If scraping fails, verify selectors in `src/dictionary.py`.
2. **Infinite Loops**: The monitor is designed to ignore existing files, but care should be taken when adding links to newly generated files to avoid uncontrolled recursion if multiple words point to each other.
3. **State Integrity**: `levels.json` is critical for correct level incrementing. Do not delete it unless a full re-index is required.
4. **Encoding**: Always use `utf-8` for reading and writing files to support phonetic symbols and special characters.
