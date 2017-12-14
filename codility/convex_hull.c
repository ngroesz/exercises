/*
 * Find the smallest convex set that contains the given points
 * Mostly an adaptation of Wikipedia's pseudo-code for:
 * Graham scan
 * Quicksort
 *
 * Definitely not guaranteed to be correct
*/

#include <stdio.h>
#include <stdlib.h>

struct Point2D {
    int x;
    int y;
    float angle;
};

int ccw(struct Point2D A1, struct Point2D A2, struct Point2D A3)
{
    return (A2.x - A1.x) * (A3.y - A1.y) - (A2.y - A1.y) * (A3.x - A1.x);
}

float slope(struct Point2D *A1, struct Point2D *A2)
{
    if (abs(A1->x - A2->y) == 0) {
        return 0;
    }
    return ((float) abs(A1->y - A2->y) / (float) abs(A1->x - A2->x));
}

int partition(struct Point2D A[], int start, int end)
{
    struct Point2D pivot = A[start];
    struct Point2D swap;

    int i = start - 1;
    int j = end + 1;
    do {
        do {
            ++i;
        } while(A[i].angle < pivot.angle);

        do {
            --j;
        } while(A[j].angle > pivot.angle);

        if (i >= j) {
            return j;
        }

        swap = A[i];
        A[i] = A[j];
        A[j] = swap;
    } while(1);

    return i + 1;
}

void quicksort(struct Point2D A[], int start, int end)
{
    if (start < end) {
        int partition_index = partition(A, start, end);
        quicksort(A, start, partition_index);
        quicksort(A, partition_index + 1, end);
    }
}

void print_point(struct Point2D *point)
{
    printf("%d:%d angle: %f\n", point->x, point->y, point->angle);
}

int convex_hull(struct Point2D A[], int N)
{
    struct Point2D *lowest_point = NULL;
    struct Point2D swap;

    for(int i = 0; i < N; ++i) {
        if (lowest_point == NULL || A[i].y < lowest_point->y || (A[i].y == lowest_point->y && A[i].x < lowest_point->x)) {
            lowest_point = &A[i];
        }
    }

    swap = A[0];
    A[0] = *lowest_point;
    *lowest_point = swap;

    for(int i = 0; i < N; ++i) {
        A[i].angle = slope(&A[i], &A[0]);
    }

    quicksort(A, 0, N - 1);

    int final_points_size = 1;
    for(int i = 1; i < N; ++i) {
        while(i < N -1 && ccw(A[0], A[i], A[i + 1]) == 0) {
            ++i;
        }
        A[final_points_size++] = A[i];
    }

    struct Point2D **path = calloc(N, sizeof(struct Point2D *));

    path[0] = &A[0];
    path[1] = &A[1];
    path[2] = &A[2];

    int path_size = 3;

    for (int i = 3; i < final_points_size; ++i) {
        while (ccw(*path[path_size - 2], *path[path_size - 1], A[i]) <= 0) {
            --path_size;
        }
        path[++path_size - 1] = &A[i];
    }

    puts("path:");
    for(int i = 0; i < path_size; ++i) {
        print_point(path[i]);
    }

    free(path);

    return path_size;
}

int main()
{
    struct Point2D A[6];

    A[0].x = 3;
    A[1].x = 6;
    A[2].x = 2;
    A[3].x = 5;
    A[4].x = 1;
    A[5].x = 4;

    A[0].y = 2;
    A[1].y = 3;
    A[2].y = 5;
    A[3].y = 2;
    A[4].y = 1;
    A[5].y = 4;

    printf("convex_hull %d\n", convex_hull(A, 6));

    struct Point2D points[8] = {{0, 3}, {1, 1}, {2, 2}, {4, 4}, {0, 0}, {1, 2}, {3, 1}, {3, 3}};

    printf("convex_hull: %d\n", convex_hull(points, sizeof(points) / sizeof(points[0])));
}
