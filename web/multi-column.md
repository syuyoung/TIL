## Multi-Column

일반 블록 레이아웃을 확장하여 여러 텍스트 다단으로 쉽게 정리하며, 가독성 확보

### columns

다단을 정의

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| auto | 브라우저가 단의 너비와 개수를 설정 | auto |
| column-width | 단의 최적 너비를 설정 | auto |
| column-count | 단의 개수를 설정 | auto |

### column-width

단의 최적 너비를 설정

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| auto | 브라우저가 단의 너비를 설정 | auto |
| 단위 | px, em, cm 등 단위로 지정 |   |

### column-count

단의 개수를 설정

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| auto | 브라우저가 단의 개수를 설정 | auto |
| 숫자 | 단의 개수를 설정 |   |

### column-gap

단과 단 사이의 간격 설정

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| normal | 브라우저가 단과 단 사이의 간격을 설정(1em) | normal |
| 단위 | px, em, cm 등 단위로 지정 |   |

### column-rule

단과 단 사이의 (구분)선을 지정

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| column-width | 선의 두께를 지정 | medium |
| column-style | 선의 종류를 지정 | none |
| column-color | 선의 색상을 지정 | 요소의 글자색과 동일 |

### column-rule-width

단과 단 사이 선의 두께 설정

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| medium | 중간 두께 선 | medium |
| thin | 얇은 두께 선 |   |
| thick | 두꺼운 두께 선 |   |
| 단위 | px, em, cm 등 단위로 지정 |   |

### column-rule-style

단과 단 사이 선의 종류 설정

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| none | 선 없음 | none |
| hidden | 선 없음과 동일(table요소에서 사용) |   |
| solid | 실선(일반선) |   |
| dotted | 점선 |   |
| dashed | 파선 |   |
| double | 두 줄선 |   |
| groove | 홈이 파여있는 모양(선) |   |
| ridge | 솟은 모양(선, groove의 반대) |   |
| inset | 요소 전체가 들어간 모양(선) |   |
| outset | 요소 전체가 나온 모양(선) |   |

### column-rule-color

단과 단 사이 선의 색상 설정

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| 색상 | 선의 색상을 지정 | 요소의 글자색과 동일 |