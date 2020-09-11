# :bulb: Algorithm - Python

### Algorithms implemented in Python - 파이썬으로 구현된 알고리즘    

``` python
is_learned = False
if not is_learned:
  print(do study please!)
```   

These implementations are for learning purposes. They may not be the best efficient.   
- 공부한 내용을 기반으로 직접 구현을 하였기 때문에 효율성이 좋지 않을수도 있습니다.   

## :penguin: Tip   
- #### 알고리즘 문제 풀 때 `약 1억번 연산 = 1초` 정도로 가정하고 자신이 생각한 방법의 시간복잡도를 계산해보고 문제 풀이 해야합니다.   
  - 시간복잡도가 `nlog(n)`일 경우 `n<=5,000,000` 이여야만 `500,000,000log(500,000,000) = 33,494,850`으로 1초 수행 가능      
  - 시간복잡도가 `n^2`일 경우 `n<=10,000` 이여야만 `10,000^2 = 100,000,000`으로 1초 수행 가능      
  - 시간복잡도가 `n^3`일 경우 `n<=500` 이여야만 `500^3 = 125,000,000`으로 1초 수행 가능      
  - 시간복잡도가 `2^n`일 경우 `n<=20` 이여야만 `2^20 = 1,048,576`으로 1초 수행 가능      
  - 시간복잡도가 `n!`일 경우 `n<=10` 이여야만 `10! = 3,628,800`으로 1초 수행 가능    
  
- #### 자신의 답이 틀렸을 경우    
  __1. 가장 작거나 큰 데이터(테스트 케이스)를 넣어 확인해봅니다.__   
  __2. 코드를 하나 더 작성하여 두 개의 코드를 비교해봅니다.__   
  __3. 테스트 케이스 방식 순서를 바꿔 실행해 봅니다.__   
    - ex) 3,4,10 => 10,4,3 
    - __Test case는 일반적으로 크기가 증가하는 순으로 주어지는데 이러한 초기화가 제대로 안되어 있을 경우가 있습니다.__    
   
- #### 자주 발생하는 구현의 문제로 시간초과가 날 경우   
  - __브루트 포스일 경우__   
    ```python
    if (ans < go(index+1):
      ans = go(index+1)
      
    #go()함수가 계속해서 호출되기 때문에 위의 코드를 밑의 코드로 수정
    
    temp = go(index+1)
    if (ans < temp:
      ans = temp
    ```
    
- #### 자주 발생하는 런타임 에러   
  ```java
  d = new int[n]
  d[0] = 0
  d[1] = 1  # n = 1일 경우 runtime error
  d[2] = 2  # n = 1~2일 경우 runtime error 
  for(i = 3; i < n; i++;){ # n = 1~3일 경우 index가 i=3부터 존재하지 않기 때문에 java에서는 runtime error 발생, but Python에서는 그냥 무시함
    ....
  }
  ```
  
- #### 정답을 특정값으로 나눈 나머지를 구하라고 할 경우(%)    
  - 답을 구하는 단계마다 `해당 단계 답 % mod` 그리고 `최종 답 % mod` 해줘야 합니다.   
  - 이렇게 하는 이유는 int, long, long long 등 자료형의 범위를 넘어가기 때문입니다.   
  
- #### 불가능하면 -1 출력해야 하는 경우   
  - -1 출력 시 절대로 프로그램을 종료시키게 코딩하면 안됩니다.   
  - ex) Test case 3개 입력 시 3개에 대한 정답이 나와야 하지만 종료하게 만들었을 경우 중간에 바로 종료될 수 있습니다.   

  
- #### DFS로 풀 수 있는 문제는 BFS로도 풀 수 있습니다. BFS는 주로 `가중치가 1`인 그래프의 최단 경로를 구할 때 사용합니다.    
- #### 문자열 알고리즘   
  - __KMP : 문자열 S에서 패턴 P를 찾습니다.__   
  - __Trie : 문자열 N개 중에서 문자열 S를 찾습니다.__   
    - ex) 특정 문자열 검색, 성+이름 검색 등    하지만 공간적인 이유에서 잘 사용하지는 않습니다. 이유는 여기서 확인해보세요. [https://github.com/seongbeenkim/CS-Interview/tree/master/Algorithm#trie]
  - __Aho-Corasik : 문자열 N개 중에서 패턴 P를 찾습니다. = KMP + Trie__    
    - ex) 이름만 같은 사람 검색    


## :punch: Coding challenge websites
* Baekjoon Online Judge   
<https://www.acmicpc.net/>


