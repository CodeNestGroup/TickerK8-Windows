# Requests na urllbi

#############################
#       Introduction        #
#############################



#   The Pexels API enables programmatic access to the full Pexels content library, including photos, videos.
#   All content is available free of charge, and you are welcome to use Pexels content for anything you'd like, as long as it is within our Guidelines.
#   The Pexels API is a RESTful JSON API, and you can interact with it from any language or framework with an HTTP library.
#   Alternately, Pexels maintains some official Client Libraries you can use.
#   If you have any questions, feel free to check out our FAQ or email us at api@pexels.com.
#   Note: For historical reasons, all endpoints begin with https://api.pexels.com/v1/ except for video endpoints, which begin with https://api.pexels.com/videos/.
#   Please see the individual endpoints listed below for more details about how to call each endpoint.






#########################
#       Guidelines      #
#########################



#   Whenever you are doing an API request make sure to show a prominent link to Pexels.
#   You can use a text link (e.g. "Photos provided by Pexels") or a link with our logo.
#   Always credit our photographers when possible (e.g. "Photo by John Doe on Pexels" with a link to the photo page on Pexels).
#   You may not copy or replicate core functionality of Pexels (including making Pexels content available as a wallpaper app).
#   Do not abuse the API. By default, the API is rate-limited to 200 requests per hour and 20,000 requests per month.
#   You may contact us to request a higher limit, but please include examples, or be prepared to give a demo, that clearly shows your use of the API with attribution.
#   If you meet our API terms, you can get unlimited requests for free.
#   Abuse of the Pexels API, including but not limited to attempting to work around the rate limit, will lead to termination of your API access.



#############################
#       Authorization       #
#############################



#   Authorization is required for the Pexels API. Anyone with a Pexels account can request an API key, which you will receive instantly.
#   All requests you make to the API will need to include your key. This is provided by adding an Authorization header.
#   Exemple:
#   requests.get('https://api.pexels.com/v1/search', headers={'Authorization': f'{self.api_key}'})


import requests, time, json


class Pexels(object):
#   Self variables
    def __init__(self):
        super().__init__()
        self.api_key = None

#   Api | Set Key
    def Api_key_set(self, key=str):
        self.api_key = key



#################################
#       Request Statistics      #
#################################



#   To see how many requests you have left in your monthly quota, successful requests from the Pexels API include three HTTP headers:
#   Response Header:	    Meaning:
#   X-Ratelimit-Limit	    Your total request limit for the monthly period
#   X-Ratelimit-Remaining 	How many of these requests remain
#   X-Ratelimit-Reset	    UNIX timestamp of when the currently monthly period will roll over
#   Note: These response heaaders are only returned on successful (2xx) responses.
#   They are not included with other responses, including 429 Too Many Requests, which indicates you have exceeded your rate limit.
#   Please be sure to keep track of X-Ratelimit-Remaining and X-Ratelimit-Reset in order to manage your request limit.



#   Api | Ratelimit | Limit
    def x_ratelimit_limit(self):
        if not self.api_key:
            raise ApiKeyError()
        api_response = requests.get('https://api.pexels.com/v1/search',
                                    headers={'Authorization': f'{self.api_key}'
                                             },
                                    params={"query": "a",
                                            "per_page": 1
                                            }
                                    )
        if api_response.status_code == 200:
            return api_response.headers.get('X-Ratelimit-Limit')
        else:
            raise ApiResponseError(api_response.status_code)




#   Api | Ratelimit | Remaining
    def x_ratelimit_remaining(self):
        if not self.api_key:
            raise ApiKeyError()
        api_response = requests.get('https://api.pexels.com/v1/search',
                                    headers={'Authorization': f'{self.api_key}'
                                         },
                                    params={"query": "a",
                                            "per_page": 1
                                        }
                                )
        if api_response.status_code == 200:
            return api_response.headers.get('X-Ratelimit-Remaining')
        else:
            raise ApiResponseError(api_response.status_code)



#   Api | Ratelimit | Reset
    def x_ratelimit_reset(self):
        if not self.api_key:
            raise ApiKeyError()
        api_response = requests.get('https://api.pexels.com/v1/search',
                                    headers={'Authorization': f'{self.api_key}'
                                        },
                                    params={"query": "a",
                                            "per_page": 1
                                       }
                                )
        if api_response.status_code == 200:
            return time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime(int(api_response.headers.get('X-Ratelimit-Reset'))))
        else:
            raise ApiResponseError(api_response.status_code)



#########################
#       Pagination      #
#########################


#   Most Pexels API requests return multiple records at once. All of these endpoints are paginated, and can return a maximum of 80 requests at one time.
#   Each paginated request accepts the same parameters and returns the same pagination data in the response.
#   Note: The prev_page and next_page response attributes will only be returned if there is a corresponding page.





######################
#       Photos      #
#####################



