import threading
import requests

# 스크래핑할 웹사이트 URL 리스트
urls = [
    'https://www.google.com',
    'https://www.example.com',
    'https://www.python.org',
    # 여기에 더 많은 URL을 추가할 수 있습니다.
]

# URL에서 데이터를 가져오는 함수
def fetch_url(url):
    response = requests.get(url)
    print(f'{url}: {response.status_code}')

# 스레드를 생성하고 시작하는 함수
def main():
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()

    # 모든 스레드가 종료될 때까지 기다립니다.
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()