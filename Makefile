##
## EPITECH PROJECT, 2020
## Makefile
## File description:
## classic Makefile with with unit tests
##

CC	=	gcc


##?				NORMAL TESTS
MAIN	=	src/main.c	\

SRC		=	src/start_project.c			\

OBJ		=	$(SRC:.c=.o)

NAME	=	project

CPPFLAGS	=	-I./include -Wall -Wextra -g3
#!#######################################################

##?				UNIT TESTS
COVER		=	--coverage

CRITERION	=	-lcriterion

TEST_NAME	=	unit_tests

SRC_TEST	=	tests/unit_tests/basic_tests.c	\
				$(SRC)							\

OBJ_TEST	=	$(SRC_TEST:.c=.o)

GCDA		=	*.gcda
GCNO		=	*.gcno
#!#######################################################

all:	$(NAME)

$(NAME):	$(OBJ)
	$(CC) -o $(NAME) $(MAIN) $(SRC) $(CPPFLAGS) $(CLIBS)

tests_run:	$(OBJ_TEST)
	$(CC) -o $(TEST_NAME) $(COVER) $(CPPFLAGS) \
	$(SRC_TEST) $(CLIBS) $(CRITERION)
	./$(TEST_NAME)

tests_clean:
	rm -f $(OBJ_TEST)
	rm -f $(GCDA)
	rm -f $(GCNO)

clean:
	rm -f $(OBJ)
	rm -f $(OBJ_TEST)
	find -name '*.gcda' -delete
	find -name '*.gcno' -delete

fclean:	clean
	rm -f $(NAME)
	rm -f $(TEST_NAME)

re:	fclean all

.PHONY: all clean fclean re
