
// DATA TYPES

// PRIMITIVE DATA TYPES

    
    /* 
        String - Use for text values
        Boolean - Use for true/false values
        Number  -  Use for both integers and floating-point numbers
        Undefined - Use undefined when a variable has been declared but not assigned a value
        Null - Use null when you explicity want to indicate "no value"

        Which data types are primitives and non-primitives?
            Primitives: String, Number, Boolean, Undefined, Null, Symbol, BigInt
            Non-Primitives: Object, Array, Function, Map, Set   
    */

     

/* 
    VARIABLES
        Use `let` to declare variables that can be reassigned
        
        Use `const` to declare variables that should not be reassigned
            - If it stores a mutable type like an array or object, its contents can still be changed
            - Its best to declare objects by default with const unless you have a specific reason to reassign it later
        
        Convention is to use camelCase for variable names rather than snake
        case or kebab-case in python

        var is outdated and should be avoided, it is a variable declaration method from older versions of JavaScript
        that can change in value and scope in unexpected ways.
            - Var is function-scoped, while let and const are block-scoped.
            - var is hoisted to the top of its scope and initialized with undefined, whereas let and const are hoisted but not initialized.

        Block scope vs Function scope 
            - Block scope means that a variable is only accessible within the block (denoted by curly braces {}) in which it is defined.
            - Function scope means that a variable is accessible anywhere within the function in which it is defined.
    

        
*/

function test() {
    console.log(x);
    var x = 2;
    console.log(x);

    // Will output 2 for the first console log because of hoisting, var declarations are hoisted to the top of their scope
        // Therefore, the declaration of x is moved to the top, but not its assignment.
}

/* 
    ARITHMETHIC OPERATORS
        +  Addition
        -  Subtraction
        *  Multiplication
        /  Division
        %  Modulus (Remainder)
        ** Exponentiation

        +=  Addition Assignment
        -=  Subtraction Assignment
        *=  Multiplication Assignment
        /=  Division Assignment

        When you do operations with different data types, JavaScript will attempt to coerce one type to another
            number + string => string concatenation
            number - string => number subtraction (if string can be coerced to number)
            strting + number => string concatenation
            5 + "5" = "55"
            5 - "2" = 3
            6 + true = 7 
                - true is coerced to 1
            6 + false = 6
                - false is coerced to 0
            
*/

/* 
    TYPE CONVERSIONS
        You can explicitly convert data types using built-in functions:
            String(value) - Converts value to a string
            Number(value) - Converts value to a number
            Boolean(value) - Converts value to a boolean

            parseInt(string) - Converts string to an integer
            parseFloat(string) - Converts string to a floating-point number

            x.toString() - Converts x to a string

*/

/* 
    COMPARISON OPERATORS
        ==  Equality (loose) - Compares values after type coercion
        === Equality (strict) - Compares values and types without type coercion
        !=  Inequality (loose) - Compares values after type coercion
        !== Inequality (strict) - Compares values and types without type coercion
        >   Greater than
        <   Less than
        >=  Greater than or equal to
        <=  Less than or equal to

        It's generally recommended to use strict equality (===) and strict inequality (!==) to avoid unexpected results from type coercion.

        null == undefined // true
        null === undefined // false 
        0 == false // true       
        0 === false // false
        1 == "1" // true
        1 === "1" // false

*/

/* 
    LOGICAL OPERATORS
        &&  Logical AND - true if both operands are true
        ||  Logical OR - true if at least one operand is true
        !   Logical NOT - negates the boolean value of the operand

        These operators are commonly used in conditional statements to control the flow of execution based on multiple conditions.

*/

/* 
    CONDITIONALS
        Use if, else if, and else to control the flow of your program based on conditions

        Syntax:
            if (condition1) {
                // code to execute if condition1 is true
            } else if (condition2) {
                // code to execute if condition2 is true
            } else {
                // code to execute if none of the above conditions are true
            }

            If you have single line statements, you can omit the curly braces, but it's generally good practice to include them for readability.

        You can also use the ternary operator for simple conditional assignments:
            condition ? expressionIfTrue : expressionIfFalse

*/

/* 
    SWITCH STATEMENTS
        Use switch statements for multiple discrete values of a single variable

        Syntax:
            switch (expression) {
                case value1:
                    // code to execute if expression === value1
                    break;
                case value2:
                    // code to execute if expression === value2
                    break;
                ...
                default:
                    // code to execute if none of the cases match
            }

        Remember to include break statements to prevent fall-through, unless that's the intended behavior.
        switch fall-through can be useful in some scenarios, but it can also lead to bugs if not used carefully.
*/

