# HTML 테이블

## table, tr, th, td
데이터 표(table)의 행(줄 / tr)과 열(칸, 셀(Cell) / th, td)을 생성.  
(Table Row, Table Header, Table Data)

## th

‘머리글 칸’을 지정

| 속성 | 의미 | 값 | 기본값 |
| --- | --- | --- | --- |
| abbr | 열에 대한 간단한 설명 |   |   |
| headers | 관련된 하나 이상의 다른 머리글 칸 id 속성 값 |   |   |
| colspan | 확장하려는(병합) 열의 수 |   | 1 |
| rowspan | 확장하려는(병합) 행의 수 |   | 1 |
| scope | 자신이 누구의 ‘머리글 칸’인지 명시 | col: 자신의 열   colgroup: 모든 열   row: 자신의 행   rowgroup: 모든 행   auto | auto |

## td

| 속성 | 의미 | 값 | 기본값 |
| --- | --- | --- | --- |
| headers | 관련된 하나 이상의 다른 머리글 칸 id 속성 값 |   |   |
| colspan | 확장하려는(병합) 열의 수 |   | 1 |
| rowspan | 확장하려는(병합) 행의 수 |   | 1 |

## caption

표의 제목을 설정.

-   열리는 TABLE 태그 바로 다음에 작성해야 함.
-   table 당 하나의 caption만 사용 가능.

## colgroup, col

표의 열들을 공통적으로 정의하는 컬럼(col)과 그의 집합(colgroup).  
(Column, Column Group)

| 속성 | 의미 | 값 | 기본값 |
| --- | --- | --- | --- |
| span | 연속되는 열 수 | 숫자(Number) | 1 |

## thead, tbody, tfoot

표의 머리글(thead), 본문(tbody), 바닥글(tfoot)을 지정.

-   기본적으로 테이블의 레이아웃에 영향을 주지 않음.