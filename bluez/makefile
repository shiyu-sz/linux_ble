
CC = gcc
TARGET = advtest
INCLUDES += -I./ -I./include

CompileFlags += -g -c -Wall

SRCS = main.c \
	src/shared/crypto.c \
	src/shared/mainloop.c \
	src/shared/hci.c \
	src/shared/mgmt.c \
	src/shared/mainloop-notify.c \
	src/shared/util.c \
	src/shared/io-mainloop.c \
	src/shared/queue.c \
	src/shared/timeout-mainloop.c
OBJS = $(SRCS:.c=.o)

# 公用
LIBS += -L./

%.o: %.c
	$(CC) $(CFLAGS) $(INCLUDES) $(CompileFlags) -c -o $@ $<

$(TARGET): $(OBJS)
	$(CC) -o $@ $(OBJS) $(LIBS) $(LDFLAGS)

all:$(TARGET)

clean:
	rm -rf $(TARGET) *.o *~
