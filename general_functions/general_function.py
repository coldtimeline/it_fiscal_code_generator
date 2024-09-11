import string

def digit_or_special_present(input_string):
    """
    Check if the input string contains any numbers or special characters.

    Parameters:
    input_string (str): The string to be checked.

    Returns:
    bool: True if the string contains numbers or special characters, False otherwise.
    """

    # Define the set of special characters
    special_characters = set(string.punctuation)

    # Check each character in the string
    for char in input_string:
        # If the character is a digit or a special character, return True
        if char.isdigit() or char in special_characters:
            return True

    # If no digits or special characters are found, return False
    return False






def is_empty_or_only_space(s):
    """
    This function checks if a given string is not empty or only spaces.

    Parameters:
    s (str): The string to check.

    Returns:
    bool: True if the string is empty or only spaces, False otherwise.
    """

    # If the string is empty or only spaces, return True
    if s.strip() == '':
        return True

    # If the string is not empty and not only spaces, return False
    return False




def is_vowel(char):
    """
    Check if the provided character is a vowel.

    Parameters:
    char (str): A single character to be checked.

    Returns:
    bool: True if the character is a vowel, False otherwise.
    """

    # Define a list of vowels
    vowels = 'aeiouAEIOUùàòèéì'

    # Check if the character is a vowel
    return char in vowels



def divide_vowels_consonants(word):
    """
    This function takes a word as input and returns two string:
    one containing the vowels and the other containing consonants.
    This function works only with alphabetic characters, so the imput word should be
    controlled before calling this function.

    Parameters:
    word (str): The input word.

    Returns:
    vowels (str): The string containing the vowels.
    consonants (str): The string containing the consonants.
    """


    # Initialize empty strings for vowels and consonants
    vowels = ""
    consonants = ""

    # Eliminate al spaces
    word_wo_spaces = word.replace(" ", "")
    # Iterate through each character in the word
    for char in word_wo_spaces:
        # Check if the character is a vowel
        if is_vowel(char):
            vowels += char
        # If the character is not a vowel, it must be a consonant
        else:
            consonants += char

    # Return the two strings
    return vowels, consonants





def is_name_ok(name):
    """
    This function checks if a given name is valid. The name is valid if it is
    not empty or not contains only spaces and does not contain any
    special characters or numbers.

    Parameters:
    name (str): The name to check.

    Returns:
    bool: True if the name is valid, False otherwise.
    """

    # Check if the name is not empty or only spaces
    if is_empty_or_only_space(name):
        return False

    # Check if the name contains only letters. Not use the isalpha() string
    # method because it does not work with spaces that may be present in
    # the name. Points or similar are not accepted as separator
    if digit_or_special_present(name):
        return False

    # If the name is valid, return True
    return True




def is_surname_ok(surname):
    """
    This function checks if a given surname is valid. The surname is valid if
    it is empty or contains only spaces or does not contain any
    special characters or numbers.
    Parameters:
    surname (str): The surname to check.

    Returns:
    bool: True if the surname is valid, False otherwise.

    """
    # Check if the surname contains only letters. Not use the isalpha() string
    # method because it does not work with spaces that may be present in
    # the surname
    if digit_or_special_present(surname):
        return False

    # If the surname is valid, return True
    return True





def is_gender_ok(gender):
  """
  This function checks if the gender is M or F. In particular M,m,F,f are
  allowed, or those letter with spaces.

  Parameters:
  gender (str): The gender to check.

  Returns:
  bool: True if the gender is valid, False otherwise.
  """

  if gender.strip() == 'M' or gender.strip() == 'm' or gender.strip() == 'F' or gender.strip() == 'f':
    return True
  else:
    return False





def is_place_of_birth_ok(place_of_birth):
  """
  This function checks if the place of birth is valid. In particular should not
  be empty or only spaces, and digit should not be present.

  Parameters:
  place_of_birth (str): The place of birth to check.

  Returns:
  bool: True if the place of birth is valid, False otherwise.
  """

  # Check if the place of birth is not empty or only spaces
  if is_empty_or_only_space(place_of_birth):
    return False
  
  #Check if nubers are present
  for char in place_of_birth:
    if char.isdigit():
      return False
  #Otherwise return true
  return True




def gender_to_boolean(gender):
  """
  This function takes a string representing the gender and returns a boolean
  value. If the gender is 'M' or 'm' return true, if the gender is 'F' or 'f'
  return false.

  Parameters:
  gender (str): The input gender.

  Returns:
  bool: The corresponding boolean value.


  """
  if gender.strip() == 'M' or gender.strip() == 'm':
    return True
  else:
    return False