#   Api | Photos | The Photo Resource
#   Description:
#   The Photo resource is a JSON formatted version of a Pexels photo. The Photo API endpoints respond with the photo data formatted in this shape.

    def the_photo_resource(self, photo_id):
        if not self.api_key:
            raise ApiKeyError()
        if type(photo_id) != int:
            raise ApiDataTypeError('photo_id', 'int', photo_id)
        api_response = requests.get(f'https://api.pexels.com/v1/photos/{photo_id}',
                            headers={'Authorization': f'{self.api_key}'})
        if api_response.status_code == 200:
            return api_response.json()
        else:
            raise ApiResponseError(api_response.status_code)

#   Response:
#   - id (integer) - The id of the photo
#   - width (integer) - The real width of the photo in pixels
#   - height (integer) - The real hieght of the photo in pixels
#   - url (string) - The Pexels URL where the photo is located.
#   - photographer (string) - The name of the photographer who took the photo.
#   - photographer_url (string) - The URL of the photographer's Pexels profile.
#   - photographer_id (integer) - The id of the photographer.
#   - avg_color (string) - The average color of the photo. Useful for a placeholder while the image loads.
#   - src (object) - An assortment of different image sizes that can be used to display this Photo.
#       * original (string) - The image without any size changes. It will be the same as the width and height attributes.
#       * large (string) - The image resized to W 940px X H 650px DPR 1.
#       * large2x (string) - The image resized W 940px X H 650px DPR 2.
#       * medium (string) - The image scaled proportionally so that it's new height is 350px.
#       * small (string) - The image scaled proportionally so that it's new height is 130px.
#       * portrait (string) - The image cropped to W 800px X H 1200px.
#       * landscape (string) - The image cropped to W 1200px X H 627px.
#       * tiny (string) - The image cropped to W 280px X H 200px.
#   - alt (string) - Text description of the photo for use in the alt attribute.



#   Api | Photos | Search Photos
#   Description:
#   GET https://api.pexels.com/v1/search
#   This endpoint enables you to search Pexels for any topic that you would like.
#   For example your query could be something broad like Nature, Tigers, People. Or it could be something specific like Group of people working.

    def search_for_photos(self, query='Exemple', orientation='landscape', size='small', color='red', locale='en-US', page=1, per_page=15):
        # Rise Errors for Api
        # Api | Error | Key
        if not self.api_key:
            raise ApiKeyError()
        # Api | Error | Data Type
        if type(query) != str:
            raise ApiDataTypeError('Query', 'str', query)
        elif type(page) != int:
            raise ApiDataTypeError('Page', 'int', page)
        elif type(per_page) != int:
            raise ApiDataTypeError('Page', 'int', per_page)
        # Api | Error | Insert
        elif orientation not in ('landscape', 'portrait', 'squere'):
            raise ApiDataInsertError('orientation')
        elif size not in ('small', 'medium', 'large'):
            raise ApiDataInsertError('size')
        elif color not in ('red', 'orange', 'yellow', 'green', 'turquoise', 'blue', 'violet', 'pink', 'brown', 'black', 'gray', 'white') and not color_hex(color):
            raise ApiDataInsertError('color')
        elif locale not in ('en-US', 'pt-BR', 'es-ES', 'ca-ES', 'de-DE', 'it-IT', 'fr-FR', 'sv-SE', 'id-ID', 'pl-PL', 'ja-JP', 'zh-TW', 'zh-CN', 'ko-KR', 'th-TH', 'nl-NL', 'hu-HU', 'vi-VN', 'cs-CZ',
                            'da-DK', 'fi-FI', 'uk-UA', 'el-GR', 'ro-RO', 'nb-NO', 'sk-SK', 'tr-TR', 'ru-RU'):
            raise ApiDataInsertError('locale')
        elif per_page > 80:
            raise ApiDataInsertError('per_page')

        # Query
        api_response = requests.get('https://api.pexels.com/v1/search',
                                    headers={'Authorization': f'{self.api_key}'},
                                    params={'query': query,                 # Query       | (string, required)  | The search query. Ocean, Tigers, Pears, etc.
                                            'orientation': orientation,     # Orientation | (string, optional)  | Desired photo orientation. The current supported orientations are: landscape, portrait or square.
                                            'size': size,                   # Size        | (string, optional)  | Minimum photo size. The current supported sizes are: large(24MP), medium(12MP) or small(4MP).
                                            'color': color,                 # Color       | (string, optional)  | Desired photo color. Supported colors: red, orange, yellow, green, turquoise, blue, violet, pink, brown, black, gray, white or any hexidecimal color code (e.g. #ffffff).
                                            'locale': locale,               # Locale      | (string, optional)  | The locale of the search you are performing. The current supported locales are: 'en-US'
                                            'page': page,                   # Page        | (integer, optional) | The page number you are requesting. Default: 1
                                            'per_page': per_page,           # Per Page    | (integer, optional) | The number of results you are requesting per page. Default: 15 Max: 80
                                            })
        # Rise Error for HTTP
        if api_response.status_code == 200:
            return api_response.json()
        else:
            raise ApiResponseError(api_response.status_code)

