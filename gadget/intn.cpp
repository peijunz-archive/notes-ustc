#include <iostream>
#include <cstdint>
template<int N, bool C = true>
/// Int of at least given size
struct least {
    typedef typename least < N + (N < 9 && N > 1), (N < 9 && N > 1) >::_int _int;
};
template<int N>
struct least<N, false> {
    typedef void _int;
};

template<bool C>
struct least<1, C> {
    typedef int8_t _int;
};

template<bool C>
struct least<2, C> {
    typedef int16_t _int;
};
template<bool C>
struct least<4, C> {
    typedef int32_t _int;
};
template<bool C>
struct least<8, C> {
    typedef int64_t _int;
};
typedef least<5>::_int mint;
int main(){
    mint a=5;
    printf("%d\t%d\n", a, sizeof(a));
}
