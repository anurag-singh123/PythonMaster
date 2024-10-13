# Write a Python program to read the contents of a file, count the number of words, and write the word count to another file.

def count_words(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as file:
            # Read the entire file into a string
            text = file.read()
            
            # Split the string into individual words
            words = text.split()
            
            # Count the number of words
            word_count = len(words)
            
        # Open the output file in write mode
        with open(output_file, 'w') as file:
            # Write the word count to the output file
            file.write(f"The word count is: {word_count}\n")
        
        print(f"Word count written to {output_file} successfully!")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
count_words('input.txt', 'output.txt')