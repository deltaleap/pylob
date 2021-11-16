#include <string>
#include <stdint.h>

typedef uint32_t price_t;
typedef uint32_t quantity_t;
typedef uint32_t timestamp_t;

struct trade_t {
    timestamp_t timestamp
    price_t price;
    quantity_t quantity;
    uint32_t direction;
};

struct Trades {
    std::string name;

    trade_t last_trade;

    void add(price_t price, quantity_t quantity, std::string direction);

};
