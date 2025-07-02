new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log("Async Task Completed")
        resolve();
    }, 2000)
}).then(() => console.log('First task resolved'))