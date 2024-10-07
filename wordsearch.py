
#Description: this program replicates the word search game

# 2. Write your program here: 

#CONSTANTS: 

RIGHT_LEFT = 1 

LEFT_RIGHT = -1

#question 1 
def is_outside_list(letter_list, index):
    ''' (lst, int) -> boolean
    
    Returns boolean variable False if index is not out of range
    
    >>> is_outside_list(['A','B','C','D'], 4)
    True
    >>> is_outside_list(['A','B','C','D','E', 'F'], 4)
    False
    >>> is_outside_list(['A','B','C','D','E', 'F'], 6)
    True
    '''
    if index < 0 or index >((len(letter_list))-1):
        return True
    
    return False

#question 2
def letter_positions(letter_list, character):
    '''
    (list<str>, str) -> list<int>
    Returns a list of integers that indicates where the character in the
     letter_list may be found 

    
    >>> letter_positions(['A','B','C','D', 'C', 'M'], 'C')
    [2, 4]
    >>> letter_positions(['A','C','C','D', 'E', 'E', 'C'], 'C')
    [1, 2, 6]
    >>> letter_positions(['A','C','C','D', 'E', 'E', 'C'], 'F')
    []
    '''
    indice_list = []
     
    #finding and collecting indices where character is found
    for i in range(len(letter_list)):
        if letter_list[i] == character:
          indice_list += [i]
    
    return indice_list
         
#question 3
def valid_word_pos_direction(letter_list, word, index, direction):
    '''
    (list<str>, str, int, int) -> boolean
     
    Returns a boolean variable to indicate if the input word can be found at
    the inputed index and direction
            
    >>> valid_word_pos_direction(['A','B','C','D', 'C', 'M'], 'MCD', 5,-1)
    True
    >>> print(valid_word_pos_direction(['M','M','O','O', 'C', 'M'], 'MOM', 1,1))
    False
    >>> print(valid_word_pos_direction(['M','M','H','U', 'D', 'D'], 'DUH', 4,-1))
    True
        
    '''
    #to collect letters from lists that match word
    new_list = []

    
    #validate that index is in range 
    if not is_outside_list(letter_list, index):
        
            
            for j in range(len(word)):
                if letter_list[index] == word[j]:
                    new_list += letter_list[index]
                    
                    #transversing right to left:
                    if direction == RIGHT_LEFT:
                        index += 1
                    
                    #transversing left to right:
                    if direction == LEFT_RIGHT:
                        index -= 1
                    
                    if len(new_list) == len(word):
                        return True
                    
                    if is_outside_list(letter_list, index):
                        return False
        
    return False

#question 4
def direction_word_given_position(letter_list, word, index):
    '''
     (list<str>, str, int) -> list<int>
     
     Returns a list of directions in which the word has been found. If the word
     is not found, then the function will return an empty list        
        
    >>> direction_word_given_position(['A','B','C','D', 'C', 'M'], 'MCD', 6)
    []
    >>> direction_word_given_position(['A','B','C','D', 'C', 'M'], 'MCD', 5)
    [-1]
    >>> direction_word_given_position(['A','B','C','D', 'C', 'M'], 'MOM', 5)
    []
    >>> direction_word_given_position(['M','O','M','O', 'O', 'M'], 'MO', 2)
    [-1, 1]
        '''
    
    direction_list = []
    
    if not is_outside_list(letter_list, index):
        
        if word[0] == letter_list[index]:
            if valid_word_pos_direction(letter_list, word, index, LEFT_RIGHT):
                direction_list += [LEFT_RIGHT]
                
            if valid_word_pos_direction(letter_list, word, index, RIGHT_LEFT):
                direction_list += [RIGHT_LEFT]
        
    return direction_list

#question 5
def position_direction_word(letter_list, word):
    '''
    (list<str>, str) -> list<list<str>
    
    Returns a nested list containing a list pairing indices and positions where
    the word can be found in the letter list
    
    >>> position_direction_word(['A','M','U','U', 'M', 'M'],'MUUM')
    [[1, 1], [4, -1]]
    >>> position_direction_word(['A','M','U','U', 'M', 'M'],'DUUH')
    []
    >>> position_direction_word(['A','U','P','A', 'A', 'P'],'UP')
    [[1, 1]]
    '''
    new_list= []
    
    character = word[0]
    
    index = letter_positions(letter_list, character)
    
    #if the word is not found in the list 
    if index == []:
        return new_list
    
    
    #for each index find the direction of the word
    for i in range(len(index)):
        
        direction = direction_word_given_position(letter_list, word, index[i])
        
        #pair each direction with it's index
        for j in range(len(direction)):
            new_list += ([[index[i]] + [direction[j]]])
        
        #end for loop when list ends
        if i == (len(index)-1):
            return new_list
        

