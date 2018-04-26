from gist_search.utils import get_gists


def search_gists(username, description=None, file_name=None):
    result = []
    if not description and not file_name:
        print("At least one search parameter must be specified")
        return
    gists = get_gists(username)
    
    # inverse  (filter out failures and add everything remaining at end)
    # LIMITS THE NUMBER OF PERMUTATIONS COMBINATIONS IN A POSITIVE APPROACH
    # 
    
    for gist in gists:
        if description and description not in gist["description"]:
            continue
        
        if file_name:
            found = False
            for file_names in gist['files']:
                if file_name in file_names:
                    found = True
            if not found :
                continue
    
        result.append(gist)
    return result
    

        
        
if __name__ == '__main__':
    search_gists("santiagobasulto",file_name="tests") 