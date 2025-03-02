CC := gcc

SRC_FILES := {{ sources|join(' ') }}
OBJ_FILES := $(subst .c,.o,$(SRC_FILES))

NAME := {{ name }}

.PHONY: all

all: $(NAME)

$(NAME): $(OBJ_FILES)
	$(CC) $^ -o $@

%.o: %.c
	$(CC) -c $< -o $@