def generate_day_gender_code(gender, day_of_birth):
    """
    Determine the day of birth part of the code based on gender.

    Parameters:
    gender (bool): The gender of the individual, where True represents male and False represents female.
    day_of_birth (int): The day of birth of the individual.

    Returns:
    int: The original day of birth if the gender is male, otherwise the day of birth plus 40.
    """
    # Check if the input gender is True (male) return return the day of birth as
    # it is, otherwise add 40
    if gender:
        return day_of_birth
    else:
        return day_of_birth + 40





def generate_name_code(vowels_ucase, consonants_ucase):  #DA METTERE A POSTO PER QUANTO TIGUARDA I CASI TIPO 1 CONSONANTE E UNA VOCALE
    """
    Generates a three-character string based on the consonants and vowels
    of the name, according to agenzia delle entrate rules.

    Parameters:
    consonants_ucase (str): String containing all the consonants of the name, unknown case.
    vowels_ucase (str): String containing all the vowels of the name, unknown case.

    Returns:
    str: A three-character string according to the specified rules.
    """

    # Initialize the output string
    code = ""
    # Make consonants and vowels upper case
    consonants = consonants_ucase.upper()
    vowels = vowels_ucase.upper()
    #eliminate all spaces
    consonants = consonants.replace(" ", "")
    vowels = vowels.replace(" ", "")

    # Case 1: Four or more consonants
    if len(consonants) >= 4:
        code = consonants[0] + consonants[2] + consonants[3]
    # Case 2: Three consonants
    elif len(consonants) == 3:
        code = consonants[0] + consonants[1] + consonants[2]
    # Case 3: Two consonants and one vowels
    elif len(consonants) == 2 and len(vowels) >= 1:
        code = consonants[0] + consonants[1] + vowels[0]
    # Case 4: Two consonants and no vowels
    elif len(consonants) == 2 and len(vowels) == 0:
        code = consonants[0] + consonants[1] + 'X'
    # Case 5: One consonants and two vowels
    elif len(consonants) == 1 and len(vowels) >= 2:
        code = consonants[0] + vowels[0] + vowels[1]
    # Case 6: One consonants and one vowel
    elif len(consonants) == 1 and len(vowels) == 1:
        code = consonants[0] + vowels[0] + 'X'
    # Case 7: One consonants and zero vowel
    elif len(consonants) == 1 and len(vowels) == 0:
        code = consonants[0] + 'X' + 'X'
    # Case 8: Zero consonants and three vowel
    elif len(consonants) == 0 and len(vowels) >= 3:
        code = vowels[0] + vowels[1] + vowels[2]
    # Case 9: Zero consonants and two vowel
    elif len(consonants) == 0 and len(vowels) == 2:
        code = vowels[0] + vowels[1] + 'X'
    # Case 10: Zero consonants and one vowel
    elif len(consonants) == 0 and len(vowels) == 1:
        code = vowels[0] + 'X' + 'X'

    # Case 11: Zero consonants and zero vowel is not permitted, so rise an error
    else:
        raise ValueError("Invalid input name")

    return code




def generate_surname_code(vowels_ucase, consonants_ucase):
    """
    Generates a three-character string based on the consonants and vowels
    of the surname, according to agenzia delle entrate rules.

    Parameters:
    consonants_ucase (str): String containing all the consonants of the name, unknown case.
    vowels_ucase (str): String containing all the vowels of the name, unknown case.

    Returns:
    str: A three-character string according to the specified rules.
    """
    # Initialize the output string
    code = ""
    # Make consonants and vowels upper case
    consonants = consonants_ucase.upper()
    vowels = vowels_ucase.upper()
    #eliminate all spaces
    consonants = consonants.replace(" ", "")
    vowels = vowels.replace(" ", "")



    # Case 1: Four or more consonants
    if len(consonants) >= 3:
        code = consonants[0] + consonants[1] + consonants[2]
    # Case 1: Two consonants and one vowels
    elif len(consonants) == 2 and len(vowels) >= 1:
        code = consonants[0] + consonants[1] + vowels[0]
    # Case 2: Two consonants and no vowels
    elif len(consonants) == 2 and len(vowels) == 0:
        code = consonants[0] + consonants[1] + 'X'
    # Case 3: One consonants and two vowels
    elif len(consonants) == 1 and len(vowels) >= 2:
        code = consonants[0] + vowels[0] + vowels[1]
    # Case 4: One consonants and one vowel
    elif len(consonants) == 1 and len(vowels) == 1:
        code = consonants[0] + vowels[0] + 'X'
    # Case 5: One consonants and zero vowel
    elif len(consonants) == 1 and len(vowels) == 0:
        code = consonants[0] + 'X' + 'X'
    # Case 6: Zero consonants and three vowel
    elif len(consonants) == 0 and len(vowels) >= 3:
        code = vowels[0] + vowels[1] + vowels[2]
    # Case 7: Zero consonants and two vowel
    elif len(consonants) == 0 and len(vowels) == 2:
        code = vowels[0] + vowels[1] + 'X'
    # Case 8: Zero consonants and one vowel
    elif len(consonants) == 0 and len(vowels) == 1:
        code = vowels[0] + 'X' + 'X'
    # Case 9: Zero consonants and zero vowel
    else:
        code = 'XXX'


    return code







