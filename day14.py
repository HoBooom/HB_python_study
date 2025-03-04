import os

people = [
    {
        "name": "홍길동",
        "follower": 3500,
        "job": "개발자",
        "national": "한국"
    },
    {
        "name": "이영희",
        "follower": 12000,
        "job": "디자이너",
        "national": "한국"
    },
    {
        "name": "김철수",
        "follower": 870,
        "job": "마케터",
        "national": "한국"
    },
    {
        "name": "안나",
        "follower": 15300,
        "job": "유튜버",
        "national": "미국"
    },
    {
        "name": "존 스미스",
        "follower": 4200,
        "job": "교수",
        "national": "영국"
    },
    {
        "name": "마리아",
        "follower": 21000,
        "job": "가수",
        "national": "스페인"
    },
    {
        "name": "사쿠라",
        "follower": 580,
        "job": "작가",
        "national": "일본"
    },
    {
        "name": "왕밍",
        "follower": 9300,
        "job": "모델",
        "national": "중국"
    },
    {
        "name": "조슈아",
        "follower": 740,
        "job": "개발자",
        "national": "미국"
    },
    {
        "name": "박민수",
        "follower": 4100,
        "job": "기자",
        "national": "한국"
    },
    {
        "name": "이루다",
        "follower": 15000,
        "job": "의사",
        "national": "한국"
    },
    {
        "name": "데이비드",
        "follower": 19000,
        "job": "마케터",
        "national": "캐나다"
    },
    {
        "name": "알렉스",
        "follower": 2200,
        "job": "연구원",
        "national": "호주"
    },
    {
        "name": "조르지오",
        "follower": 500,
        "job": "건축가",
        "national": "이탈리아"
    },
    {
        "name": "줄리아",
        "follower": 7600,
        "job": "유튜버",
        "national": "프랑스"
    },
    {
        "name": "황준호",
        "follower": 13000,
        "job": "가수",
        "national": "한국"
    },
    {
        "name": "장예린",
        "follower": 990,
        "job": "디자이너",
        "national": "한국"
    },
    {
        "name": "오세훈",
        "follower": 300,
        "job": "개발자",
        "national": "한국"
    },
    {
        "name": "케이트",
        "follower": 20000,
        "job": "배우",
        "national": "미국"
    },
    {
        "name": "페드로",
        "follower": 1700,
        "job": "교수",
        "national": "멕시코"
    },
    {
        "name": "김소라",
        "follower": 4600,
        "job": "작가",
        "national": "한국"
    },
    {
        "name": "리사",
        "follower": 7800,
        "job": "기자",
        "national": "태국"
    }
]

point = 0

idx_A = 0
idx_B = 1

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    a_follower = people[idx_A]['follower']
    b_follower = people[idx_B]['follower']
    print(f"Your current point : {point}")
    print(f"compare A : {people[idx_A]['name']}, job : {people[idx_A]['job']}, national : {people[idx_A]['national']}")
    print("vs")
    print(f"compare B : {people[idx_B]['name']}, job : {people[idx_B]['job']}, national : {people[idx_B]['national']}")
    choice = input("who has more follower? Type 'A' or 'B': ")
    if choice == 'A' and a_follower > b_follower:
        point += 1
        idx_B += 1
    elif choice == 'B' and b_follower > a_follower:
        point += 1
        idx_A = idx_B
        idx_B += 1
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Your Wrong! final point : {point}")
        break