#   Response:
#   - total_results (integer) - The total number of results for the request.
#   - page (integer) - The current page number.
#   - per_page (integer) - The number of results returned with each page.
#   - photos (array) - An array of Photo objects.
#       * id (integer) - Photo id.
#       * width (integer) - Width of Photo.
#       * height (integer) - Height of Photo.
#       * url (string) - Url to Photo.
#       * photographer (string) - Name and surname of Photograpger
#       * photographer_url (string) - Url to Photograhper of Photo.
#       * photographer_id (intiger) - Photographer ID.
#       * avg_color (string) - Average color of image.
#       * src (string) - Url address to formats of Photo.
#           - original (string) - Url address to orginal size Photo.
#           - large2x (string) - Url address to large x 2 size Photo.
#           - large (string) - Url address to large size Photo.
#           - medium (string) - Url address to medium size Photo.
#           - small (string) - Url address to small size Photo.
#           - portrait (string) - Url address to portrait size Photo.
#           - landscape (string) - Url address to landscape size Photo.
#           - tiny (string) - Url address to tiny size Photo.
#       * liked (bool) - Bool if you liked Photo.
#       * alt (string) - Alternative text if image doesn't load.
#   - prev_page (string, optional) - URL for the previous page of results, if applicable.
#   - next_page (string, optional) - URL for the next page of results, if applicable.



#   Api | Photos | Curated Photos
#   Description:
#   GET https://api.pexels.com/v1/curated
#   This endpoint enables you to receive real-time photos curated by the Pexels team.
#   We add at least one new photo per hour to our curated list so that you always get a changing selection of trending photos.

    def curated_photos(self, page=1, per_page=15):
        # Rise Errors for API
        # Api | Error | Key
        if not self.api_key:
            raise ApiKeyError()
        # Api | Error | Data Type
        elif type(page) != int:
            raise ApiDataTypeError('Page', 'int', page)
        elif type(per_page) != int:
            raise ApiDataTypeError('Page', 'int', per_page)
        # Api | Error | Insert
        elif per_page > 80:
            raise ApiDataInsertError('per_page')
        api_response = requests.get('https://api.pexels.com/v1/curated',
                                    headers={'Authorization': f'{self.api_key}'},
                                    params={'page': page,                   # Page        | (integer, optional) | The page number you are requesting. Default: 1
                                            'per_page': per_page            # Per Page    | (integer, optional) | The number of results you are requesting per page. Default: 15 Max: 80
                                            })
        if api_response.status_code == 200:
            return api_response.json()
        else:
            raise ApiResponseError(api_response.status_code)

#   Response:
#   - total_results (integer) - The total number of results for the request.
#   - page (intiger) - The current page number.
#   - per_page (integer) - The number of results returned with each page.
#   - photos (array) - An array of Photo objects.
#       * id (integer) - Photo id.
#       * width (integer) - Width of Photo.
#       * height (integer) - Height of Photo.
#       * url (string) - Url to Photo.
#       * photographer (string) - Name and surname of Photograpger
#       * photographer_url (string) - Url to Photograhper of Photo.
#       * photographer_id (intiger) - Photographer ID.
#       * avg_color (string) - Average color of image.
#       * src (string) - Url address to formats of Photo.
#           - original (string) - Url address to orginal size Photo.
#           - large2x (string) - Url address to large x 2 size Photo.
#           - large (string) - Url address to large size Photo.
#           - medium (string) - Url address to medium size Photo.
#           - small (string) - Url address to small size Photo.
#           - portrait (string) - Url address to portrait size Photo.
#           - landscape (string) - Url address to landscape size Photo.
#           - tiny (string) - Url address to tiny size Photo.
#       * liked (bool) - Bool if you liked Photo.
#       * alt (string) - Alternative text if image doesn't load.
#   - prev_page (string, optional) - URL for the previous page of results, if applicable.
#   - next_page (string, optional) - URL for the next page of results, if applicable.



#   Api | Photos | Get a Photo
#   Description:
#   GET https://api.pexels.com/v1/photos/:id
#   Retrieve a specific Photo from its id.
    def get_a_photo(self, id_photo):
        # Rise Errors for API
        # Api | Error | Key
        if not self.api_key:
            raise ApiKeyError()
        # Api | Error | Data Type
        elif type(id_photo) != int:
            raise ApiDataTypeError('Id Photo', 'int', id_photo)
        api_response = requests.get(f'https://api.pexels.com/v1/photos/:{id_photo}',        # id | (integer, required) | The id of the photo you are requesting.
                                    headers={'Authorization': f'{self.api_key}'})
        if api_response.status_code == 200:
            return api_response.json()
        else:
            raise ApiResponseError(api_response.status_code)