def generate_month_char(month):
    """
    Converts an integer number (representing month of birth)
    to a corresponding character based on Agenzia delle Entrate rules

    Parameters:
    month (int): The input integer number representing the month.

    Returns:
    str: The corresponding character as per the rules.

    Raises:
    ValueError: If the number is not between 1 and 12 inclusive.
    """
    # Dictionary mapping numbers to characters
    number_char_map = {
        1: 'A', 5: 'E', 9: 'P',
        2: 'B', 6: 'H', 10: 'R',
        3: 'C', 7: 'L', 11: 'S',
        4: 'D', 8: 'M', 12: 'T'
    }

    # Check if the number is in the valid range
    if month not in number_char_map:
        raise ValueError("Number must be between 1 and 12 inclusive.")

    # Return the corresponding character
    return number_char_map[month]





def last_two_digits(year):
    """
    This function takes a year as input and returns the last two digits of that year.
    Raises an error if the value is negative.

    Parameters:
    year (int): The year of birth

    Returns:
    str: The last two digits of the year as a two-digit string

    Raises:
    ValueError: If the year is negative
    """

    # Check if the year is negative
    if year < 0:
        raise ValueError("Year cannot be negative")

    # Convert the year to string
    year_str = str(year)

    # Get the last two digits
    last_two_digits = year_str[-2:]

    # If the year has less than two digits, prepend a '0'
    if len(last_two_digits) < 2:
        last_two_digits = '0' + last_two_digits

    return last_two_digits






def even_position_to_number(char):
    """
    This function take a char which must be an upper character or a digit and
    returns a value according to agenzia delle entrate rules, for even positioned
    characters or digits

    Parameters:
    char (char): the char to convert

    Returns:
    int: the converted value
    """

    # Dictionary mapping numbers to characters
    even_position_to_number_map = {
        "A": 0, "0": 0,
        "B": 1, "1": 1,
        "C": 2, "2": 2,
        "D": 3, "3": 3,
        "E": 4, "4": 4,
        "F": 5, "5": 5,
        "G": 6, "6": 6,
        "H": 7, "7": 7,
        "I": 8, "8": 8,
        "J": 9, "9": 9,
        "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19,
        "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25

    }

    # Check if the character is in the map
    if char not in even_position_to_number_map:
        raise ValueError("Invalid character")

    # Return the corresponding value
    return even_position_to_number_map[char]






def odd_position_to_number(char):
    """
    This function take a char which must be an upper character or a digit and
    returns a value according to agenzia delle entrate rules, for odd positioned
    characters or digits

    Parameters:
    char (char): the char to convert

    Returns:
    int: the converted value
    """

    # Dictionary mapping numbers to characters
    odd_position_to_number_map = {
        "A": 1, "0": 1,
        "B": 0, "1": 0,
        "C": 5, "2": 5,
        "D": 7, "3": 7,
        "E": 9, "4": 9,
        "F": 13, "5": 13,
        "G": 15, "6": 15,
        "H": 17, "7": 17,
        "I": 19, "8": 19,
        "J": 21, "9": 21,
        "K":2, "L":4, "M":18, "N":20, "O":11, "P":3, "Q":6, "R":8, "S":12, "T":14,
        "U":16, "V":10, "W":22, "X":25, "Y":24, "Z":23

    }

    # Check if the character is in the map
    if char not in odd_position_to_number_map:
        raise ValueError("Invalid character")

    # Return the corresponding value
    return odd_position_to_number_map[char]




