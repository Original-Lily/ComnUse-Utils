# GoScan: Web Technology Scanning Utility 

GoScan is a command-line tool developed in Go (Golang) that allows users to analyze  the web technologies used by websites. With GoScan, you can gain much quicker knowledge reguarding the technologies & frameworks behind websites.

## Features

- **Technology Detection:** GoScan detects and reports various web technologies used by a target website, including frameworks, programming languages, web servers, and more.
- **Fast and Efficient:** Built usign GoLand is designed for efficiency, allowing you to quickly gather information about multiple websites with minimal external requirements.
- **Easy to Use:** GoScan is simple and intuitive, making it accessible for both beginners and experienced users.

## Installation

To install GoScan, you need to have Go installed on your system. Follow these steps to install GoScan:

1. Clone the repository:

   ```
   git clone https://github.com/Original-Lily/GoScan.git
   ```

2. Navigate to the project directory:

   ```
   cd GoScan
   ```

3. Build the binary:

   ```
   go build
   ```

4. Run GoScan:

   ```
   ./GoScan -target example.com
   ```

   Replace `example.com` with the target website.

## Usage

GoScan provides a simple syntax for detecting web technologies. Here's how you can use it:

```
Usage: GoScan [options]

Options:
  -target string
        Specify the target website for technology detection.
  -output string
        Specify the output format (json, text) [default: text].
  -h, --help
        Show this help message and exit.
```

Example usage:

```
./GoScan -target example.com -output text
```

This command will detect web technologies used by `example.com` and output the results in text format.

## Output Format

GoScan provides two output formats: plain text and JSON.

- **Text Format:** Plain text output provides a human-readable format, displaying the detected technologies in a clear and concise manner.

  Example text output:
  
  ```
  Target: example.com

  Detected Technologies:
  - Programming Language: Go
  - Web Server: nginx
  - Framework: Tailwind
  ...
  ```


- **JSON Format:** JSON output provides a structured and machine-readable format, suitable for further processing and integration with other tools.
  
  Example JSON output:
  
  ```json
  {
    "Target": "example.com",
    "Technologies": {
      "Programming Language": "HTML",
      "Web Server": "nginx",
      "Framework": "Tailwind",
      etc
    }
  }
  ```
