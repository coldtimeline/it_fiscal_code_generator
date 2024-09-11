def test_is_vowel():
    # Test the function
    assert is_vowel('a') == True
    assert is_vowel('A') == True
    assert is_vowel('b') == False
    assert is_vowel('B') == False

    #one should also test Empty String Uppercase Vowels Non-alphabetic Characters Multiple Characters Non-English Vowels Boundary Cases



def test_divide_vowels_consonants():
    assert divide_vowels_consonants("ciao")[0] == "iao"
    assert divide_vowels_consonants("ciao")[1] == "c"
    assert divide_vowels_consonants("ciao")[0] + divide_vowels_consonants("ciao")[1] == "iaoc"
    assert divide_vowels_consonants("")[0] == ""
    assert divide_vowels_consonants("")[1] == ""
    assert divide_vowels_consonants("   ")[0] == ""
    assert divide_vowels_consonants("  ")[1] == ""
    assert divide_vowels_consonants("a  ")[0] == "a"
    assert divide_vowels_consonants("a  ")[1] == ""






def test_is_name_ok():
    assert  is_name_ok('cate')==True
    assert  is_name_ok('cate5')==False
    assert  is_name_ok('')==False
    assert  is_name_ok('    ')==False
    assert  is_name_ok('gian.maria')==False #because i don't know where to divide it
    assert  is_name_ok('gian maria')==True
    assert  is_name_ok(' gian maria')==True





def test_is_surname_ok():
    assert  is_surname_ok('cate')==True
    assert  is_surname_ok('cate5')==False
    assert  is_surname_ok('')==True
    assert  is_surname_ok('    ')==True
    assert  is_surname_ok('bianchi.rossi')==False
    assert  is_surname_ok('bianchi rossi')==True
    assert  is_surname_ok(' bianchi rossi')==True





def test_is_gender_ok():
    assert is_gender_ok('M') == True
    assert is_gender_ok('m') == True
    assert is_gender_ok('F') == True
    assert is_gender_ok('f') == True
    assert is_gender_ok('maschio') == False







def test_is_place_of_birth_ok():
    assert is_place_of_birth_ok('Roma') == True
    assert is_place_of_birth_ok('Roma2') == False
    assert is_place_of_birth_ok('') == False
    assert is_place_of_birth_ok('   ') == False






def test_gender_to_boolean():
    assert gender_to_boolean('M') == True
    assert gender_to_boolean('m') == True
    assert gender_to_boolean('F') == False
    assert gender_to_boolean('f') == False







def test_generate_day_gender_code():
    assert generate_day_gender_code(True, 15) == 15  # Male, should return the day of birth
    assert generate_day_gender_code(False, day_of_birth=15) == 55  # Female, should return the day of birth plus 40







def test_generate_name_code():
    assert generate_name_code("AEI", "SDFQW") == "SFQ"  # Four or more consonants
    assert generate_name_code("AE", "SDF") == "SDF"  # Three consonants
    assert generate_name_code("AE", "SD") == "SDA"  # Two consonants and one vowel
    assert generate_name_code("", "LP") == "LPX"  # Two consonants and no vowels
    assert generate_name_code("AE", "Q") == "QAE"  # One consonants and two vowel
    assert generate_name_code("A", "B") == "BAX"  # One consonants and one vowel
    assert generate_name_code("", "B") == "BXX"  # One consonants and zero vowel
    assert generate_name_code("AEI", "") == "AEI"  # Zero consonants and three vowel
    assert generate_name_code("AE", "") == "AEX"  # Zero consonants and two vowel
    assert generate_name_code("U", "") == "UXX"  # Zero consonants and one vowel