#   Response:
#   - id (integer) - The id of the photo
#   - width (integer) - The real width of the photo in pixels
#   - height (integer) - The real hieght of the photo in pixels
#   - url (string) - The Pexels URL where the photo is located.
#   - photographer (string) - The name of the photographer who took the photo.
#   - photographer_url (string) - The URL of the photographer's Pexels profile.
#   - photographer_id (integer) - The id of the photographer.
#   - avg_color (string) - The average color of the photo. Useful for a placeholder while the image loads.
#   - src (object) - An assortment of different image sizes that can be used to display this Photo.
#       * original (string) - The image without any size changes. It will be the same as the width and height attributes.
#       * large (string) - The image resized to W 940px X H 650px DPR 1.
#       * large2x (string) - The image resized W 940px X H 650px DPR 2.
#       * medium (string) - The image scaled proportionally so that it's new height is 350px.
#       * small (string) - The image scaled proportionally so that it's new height is 130px.
#       * portrait (string) - The image cropped to W 800px X H 1200px.
#       * landscape (string) - The image cropped to W 1200px X H 627px.
#       * tiny (string) - The image cropped to W 280px X H 200px.
#   - alt (string) - Text description of the photo for use in the alt attribute.



#####################
#       Videos      #
#####################



#   Api | Videos | The Video Resource
#   Description:
#   The Video resource is a JSON formatted version of a Pexels video. The Video API endpoints respond with the video data formatted in this shape.

    def the_video_resource(self, id_video):
        # Rise Errors for API
        # Api | Error | Key
        if not self.api_key:
            raise ApiKeyError()
        # Api | Error | Data Type
        elif type(id_video) != int:
            raise ApiDataTypeError('Id Video', 'int', id_video)
        api_response = requests.get(f'https://api.pexels.com/v1/videos/{id_video}',  # id | (integer, required) | The id of the photo you are requesting.
                                    headers={'Authorization': f'{self.api_key}'})
        if api_response.status_code == 200:
            return api_response.json()
        else:
            raise ApiResponseError(api_response.status_code)

#   Response:
#   - id (integer) - The id of the video.
#   - width (integer) - The real width of the video in pixels.
#   - height (integer) - The real height of the video in pixels.
#   - url (string) - The Pexels URL where the video is located.
#   - image (string) - URL to a screenshot of the video.
#   - duration (integer) - The duration of the video in seconds.
#   - user (object) - The videographer who shot the video.
#       * id (integer) - The id of the videographer.
#       * name (string) - The name of the videographer.
#       * url (string) - The URL of the videographer's Pexels profile.
#   - video_files (array) - An array of different sized versions of the video.
#       * id (integer) - The id of the video_file.
#       * quality (string) - The video quality of the video_file.
#       * file_type (string) - The video format of the video_file.
#       * width (integer) - The width of the video_file in pixels.
#       * height (integer) - The height of the video_file in pixels.
#       * fps (integer) - The number of frames per second of the video_file.
#       * link (string) - A link to where the video_file is hosted.
#   - video_pictures (array) - An array of preview pictures of the video.
#       * id (integer) - The id of the video_picture.
#       * picture (string) - A link to the preview image.
#       * nr (integer)



#   Api | Videos | Search for Videos
#   Description:
#   GET https://api.pexels.com/videos/search
#   This endpoint enables you to search Pexels for any topic that you would like.
#   For example your query could be something broad like Nature, Tigers, People. Or it could be something specific like Group of people working.

    def search_for_videos(self, query, orientation='landscape', size='small', locale='en-US', page=1, per_page=15):
        # Rise Errors for API
        # Api | Error | Key
        if not self.api_key:
            raise ApiKeyError()
        # Api | Error | Data Type
        elif type(query) != str:
            raise ApiDataTypeError('Query', 'str', query)
        elif type(page) != int:
            raise ApiDataTypeError('Page', 'int', page)
        elif type(per_page) != int:
            raise ApiDataTypeError('Page', 'int', per_page)
        # Api | Error | Insert
        elif orientation not in ('landscape', 'portrait', 'squere'):
            raise ApiDataInsertError('orientation')
        elif size not in ('small', 'medium', 'large'):
            raise ApiDataInsertError('size')
        elif locale not in (
        'en-US', 'pt-BR', 'es-ES', 'ca-ES', 'de-DE', 'it-IT', 'fr-FR', 'sv-SE', 'id-ID', 'pl-PL', 'ja-JP', 'zh-TW', 'zh-CN', 'ko-KR', 'th-TH', 'nl-NL', 'hu-HU', 'vi-VN', 'cs-CZ',
        'da-DK', 'fi-FI', 'uk-UA', 'el-GR', 'ro-RO', 'nb-NO', 'sk-SK', 'tr-TR', 'ru-RU'):
            raise ApiDataInsertError('locale')
        elif per_page > 80:
            raise ApiDataInsertError('per_page')
        api_response = requests.get('https://api.pexels.com/videos/search',
                                    headers={'Authorization': f'{self.api_key}'},
                                    params={'query': query,                 # Query       | (string, required)  | The search query. Ocean, Tigers, Pears, etc.
                                            'orientation': orientation,     # Orientation | (string, optional)  | Desired video orientation. The current supported orientations are: landscape, portrait or square.
                                            'size': size,                   # Size        | (string, optional)  | Minimum video size. The current supported sizes are: large(4K), medium(Full HD) or small(HD).
                                            'locale': locale,               # Locale      | (string, optional)  | The locale of the search you are performing. The current supported locales are: 'en-US'
                                            'page': page,                   # Page        | (integer, optional) | The page number you are requesting. Default: 1
                                            'per_page': per_page,           # Per Page    | (integer, optional) | The number of results you are requesting per page. Default: 15 Max: 80
                                            })
        if api_response.status_code == 200:
            return api_response.json()
        else:
            raise ApiResponseError(api_response.status_code)

