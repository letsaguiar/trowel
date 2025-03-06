CC := gcc

SRC_FILES := {{ sources|join(' ') }}
OBJ_FILES := $(subst .c,.o,$(SRC_FILES))

{% if type == "executable" %}
NAME := {{ name }}
{% elif type == "library" %}
NAME := {{ name + '.a' }}
{% endif %}

.PHONY: all

all: $(NAME)

{% if type == "executable" %}
$(NAME): $(OBJ_FILES)
	$(CC) $^ -o $@
{% elif type == "library" %}
	ar rcs $@ $^
{% endif %}

%.o: %.c
	$(CC) -c $< -o $@