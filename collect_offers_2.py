from sys import get_int_max_str_digits
from requests import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from custom_funcs import get_json






def forming_search( search_text, replacing_dict ):

    for s1 in [* replacing_dict.keys() ]:

        output_str = ''
        
        i=0
        while  i < len( search_text )  :
            
            if search_text[i:i+len( s1 ):] ==  s1  :
                output_str += replacing_dict[ s1 ]
                i+=len( s1 )
            
            else:
                output_str += search_text[i]
                i+=1
        
        search_text = output_str

    return search_text    



def collect_attrs( offer_item, attrs_pathes ):

    #print(attrs_pathes)

    attributes = {}

    
    for attr in [* attrs_pathes.keys()] :
        
        if type( attrs_pathes[ attr ] ) is dict:
        
            
            if  [* attrs_pathes[ attr ].keys() ] == [ "xpath", "mode" ]:

                
                if    attrs_pathes[ attr ][ "xpath" ]  is not  False   :
                    attr_item = offer_item.find_element(  By.XPATH, attrs_pathes[ attr ][ "xpath" ] )
                    match attrs_pathes[ attr ][ "mode" ]: #attributes[
                    
                        case "href":
                            attributes[ attr ] = attr_item.get_attribute("href")

                        case "text":
                            attributes[ attr ] = attr_item.text   
            
            
            else :
                collect_attrs( offer_item= offer_item, attrs_pathes= attrs_pathes[ attr ]  )


    return attributes    




def get_offers_items( browser, search_text, shops_ids=[] ): # int protection ?

    
    offers = {}
    shops_db = get_json( "shops_db.json" )

    
    for shop_i in shops_ids:
            
        
        shop_data = shops_db["shops_db"][str(  shop_i  )]


        shop_url = shop_data['url']
        offer_xpath = shop_data['item_xpath']
        search_prop = shop_data['search_params']['url_construct']['search_prop']
        replacing_dict = shop_data['search_params']['url_construct']['replacing']
        attrs_xpath = shop_data['attributes_xpath']
        #page_ident = shop_data['search_params']['url_construct']['page_prop']
        #pmi_item = shop_data['pages_params']['pages_mount_item_xpath']
        
        formated_search = forming_search( search_text, replacing_dict )


        offers[ shop_i ] = { "0":"0" }        
        
        
        
        for sp in search_prop :

        
        
            search_url = f"{ shop_url }/{ sp }/{ formated_search }"  
            
            
            
            def read_page(  browser, shop_data, offers, search_url, page_ident=""  ):

                offer_xpath = shop_data['item_xpath']

                browser.get(  f"{ search_url }/{ page_ident }" )
        
                item_id= int( [* offers.keys()][-1] ) + 1
                for offer_item in browser.find_elements( By.XPATH, offer_xpath ):

                    
                    offers[ item_id ] = collect_attrs( offer_item, attrs_xpath )

                    item_id += 1

                print(browser.find_elements( By.XPATH, offer_xpath ))    

                #next_page( browser, shop_data, offers )
                #enext_page_xpath = shop_data["pages_params"]["next_page_xpath"]

                def get_next_page_url( browser, shop_data ):
                    
                    next_page_button = shop_data["pages_params"]["next_page_button"]

                    try:
                        npb = browser.find_element( By.XPATH, next_page_button["xpath"] )

                        match next_page_button["mode"] :

                            case "href":
                                next_url= npb.get_attribute("href")
                                return next_url #return f"{ shop_data['url'] }{ next_url }"

                    finally: 
                        return False            

                np_url = get_next_page_url( browser, shop_data )
                if np_url is not False:
                    offers.update(  read_page( browser, shop_data, offers, search_url, page_ident= np_url  ))
                
                
                return offers
                    

            offers[shop_i] = read_page( browser, shop_data, offers[ shop_i ], search_url )


    return offers            




def main():

    ep = Service(R"C:\Users\nikita\Downloads\chromedriver_win32\chromedriver.exe")
    browser = webdriver.Chrome( service= ep )#ChromeDriverManager().install()

    print( get_offers_items( browser, "Air jordan 1", shops_ids=[0] ) )

    

if __name__=="__main__":
    main()