#   Response
#   - page (integer)
#   - per_page (integer)
#   - total_results (integer)
#   - url (string)
#   - videos (array)
#       * id (integer) - The id of the video.
#       * width (integer) - The real width of the video in pixels.
#       * height (integer) - The real height of the video in pixels.
#       * url (string) - The Pexels URL where the video is located.
#       * image (string) - URL to a screenshot of the video.
#       * duration (integer) - The duration of the video in seconds.
#       * user (array) - The videographer who shot the video.
#           - id (integer) - The id of the videographer.
#           - name (string) - The name of the videographer.
#           - url (string) -  The URL of the videographer's Pexels profile.
#       * video_files (array) - An array of different sized versions of the video.
#           - id (integer) - The id of the video_file.
#           - quality (string) - The video quality of the video_file.
#           - file_type (string) - The video format of the video_file.
#           - width (integer) - The width of the video_file in pixels.
#           - height (integer) - The height of the video_file in pixels.
#           - link (string) - A link to where the video_file is hosted.
#       * video_pictures (array) -  An array of preview pictures of the video.
#           - id (integer) - The id of the video_picture.
#           - picture (string) - A link to the preview image.
#           - nr (integer)
#   - prev_page (string)
#   - next_page (string)



#   Api | Videos | Popular Videos
#   Description:
#   GET https://api.pexels.com/videos/popular
#   This endpoint enables you to receive the current popular Pexels videos.

    def popular_videos(self, min_width=int, min_height=int, min_duration=int, max_duration=int, page=1, per_page=15):
        # Rise Errors for API
        # Api | Error | Key
        if not self.api_key:
            raise ApiKeyError()
        # Api | Error | Data Type
        elif type(min_width) != int:
            raise ApiDataTypeError('Min Width', 'int', min_width)
        elif type(min_height) != int:
            raise ApiDataTypeError('Min Height', 'int', min_height)
        elif type(min_duration) != int:
            raise ApiDataTypeError('Min Duration', 'int', min_duration)
        elif type(max_duration) != int:
            raise ApiDataTypeError('Max Duration', 'int', max_duration)
        elif type(page) != int:
            raise ApiDataTypeError('Page', 'int', page)
        elif type(per_page) != int:
            raise ApiDataTypeError('Per Page', 'int', per_page)
        # Api | Error | Insert
        elif per_page > 80:
            raise ApiDataInsertError('per_page')
        api_response = requests.get('https://api.pexels.com/videos/popular',
                                    headers={'Authorization': f'{self.api_key}'},
                                    params={'min_width': min_width,         # min_width    | (integer, optional) | The minimum width in pixels of the returned videos.
                                            'min_height': min_height,       # min_height   | (integer, optional) | The minimum height in pixels of the returned videos.
                                            'min_duration': min_duration,   # min_duration | (integer, optional) | The minimum duration in seconds of the returned videos.
                                            'max_duration': max_duration,   # max_duration | (integer, optional) | The maximum duration in seconds of the returned videos.
                                            'page': page,                   # page         | (integer, optional) | The page number you are requesting. Default: 1
                                            'per_page': per_page}           # per_page     | (integer, optional) | The number of results you are requesting per page. Default: 15 Max: 80
                                    )
        if api_response.status_code == 200:
            return api_response.json()
        else:
            raise ApiResponseError(api_response.status_code)

