#include <thread>
#include "Python.h"
#include "pybind11/pybind11.h"

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wmissing-noreturn"
#define NUM_THREADS 50

using namespace std;
namespace py = pybind11;

void f(){
    while(1){
        continue;
    }
}

py::none nothing(){
//    Py_BEGIN_ALLOW_THREADS
    f();
//    Py_END_ALLOW_THREADS
    return py::none();
}

PYBIND11_MODULE(example1, m){
    m.def("nothing", &nothing, "do nothing");
}

//  g++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` main_multi_nothread.cpp -o example1`python3-config --extension-suffix`