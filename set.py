# set (집합)
# 중복이 안되고, 순서가 없음

my_set = {1,2,3,3,4}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java도 할 수 있거나 python도 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있지만, python은 못하는 개발자)
print(java - python)
print(java.difference(python))

# python 을 할 줄 아는 사람이 늘어났을 때
python.add("김태호")
print(python)

# java를 잊었어요
java.remove("김태호")
print(java)

