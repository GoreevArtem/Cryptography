#ifndef C___RC4_H
#define C___RC4_H


#include <iostream>

using namespace ::std;

class RC4 {
public:
    void ksa(string key, int key_len);

    string prga(string in, int len);

    string encoding(string in, string key);

private:
    int S[256];
    char K[256];
};


#endif //C___RC4_H