#   Response:
#   - page (integer)
#   - per_page (integer)
#   - total_results (integer)
#   - url (string)
#   - videos (array)
#       * id (integer) - The id of the video.
#       * width (integer) - The real width of the video in pixels.
#       * height (integer) - The real height of the video in pixels.
#       * url (string) - The Pexels URL where the video is located.
#       * image (string) - URL to a screenshot of the video.
#       * duration (integer) - The duration of the video in seconds.
#       * user (array) - The videographer who shot the video.
#           - id (integer) - The id of the videographer.
#           - name (string) - The name of the videographer.
#           - url (string) -  The URL of the videographer's Pexels profile.
#       * video_files (array) - An array of different sized versions of the video.
#           - id (integer) - The id of the video_file.
#           - quality (string) - The video quality of the video_file.
#           - file_type (string) - The video format of the video_file.
#           - width (integer) - The width of the video_file in pixels.
#           - height (integer) - The height of the video_file in pixels.
#           - link (string) - A link to where the video_file is hosted.
#       * video_pictures (array) -  An array of preview pictures of the video.
#           - id (integer) - The id of the video_picture.
#           - picture (string) - A link to the preview image.
#           - nr (integer)
#   - prev_page (string)
#   - next_page (string)



#   Api | Videos | Get a Video
#   Description:
#   GET https://api.pexels.com/videos/videos/:id
#   Retrieve a specific Video from its id.

    def get_a_video(self, id_video):
        # Rise Errors for API
        # Api | Error | Key
        if not self.api_key:
            raise ApiKeyError()
        # Api | Error | Data Type
        elif type(id_video) != int:
            raise ApiDataTypeError('Id Video', 'int', id_video)
        api_response = requests.get(f'https://api.pexels.com/videos/videos/:{id_video}',
                                    headers={'Authorization': f'{self.api_key}'})   # id | (integer, required) | The id of the video you are requesting.
        if api_response.status_code == 200:
            return api_response.json()
        else:
            raise ApiResponseError(api_response.status_code)

#   Response:
#   - page (integer)
#   - per_page (integer)
#   - total_results (integer)
#   - url (string)
#   - videos (array)
#       * id (integer) - The id of the video.
#       * width (integer) - The real width of the video in pixels.
#       * height (integer) - The real height of the video in pixels.
#       * url (string) - The Pexels URL where the video is located.
#       * image (string) - URL to a screenshot of the video.
#       * duration (integer) - The duration of the video in seconds.
#       * user (array) - The videographer who shot the video.
#           - id (integer) - The id of the videographer.
#           - name (string) - The name of the videographer.
#           - url (string) -  The URL of the videographer's Pexels profile.
#       * video_files (array) - An array of different sized versions of the video.
#           - id (integer) - The id of the video_file.
#           - quality (string) - The video quality of the video_file.
#           - file_type (string) - The video format of the video_file.
#           - width (integer) - The width of the video_file in pixels.
#           - height (integer) - The height of the video_file in pixels.
#           - link (string) - A link to where the video_file is hosted.
#       * video_pictures (array) -  An array of preview pictures of the video.
#           - id (integer) - The id of the video_picture.
#           - picture (string) - A link to the preview image.
#           - nr (integer)



#########################
#       Collections     #
#########################



#   Pexels Collections are a way to group specific photos and videos into one unified gallery.
#   This can be useful if, for example, you want to expose a specific subset of Pexels content to your users.
#   You can access all your collections and the media within them via the Pexels API.
#
#   Note: Collections cannot be created or modified using the Pexels API.
#   Rather, you can manage your collections on the Pexels website, iOS or Android app. API only gives you access to featured collections and your own collections.




#   Api | Collections | The Collection Resource
#   Description:
#   The Collection resource is a JSON formatted version of a Pexels collection. The Collection list endpoint responds with the collection data formatted in this shape.

    def the_collection_resource(self):
        if not self.api_key:
            raise ApiKeyError()
        api_response = requests.get('https://api.pexels.com/collection',
                                headers={'Authorization': f'{self.api_key}'})
        if api_response.status_code == 200:
            return api_response.json()
        else:
            raise ApiResponseError(api_response.status_code)

#   Response:
#   - id (string) - The id of the collection.
#   - title (string) - The name of the collection.
#   - description (string) - The description of the collection.
#   - private (boolen) - Whether the collection is marked as private.
#   - media_count (integer) - The total number of media included in this collection.
#   - photos_count (integer) - The total number of photos included in this collection.
#   - videos_count (integer) - The total number of videos included in this collection.



#   Api | Collections | Featured Collections
#   Description:
#   GET https://api.pexels.com/v1/collections/featured
#   This endpoint returns all featured collections on Pexels.

    def featured_collections(self, page=1, per_page=15):
        # Rise Errors for API
        # Api | Error | Key
        if not self.api_key:
            raise ApiKeyError()
        # Api | Error | Data Type
        elif type(page) != int:
            raise ApiDataTypeError('Page', 'int', page)
        elif type(per_page) != int:
            raise ApiDataTypeError('Per Page', 'int', per_page)
        # Api | Error | Insert
        elif per_page > 80:
            raise ApiDataInsertError('per_page')
        api_response = requests.get('https://api.pexels.com/v1/collections/featured',
                                    headers={'Authorization': f'{self.api_key}'},
                                    params={'page': page,                   # page     | (integer, optional) | The page number you are requesting. Default: 1
                                            'per_page': per_page})          # per_page | (integer, optional) | The number of results you are requesting per page. Default: 15 Max: 80
        if api_response.status_code == 200:
            return api_response.json()
        else:
            raise ApiResponseError(api_response.status_code)

