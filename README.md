# Idle Language

## Developers

- Jesús Alejandro Galván Villarreal
- Luis Daniel Villarreal Ortega

## Requirements

- Python 3.7.2
- Antlr4

## Usage

To compile grammar and run idle, run the following command in your terminal:
```bash
$ ./idle <file-name>
```

## Development
To recompile grammar with antlr4:

```bash
$ antlr4 -Dlanguage=Python3 Idle.g4
```

To only run the compiler without recompiling the grammar:

```bash
$ python3 Idle.py <file-name>
```

# Quick reference manual

### Class declaration

Everything written in the Idle Language must be contained within a class. To declare a class, first use the declaration `type` followed by the name of the class, which must be capitalized, and then use the keyword `class`. An example of that is:

```
type HelloWorld class {
    main() {
        print("Hello world!");
    }
}
```

The function that will be first run is the function with the signature `main()` in the last class described.

### Attributes

Instance variables can be declared within a class. This is done by specifying the attributes at the beginning of the class with the keyword `var`, followed by the name and the type.

```
type HelloWorld class {
    var name string;
}
```

You can also declare more than one variable of the same type by separating the names with commas.

```
type HelloWorld class {
    var name, otherVar, anotherVar string;
}
```

Attributes are accessed by using the `$` symbol:
```
type HelloWorld class {
    var name;

    main() {
        $name = "World";
        print("Hello " + $name);
    }
}
```

Finally, attributes have visibility which is specified by the casing ot the first letter of the name. If the first letter is lowercase, it will only be available within the class, if it is uppercase, it can be accessed outside of that class.

```
type OtherClass class {
    var PublicAttribute string;
}

type HelloWorld class {
    var test OtherClass;

    main() {
        test = new OtherClass();
        test.PublicAttribute = "can be used outside of class";
    }
}
```

### Local variables

Variables are declared within a scope similarly to attribute declarations, using `var <variable-name> <type>;`. You can also use the short declaration to declare a variable and implicitly set a type by assigning a default value.

```
type HelloWorld class {
    main() {
        var localVariable string;
        localVariable = "This is a local variable";

        shortDeclaration := "This variable will be of type string".
    }
}
```

Once declared, variables may not be declared again or change types.


#### Constructors

You may define a single constructor by writing a function with the same name as the class. Constructors are called by using the keyword new. If no constructor is found, a default constructor is created.

```
type ClassWithConstructor class {
    var name string;

    ClassWithConstructor(name string) {
        $name = name;
    }
}

type HelloWorld class {
    main() {
        var testVar ClassWithConstructor;

        testVar = new ClassWithConstructor("test name");
    }
}
```

### Member functions

Member functions have to be declared within a class by declaring the name, followed by the type. 

Member functions can be either private or public. To differentiate between the two, you must start the name with a lowercase letter for a private function or an uppercase letter for a public function. 

```
type HelloWorld class {
    privateFunction() void {
        print("I'm only accessible within the class!");
    }

    PublicFunction() void {
        print("I'm accessible outside the class!");
    }
}
```

#### Function returns

To give back a result from a function, set the return type in the function signature, and use the `return` statement, followed by an expression.

```
type HelloWorld class {
    ReturningFunction() string {
        return "This function returns a string.";
    }
}
```

#### Function parameters

A function can receive parameters by stating each parameter along with its type within the parenthesis after the method name.

```
type HelloWorld class {
    privateFunction(incomingParam string) void {
        print("This class received the following param: " + incomingParam);
    }
}
```

You can also receive parameters by reference, which will change access and modify the value of the original variable sent to the function.

```
type HelloWorld class {
    privateFunction(incomingParam string ref) void {
        incomingParam = "has changed";
    }

    main() {
        localVar := "This variable";
        print(localVar); // "This variable"
        privateFunction(localVar);
        print(localVar); // "has changed"
    }
}
```

### Arrays

Vector lists may be declared by using `var <var-name> [<size>] <type>`, for example: `var arr[10] int`, for an array of ints with size 10. Similar to other types, you may declare local or instance arrays. Once declared, type and size may not change.

Elements in the array are indexed starting with zero. To access a position in the array, use an expression in between brackets, for example, to set the third element to 100, you would use:
```
arr[2] = 100;
```

Arrays are not currently supported as function parameters and cannot be accessed as public attributes.

### Conditionals

You may use a single if statement for conditional statements:

```
test := true;

if test {
    print("Test is true");
}
```

You can also include an else statement that will be executed when the first condition results to false.

```
test := false;

if test {
    print("Test is true");
}
else {
    print("Test is false");
}
```

You can also use else if to define additional conditional statements.

```
test := 3;

if test > 4 {
    print("Test is higher than 4");
}
else if test < 9 {
    print("Test is less than 9);
}
else {
    print("Test didn't pass other conditions");
}
```

### Loops

#### For loop

A for loop can be declared the following way:

```
for i := 0; i < 10; i = i + 1 {
    print(i);
}
```

#### While loop

A for loop can be declared the following way:

```
i := 0;

while i < 10 {
    print(i);
    i = i + 1;
}
```

### IO Functions

#### print

When calling the function `print`, it will print a line containg the attribute passed as parameter.

```
print("This will display on the console");
```

`print` implicitly calls `toString` if the expression used is not of type string.
```
print(3); // 3
```

#### readString

The function readStrings, retrieves a string from standard input.

#### readInt

The function readInt, retrieves an int from standard input.

#### readFloat

The function readFloat, retrieves a float from standard input.

### Inheritance

Classes may inherit from another single class. This will make available all functions and attributes declared in the parent class. Use the symbols `<-` to define inheritance.

```
type Animal class {
    var name string;
}

type Dog <- Animal class {
    var breed string;

    testFunc() void {
        print("Dog has access to both name and breed");
        print($name);
        print($breed);
    }
}
```

### Imports

You can import any .idle file into another by using the keyword `import` at the top of the file.

```
import TestFile;
```

All classes within the specified file will be included in the file containing the declaration.