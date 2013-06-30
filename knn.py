import heapq
k = 10

import math

# calculate the distance between v1 and v2
def euclidean(v1, v2):
  # v1 is the shorter one.
  d = 0.0
  for i in range(len(v1)):
    d += (v1[i] - v2[i]) ** 2
  return math.sqrt(d)


def classify(v_list, v, k):
  # classify vector 'v' from known vector list 'v_list'
  result = [] # heap!
  heapq.heapify(result)
  for vector in v_list:
    d = euclidean(v, vector)
    if len(result) < k:
      heapq.heappush(result, (d, vector))
    else:
      heapq.heapreplace(result, (d, vector))
  dic = {}
  for (d, vector) in result:
    if dic.has_key(vector[-1]):
      dic[vector[-1]]  += 1
    else:
      dic[vector[-1]] = 1
  # get the most neighbors's class
  tmp_list = [(dic[k], k) for k in dic.keys()]
  tmp_list.sort()
  the_voted_class = tmp_list[-1][1]
  v[-1] = the_voted_class
  return v

def knn(train_list, test_list):
  global k
  # given 2 vector list(the training set and the test data), do the clustering using 'K-NN' algorithm
  for vector in test_list:
    classify(train_list, vector, k)

  return test_list

def file2list(f, column_number):
  L = []
  lines = f.readlines()
  for line in lines:
    # split the line into parts.
    words = line.strip().split('\t')
    l = []
    for word in words[:-1]:
      if word:
        l.append(float(word))
    l.append(int(words[-1]))
    L.append(l)
  return L

def list2file(L, file_name):
  f = open(file_name, 'wb')
  for l in L:
    for item in l:
      f.write( str(item) + '\t' )
    f.write('\n')
  f.close()
  return f

def run(train_data_file_name, test_data_file_name):
  train_file = open(train_data_file_name)
  test_file = open(test_data_file_name)
  train_list = file2list(train_file, 3)
  test_list = file2list(test_file, 3)
  print test_list[0]
  result = knn(train_list, test_list)
  print result[0]
  list2file(result, 'result.txt')

if __name__ == '__main__':
  run('datingTrainingSet.txt', 'datingTestSet.txt')
