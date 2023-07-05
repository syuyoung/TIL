## Animation

요소에 애니메이션을 설정/제어

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| animation-name | @keyframes규칙의 이름을 지정 | none |
| animation-duration | 애니메이션의 지속 시간 설정 | 0s |
| animation-timing-function | 타이밍 함수 지정([타이밍 함수란?](http://easings.net/ko)) | ease |
| animation-delay | 애니메이션의 대기 시간 설정 | 0s |
| animation-iteration-count | 애니메이션의 반복 횟수 설정 | 1 |
| animation-direction | 애니메이션의 반복 방향 설정 | normal |
| animation-fill-mode | 애니메이션의 전후 상태(위치) 설정 | none |
| animation-play-state | 애니메이션의 재생과 정지 설정 | running |

### animation-name

@keyframes규칙(애니메이션 프레임)의 이름을 지정

  

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| none | 애니메이션을 지정하지 않음 | none |
| @keyframes이름 | 이름이 일치하는 @keyframes규칙의 애니메이션을 적용 |   |

### animation-duration

애니메이션의 **지속** 시간 설정

  

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| 시간 | 지속 시간을 설정 | 0s |

### animation-timing-function

타이밍 함수(애니메이션 효과를 계산하는 방법) 지정

  

| 값 | 의미 | 기본값 | Cubic Bezier 값 |
| --- | --- | --- | --- |
| ease | 빠르게 - 느리게 | ease | cubic-bezier(.25, .1, .25, 1) |
| linear | 일정하게 |   | cubic-bezier(0, 0, 1, 1) |
| ease-in | 느리게 - 빠르게 |   | cubic-bezier(.42, 0, 1, 1) |
| ease-out | 빠르게 - 느리게 |   | cubic-bezier(0, 0, .58, 1) |
| ease-in-out | 느리게 - 빠르게 - 느리게 |   | cubic-bezier(.42, 0, .58, 1) |
| cubic-bezier(n,n,n,n) | 자신만의 값을 정의(0~1) |   |   |
| steps(n) | n번 분할된 애니메이션 |   |   |

### animation-delay

애니메이션의 **대기** 시간 설정(음수 허용)

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| 시간 | 대기 시간을 설정 | 0s |

### animation-iteration-count

애니메이션의 반복 횟수를 설정

|   | 의미 | 기본값 |
| --- | --- | --- |
| 숫자 | 반복 횟수를 설정 | 1 |
| infinite | 무한 반복 |   |

### animation-direction

애니메이션의 반복 방향을 설정

  

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| normal | 정방향만 반복 | normal |
| reverse | 역방향만 반복 |   |
| alternate | 정방향에서 역방향으로 반복(왕복) |   |
| alternate-reverse | 역방향에서 정방향으로 반복(왕복) |   |

### animation-fill-mode

애니메이션의 전후 상태(위치)를 설정

  

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| none | 기존 위치에서 시작 -> 애니메이션 시작 위치로 이동 -> 동작 -> 기존 위치에서 끝 | none |
| forwards | 기존 위치에서 시작 -> 애니메이션 시작 위치로 이동 -> 동작 -> 애니메이션 끝 위치에서 끝 |   |
| backwards | 애니메이션 시작 위치에서 시작 -> 동작 -> 기존 위치에서 끝 |   |
| both | 애니메이션 시작 위치에서 시작 -> 동작 -> 애니메이션 끝 위치에서 끝 |   |

### animation-play-state

애니메이션의 재생과 정지를 설정

  

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| running | 애니메이션을 동작 | running |
| paused | 애니메이션 동작을 정지 |   |