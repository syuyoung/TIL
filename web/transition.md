# **transition**

CSS 속성의 시작과 끝을 지정(전환 효과)하여 중간 값에 애니메이션 효과를 줌

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| transition-property | 전환 효과를 사용할 속성 이름 | all |
| transition-duration | 전환 효과의 지속시간 설정 | 0s |
| transition-timing-function | 타이밍 함수 지정([타이밍 함수란?](http://easings.net/ko)) | ease |
| transition-delay | 전환 효과의 대기시간 설정 | 0s |

```
transition: 속성이름 지속시간 [타이밍함수 대기시간];
```
# **transition-timing-function**

타이밍 함수(애니메이션 전환 효과를 계산하는 방법) 지정

| 값 | 의미 | 기본값 | Cubic Bezier 값 |
| --- | --- | --- | --- |
|   |   |   |   |
| ease | 빠르게 - 느리게 | ease | cubic-bezier(.25, .1, .25, 1) |
| linear | 일정하게 |   | cubic-bezier(0, 0, 1, 1) |
| ease-in | 느리게 - 빠르게 |   | cubic-bezier(.42, 0, 1, 1) |
| ease-out | 빠르게 - 느리게 |   | cubic-bezier(0, 0, .58, 1) |
| ease-in-out | 느리게 - 빠르게 - 느리게 |   | cubic-bezier(.42, 0, .58, 1) |
| cubic-bezier(n,n,n,n) | 자신만의 값을 정의(0~1) |   |   |
| steps(n) | n번 분할된 애니메이션 |   |   |