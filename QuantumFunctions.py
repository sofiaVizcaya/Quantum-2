import math
import numpy as np
from numpy.linalg import eig
x = np.array([-3-1j,2j,1j,2])
y = np.array([5+10j,22-3j,5+1j,0])

def Probability_at_State(Array,Location):
    np.array(Array)
    denominator = np.linalg.norm(Array)**2
    Y = (np.linalg.norm(Array[Location])**2)/denominator
    return(str(float(Y*100))+"%")
def amplitud_vector(Array, Array_1):
    np.array(Array),np.array(Array_1)
    denominator = np.linalg.norm(Array)
    denominator_1 = np.linalg.norm(Array_1)
    Array = Array /denominator
    Array_div = Array_1 / denominator_1
    Array_div_conjugate = []
    for i in Array_div:
        b = np.conjugate(i)
        Array_div_conjugate.append(b)
    result = np.inner(Array, Array_div_conjugate)
    return result

def Probability_one_state_to_other(Array, Array_1):
    np.array(Array),np.array(Array_1)
    Probability_Array, Probability_Array_1 = [],[]
    for i in Array:
        Y = (np.linalg.norm(i)/np.linalg.norm(Array))**2
        Probability_Array.append(Y)
    for j in Array_1:
        Y = (np.linalg.norm(j)/np.linalg.norm(Array_1))**2
        Probability_Array_1.append(Y)
    tensor_dot = []
    pointer =[]
    count = 0
    for i in Probability_Array:
        count_1 = 0
        for j in Probability_Array_1:
            tensor_dot.append(i*j)
            pointer.append(str(count)+" "+str(count_1))
            count_1 = count_1 + 1
            print("The probability of moving from " +str(count)+" to "+str(count_1)+" is: "+str(i*j*100)+"%")
        count = + 1
    return
def Hermitian_mat(Array):
    M = np.transpose(Array)
    A = []
    for i in M:
        A.append(np.conjugate(i))
    if (np.array(A)).all() == (np.array(Array)).all():
        return True
    else:
        return False
def MeanandVariance(Array, Array_1):
    if Hermitian_mat(Array):
        pre_Media = np.multiply(Array_1,Array_1)
        Media = np.multiply(Array,pre_Media)
        print(Media)
        Array_2 = (Array - (Media @(np.eye(len(Array)))))**2
        return ("The variace is : " + str(Array_2 * Array_1))
    else:
        return "The matrix is nor hermitian. It is not posible to return it's variance"


def EigenValuesProbability(Array, Array_1):
    print(np.linalg.eig(Array))
    Probability_one_state_to_other(Array, Array_1)
    return
def FinalState(Unitary,t):
    #assuming that the matrix is unitary and there is no obserbable we can use this function
    if len(Unitary) == t:
        Final_State = []
        time = 0
        for i in Unitary:
            result = i * time
            Final_State.append(result)
            time = time + 0
        r = 1
        for i in Final_State:
            r = r * i
        return r
    else:
        return("Check that your using the right amount of time or that your using the right amount of variables on the Un")

         

