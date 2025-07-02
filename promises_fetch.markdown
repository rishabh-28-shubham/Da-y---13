# Understanding Promises in JavaScript

A `Promise` is a proxy for a value not necessarily known when the promise is created. It allows you to associate handlers with an asynchronous action's eventual success value or failure reason. This lets asynchronous methods return values like synchronous methods: instead of immediately returning the final value, the asynchronous method returns a *promise* to supply the value at some point in the future.

A `Promise` is in one of these states:

- *pending*: initial state, neither fulfilled nor rejected.
- *fulfilled*: meaning that the operation was completed successfully.
- *rejected*: meaning that the operation failed.

![Flowchart showing how the Promise state transitions between pending, fulfilled, and rejected via then/catch handlers. A pending promise can become either fulfilled or rejected. If fulfilled, the "on fulfillment" handler, or first parameter of the then() method, is executed and carries out further asynchronous actions. If rejected, the error handler, either passed as the second parameter of the then() method or as the sole parameter of the catch() method, gets executed.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/promises.png)\## 1. Basic Promise Creation and Consumption

The first example creates a simple Promise that resolves after a delay.

```javascript
const firstTask = new Promise((resolve, reject) => {
  setTimeout(() => {
    console.log('Async task completed');
    resolve();
  }, 1000);
});

firstTask.then(() => console.log('First task resolved'));
```

**Explanation**:

- `firstTask` is a Promise that executes an asynchronous operation using `setTimeout`.
- After 1 second, it logs a message and resolves the Promise.
- The `.then()` method handles the resolved state, logging a confirmation message.

## 2. Another Simple Promise

This example shows another Promise with similar functionality but no variable assignment.

```javascript
new Promise((resolve, reject) => {
  setTimeout(() => {
    console.log('Second async task');
    resolve();
  }, 1000);
}).then(() => console.log('Second task resolved'));
```

**Explanation**:

- This Promise is created and consumed inline without storing it in a variable.
- It logs a message after 1 second and resolves, triggering the `.then()` callback.

## 3. Resolving with Data

This Promise resolves with an object containing user data.

```javascript
const userTask = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve({ student: 'sai', enrollment: '32421423' });
  }, 1000);
});

userTask.then((user) => console.log(user));
```

**Explanation**:

- `userTask` resolves with an object containing `student` and `enrollment`.
- The `.then()` method receives this object and logs it.

## 4. Promise with Error Handling

This example introduces error handling using `.catch()` and `.finally()`.

```javascript
const authTask = new Promise((resolve, reject) => {
  setTimeout(() => {
    const hasError = true;
    if (!hasError) {
      resolve({ username: 'coder', password: 'secure123' });
    } else {
      reject('ERROR: Authentication failed');
    }
  }, 1000);
});

authTask
  .then((user) => {
    console.log(user);
    return user.username;
  })
  .then((username) => console.log(username))
  .catch((error) => console.log(error))
  .finally(() => console.log('Auth task completed'));
```

**Explanation**:

- `authTask` simulates a conditional operation that fails (`hasError` is `true`).
- If successful, it resolves with user data; otherwise, it rejects with an error message.
- The first `.then()` logs the user object and returns the username.
- The second `.then()` logs the username.
- The `.catch()` handles the error, logging the error message.
- The `.finally()` runs regardless of the outcome, logging a completion message.

## 5. Using Async/Await

This example rewrites the error-handling Promise using async/await syntax.

```javascript
const scriptTask = new Promise((resolve, reject) => {
  setTimeout(() => {
    const hasError = true;
    if (!hasError) {
      resolve({ username: 'jsdev', password: 'code123' });
    } else {
      reject('ERROR: Script execution failed');
    }
  }, 1000);
});

async function processScriptTask() {
  try {
    const result = await scriptTask;
    console.log(result);
  } catch (error) {
    console.log(error);
  }
}

processScriptTask();
```

**Explanation**:

- `scriptTask` is similar to `authTask` but uses async/await for consumption.
- The `processScriptTask` function uses `try/catch` to handle resolution or rejection.
- `await` pauses execution until the Promise resolves or rejects.

# Fetch () :-

The fetch() method of the Window interface starts the process of fetching a resource from the network, returning a promise that is fulfilled once the response is available.

The promise resolves to the Response object representing the response to your request.

A fetch() promise only rejects when the request fails, for example, because of a badly-formed request URL or a network error. A fetch() promise *does not* reject if the server responds with HTTP status codes that indicate errors (404, 504, etc.).

## 6. Fetching Data with Async/Await

This example fetches user data from an API using async/await (commented out in the original).

```javascript
async function fetchUsers() {
  try {
    const response = await fetch('https://api.github.com/users/ShivanshMehtaa');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.log('Error:', error);
  }
}

// fetchUsers();
```

**Explanation**:

- The `fetchUsers` function uses the Fetch API to retrieve user data.
- `await fetch(...)` sends a GET request, and `await response.json()` parses the response.
- Errors are caught and logged in the `catch` block.

## 7. Fetching Data with Promises

This example uses the Fetch API with Promise chains.

```javascript
fetch('https://api.github.com/users/ShivanshMehtaa')
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.log(error));
```

**Explanation**:

- This code fetches GitHub user data using the Fetch API.
- The first `.then()` converts the response to JSON.
- The second `.then()` logs the parsed data.
- The `.catch()` handles any errors during the fetch.

## Key Changes from Original Code

- Variable names changed for clarity (e.g., `promiseOne` to `firstTask`, `promiseFour` to `authTask`).
- Arrow functions used consistently for modern syntax.
- Error variable renamed from `error` to `hasError` to avoid shadowing.
- Consistent indentation and formatting for readability.

This refactored code and explanation provide a clear understanding of Promises, async/await, and Fetch API usage in JavaScript.