import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline() # read each line of languages.txt and store in variable called "line"

    if line: # if current line is not empty string > return TRUE
        print_line(line, encoding, errors) # call print_line function, defined below
        return main(language_file, encoding, errors) # what would happen without return? #  looping the function by returning to the top # technically legal


def print_line(line, encoding, errors): # define print_line function called in main function above
    next_lang = line.strip() # it's a simple stripping of the trailling \n on the line string # need more attention to this
    raw_bytes = next_lang.encode(encoding, errors=errors) # encode the line into utf-8
    cooked_string = raw_bytes.decode(encoding, errors=errors) # decode the line into Roman characters # the "cooked" string is the result of bytes decoding

    print(raw_bytes, "<===>", cooked_string) # display utf-8 (Unicode Transformation Format)


languages = open("languages.txt", encoding = "utf-8") # open the languages.txt file under utf-8 encoding

main(languages, encoding, error) # call funtion

# Decode Bytes, Encode Strings #DBES
