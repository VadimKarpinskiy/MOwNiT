#include <iostream>
using std::cout;

const int N = 100;

float kahan_sum(float arr[N]){
    float sum = 0.0f;
    float err = 0.0f;
    for (int i = 0; i < N; i++){
        float y = arr[i] - err;
        float tmp = sum + y;
        err = (tmp - sum) - y;
        sum = tmp;
    }
    return sum;
}

int main() {
    float v = 0.177;
    float arr[N];
    for (int i = 0; i < N; i++)
        arr[i] = v;
    cout << kahan_sum(arr);
    return 0;
}