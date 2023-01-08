from asyncio.windows_events import NULL
from contextlib import nullcontext
import requests
import json

TMDB_API_KEY = '38ee27fa3688e2ed93068da12e4c2386'

def get_movie_datas():
    # 최종 dump 데이터
    total_data = []

    # 장르 데이터
    request_url_gerne = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR"
    # 요청한 데이터를 json형태로 변환하여 변수 genres에 저장
    # genres는 dict 형태의 data
    genres = requests.get(request_url_gerne).json()
    for genre in genres['genres']:
        
        fields = {
            'name': genre['name'],
        }

        data = {
            "model": "movies.genre",
            "pk": genre['id'],
            "fields": fields
        }

        total_data.append(data)

    
    # Get Popular : 1페이지 ~ 500페이지(페이지당 20개, 총 10,000개)
    for i in range(1, 501):
        # url 생성
        request_url_popular = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        # 요청한 데이터를 json형태로 변환하여 변수 movies에 저장
        # movies는 딕셔너리 형태의 데이터임
        movies_popular = requests.get(request_url_popular).json()
        # 영화 리스트 데이터는 현재 results가 key인 value에 리스트 형태로 저장되어 있음
        for movie_popular in movies_popular['results']:
            # poster_path와 overview가 없는 값은 가져오지 않음
            if movie_popular.get('overview') != '' and movie_popular.get('poster_path') != None and movie_popular.get('release_date') != None:
            # if movie_popular.get('release_date', ''):
                fields = {
                    'title': movie_popular['title'],
                    'release_date': movie_popular['release_date'],
                    'popularity': movie_popular['popularity'],
                    'overview': movie_popular['overview'],
                    'vote_average': movie_popular['vote_average'],
                    'vote_count' : movie_popular['vote_count'],
                    'poster_path': movie_popular['poster_path'],
                    'video_url': [],
                    'genre_check': movie_popular['genre_ids'],
                    'like_movie_users' : [],
                }

                data = {
                    "model": "movies.movie",
                    "pk": movie_popular['id'],
                    "fields": fields
                }

                total_data.append(data)
    

    # Get Trending : 
    # 인기 영화 데이터 : 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 501):
        # url 생성
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        # 요청한 데이터를 json형태로 변환하여 변수 movies에 저장
        # movies는 딕셔너리 형태의 데이터임
        movies_trending = requests.get(request_url).json()
        # 영화 리스트 데이터는 현재 results가 key인 value에 리스트 형태로 저장되어 있음
        for movie_trending in movies_trending['results']:
            # poster_path와 overview, release_date가 없는 값은 가져오지 않음
            if movie_trending.get('release_date', '') and (movie_trending.get('overview') != '' and movie_trending.get('poster_path') != None and movie_trending.get('release_date') != None):
                fields = {
                    'title': movie_trending['title'],
                    'release_date': movie_trending['release_date'],
                    'popularity': movie_trending['popularity'],
                    'overview': movie_trending['overview'],
                    'vote_average': movie_trending['vote_average'],
                    'vote_count' : movie_trending['vote_count'],
                    'poster_path': movie_trending['poster_path'],
                    'video_url': [],
                    'genre_check': movie_trending['genre_ids'],
                    'like_movie_users' : [],
                }

                data = {
                    "model": "movies.movie",
                    "pk": movie_trending['id'],
                    "fields": fields
                }

                total_data.append(data)
                
    
    # json 파일 생성
    with open("movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=2, ensure_ascii=False)

get_movie_datas()