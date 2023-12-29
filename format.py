def process_file(filename):
    try:
        """
        Process a file by converting its content to lowercase
        and replacing spaces with hyphens.
        """
        with open(filename, 'r') as file:
            lines = file.readlines()

        processed_lines = []
        for line in lines:
            words = line.split()
            lowercase_words = [word.lower() for word in words]
            hyphenated_line = '-'.join(lowercase_words)
            processed_lines.append(hyphenated_line)

        processed_text = '\n'.join(processed_lines)

        with open(filename, 'w') as file:
            file.write(processed_text)

        print(f'Successfully processed "{filename}".')

    except FileNotFoundError:
        print(f'File "{filename}" not found.')
    except Exception as e:
        print(f'Error processing file: {str(e)}')

def format_to_get_only_minors(filename):
    try:
        """
        Format a file to retain only lines containing the word "minor"
        (case-insensitive) and remove others.
        """
        with open(filename, 'r') as file:
            lines = file.readlines()

        filtered_lines = []
        for line in lines:
            if 'minor' in line.lower():
                filtered_lines.append(line)

        processed_text = '\n'.join(filtered_lines)

        with open(filename, 'w') as file:
            file.write(processed_text)

        print(f'Successfully processed "{filename}".')

    except FileNotFoundError:
        print(f'File "{filename}" not found.')
    except Exception as e:
        print(f'Error processing file: {str(e)}')

# Example usage:
# format_to_get_only_minors("agricultural-sciences_minors.txt")