/* 
    ARRAYS
        Use arrays to store ordered collections of values

        Syntax:
            let arrayName = [element1, element2, element3, ...];
            const arrName = new Array(element1, element2, ...);

        Arrays can hold elements of different data types, including other arrays and objects.

        Common array methods:
            array.push(element) - Adds an element to the end of the array
            array.pop() - Removes and returns the last element of the array
            array.shift() - Removes and returns the first element of the array
            array.unshift(element) - Adds an element to the beginning of the array
            array.length - Returns the number of elements in the array
            array.indexOf(element) - Returns the index of the first occurrence of the element, or -1 if not found
            array.slice(start, end) - Returns a shallow copy of a portion of the array from start to end (not inclusive)
            array.splice(start, deleteCount, item1, item2, ...) - Changes the contents of an array by removing or replacing existing elements and/or adding new elements in place

        array concatenation:
            let newArray = array1.concat(array2);

        array joining:
            let str = array.join(separator);
    
        array destructuring:
            let [var1, var2] = array;
        
        array spread operator:
            let newArray = [...array1, ...array2];


*/      

/* 
    WHILE LOOPS
        Use while loops to execute a block of code as long as a specified condition is true
        Syntax:
            while (condition) {
                // code to be executed
            }
    

*/

/* 
    for LOOPS
        Use for loops to execute a block of code a specific number of times
        Syntax: 
            for (initialization; condition; increment) {
                // code to be executed
            }

    fOR LET OF LOOPS
        Use for...of loops to iterate over iterable objects like arrays and strings
        Syntax:         
            for (variable of iterable) {
                // code to be executed
            }

*/


/* 
    SETS
        Use sets to store collections of unique values
        Syntax:
            let setName = new Set([value1, value2, ...]);   
        Common set methods:
            set.add(value) - Adds a value to the set                
            set.delete(value) - Removes a value from the set
            set.has(value) - Returns true if the set contains the value
            set.size - Returns the number of unique values in the set


*/

/* 
    SETS VS ARRAYS
        Sets automatically enforce uniqueness, while arrays can contain duplicate values.
        Sets provide faster lookups for checking the existence of a value compared to arrays.
        Arrays maintain the order of elements, while sets do not guarantee order.   

    Why does sets have faster lookups than arrays?
        Sets are implemented using hash tables, which allow for average O(1) time complexity for lookups.
        Arrays require O(n) time complexity for lookups since they may need to iterate through each element to find a match.
    
    Why do sets not guarantee order?
        Sets are designed for uniqueness and efficient lookups, not for maintaining order.
        The underlying implementation of sets does not prioritize the order of elements, leading to potential reordering during operations.

*/


/* 
    objectS
        Use objects to store collections of key-value pairs
        Syntax:     
            let objectName = {
                key1: value1,
                key2: value2,
                ...
            };

        Accessing object properties:
            objectName.key1 // dot notation
            objectName["key1"] // bracket notation          
        Common object methods:
            Object.keys(object) - Returns an array of the object's keys
            Object.values(object) - Returns an array of the object's values
            Object.entries(object) - Returns an array of the object's key-value pairs as [key, value] arrays

            object destructuring:
                let {key1, key2} = objectName;  
                
            object spread operator:
                let newObject = {...object1, ...object2};   

*/


/* 
    MAPS
        Use maps to store collections of key-value pairs with any data type as keys
        Syntax:
            let mapName = new Map([[key1, value1], [key2, value2], ...]);   
        
        Common map methods:
            map.set(key, value) - Adds or updates a key-value pair in the map       
            map.get(key) - Returns the value associated with the key
            map.delete(key) - Removes a key-value pair from the map
            map.has(key) - Returns true if the map contains the key
            map.size - Returns the number of key-value pairs in the map 
        
        
    Objects vs Maps
        Maps allow keys of any data type, while object keys are typically strings or symbols.
        Maps maintain the order of insertion for key-value pairs, while objects do not guarantee order.
        Maps provide built-in methods for common operations, while objects require manual implementation for some functionalities.

    

*/

/* 
    ERROR HANDLING
        Use try...catch blocks to handle runtime errors gracefully
        Syntax:
            try {       
                // code that may throw an error
            } catch (error) {
                // code to handle the error
            } finally {
                // code that will always execute, regardless of whether an error occurred or not
            }               

        generate your own errors using the throw statement:
            throw new Error("Error message");   

        Why use error handling?
            Prevents program crashes by catching and handling errors
            Provides meaningful error messages to users or developers
            Allows for cleanup or alternative actions in case of errors
        
        Why throw your own errors?
            To indicate specific error conditions in your code
            To provide custom error messages for better debugging
            To enforce certain constraints or validations in your application
        

*/

