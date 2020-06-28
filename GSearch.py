from google_images_search import GoogleImagesSearch
class GSearch:




    _search_params = {
        'q': 'puppies',
        'num': 1
    }

    
    def SearchNow(Query):

        Query = str(Query);
        params = {
            'q' : Query,
            'num' : 1,
            
        }
        gis.search(search_params=params, path_to_dir='assets/');

