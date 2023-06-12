FOLDER="result"
# cp ../template.html index.html
# g++ -std=c++17 -Wall -Wextra -O2 ../main.cpp -o main
./main
dot -Tsvg rotations.dot > rotations.svg
dot -Tsvg matchings.dot > matchings.svg