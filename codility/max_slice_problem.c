#include <stdbool.h>
#include <stdio.h>
/* 
 * https://codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/
 *
 *
*/

int solution(int A[], int N)
{
    bool greatest_increase_set = false;
    int greatest_increase;
    bool lowest_value_set = false;
    int lowest_value;

    for (int i = 0; i < N; ++i) {
        if (!lowest_value_set || A[i] < lowest_value) {
            lowest_value = A[i];
            lowest_value_set = true;
        }
        if (!greatest_increase_set || A[i] - lowest_value > greatest_increase) {
            greatest_increase = A[i] - lowest_value;
            greatest_increase_set = true;
        }
    }
    return greatest_increase;
}

int main()
{
    int A[] = {23171, 21011, 21123, 21366, 21013, 21367};

    printf("solution(): %d\n", solution(A, 6));
}