/* 
    FUNCTIONS
        Use functions to encapsulate reusable blocks of code
        Syntax:
            function functionName(parameters) {
                // code to be executed
            }   
        Functions can also be defined using function expressions or arrow functions:
            const functionName = function(parameters) {
                // code to be executed
            };          
            const functionName = (parameters) => {
                // code to be executed
            };  
        Functions can return values using the return statement:
            function functionName(parameters) {     
                return value;
            }       
        
    
    Difference between function declarations and function expressions and arrow functions:
        Function Declarations:
            Hoisted to the top of their scope, allowing them to be called before they are defined.          
            Have their own 'this' context based on how they are called.
        Function Expressions:           
            Not hoisted, so they must be defined before they are called.
            Have their own 'this' context based on how they are called.
        Arrow Functions:
            Not hoisted, so they must be defined before they are called.
            Do not have their own 'this' context; they inherit 'this' from the surrounding lexical scope.       

    REST PARAMETERS AND SPREAD OPERATOR
        Use rest parameters to accept a variable number of arguments in a function
        Syntax:     
            function functionName(...restParameters) {
                // code to be executed
            }   
        
        Use the spread operator to expand an iterable (like an array) into individual elements
        Syntax:     
            functionName(...iterable);  

*/


/* 
    MAP, FILTER, REDUCE
        Use map to create a new array by applying a function to each element of an existing array           
        Syntax:
            let newArray = array.map((element) => {
                // return transformed element
            }); 

        Use filter to create a new array with elements that pass a specified condition
        Syntax:
            let newArray = array.filter((element) => {
                // return true to keep the element, false to exclude it
            }); 
        
        Use reduce to accumulate a single value from an array by applying a function to each element
        Syntax:
            let result = array.reduce((accumulator, element) => {
                // return updated accumulator
            }, initialValue);   


*/

/* 
    THIS KEYWORD    
        The this keyword refers to the context in which a function is called
        In a regular function, this refers to the object that called the function
        In an arrow function, this refers to the surrounding lexical context    

*/

/* 
    PROMISES
        Use promises to handle asynchronous operations in JavaScript
        Syntax: 
            let promise = new Promise((resolve, reject) => {
                // asynchronous operation
                if (success) {  
                    resolve(value); // operation succeeded
                } else {
                    reject(error); // operation failed
                }       
            });   

        Consuming promises using then and catch:    
            promise.then((value) => {
                // handle resolved value
            }).catch((error) => {
                // handle rejected error
            }); 

    Why use promises?
        Simplifies asynchronous code by avoiding callback hell
        Provides a clear and structured way to handle success and error cases
        Allows for chaining multiple asynchronous operations in a readable manner   

    What is a promise?
        A promise is an object that represents the eventual completion (or failure) of an asynchronous operation and its resulting value.
    
    What are the states of a promise?
        Pending: The initial state, neither fulfilled nor rejected.
        Fulfilled: The operation completed successfully, and the promise has a resulting value.
        Rejected: The operation failed, and the promise has a reason for the failure (error).   

    Why use then and catch?
        then allows you to handle the resolved value of a promise when it is fulfilled.
        catch allows you to handle errors when a promise is rejected.
        They provide a clean and organized way to manage asynchronous code flow.
    
    What is async and await?
        async and await are syntactic sugar built on top of promises that allow you to write asynchronous code in a more synchronous-looking manner.
        An async function returns a promise, and the await keyword can be used inside an async function to pause execution until a promise is resolved or rejected.

    Promises vs async/await
        Promises provide a way to handle asynchronous operations using then and catch methods, allowing for chaining and error handling.
        async/await allows you to write asynchronous code that looks synchronous, making it easier to read and maintain.
        async/await is built on top of promises, so they can be used together seamlessly.

    Promises.all 
        Use Promise.all to run multiple promises in parallel and wait for all of them to resolve
        Syntax:
            Promise.all([promise1, promise2, ...]).then((values) => {
                // handle array of resolved values
            });             

            

*/


/* 
    FETCH API
        Use the Fetch API to make HTTP requests and handle responses
        Syntax: 
            fetch(url, options)
                .then((response) => {
                    // handle response  
                })
                .catch((error) => {
                    // handle error
                });
    Why use the Fetch API?
        Provides a modern and flexible way to make HTTP requests in JavaScript
        Returns promises, allowing for easy handling of asynchronous operations
        Supports various request methods (GET, POST, PUT, DELETE, etc.) and options for customization
    
    FETCH WITH ASYNC/AWAIT
        Use async/await with the Fetch API for cleaner and more readable asynchronous code
        Syntax:
            const fetchData = async (url) => {
                try {
                    const response = await fetch(url);  
                    const data = await response.json();
                    // handle data
                } catch (error) {
                    // handle error
                }       
            };  
    
    .json() method
        The .json() method is used to parse the response body of a fetch request as JSON
        It returns a promise that resolves to a JavaScript object or array  

    

*/

const promise1 = new Promise( (resolve, reject) => {
    if (true) {
        resolve('Promise 1 resolved');
    } else {
        reject('promise 1 rejected');
    }
})

promise1.then( (value) => {
    console.log(value);
})
.catch( (error) => {
    console.error(error);
})


const getUserData = async (userId) => {
    try {
        const user = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}`);
        const userData = await user.json();
        console.log(userData)
        return userData
    } catch(error) {
        console.log(`Error fetching userdata: ${error}`)
    }
}