def build_keys( polymetric_dict ): #wtf polymetric

            output_dict = {}

            for key in [*polymetric_dict.keys()]:
                
                if type( polymetric_dict[key] ) is dict:
                    output_dict[ key ] =     build_keys( polymetric_dict[key] )

                else:
                    output_dict[ key ] = False

            return output_dict


a={
        "title":"",
        "price":{
                "pln":0,
                "usd":0,
                "eur":0,
                "byn":0
                },
        "brand":"",
        "link":"",
        "shop_labels": []
    }


#print( build_keys(a)            )

if type("huj") == str:
    print("da")

    match type( "huj" ) :

        case dict :
            print('its dict')
                
        case str :
            print('its str')
            
            