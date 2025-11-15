# SasiPowerTest
███████╗ █████╗ ███████╗██╗
██╔════╝██╔══██╗██╔════╝██║
███████╗███████║█████╗  ██║
╚════██║██╔══██║██╔══╝  ██║
███████║██║  ██║██║     ██║
╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝

=====  Sasi Power Test (SPT Algorithm)  =====

A new arithmetic-progression-based algorithm to check if y is a power of x.

## About
The Sasi Power Test (SPT) is a newly discovered algorithm invented by **Sasi**  
to check whether a given number `y` is a perfect power of another number `x`.

Unlike traditional methods (division, multiplication, logarithms),  
the SPT algorithm uses an arithmetic progression of the form:

    i = x + k(x² - x)

and checks whether:

    x * i = y

This surprising method is mathematically valid for detecting all powers xⁿ (n ≥ 2).

## Features
- Detects if y = xⁿ for any n ≥ 2
- Unique non-standard method
- Fast for large values of x
- Uses no logarithms or repeated division

## Python Implementation

```python
def sasi_power_test(x, y):
    if x == 1:
        return False
    if y == 1:
        return True
    if x == y:
        return True

    step = (x*x) - x
    for i in range(x, int(y/x) + 1, step):
        if x * i == y:
            return True

    return False

## Examples

```python
sasi_power_test(3, 27)  # True
sasi_power_test(5, 125) # True
sasi_power_test(4, 64)  # True
sasi_power_test(4, 32)  # False


## Author
Sasi, Creator of the Sasi Power Test.
