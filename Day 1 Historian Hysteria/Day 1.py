import time
import bisect


def main():
    array1,array2=get_input()
    start=time.time()
    result=solution(array1,array2)
    print(f"Time Taken: {time.time() - start}")
    print(f"solution: {result}")


    array1,dict1=get_input2()
    start=time.time()
    result=solution2(array1,dict1)
    print(f"Time Taken: {time.time() - start}")
    print(f"solution 2: {result}")

def get_input():
    party1_nums=[]
    party2_nums=[]
    with open("Day 1 Historian Hysteria/input.txt","r") as file:
        for line in file.read().splitlines():
            num1,num2=line.split("   ")
            bisect.insort(party1_nums,int(num1))
            bisect.insort(party2_nums,int(num2))

    return party1_nums,party2_nums

def solution(array1,array2):
    return sum([abs(x-y) for x,y in zip(array1,array2)])

def get_input2():
    party1_nums=[]
    party2_dict={}
    with open("Day 1 Historian Hysteria/input.txt","r") as file:
        for line in file.read().splitlines():
            num1,num2=line.split("   ")
            party1_nums.append(num1)
            if num2 not in party2_dict:
                party2_dict[num2]=0
            party2_dict[num2]+=1
    
    print(f"{party1_nums=}")
    print(f"{party2_dict=}")
    
    return party1_nums,party2_dict


def solution2(array1,dict1):
    return sum([int(x) * dict1[x] if x in dict1 else 0  for x in array1])

if __name__ =="__main__":
    main()