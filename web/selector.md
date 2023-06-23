### **<기본 선택자 (Basic Selectors)>**

#### **<전체 선택자 (Universal Selector)>**

 (요소 내부의) 모든 요소를 선택

 \*

```
* {
  color: red;
}
```

#### **<태그 선택자 (Type Selector)>**

 태그 이름이 E인 요소 선택

 E

```
E {
  color: red;
}
```

#### **<클래스 선택자 (Class Selector)>**

 HTML Class 속성 값이 E인 요소 선택

 .E

```
.E {
  color: red;
}
```

#### **<아이디 선택자 (Id Selector)>**

 HTML Id속성 값이 E인 요소 선택

 #E

```
#E {
  color: red;
}
```

### **<복합 선택자 (Combinators)>**

#### **<일치 선택자 (Basic Combinator)>**

 E, F를 **동시에** 만족하는 요소 선택

 EF

```
span.orange {
  color: red;
}
```

```
<div>
  <ul>
    <li>사과</li>
    <li>딸기</li>
    <li class="orange">오렌지</li>
  </ul>
  <div>당근</div>
  <p>토마토</p>
  <span class="orange">오렌지</span>  <!--선택-->
</div>
```

#### **<자식 선택자 (Child Combinator)>**

 E의 자식 요소 F를 선택

 E > F

```
ul > .orange {
  color: red;
}
```

```
<div>
  <ul>
    <li>사과</li>
    <li>딸기</li>
    <li class="orange">오렌지</li>  <!--선택-->
  </ul>
  <div>당근</div>
  <p>토마토</p>
  <span class="orange">오렌지</span>
</div>
```

#### **<후손(하위) 선택자 (Descendant Combinator)>**

 E의 후손(하위) 요소 F를 선택

 E F

```
div .orange {
  color: red;
}
```

```
<div>
  <ul>
    <li>사과</li>
    <li>딸기</li>
    <li class="orange">오렌지</li>  <!--선택-->
  </ul>
  <div>당근</div>
  <p>토마토</p>
  <span class="orange">오렌지</span>  <!--선택-->
</div>
```

#### **<인접 형제 선택자 (Adjacent Sibling Selector Combinator)>**

E의 다음 형제 요소 F 하나만 선택

E + F

```
.orange + li {
  color: red;
}
```

```
<ul>
  <li>딸기</li>
  <li>수박</li>
  <li class="orange">오렌지</li>
  <li>망고</li>  <!--선택-->
  <li>사과</li>
</ul>
```

#### **<일반 형제 선택자 (General Sibling Selector Combinator)>**

E의 다음 형제 요소 F 모두 선택

E ~ F

```
.orange ~ li {
  color: red;
}
```

```
<ul>
  <li>딸기</li>
  <li>수박</li>
  <li class="orange">오렌지</li>
  <li>망고</li>  <!--선택-->
  <li>사과</li>  <!--선택-->
</ul>
```

### **<가상 클래스 선택자 (Pseudo-Classes Selectors)>**

#### **<hover>**

E에 마우스(포인터)가 올라가있는 동안에만 E 선택

E:hover

#### **<active>**

E를 마우스로 클릭하는 동안에만 E 선택

E:active

#### **<focus>**

E가 포커스된 동안에만 E 선택, 대화형 콘텐츠에서 사용 가능

E:focus

#### **<first-child>**

E가 형제 요소 중 첫번째 요소라면 선택

E:first-child

#### **<last-child>**

E가 형제 요소 중 마지막 요소라면 선택

E:last-child

#### **<nth-child>**

E가 형제 요소 중 n번째 요소라면 선택 (n 키워드 사용시 0부터 해석 (Zero-base))

E:nth-child(n)

#### **<nth-of-type>**

E의 타입(태그이름)과 동일한 타입인 형제 요소 중 E가 n번째 요소라면 선택 (n 키워드 사용시 0부터 해석 (Zero-base))

E:nth-of-type(n)

#### **<부정 선택자>**

선택자 S가 아닌 조건 E 선택

E:not(S)

### **<가상 요소 선택자 (Pseudo-Elements Selectors)>**

#### **<before>**

 E 요소 내부의 앞에, 내용(content)을 삽입

content  속성 필수

E::before

#### **<after>**

E 요소 내부의 뒤에, 내용(content)을 삽입

content  속성 필수

E::after

### **<속성 선택자 (Attribute Selectors)>**

#### **<attr>**

속성 attr을 포함한 요소 선택

```
[disabled] {
  opacity: 0.2;
}
```

```
<input type="text" value="HEROPY">
<input type="password" value="1234">
<input type="text" value="disabled text" di
```

#### **<attr=value>**

속성 attr을 포함하며 속성 값이 value인 요소 선택

```
[disabled] {
  opacity: 0.2;
}
```

```
<input type="text" value="HEROPY">
<input type="password" value="1234">
<input type="text" value="disabled text" di
```

#### **<attr^=value>**

속성 attr을 포함하며 속성 값이 value로 시작하는 요소 선택

```
[class^="btn-"] {
  font-weight: bold;
  border-radius: 4px;
}
```

```
<button class="btn-success">Success</button>
<button class="btn-danger">Danger</button>
<button>Normal</button>
```

#### **<attr$=value>**

속성 attr을 포함하며 속성 값이 value로 끝나는 요소 선택

```
[class^="btn-"] {
  font-weight: bold;
  border-radius: 4px;
}
[class$="success"] {
  color: green;
}
[class$="danger"] {
  color: red;
}
```

```
<button class="btn-success">Success</button>
<button class="btn-danger">Danger</button>
<button>Normal</b
```