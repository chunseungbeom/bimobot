class Keyboard:
    buttons = [  # 메세지 선언 시 기본 값, 사용되지 않아야 함
        "foo",
    ]
    homeButtons = [  # 채팅방 입장 시 메인 버튼
        "오늘의 식단",
        "내일의 식단",
        # "이번주 식단",
        "식단 평가하기",
    ]
    todayButtons = [  # 오늘의 식단 선택
        "전체 식단 보기",
        "오늘의 점심",
        "오늘의 저녁",
        "학생식당",
        "기숙사식당",
        "교직원식당(생활관)",
        "교직원식당(종합관)",
        "취소",
    ]
    # TODO today와 tomorrow버튼 스트링 공유
    tomorrowButtons = [  # 내일의 식단 선택
        "전체 식단 보기",
        "오늘의 점심",
        "오늘의 저녁",
        "학생식당",
        "기숙사식당",
        "교직원식당(생활관)",
        "교직원식당(종합관)",
        "취소",
    ]
    placeButtons = [  # 식단 평가하기 장소 버튼
        "전체 식단 보기",
        "오늘의 점심",
        "오늘의 저녁",
        "학생식당",
        "기숙사식당",
        "교직원식당(생활관)",
        "교직원식당(종합관)",
        "취소",
    ]
    timeButtons = [  # 식단 평가하기 시간대 버튼
        "아침",
        "점심",
        "저녁",
        "취소",
    ]
    scoreButtons = [  # 식단 평가하기 점수 버튼
        "5",
        "4",
        "3",
        "2",
        "1",
        "취소",
    ]