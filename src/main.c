/*
** EPITECH PROJECT, 2020
** main.c
** File description:
** - Call project with start_project function
** - Print Help if arg is -h
*/

#include "project.h"

int main(int ac, char const * const *av)
{
    (void)ac;
    return start_project(av);
}
