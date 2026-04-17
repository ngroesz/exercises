/*
 * just a basic implementation of quicksort
*/

#include <stdio.h>

int partition(int A[], int low, int high)
{
    int pivot = A[low];
    int i = low - 1;
    int j = high + 1;
    do {
        do {
            ++i;
        } while(A[i] < pivot);

        do {
            --j;
        } while(A[j] > pivot);

        if (i >= j) {
            return j;
        }

        int swap = A[i];
        A[i] = A[j];
        A[j] = swap;
    } while(1);
}
void quicksort(int A[], int low, int high)
{
    if (low < high) {
        int partition_index = partition(A, low, high);
        quicksort(A, low, partition_index);
        quicksort(A, partition_index + 1, high);
    }
}

int main()
{
    int A[] = {100, 800, 200, 300};

    quicksort(A, 0, 3);

    for(int i = 0; i <= 3; ++i) {
        printf("%d\n", A[i]);
    }
}
