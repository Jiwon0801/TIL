# set 함수: 중복 없음, unordered
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
# print(s1)
#
# s2 = set('hello')
# print(s2)
#
# s3 = set()
# print(s3)
#
# s4 = {}
# print(type(s4))

# 교집합
print(s1 & s2)
print(s1.intersection(s2))

#합집합
print(s1 | s2)
print(s1.union(s2))

#차집합
print(s1 - s2)
print(s1.difference(s2))
print(s2.difference(s1))
