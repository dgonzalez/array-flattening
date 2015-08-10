# array-flattening
This program resolves the array flattening problem.

I have written few tests (python doctests) in order to verify the results.

The choosen language is Python and there is a reason behind it: although the problem states an arbitrary nested array
the example given is an arbitrary nested array of arrays and ints (some of the elements are not `iterable`) so I 
selected a language with weak typing in order to avoid verbosity (in Java I would have used a `List<Object>` which
would have make the code harder to read).

There are some tests that covers the most typical corner cases and also the given example.

There is an issue with this approach which is related to the fact that the solution is recursive: the stack overflow exception can occur on an arbitrary long input data (although this script is using tail recursion).

The way to solve the stack overflow exception would be create an iterative version of the program (as every single recursive algorithm have at least one iterative solution given the Church-Turing thesis).
