# Batch

A command-line utility for batch downloading files from URL lists with customizable input and output paths.

## Features

- Select from available .txt files containing URLs
- Specify custom output directory
- Preview URLs before downloading
- Download progress tracking
- Summary of download results

## Requirements

- Python 3.6+
- Required packages: `requests`

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Hearsay-Law/batch.git
   cd batch
   ```

2. Install required dependencies:
   ```
   pip install requests
   ```

## Usage

1. Create a .txt file with one URL per line
2. Run the script:
   ```
   python batch.py
   ```
3. Follow the prompts to:
   - Select a URL list file
   - Choose an output directory
   - Confirm downloads

## Example

```
===============================================================
                      FILE DOWNLOADER
===============================================================
Started at 14:30:25

Available .txt files:
  1. documents.txt
  2. images.txt
  3. videos.txt

Enter the number of the file to use: 1

Enter the output directory path (or press Enter for current directory): downloads

Found 15 URLs in documents.txt
First 3 URLs:
  1. https://example.com/doc1.pdf
  2. https://example.com/doc2.pdf
  3. https://example.com/doc3.pdf

Proceed with download? (y/n): y

Downloading files to: downloads
[1/15] Downloading doc1.pdf...
  Success: doc1.pdf (245.3 KB)
...
```
