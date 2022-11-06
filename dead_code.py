def get_int( _string, sort=True  ):

    
    ints = []

    num = ""
    for i in _string :

        if i.isdigit() :
            num += i

        elif num != "" :
            ints.append( int( num ) )    
            num = ""

    if  num != "" :
        ints.append( int( num ) )    
        num = ""      
        
        
    
    
    
    if sort is True :        
        ints.sort()

    return ints    





def get_pages_list( browser, pmi_item ):
    
    pmi = browser.find_element( By.XPATH, pmi_item["xpath"] )

    
    match pmi_item["mode"]:
        
        case "text":
            pages_mount = pmi.text

        case _:
            return None    

    
    ints = get_int( _string= pages_mount, sort= True )

    return ints[-1]