# transform

요소의 변환 효과(변형)를 지정

## transform 2D 변환 함수

| 값(변환함수) | 의미 | 단위 |
| --- | --- | --- |
| translate(x, y) | 이동(X축, Y축) | 단위 |
| translateX(x) | 이동(X축) | 단위 |
| translateY(y) | 이동(Y축) | 단위 |
| scale(x, y) | 크기(X축, Y축) | 없음(배수) |
| scaleX(x) | 크기(X축) | 없음(배수) |
| scaleY(y) | 크기(Y축) | 없음(배수) |
| rotate(degree) | 회전(각도) | deg |
| skew(x-deg, y-deg) | 기울임(X축, Y축) | deg |
| skewX(x-deg) | 기울임(X축) | deg |
| skewY(y-deg) | 기울임(Y축) | deg |
| matrix(n,n,n,n,n,n) | 2차원 변환 효과 | 없음 |

## transform 3D 변환 함수

| 값(변환함수) | 의미 | 단위 |
| --- | --- | --- |
| translate3d(x, y, z) | 이동(X축, Y축, Z축) | 단위 |
| translateZ(z) | 이동(Z축) | 단위 |
| scale3d(x, y, z) | 크기(X축, Y축, Z축) | 없음(배수) |
| scaleZ(z) | 크기(Z축) | 없음(배수) |
| rotate3d(x, y, z, a) | 회전(X벡터, Y벡터, Z벡터, 각도) | 없음, deg |
| rotateX(x) | 회전(X축) | deg |
| rotateY(y) | 회전(Y축) | deg |
| rotateZ(z) | 회전(Z축) | deg |
| perspective(n) | 원근법(거리) | 단위 |
| matrix3d(n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n) | 3차원 변환 효과 | 없음 |

## matrix(a,b,c,d,e,f)

요소의 2차원 변환(Transforms) 효과를 지정  
scale(), skew(), translate() 그리고 rotate()를 지정

## transform 변환 속성

| 속성 | 의미 |
| --- | --- |
| transform-origin | 요소 변환의 기준점을 설정 |
| transform-style | 3D 변환 요소의 자식 요소도 3D 변환을 사용할지 설정 |
| perspective | 하위 요소를 관찰하는 원근 거리를 설정 |
| perspective-origin | 원근 거리의 기준점을 설정 |
| backface-visibility | 3D 변환으로 회전된 요소의 뒷면 숨김을 설정 |

## transform-origin

요소 변환의 기준점을 설정

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| X축 | left, right, center, %, 단위 | 50% |
| Y축 | top, bottom, center, %, 단위 | 50% |
| Z축 | 단위 | 0 |

## transform-style

3D 변환 요소의 자식 요소도 3D 변환을 사용할지 설정

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| flat | 자식 요소의 3D 변환을 사용하지 않음 | flat |
| preserve-3d | 자식 요소의 3D 변환을 사용함 |   |

## perspective

하위 요소를 관찰하는 원근 거리를 설정

| 값 | 의미 |
| --- | --- |
| 단위 | px, em, cm 등 단위로 지정 |

### perspective 속성과 함수의 차이점

| 속성/함수 | 적용대상 | 기준점 설정 |
| --- | --- | --- |
| perspective | 관찰 대상의 부모 요소 | perspective-origin |
| transform: perspective() | 관찰 대상 | transform-origin |

## perspective-origin

원근 거리의 기준점을 설정

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| X축 | left, right, center, %, 단위 | 50% |
| Y축 | top, bottom, center, %, 단위 | 50% |

## backface-visibility

3D 변환으로 회전된 요소의 뒷면 숨김을 설정

| 값 | 의미 | 기본값 |
| --- | --- | --- |
| visible | 뒷면 숨기지 않음 | visible |
| hidden | 뒷면 숨김 |   |