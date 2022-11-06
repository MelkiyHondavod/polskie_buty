import json

def get_json( file_name, file_path= None ):
    
    if file_path == None:
        with open("config.json") as c_f:
            file_path = json.load( c_f )["common_data"]["folder_path"]
    
    with open( f"{file_path}\\{file_name}" ) as j_f :
        json_data = json.load( j_f )

    return json_data    

