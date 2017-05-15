import math

l = [1,2,4,7,12,36,22,59,70]

def binary_search(list,element_toSearch):
    l_index = 0
    r_index = len(l)-1
    found = False

    while (l_index <= r_index and found == False):
        m_index = math.floor((l_index + r_index)/2)
        if (l[m_index] == element_toSearch):
            found = True
        elif (l[m_index] < element_toSearch):
            r_index = m_index + 1
        elif (l[m_index] > element_toSearch):
            l_index = m_index -1
        return found

print (binary_search(l,0))
