# 함수 mapping 
import seaborn as sns
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
df['ten'] = 10

# 특정 행과 열을 선택하기 위한 인덱싱 방법. :은 모든행, 다음은 [ ]안의 해당 컬럼만 가져온다.

# 함수 2개 정의하여 모든 시리즈의 모든원소에 적용

def Multiplication_10(n): # 10을 곱해주는 함수
    return n * 10

def add_two_obj(a,b): # a, b를 더해주는 함수
    return a + b

# 시리즈 2개를 만들어, apply()함수를 통해 각각 적용시키기
sr1 = df['age'].apply(Multiplication_10) # age의 모든원소레 10을 곱함
print(sr1.head())
print('\n')

sr2 = df['fare'].apply(add_two_obj,b=100) # a는 fare의 모든원소, b는 100
print(sr2.head())
print('\n')

# applymap은 데이터프레임 전체요소에 적용
df_map = df.applymap(add_two_obj, b = 100)
print(df_map.head())
print('\n')

# axis=1은 df의 열, axis=0은 df의 행에 함수를 적용시킨다.
def isnull_value(series): # 결측값 확인하는 함수
    return series.isnull()

result = df.apply(isnull_value, axis=1)
print(result.head())
print('\n')
print(type(result))


# 응용하기
def max_min(n):  # 최대값에서 최소값 빼는 함수
    return n.max() - n.min()

df5 = df.head()
result0 = df5.apply(max_min, axis=0) # 위 아래 : 각 행들의 연산, 열에 대한 결과
result1 = df5.apply(max_min, axis=1) # 양 옆 : 각 열들의 연산, 행에 대한 결과
print("원본\n", df5.head())
print()
print("axis=0\n", result0.head())
print()
print("axis=1\n", result1.head())
