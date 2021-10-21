#include <iostream>
#include <string.h>


typedef struct myarray_t {
    int len;
    double data[];
} myarray_t;

myarray_t*
init_arr(int len) {
    myarray_t* arr;
    arr = (myarray_t*) malloc(sizeof(myarray_t) + sizeof(double) * (len));  // len or len-1?
    arr->len = len;
    return arr;
}

void
reset_arr (myarray_t* arr) {
    memset(arr->data, '\0', sizeof(double) * arr->len);
}

void
print_arr (myarray_t* arr) {
    for(int i = 0; i < arr->len; i++) {
        std::cout << arr->data[i] << std::endl;
    }
}

void
arr_add(myarray_t* arr, double new_value) {

    int index = 0;

    // search position
    for (int i = 0; i < arr->len; i++) {

        // if the value is already in the array, return
        if (arr->data[i] == new_value) {
            return;
        }
        // if the value is bigger that the new value, we already
        // over the position, so we need to exit the loop and start
        // shifting all the elements
        if (arr->data[i] > new_value) {
            index = i;
            break;
        }

        // if the value is 0, we already at the end of the region
        // of the array that is actually populated
        if (arr->data[i] == 0) {
            index = i;
            break;
        }
    }

    // shift elements after the index
    // by iterating the array in reverse
    for (int i = arr->len; i > index; i--) {
        arr->data[i] = arr->data[i - 1];
    }

    // add the new value
    arr->data[index] = new_value;
}


void
arr_remove(myarray_t* arr, double value) {
    // set index to -1
    int index = -1;

    // iterate over the array
    for (int i = 0; i < arr->len; i++) {
        // if the value is equal to the one we want to remove
        // then set index var to the index of the element.
        if (arr->data[i] == value) {
            index = i;
        }

        // if the index is different from -1 it means
        // that we already found the value to remove,
        // so let overwrite the array element with the following value
        if (index != -1) {
            arr->data[i] = arr->data[i + 1];
        }
    }

    // if we didn't find the value, the index remain to -1, so we can return
    // TODO(mattia): maybe this piece of code isn't useful.
    if(index == -1) {
        return;
    }
}

double
arr_pop(myarray_t* arr) {

    // store the first value
    double res = arr->data[0];

    // iterate over the array to shift left all the elements
    for (int i = 0; i < arr->len; i++) {
        arr->data[i] = arr->data[i+1];
    }

    return res;
}


int main() {
    // test my array

    // declare and init
    myarray_t* arr = init_arr(5);

    std::cout << "arr addrss" << std::endl;
    std::cout << arr << std::endl;
    std::cout << "arr->len" << std::endl;
    std::cout << arr->len << std::endl;
    std::cout << "arr->data (addrss of data)" << std::endl;
    std::cout << arr->data << std::endl;

    std::cout << "before reset" << std::endl;
    print_arr(arr);

    arr->data[0] = 1.2;
    arr->data[3] = 1.3;

    std::cout << "after new values" << std::endl;
    print_arr(arr);

    reset_arr(arr);
    std::cout << "after reset" << std::endl;
    print_arr(arr);

    std::cout << "adding 1.3" << std::endl;
    arr_add(arr, 1.3);
    print_arr(arr);
    std::cout << "adding 4.3" << std::endl;
    arr_add(arr, 4.3);
    print_arr(arr);
    std::cout << "adding 3.2" << std::endl;
    arr_add(arr, 3.2);
    print_arr(arr);
    std::cout << "adding 2.0" << std::endl;
    arr_add(arr, 2);
    print_arr(arr);
    std::cout << "adding 2.0" << std::endl;
    arr_add(arr, 2);
    print_arr(arr);

    std::cout << "removing 2.0" << std::endl;
    arr_remove(arr, 2);
    print_arr(arr);
    std::cout << "removing 2.0" << std::endl;
    arr_remove(arr, 2);
    print_arr(arr);
    std::cout << "removing 4.3" << std::endl;
    arr_remove(arr, 4.3);
    print_arr(arr);

    std::cout << "popping the first value" << std::endl;
    int a = arr_pop(arr);
    std::cout << "popped result: " << a << std::endl;
    print_arr(arr);
}
