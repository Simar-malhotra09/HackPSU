from playwright.sync_api import sync_playwright
from format import format_to_get_only_minors

def get_fields():
    try:
        """
        Launch a Chromium browser, navigate to a URL, extract its text content,
        and save it to a file called "output.txt".
        """
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            # Navigate to a URL
            page.goto('https://bulletins.psu.edu/undergraduate/colleges/')

            # Extract text content from the page
            text_content = page.inner_text('body')

            # Define the output file name
            output_file = 'output.txt'

            # Save the text content to the output file
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(text_content)

            # Close the browser
            browser.close()

    except Exception as e:
        print(f'Error in get_fields: {str(e)}')

def get_minors_list(field):
    try:
        """
        Launch a Chromium browser, navigate to a specific URL based on the field,
        extract its text content, save it to a file, and format it to retain only lines
        containing the word "minor" (case-insensitive).
        """
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            # Navigate to a URL with the field parameter
            url = f'https://bulletins.psu.edu/undergraduate/colleges/{field}//#majorsminorsandcertificatestext'
            page.goto(url)

            # Extract text content from the page
            text_content = page.inner_text('body')

            # Define the output file name with the field name
            output_file = f'{field}_minors.txt'

            # Save the text content to the output file
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(text_content)

            # Format the file to retain only lines with "minor"
            format_to_get_only_minors(output_file)

            # Close the browser
            browser.close()

    except Exception as e:
        print(f'Error in get_minors_list: {str(e)}')

def minors_from_each_field(filename):
    try:
        """
        Process a file line by line, treating each line as a field name,
        and retrieve and format minors' information for each field.
        """
        with open(filename, 'r') as file:
            lines = file.readlines()
            for field in lines:
                processed_text = get_minors_list(field)

            print(f'Successfully processed "{filename}".')

    except FileNotFoundError:
        print(f'File "{filename}" not found.')
    except Exception as e:
        print(f'Error processing file: {str(e)}')

minors_from_each_field("output.txt")
