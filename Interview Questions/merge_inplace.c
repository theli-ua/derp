/*
Given an integer array of which both first half and second half are sorted. Write a function to merge the two parts to create one single sorted array in place [do not use any extra space].
e.g. If input array is [1,3,6,8,-5,-2,3,8] It should be converted to: [-5,-2,1,3,3,6,8,8]
*/
#include <stdio.h>
#include <string.h>

int input[] = {1,3,6,8,-5,-2,3,8};

void merge(int* ar, unsigned int len)
{
    int* left = ar;
    int leftLength = len/2;
    int* right = ar + leftLength;
    int* end = right + leftLength;
    while (leftLength > 0 && right < end)
    {
        if(*left < *right)
        {
            leftLength--;
            left++;
        }
        else
        {
            int value = *right++;
            memmove(left + 1, left, leftLength * sizeof(int));
            *left++ = value;
        }
    }
}

int main(int argc, char** argv)
{
    int i;
    int n = sizeof(input) / sizeof(input[0]);
    printf("input:\n");
    for (i = 0; i < n ; ++i)
    {
        printf("%d, ",input[i]);
    }
    
    merge(&input[0], n);

    printf("\noutput:\n");
    for(i = 0 ; i < n ; ++i)
    {
        printf("%d, ",input[i]);
    }
    
    printf("\n");
    return 0;
}
