# breast-cancer-risk-factors

## 1. Introduction

개인의 특성을 이용해 breast cancer의 risk를 확인하는 알고리즘입니다.

## 2. Data

데이터의 출처는 다음과 같습니다.

https://www.bcsc-research.org/data/rf

## 3. BluePrint

flask_app<br>
&nbsp;&nbsp;├ __init__.py<br>
&nbsp;&nbsp;└ templates<br>
&nbsp;&nbsp;&nbsp;&nbsp;├ index.html<br>
&nbsp;&nbsp;&nbsp;&nbsp;├ input.html<br>
&nbsp;&nbsp;&nbsp;&nbsp;└ output.html<br>
dataset<br>
&nbsp;&nbsp;├ data.csv<br>
&nbsp;&nbsp;├ test.csv<br>
&nbsp;&nbsp;├ train.csv<br>
&nbsp;&nbsp;├ validation.csv<br>
&nbsp;&nbsp;└ data.db<br>

heroku를 통해 flask_app을 실행시키면 작동되도록 설계하였습니다.

## 4. Hypothesis
분석하기 전 저는 두 가지 가설을 세우고 학습을 진행하였습니다. 나이가 많을수록 breast cancer에 걸릴 가능성이 높다, 살이 찔수록 breast cancer에 걸릴 가능성이 높다입니다.

## 5. Conclusions
- 나이는 breast cancer에 영향을 미칩니다. 다만 50~60대에서 가장 높습니다.
- 비만율은 breast cancer에 어느정도 영향을 미칩니다. 다만 두드러지는 결과는 보지 못하였습니다.
- 이외에도 가족력, 이전에 breast 관련 질환을 앓았는지 여부, 인종 등이 breast cancer에 큰 영향을 미쳤습니다.