def test_generate_surname_code():
    assert generate_surname_code("", "BLTKJ") == "BLT"  # Lot of consonants
    assert generate_surname_code("AE", "BLTKJ") == "BLT"  # Lot of consonants
    assert generate_surname_code("", "BLT") == "BLT"  # Three consonants
    assert generate_surname_code("AE", "BL") == "BLA"  # Two consonants and one vowel
    assert generate_surname_code("", "BL") == "BLX"  # Two consonants and no vowels
    assert generate_surname_code("AE", "B") == "BAE"  # One consonants and two vowel
    assert generate_surname_code("AEUI", "B") == "BAE"  # One consonants and more vowel
    assert generate_surname_code("A", "B") == "BAX"  # One consonants and one vowel
    assert generate_surname_code("", "B") == "BXX"  # One consonants and zero vowel
    assert generate_surname_code("AEI", "") == "AEI"  # Zero consonants and three vowel
    assert generate_surname_code("AEI", "") == "AEI"  # lots of vowel
    assert generate_surname_code("AE", "") == "AEX"  # Zero consonants and two vowel
    assert generate_surname_code("U", "") == "UXX"  # Zero consonants and one vowel
    assert generate_surname_code("", "") == "XXX"  # Zero consonants and zero vowel
    assert generate_surname_code(divide_vowels_consonants("Rocchini")[0], divide_vowels_consonants("Rocchini")[1]) == "RCC"







def test_generate_month_char():
    assert generate_month_char(1) == 'A'  # Test for number 1
    assert generate_month_char(5) == 'E'  # Test for number 5
    assert generate_month_char(9) == 'P'  # Test for number 9
    assert generate_month_char(2) == 'B'  # Test for number 2
    assert generate_month_char(6) == 'H'  # Test for number 6
    assert generate_month_char(10) == 'R'  # Test for number 10
    assert generate_month_char(3) == 'C'  # Test for number 3
    assert generate_month_char(7) == 'L'  # Test for number 7
    assert generate_month_char(11) == 'S'  # Test for number 11
    assert generate_month_char(4) == 'D'  # Test for number 4
    assert generate_month_char(8) == 'M'  # Test for number 8
    assert generate_month_char(12) == 'T'  # Test for number 12







def test_last_two_digits():
    assert last_two_digits(2023) == '23'
    assert last_two_digits(1980) == '80'
    assert last_two_digits(1979) == '79'
    assert last_two_digits(5) == '05'






def test_even_position_to_number():
    assert even_position_to_number("A") == 0
    assert even_position_to_number("B") == 1
    assert even_position_to_number("C") == 2
    assert even_position_to_number("D") == 3
    assert even_position_to_number("E") == 4
    assert even_position_to_number("F") == 5
    assert even_position_to_number("G") == 6
    assert even_position_to_number("H") == 7
    assert even_position_to_number("I") == 8
    assert even_position_to_number("J") == 9
    assert even_position_to_number("K") == 10
    assert even_position_to_number("L") == 11
    assert even_position_to_number("M") == 12
    assert even_position_to_number("N") == 13
    assert even_position_to_number("O") == 14
    assert even_position_to_number("P") == 15
    assert even_position_to_number("Q") == 16
    assert even_position_to_number("R") == 17
    assert even_position_to_number("S") == 18
    assert even_position_to_number("T") == 19
    assert even_position_to_number("U") == 20
    assert even_position_to_number("V") == 21
    assert even_position_to_number("W") == 22
    assert even_position_to_number("X") == 23
    assert even_position_to_number("Y") == 24
    assert even_position_to_number("Z") == 25
    assert even_position_to_number("3") == 3
    #assert even_position_to_number("a") == 0







def test_generate_last_characther():
    assert generate_last_characther("GSTMGV78T03A944") == "T"
    assert generate_last_characther("LTZCST80A41G712") == "C"
    assert generate_last_characther("PPPGNN80A42B602") == "G"
    assert generate_last_characther("XIXTIX85H01E438") == "N"







def test_generate_city_code():
    dataset_from_internet = get_dataframe_from_web('https://dait.interno.gov.it/territorio-e-autonomie-locali/sut/elenco_codici_comuni.php')
    #dataset_from_internet.head()
    assert generate_city_code(dataset_from_internet, "MONTECCHIO EMILIA") == 'F463'







def test_find_similar_strings():
    # Create a sample DataFrame
    # Test the function with a known DataFrame and input string
    try:
        df = pd.DataFrame({'column': ['apple', 'aple', 'apl', 'bpple', 'cppl','reggio nell\'emilia', 'reggio 4']})
        similar_strings = find_similar_strings(df, 'column', 'reggio emilia')
        print(similar_strings)
    except Exception as e:
        print(str(e))

#find_similar_strings(dataset_from_internet, 'DESCRIZIONE COMUNE', 'MONTECCHIO')


