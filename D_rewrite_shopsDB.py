
import json



def write_json_file(  data, file_name  ):
    try:
        f = open( file_name, "w" )
        json.dump( data, f, indent=4 )
    finally:
        f.close()    



def get_links_list():
    links="""https://www.zalando.pl
https://worldbox.pl
https://chmielna20.pl
https://7kicks.pl
https://runcolors.pl
https://sneakerstudio.pl
https://sklep.sizeer.com
https://www.eobuwie.com.pl
https://answear.com
https://www.eobuwie.com.pl
https://galeriamarek.pl
https://50style.pl
https://streetsupply.pl
https://www.vitkac.com/pl
https://gomez.pl
https://modivo.pl
http://www.sportjam.pl
https://www.active.sklep.pl
https://supersklep.pl
https://www.mantoshop.pl
https://www.uterque.com/pl
https://www.massimodutti.com/pl
https://www.spartoo.pl"""

    return links.split("\n")


def update_shops_dict():

    try:
        with open("config.json", "r+") as f:
            
            shops = get_links_list()
            
            j_d = json.load( f )

            for i in range(0, len(shops)):
                j_d["common_data"]["shops_list"] = shops
            
            f.seek(0)
            json.dump( j_d, f, indent=4 )
            f.truncate()

    finally:
        f.close()



def build_shops_dict():

    """fill shops_db by links in <get_links_list>
    linked with: [ 
        confi.json \\ item_possible_attributes ;
        get_links_list() \\ links
     ]"""

    
    
    def build_attrs_xpath_false_dict():
        
        try:
            c_f = open("config.json", "r+")
            item_attrs = json.load( c_f )["item_possible_attributes"].copy()

        finally:
            c_f.close()    

        
        def dict_full_false( polymetric_dict ): #wtf polymetric

            output_dict = {}

            for key in [*polymetric_dict.keys()]:
                
                if type( polymetric_dict[key] ) is dict:
                    output_dict[ key ] =     dict_full_false( polymetric_dict[key] )

                else:
                    output_dict[ key ] = { 
                        "xpath":False, 
                        "mode":False 
                        }

            return output_dict

        return dict_full_false( item_attrs )


    def rewrite_shops_db( db_name= "shops_db", save_backup= True ):
        try:

            shops_links = get_links_list()

            d_f = open( f"{ db_name }.json", "r+" )
            shops_json = json.load( d_f )


            
            if save_backup is True :
                write_json_file(  shops_json, f"backups\\BACKUP_{ db_name }.json"  )
                


            for i in range(0, len( shops_links ) ):
                shop_obj = shops_json["shop_pattern"].copy()

                shop_obj["id"] = i
                shop_obj["url"] = shops_links[i]
                shop_obj["attributes_xpath"] = build_attrs_xpath_false_dict( )

                shops_json["shops_db"][ str( i ) ] = shop_obj

            d_f.seek(0)
            json.dump( shops_json, d_f, indent=4 )    
            d_f.truncate()



        finally:
            d_f.close()

    
    
    
    rewrite_shops_db()



def main():
    
    #print( get_links_list() )
    #update_shops_dict()

    #   ALARM!!!  DANGER!!! this program will rewrite shops data base! make sure you have create backup file!
    if input("password:") == "Yes, rewrite" :
        build_shops_dict()

    
    
    



if __name__=="__main__":
    main()
    print("finished")