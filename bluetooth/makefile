
CC = gcc
TARGET = bluetooth
INCLUDES += -I./

CompileFlags += -g -c -Wall

SRCS = main.c
OBJS = $(SRCS:.c=.o)

# 公用
LIBS += -lbluetooth

%.o: %.c
	$(CC) $(CFLAGS) $(INCLUDES) $(CompileFlags) -c -o $@ $<

$(TARGET): $(OBJS)
	$(CC) -o $@ $(OBJS) $(LIBS) $(LDFLAGS)

all:$(TARGET)

clean:
	rm -rf $(TARGET) *.o *~
