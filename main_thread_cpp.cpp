#include <thread>

using namespace std;

#define NUM_THREADS 50


void f(){
    while(1){
        continue;
    };
}

void run_dead(){

    std::thread threads[NUM_THREADS];
    for(int i = 0; i < NUM_THREADS; ++i)
    {
        threads[i] = std::thread(f);
    }


    for (int i = 0; i < NUM_THREADS; ++i) {
        threads[i].join();

    }
};
int main(void){
    run_dead();
}