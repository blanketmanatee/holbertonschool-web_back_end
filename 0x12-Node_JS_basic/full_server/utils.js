Create a file full_server/utils.js, in the file create a function named readDatabase that accepts a file path as argument:
It should read the database asynchronously
It should return a promise
When the file is not accessible, it should reject the promise with the error
When the file can be read, it should return an object of arrays of the firstname of students per fields