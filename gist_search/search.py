from gist_search.utils import get_gists


def search_gists(username, description=None, file_name=None):
    result = []
    if not description and not file_name:
        print("At least one search parameter must be specified")
        return
    gists = get_gists(username)
    
    if description:
        for gist in gists:
            if description in gist["description"]:
                result.append(gist)
        return result

    if file_name:
        for gist in gists:
            for file_names in gist['files']:
                if file_name in file_names:
                    print(file_name)
                    result.append(gist)
                    break
        return result
        
        
if __name__ == '__main__':
    search_gists("santiagobasulto",file_name="tests") 