#question 6
def cross_word_position_direction(bool_letter_list, length_word, index, direction):  
    '''
    (list<boolean>, list<str>, int, int) -> None
    
    Mutates list based on where a word is found at which index and in
    which direction
    
    >>> l = [True, False, True, False, True, False]
    >>> cross_word_position_direction(l,3, 5, -1)
    >>> l
    [True, False, True, True, True, True]
    
    >>> l = [True, True, True, False, False, False]
    >>> cross_word_position_direction(l, 2, 6, -1)
    >>> l
    [True, True, True, False, False, False]
    
    >>> l = [True, True, True, True, False, False]
    >>> cross_word_position_direction(l,2, 4, 1)
    >>> l
    [True, True, True, True, True, True]
    '''
    
    if not is_outside_list(bool_letter_list, index):
    
    
        for i in range (length_word):
            bool_letter_list[index] = True
            
            #transverse right to left
            if direction == RIGHT_LEFT:
                index += 1
            
            #transverse left to right
            if direction == LEFT_RIGHT:
                index -= 1
        
    else:
        bool_letter_list
    

#question 7
def cross_word_all_position_direction(bool_letter_list, length_word,
    list_position_direction):
    
    '''
    (list<boolean>, int, list<list<int>) -> None
    
    Mutates booleans list after calling cross_word_position_direction

    
    >>> l = [False, False, False, False, False,False,False]
    >>> cross_word_all_position_direction(l, 2, [[3,-1],[3,1]])
    >>> l
    [False, False, True, True, True, False, False]
    
    >>> l = [False, False, False, False, False,False,False]
    >>> cross_word_all_position_direction(l, 2, [[3,1]])
    >>> l
    [False, False, False, True, True, False, False]
    
    
    >>> l= [False, False, False, False, False,False,False]
    >>> cross_word_all_position_direction(l, 4, [])
    >>> l
    [False, False, False, False, False, False, False]
    '''

    #for empty list_position_direction (word is not in the list) return the
    #same bool_letter_list
    if len(list_position_direction) == 0:
        bool_letter_list
           
    #for nested lists
    elif type(list_position_direction[0]) == list:
        
        for i in range(len(list_position_direction)):
            
            index = list_position_direction[i][0]

            direction = list_position_direction[i][1]

            cross_word_position_direction(bool_letter_list, length_word, index,
                                          direction)
    
#question 8
def find_magic_word(letter_list, bool_letter_list):
    '''
    (list<str>, list<boolean>) -> str
    

    Returns the magic word in the list found when the remaining letters are
    collected after crossing off the words based on the boolean_list  
    
    >>> find_magic_word(['C','A','B','C','D','O','M','P'],[False, True, True,True,True,False,False,False])
    'COMP'
    >>> find_magic_word(['A','A','P','L','D','D','U','P'], [True, True, True,True,True,True,True,True])
    ''
    
    >>> find_magic_word(['A','A','P','L','D','D','U','H'],[False, True,True,True,False,True,True])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/Users/ashraqat/Desktop/assignment_3.py", line 295, in find_magic_word
        raise ValueError('Both lists should have the same size')
    ValueError: Both lists should have the same size
    '''
    magic_list = []
    
    if len(letter_list) != len(bool_letter_list):
        
        raise ValueError('Both lists should have the same size')
    
    for i in range(len(bool_letter_list)):
        
        if bool_letter_list[i] == False:
            magic_list += letter_list[i]
    
    magic_word = ''.join(magic_list)
    
    return magic_word
    
#question 9
def word_search(letter_list,word_list):
    '''
    (list<letter>, list<str>) -> str 
    

    Returns the magic word in the list found when the remaining letters are
    collected after crossing off the words using find_magic_word()
    
    >>> word_search(['C','W','I','K','I','P','E','D','I','A','O','M','M','O','D','N','A','R','P'],['WIKIPJEDIA','FANDOM'])
    'CWIKIPEDIAOMMODNARP'
    
    >>> word_search(['C','N','I','K','I','F','E','E','L','S','O','S','S','A','D','G','A','A','T'],['NIKI','FEELS','SO','SSAD'])
    'CGAAT'
    
    >>> word_search(['C','N','I','K','I','F','E','E','L','S','O','S','S','A','D','G','A','A','T'],['VIKI','VEELS','ZO','ZZAD'])
    'CNIKIFEELSOSSADGAAT'
    
    ''' 
    bool_letter_list = [False] * len(letter_list)

    
    for i in range(len(word_list)):
        
        word = word_list[i]
        
        list_position_direction = position_direction_word(letter_list, word)
        
        if list_position_direction != []:
            length_word = len(word)
            
            #modify bool_letter_list
            cross_word_all_position_direction(bool_letter_list, length_word,
                                              list_position_direction)
    
    magic_word = find_magic_word(letter_list, bool_letter_list)
    
    return magic_word

#question 10
def word_search_main(letters,words):
    '''
   (str, str) -> str

    Returns the magic word after calling word_search
    
    Examples:
    >>> word_search_main('PjAVA++CJSYLQSPHPTGOHNILTOKOmatLABNTFIWSRUSTYBURTRAd', 'java-C++-JS-SQL-php-GO-kotlin-MATLaB-SWIFT-RUSt-ruby-DART')
    'PYTHON'
    
    >>> word_search_main('happybthanksgivingytcoe','happy-thanksgiving-oct')
    'BYE'
    
    >>> word_search_main('happybthanksgivingytoee','-happythanksgiving-Oct')
    'BYTOEE'
    
    '''
    words = words.upper()

    words = words.split('-')

    letter_list = list(letters.upper())
          
    magic_word = word_search(letter_list, words)
    
    return magic_word

