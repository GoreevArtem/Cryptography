#include "RC4.h"

using namespace std;

void swap(char *a, char *b){
    char tmp = *a;
    *a = *b;
    *b = tmp;
}
// Развертывание ключей
void RC4::ksa(string key, int key_len) {
    for (auto i = 0; i < 256; i++) {
        S[i] = i;
    }
    int j = 0, temp;
    for (auto i = 0; i < 256; i++) {
        j = (j + S[i] + key[i % key_len]) % 256;
        swap(S[i], S[j]);
    }
}

// Псевдослучайная генерация
string RC4::prga(string in, int len) {
    int i = 0, j = 0, x = 0, temp;
    for (x = 0; x < len; x++) {
        i = (i + 1) % 256;
        j = (j + S[i]) % 256;
        temp = S[i];
        S[i] = S[j];
        S[j] = temp;
        K[x] = in[x] ^ S[(S[i] + S[j]) % 256];
    }

    return K;
}

string RC4::encoding(string in, string key) {
    int key_size = (int) key.size();
    int str_size = (int) in.size();

    // Create Key Stream
    ksa(key, key_size);
    // Encrypt or Decrypt input (plaintext)
    return prga(in, str_size);
}
