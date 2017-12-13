/*
These are just some naive implementations of functions you would find in the standard C string library, as well as some test harness code
I tried to not look up solutions
Definitely not guaranteed to be correct
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int string_length(const char *string)
{
    const char *s;
    s = string;
    while (*(++s));

    return (s - string);
}

void string_copy(const char *a, char *b)
{
    char *start;
    start = b;
    for(; *a; ++a, ++b) {
        *b = *a;
    }
    b = start;
}

int stricmp(const char *a, const char *b)
{
    if (strlen(a) != strlen(b)) {
        return -1;
    }

    for(;; ++a, ++b) {
        int d = tolower(*a) - tolower(*b);
        if (d != 0 || !*a) {
            return d;
        }
    }
}

char *string_substring(char *a, char *b)
{
    if (string_length(b) > string_length(a)) {
        return '\0';
    }

    char *b_ptr, *substr_ptr;
    b_ptr = b;
    substr_ptr = a;

    while(*a && *b_ptr) {
        if (*b_ptr == *a) {
            ++a;
            ++b_ptr;
        } else {
            b_ptr = b;
            ++a;
            substr_ptr = a;
        }
    }
    if (*b_ptr == '\0') {
        return substr_ptr;
    } else {
        return '\0';
    }
}

void do_string_substring()
{
    char *substr;
    substr = string_substring("hello how are you today", "how");

    printf("string_substring() result: %s\n", substr);

    printf("strstr result: %s\n", strstr("hello how are you today", "how"));
}

void do_string_copy()
{
    char a[] = "a bit of a string, here, mate.";
    char *b = malloc(sizeof(char) * string_length(a) + 1);

    string_copy(a, b);
    printf("string_copy(%s): %s\n", a, b);
    free(b);
}

void do_string_length()
{
    char *strings[] = {"hello", "fido", "c"};
    int i;
    for (i = 0; i < 3; ++i) {
        printf("string_length(%s): %d\n", strings[i], string_length(strings[i]));
    }
}

void do_stricmp()
{
    char *strings[][3] = {{"hello", "hi"}, {"bout", "bout"}, {"about", "bout"}};

    int i;
    for(i = 0; i < 3; ++i) {
        printf("stricmp(%s, %s): %d\n", strings[i][0], strings[i][1], stricmp(strings[i][0], strings[i][1]));
    }
}

int main()
{
    do_string_length();
    do_stricmp();
    do_string_copy();
    do_string_substring();
}