#   Response:
#   - collections (array) - An array of Collection objects.
#       * id (string)
#       * title (string)
#       * description (boolean)
#       * private (boolean)
#       * media_count (integer)
#       * photos_count (integer)
#       * videos_count (integer)
#   - page (integer) - The current page number.
#   - per_page (integer) - The number of results returned with each page.
#   - total_results (integer) - The total number of results for the request.
#   - prev_page (string, optional) - URL for the previous page of results, if applicable.
#   - next_page (string, optional) - URL for the next page of results, if applicable.

#   Api | Collections | My Collections
#   Description:
#   GET https://api.pexels.com/v1/collections
#   This endpoint returns all of your collections.
    def my_collections(self, page=1, per_page=15):
        # Rise Errors for API
        # Api | Error | Key
        if not self.api_key:
            raise ApiKeyError()
        # Api | Error | Data Type
        elif type(page) != int:
            raise ApiDataTypeError('Page', 'int', page)
        elif type(per_page) != int:
            raise ApiDataTypeError('Per Page', 'int', per_page)
        # Api | Error | Insert
        elif per_page > 80:
            raise ApiDataInsertError('per_page')
        api_response = requests.get('https://api.pexels.com/v1/collections',
                                    headers={'Authorization': f'{self.api_key}'},
                                    params={'page': page,                   # page | (integer, optional) | The page number you are requesting. Default: 1
                                            'per_page': per_page})          # per_page | (integer, optional) | The number of results you are requesting per page. Default: 15 Max: 80
        if api_response.status_code == 200:
            return api_response.json()
        else:
            raise ApiResponseError(api_response.status_code)

#   Response:
#   - collections (array) - An array of Collection objects.
#       * id (string)
#       * title (string)
#       * description (boolean)
#       * private (boolean)
#       * media_count (integer)
#       * photos_count (integer)
#       * videos_count (integer)
#   - page (integer) - The current page number.
#   - per_page (integer) - The number of results returned with each page.
#   - total_results (integer) - The total number of results for the request.
#   - prev_page (string, optional) - URL for the previous page of results, if applicable.
#   - next_page (string, optional) - URL for the next page of results, if applicable.




#   Api | Collections | Collection Media
#   Description:
#   GET https://api.pexels.com/v1/collections/:id
#   This endpoint returns all the media (photos and videos) within a single collection. You can filter to only receive photos or videos using the type parameter.

    def collection_media(self, type_media='photos', sort='asc', page=1, per_page=15):
        # Rise Errors for API
        # Api | Error | Key
        if not self.api_key:
            raise ApiKeyError()
        # Api | Error | Data Type
        elif type(page) != int:
            raise ApiDataTypeError('Page', 'int', page)
        elif type(per_page) != int:
            raise ApiDataTypeError('Per Page', 'int', per_page)
        # Api | Error | Insert
        elif type_media not in ('photos', 'videos'):
            raise ApiDataInsertError('type_media')
        elif sort not in ('asc', 'desc'):
            raise ApiDataInsertError('sort')
        elif per_page > 80:
            raise ApiDataInsertError('per_page')
        api_response = requests.get('https://api.pexels.com/v1/collections/:id',
                                    headers={'Authorization': f'{self.api_key}'},
                                    params={'type': type_media,             # type     | (string, optional)  | The type of media you are requesting. If not given or if given with an invalid value, all media will be returned. Supported values are photos and videos.
                                            'sort': sort,                   # sort     | (string, optional)  | The order of items in the media collection. Supported values are: asc, desc. Default: asc
                                            'page': page,                   # page     | (integer, optional) | The page number you are requesting. Default: 1
                                            'per_page': per_page})          # per_page | (integer, optional) | The number of results you are requesting per page. Default: 15 Max: 80
        if api_response.status_code == 200:
            return api_response.json()
        else:
            raise ApiResponseError(api_response.status_code)

#   Response:
#   - id (string) - The id of the collection you are requesting.
#   - media (array) - An array of media objects. Each object has an extra type attribute to indicate the type of object.
#            | PHOTO |                              | Video |
#       * type (string)                 |       * type (string)
#       * id (intiger)                  |       * id (intiger)
#       * width (intiger)               |       * width (intiger)
#       * height (intiger)              |       * height (intiger)
#       * url (string)                  |       * duration (intiger)
#       * photographer (string)         |       * full_res (string, null)
#       * photographer_url (string)     |       * tags (array)
#       * photographer_id (intiger)     |       * url (string)
#       * avg_color (string)            |       * image (string)
#       * src (array)                   |       * avg_color (string, null)
#           - original (string)         |       * user (array)
#           - large2x (string)          |           - id (intiger)
#           - large (string)            |           - name (string)
#           - medium (string)           |           - url (string)
#           - small (string)            |       * video_files (array)
#           - portrait (string)         |           - id (intiger)
#           - landscape (string)        |           - quality (string)
#           - tiny (string)             |           - file_type (string)
#       * liked (boolean)               |           - width (intiger)
#                                       |           - height (intiger)
#                                       |           - link (string)
#                                       |       * video_pictures (array)
#                                       |           - id (intiger)
#                                       |           - nr (intiger)
#                                       |           - picture (string)
#   - page (integer) - The current page number.
#   - per_page (integer) - The number of results returned with each page.
#   - total_results (integer) - The total number of results for the request.
#   - prev_page (string, optional) - URL for the previous page of results, if applicable.
#   - next_page (string, optional) - URL for the next page of results, if applicable.