def generate_last_characther(input_code):
    """
    This function take the string of uncompleted code and return the last character
    that must be added to the code to complete it, based on rules
    from Agenzia dell'Entrate

    Parameters:
    input_code (str): the string of uncompleted code

    Returns:
    char: the new last character of the code
    """

    if input_code == "":
        raise ValueError("Input code cannot be empty")
    if len(input_code) != 15:
        raise ValueError("Input code must have 10 characters")

    #input_code = input_code.upper()
    input_code_even = ""
    input_code_odd = ""
    odd_position_sum=0
    even_position_sum=0


    # Dividing the string in odd and even position, using string slicing
    # Agenzia delle entrate consider the first character as in a odd position
    input_code_even = input_code[1::2]
    input_code_odd = input_code[::2]


    for char in input_code_odd:
        odd_position_sum += odd_position_to_number(char)

    for char in input_code_even:
        even_position_sum += even_position_to_number(char)


    total_sum = odd_position_sum + even_position_sum
    last_digit_number = total_sum % 26
    last_digit_char = chr(last_digit_number + 65)

    return last_digit_char





import pandas as pd

def get_dataframe_from_web(url):
    """
    This function takes a URL of a webpage containing an HTML table and returns a pandas DataFrame.

    Parameters:
    url (str): The URL of the webpage containing the HTML table.

    Returns:
    df (DataFrame): A pandas DataFrame containing the data from the HTML table.

    Raises:
    ValueError: If the URL does not contain a valid HTML table.
    """
    try:
        # Use the pandas read_html function to read the HTML table into a list of DataFrames
        dfs = pd.read_html(url)

        # Check if any tables were found
        if not dfs:
            raise ValueError("No tables found at the provided URL.")

        # Return the first table found
        return dfs[0]

    except Exception as e:
        # If an error occurs, raise it
        raise ValueError(f"An error occurred while trying to read the HTML table: {e}")




def generate_city_code(city_df, city_name):
    """
    This function searches for a city in the 'DESCRIZIONE COMUNE' column of the dataframe
    and returns its corresponding code from the 'CODICE BELFIORE' column.

    Parameters:
    city_df (pandas.DataFrame): The dataframe containing the city data.
    city_name (str): The name of the city to search for.

    Returns:
    str: The code of the city if found, otherwise None.
    """

    #access the first dataframe
    #city_df = city_df[0]

    # Filter the dataframe to find the row with the given city name
    city_row = city_df[city_df['DESCRIZIONE COMUNE'] == city_name]

    # Check if the city was found and return the corresponding code
    if not city_row.empty:
        return city_row['CODICE BELFIORE'].values[0]
    else:
        return None





from fuzzywuzzy import fuzz
#import pandas as pd

def find_similar_strings(df, column, input_string, threshold=80):
    """
    This function searches for strings similar to the input string in a specific column of a pandas DataFrame.

    Parameters:
    df (DataFrame): The pandas DataFrame to search.
    column (str): The column in the DataFrame to search.
    input_string (str): The string to find similar strings to.
    threshold (int): The similarity threshold. Strings with a similarity score above this threshold will be considered similar.

    Returns:
    similar_strings (list): A list of strings found to be similar to the input string.

    Raises:
    ValueError: If no similar strings are found.
    """
    # Ensure the column exists in the DataFrame
    if column not in df.columns:
        raise ValueError(f"The column '{column}' does not exist in the DataFrame.")

    # Find similar strings
    similar_strings = [str for str in df[column] if fuzz.ratio(input_string, str) > threshold]

    # Raise an error if no similar strings are found
    if not similar_strings:
        raise ValueError(f"No strings similar to '{input_string}' were found in the column '{column}'.")

    return similar_strings







def select_string(strings):
    """
    This function takes a list of strings as input and returns a string based on
    user selection.
    
    Parameters:
    strings (list): A list of strings.

    Returns:
    str: A string based on user selection.

    Raises:
    ValueError: If the list is empty or the user selection is invalid.
    """
    
    # If the list is empty, raise an error
    if not strings:
        raise ValueError("The list is empty.")
    
    # If the list contains one string, return that string
    if len(strings) == 1:
        return strings[0]
    
    # If the list contains two or more strings, show to the user the strings, each of them numbered
    for i, string in enumerate(strings):
        print(f"{i+1}. {string}")
    
    # Ask the user which string he needs
    selection = input("Please enter the number of the place you were born: ")
    
    # If the user answers with a number identifying a string, return that string
    if selection.isdigit() and 1 <= int(selection) <= len(strings):
        return strings[int(selection) - 1]
    
    # Otherwise raise an error
    else:
        raise ValueError("Invalid selection.")


#select_string(find_similar_strings(dataset_from_internet, 'DESCRIZIONE COMUNE', 'MONTECCHIO'))




