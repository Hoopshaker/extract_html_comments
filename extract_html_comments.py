#!/bin/python3
import argparse
from bs4 import BeautifulSoup, Comment

def extract_html_comments(file_path):
    """
    Extracts all HTML comments from the given HTML file.

    Args:
        file_path (str): The path to the HTML file.

    Returns:
        list: A list of all HTML comments found in the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))

    return comments

def main():
    """
    Extracts and displays all HTML comments from the given HTML file.
    """
    parser = argparse.ArgumentParser(description='Extract HTML comments from a given HTML file.')
    parser.add_argument('--filepath', required=True, help='The path to the HTML file to analyze.')

    args = parser.parse_args()
    file_path = args.filepath

    comments = extract_html_comments(file_path)

    if comments:
        print("HTML Comments found:")
        for comment in comments:
            print(comment)
    else:
        print("No HTML comments found.")

if __name__ == '__main__':
    main()

