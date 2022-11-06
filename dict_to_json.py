def replace( big_ass, s1, s2 ):

    output_str = ''
        
    i=0
    while  i < len( big_ass )  :
            
        if big_ass[i:i+len( s1 ):] ==  s1  :
            output_str += s2
            i+=len( s1 )
            
        else:
            output_str += big_ass[i]
            i+=1
    
    return output_str


def main():

    f = open("dict_to_json.txt","r")
    main_s = f.readlines()
    f.close()


    replace_dict={
        "{'":'{"',
        "'}":'"}',
        "': '":'": "',
        "', '":'", "',
        
    }    

    for s1 in [* replace_dict.keys() ]:
        main_s = replace( main_s, s1, replace_dict[s1] )

    print( main_s )    



if __name__ == "__main__":
    main()