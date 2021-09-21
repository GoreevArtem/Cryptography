#include <iostream>
#include "RC4.h"

using namespace::std;

RC4 rc4;

int main(int argc, const char * argv[])
{
    // encoding
    string key, str, out;
    cout << "Encoding\nInput key: ";
    cin >> key;
    cout << "Input Plaintext:";
    cin >> str;
    out = rc4.encoding(str, key);
    cout << "Ciphertext:\t" << out << endl;
    cout << "Plaintext:\t" << rc4.encoding(out, key) << endl;

    // decoding
    cout << "Decoding\nCiphertext:\t" << out << endl;
    cout << "Plaintext:\t" << rc4.encoding(out, key) << endl;

    return 0;
}