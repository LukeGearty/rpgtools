#compiler and flags
CXX = clang++
CXXFLAGS = -std=c++14 -Wall -Wextra -g

#target
TARGET = vtm_character

SRCS = main.cpp Attributes.cpp ChooseClan.cpp
OBJS = $(SRCS:.cpp=.o)

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(TARGET)