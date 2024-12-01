from input_gen import day1_input
import matplotlib.pyplot as plt
import timeit


def solution1(array1,array2):
    array1=sorted(array1)
    array2=sorted(array2)
    return sum([abs(x-y) for x,y in zip(array1,array2)])


def solution2(array1,array2):
    array1=sorted(array1)
    dict2={}
    for x in array2:
        if x not in dict2:
            dict2[str(x)]=0
        dict2[str(x)]+=1

    return sum([int(x) * dict2[x] if x in dict2 else 0  for x in array1])


def main():
    plot_array_y_s1=[]
    plot_array_x_s1=[]
    plot_array_y_s2=[]
    plot_array_x_s2=[]
    max=1_000_000
    step=max//10
    repeat=5
    for n in range(1,max,step):
        print(round((n/max) *100) , "%")
        a1,a2=day1_input(n)
        time_taken=timeit.Timer(lambda: solution1(a1,a2)).timeit(repeat)
        plot_array_x_s1.append(n)
        plot_array_y_s1.append(time_taken)

        time_taken=timeit.Timer(lambda: solution2(a1,a2)).timeit(repeat)
        plot_array_x_s2.append(n)
        plot_array_y_s2.append(time_taken)


    plt.plot(plot_array_x_s1, plot_array_y_s1,color='green',label='part 1')
    plt.plot(plot_array_x_s2, plot_array_y_s2,color='blue',label='part 2')
    plt.legend()
    plt.xlabel=('Input size')
    plt.ylabel('Time taken seconds')
    plt.show()


if __name__=="__main__":
    main()