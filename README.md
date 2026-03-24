# Recursive Word Dictionary Generator

An automated system for generating English word study notes in Markdown format. It monitors your notes for Obsidian-style internal links (`[[word]]`) and automatically creates a corresponding explanation file enriched with **Collins Dictionary** data.

## 🚀 Features

-   **Automatic Monitoring**: Real-time detection of new `[[word]]` links using the `watchdog` library.
-   **Authentic Data**: Fetches **IPA (International Phonetic Alphabet)** and definitions directly from [Collins Dictionary](https://www.collinsdictionary.com/).
-   **Recursive Level Tracking**: Automatically tracks the "Level" of each word (Root = Level 0, words in root = Level 1, etc.) and stores the state in `levels.json`.
-   **Configurable**: Specify your root file path via `config.json`.
-   **Smart Formatting**: Prevents word merging and handles special phonetic characters correctly using UTF-8.

## 🛠️ Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/kaka3052/recursive-dictionary.git
    cd recursive-dictionary
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 📖 Usage

1.  **Configure your root file**:
    Edit `config.json` to point to your main note:
    ```json
    {
        "root_file": "notes/root.md"
    }
    ```

2.  **Start the generator**:
    ```bash
    python main.py
    ```

3.  **Create links**:
    In `notes/root.md` (or any other `.md` file in the same directory), add a link:
    `This is a new [[concept]].`

4.  **Automatic Generation**:
    The system will detect the link and create `notes/concept.md` with the following structure:
    -   Word Title
    -   IPA Pronunciation
    -   Recursive Level
    -   Full Collins Definition

## 📂 Project Structure

-   `main.py`: Entry point for the monitoring service.
-   `src/`: Core logic (monitor, scraper, parser, generator, state).
-   `config.json`: Configuration for the root file path.
-   `notes/`: The directory where your Markdown notes reside.
-   `GEMINI.md`: Detailed technical specification and developer guidelines.

## 📝 Requirements

-   Python 3.10+
-   Dependencies: `watchdog`, `requests`, `beautifulsoup4`, `curl-cffi`.

## 🤝 Contributing

Feel free to open issues or submit pull requests for any improvements!

## 📜 License

MIT License