#____________________________________________________________________________________________#

#####################
#       Errors      #
#####################

# Api | Key
class ApiKeyError(Exception):
    def __init__(self):
        super().__init__("Missing Api Key, first define Api Key in function 'Api_key_set'")


# Api | Response
class ApiResponseError(Exception):
    # Main #
    def __init__(self, code=int):
        super().__init__(self.code_description(code))
    # Code #
    def code_description(self, code):
        # 2xx Success
        if code == 204:
            return 'The request was processed, but there is no content to return.'

        # 3xx Redirection
        elif code == 301:
            return 'The resource has been permanently moved to a new location.'
        elif code == 302:
            return 'The resource is temporarily located at a different URL.'
        elif code == 304:
            return 'The resource has not been modified since the last request.'
        # 4xx
        elif code == 400:
            return 'The request is poorly formatted or unrecognizable.'
        elif code == 401:
            return 'Authentication is required and has not been provided or is invalid.'
        elif code == 403:
            return 'The server is refusing to allow access to the resource.'
        elif code == 404:
            return 'The server cannot find the requested resource.'
        elif code == 405:
            return 'The method used in the request is not allowed for the resource.'
        elif code == 429:
            return 'The client has sent too many requests in a short time (rate limiting).'
        # 5xx
        elif code == 500:
            return 'A general server error, often due to unhandled conditions.'
        elif code == 501:
            return 'The server does not support the functionality required to fulfill the request.'
        elif code == 502:
            return 'The server acting as a gateway or proxy received an invalid response from the upstream server.'
        elif code == 503:
            return 'The server is temporarily unavailable (e.g., due to overload or maintenance).'
        elif code == 504:
            return 'The gateway or proxy server did not receive a timely response from the upstream server.'

# Api | Data Insert
class ApiDataTypeError(Exception):
    # Main
    def __init__(self, param, object_type_correct,  object_type_error):
        self.message = f'Data of \'{param}\' must be {object_type_correct}, no {type(object_type_error)}'
        super().__init__(self, self.message)

# Api | Data Insert
class ApiDataInsertError(Exception):
    # Main
    def __init__(self, code):
        super().__init__(self.controller(code))

    def controller(self, code):
        if code == 'query':
            return 'Query parameter is required'
        elif code == 'orientation':
            return 'The Orientation parameter takes the values: \'landscape\', \'portrait\', \'square\'.'
        elif code == 'size':
            return 'The Size parameter takes the values: \'small\', \'medium\', \'large\'.'
        elif code == 'color':
            return 'The Color parameter takes the values: \'red\', \'orange\', \'yellow\', \'green\', \'turquoise\', \'blue\', \'violet\', \'pink\', \'brown\', \'black\', \'gray\', \'white\' or any hexidecimal color code (e.g. #ffffff).'
        elif code == 'locale':
            return '''The Locale parameter takes the values: \'en-US\' \'pt-BR\' \'es-ES\' \'ca-ES\' \'de-DE\' \'it-IT\' \'fr-FR\' \'sv-SE\' \'id-ID\' \'pl-PL\' \'ja-JP\' \'zh-TW\' \'zh-CN\' \'ko-KR\'
                      \'th-TH\' \'nl-NL\' \'hu-HU\' \'vi-VN\' \'cs-CZ\' \'da-DK\' \'fi-FI\' \'uk-UA\' \'el-GR\' \'ro-RO\' \'nb-NO\' \'sk-SK\' \'tr-TR\' \'ru-RU\'.'''
        elif code == 'per_page':
            return 'The Per Page parameter takes max value 80'
        elif code == 'type_media':
            return '''The Type Media takes the values: \'photos\', \'videos\'.'''
        elif code == 'sort':
            return '''The Sort takes the values: \'asc\', \'desc\'.'''


def color_hex(color):
    if color.startswith("#") and len(color) in (4, 7):
        hex_digits = "0123456789abcdefABCDEF"
        # Sprawdzamy, czy każdy znak po '#' jest cyfrą szesnastkową
        for char in color[1:]:
            if char not in hex_digits:
                return False
        return True
    return False