from datetime import datetime
def generate_fiscal_code(name, surname, gender, date_of_birth, birth_place, placedataset):
  """
  This function takes the name, surname, gender, date of birth and birth place of a person
  and returns the fiscal code of that person.

  Parameters:
  name (str): the name of the person
  surname (str): the surname of the person
  gender (str): the gender of the person
  date_of_birth (datetime): the date of birth of the person
  birth_place (str): the birth place of the person
  placedataset (DataFrame): the dataframe containing the place codes

  Returns:
  str: the fiscal code of the person
  """
  #generate name, surname, year, month, day and gender, birth place code
  name_code = generate_name_code(divide_vowels_consonants(name)[0],divide_vowels_consonants(name)[1])
  surname_code = generate_surname_code(divide_vowels_consonants(surname)[0],divide_vowels_consonants(surname)[1])
  year_code = last_two_digits(date_of_birth.year)
  month_code = generate_month_char(date_of_birth.month)
  day_and_gender_code = last_two_digits(generate_day_gender_code(gender_to_boolean(gender),date_of_birth.day))
  place_code = generate_city_code(placedataset,birth_place)

  #generate last char
  uncompleted_code = surname_code + name_code + str(year_code) + month_code + str(day_and_gender_code) + place_code
  last_char = generate_last_characther(uncompleted_code)

  return uncompleted_code + last_char









  def get_name():
    """
    Asks the user for their name and checks if it is valid using the is_name_ok function.
    Raises a ValueError if the name is not valid.

    Returns:
    str: The valid name entered by the user.

    Raises:
    ValueError if the name is not valid.
    """
    name = input("Please enter your name, only letters and spaces accepted: ")
    if not is_name_ok(name):
        raise ValueError("The name entered is not valid. No digit, punctation or empty sting allowed")
    return name


def get_surname():
    """
    Asks the user for their surname and checks if it is valid using the is_surname_ok function.
    Raises a ValueError if the surname is not valid.

    Returns:
    str: The valid surname entered by the user.

    Raises:
    ValueError if the surname is not valid.
    """
    surname = input("Please enter your surname: ")
    if not is_surname_ok(surname):
        raise ValueError("The surname entered is not valid. No digit or punctation allowed")
    return surname

def get_gender():
    """
    Asks the user for their gender and checks if it is valid using the is_gender_ok function.
    Raises a ValueError if the gender is not valid.

    Returns:
    str: The valid gender entered by the user.

    Raises:
    ValueError if the gender is not valid.
    """
    gender = input("Please enter your gender (M/F): ")
    if not is_gender_ok(gender):
      raise ValueError("The gender entered is not valid. Please enter only one m or f")
    return gender



from datetime import datetime

def get_date_of_birth():
    """
    This function prompts the user for their date of birth.
    The date of birth should be entered in the format: DD-MM-YYYY.

    Returns:
        datetime: A datetime object representing the user's date of birth.
    """
    # Prompt the user for their date of birth
    date_of_birth_str = input("Please enter your date of birth (DD-MM-YYYY): ")

    # Convert the string to a datetime object
    # If the date is not in the correct format, this will raise a ValueError
    try:
        date_of_birth = datetime.strptime(date_of_birth_str, "%d-%m-%Y")
    except ValueError:
        print("The date of birth was not in the correct format.")
        return None

    return date_of_birth



def get_place_of_birth(df):
    """
    This function prompts the user for their place of birth.
    Then searches for the place in the dataset and returns the right name of the
    place

    Parameters:
    df (DataFrame): The dataframe containing the place codes

    Returns:
    str: The name of the place of birth.
    """
    place_of_birth = input("Please enter your city (comune) of birth: ")
    if not is_place_of_birth_ok(place_of_birth):
        raise ValueError("The place of birth entered is not valid. No digit or empty string allowed")
    #string to capital letter because string are capital letter in dataframe we used
    place_of_birth = place_of_birth.upper()
    #find the correct place of birth:
    #find_similar_string find for city with similar names in the dataset
    #select_string which one of the found string is the right one
    place_of_birth_found = select_string(find_similar_strings(df, 'DESCRIZIONE COMUNE', place_of_birth))
    
    return place_of_birth_found




def run_program():


  name = get_name()
  surname = get_surname()
  gender = get_gender()
  date_of_birth = get_date_of_birth()

  place_dataset = get_dataframe_from_web('https://dait.interno.gov.it/territorio-e-autonomie-locali/sut/elenco_codici_comuni.php')
  place = get_place_of_birth(place_dataset)

  print(generate_fiscal_code(name,surname,gender,date_of_birth,place,place_dataset))