import os
import requests
import time
from pathlib import Path

def get_txt_files():
    """Get all .txt files in the current directory"""
    current_dir = Path(os.getcwd())
    txt_files = list(current_dir.glob('*.txt'))
    return txt_files

def select_txt_file():
    """Prompt user to select a .txt file from the current directory"""
    txt_files = get_txt_files()
    
    if not txt_files:
        print("No .txt files found in the current directory.")
        return None
    
    print("\nAvailable .txt files:")
    for i, file in enumerate(txt_files):
        print(f"  {i+1}. {file.name}")
    
    while True:
        try:
            choice = input("\nEnter the number of the file to use: ")
            index = int(choice) - 1
            if 0 <= index < len(txt_files):
                return txt_files[index]
            else:
                print(f"Please enter a number between 1 and {len(txt_files)}")
        except ValueError:
            print("Please enter a valid number")

def get_output_directory():
    """Prompt user to specify an output directory"""
    while True:
        output_dir = input("\nEnter the output directory path (or press Enter for current directory): ")
        
        # Use current directory if empty
        if not output_dir:
            return Path(os.getcwd())
        
        output_path = Path(output_dir)
        
        # Create directory if it doesn't exist
        if not output_path.exists():
            try:
                create_dir = input(f"Directory doesn't exist. Create {output_dir}? (y/n): ")
                if create_dir.lower() == 'y':
                    output_path.mkdir(parents=True, exist_ok=True)
                    return output_path
                # If user doesn't want to create, loop continues
            except Exception as e:
                print(f"Error creating directory: {e}")
        else:
            return output_path

def download_files(url_file, output_dir):
    """Download files from URLs in the given file to the specified directory"""
    try:
        # Read URLs
        with open(url_file, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
        
        # Show preview
        print(f"\nFound {len(urls)} URLs in {url_file.name}")
        print("First 3 URLs:")
        for i, url in enumerate(urls[:3]):
            print(f"  {i+1}. {url}")
        
        # Confirm with user
        confirm = input("\nProceed with download? (y/n): ")
        if confirm.lower() != 'y':
            print("Download cancelled.")
            return
            
    except Exception as e:
        print(f"ERROR: Could not read URLs from {url_file}: {e}")
        return
    
    # Download files
    successful = 0
    errors = 0
    
    print(f"\nDownloading files to: {output_dir}")
    
    for i, url in enumerate(urls):
        try:
            filename = url.split('/')[-1]  # Get the last part of the URL
            filepath = output_dir / filename
            
            print(f"[{i+1}/{len(urls)}] Downloading {filename}...")
            
            response = requests.get(url, timeout=30)
            
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                file_size = len(response.content)/1024
                print(f"  Success: {filename} ({file_size:.1f} KB)")
                successful += 1
            else:
                print(f"  ERROR: Server returned status code {response.status_code}")
                errors += 1
                
        except Exception as e:
            print(f"  ERROR: Failed to download {url}: {e}")
            errors += 1
    
    # Summary
    print("\nDownload Summary:")
    print("---------------")
    print(f"Total URLs: {len(urls)}")
    print(f"Successful: {successful}")
    print(f"Errors: {errors}")
    print(f"Files saved to: {output_dir}")
    
    # List downloaded files
    files = list(output_dir.glob('*'))
    downloaded_count = len(files)
    max_display = min(10, downloaded_count)
    
    print(f"\nDownloaded files (showing first {max_display} of {downloaded_count}):")
    for file in files[:max_display]:
        print(f"  - {file.name}")
    
    if downloaded_count > 10:
        print(f"  ... and {downloaded_count - 10} more files")

def main():
    print("=" * 60)
    print("FILE DOWNLOADER".center(60))
    print("=" * 60)
    print(f"Started at {time.strftime('%H:%M:%S')}")
    
    # Get input file
    url_file = select_txt_file()
    if not url_file:
        input("\nPress Enter to exit...")
        return
    
    # Get output directory
    output_dir = get_output_directory()
    if not output_dir:
        input("\nPress Enter to exit...")
        return
    
    # Download files
    download_files(url_file, output_dir)
    
    print(f"\nScript completed at {time.strftime('%H:%M:%S')}")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()