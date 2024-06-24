//Debouncing in Java Script

/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timeout;

    return function(...args) {
        // Clear the previous timeout if any
        clearTimeout(timeout);

        // Set a new timeout
        timeout = setTimeout(() => {
            fn(...args);
        }, t);
    };
};

/**
 * Example usage:
 */
let start = Date.now();
function log(...inputs) {
    console.log([Date.now() - start, inputs]);
}

const dlog = debounce(log, 50);
setTimeout(() => dlog(1), 50);
setTimeout(() => dlog(2), 75);

/**
 * Example explanation:
 * The first call to `dlog(1)` at t=50ms is cancelled because the second call to `dlog(2)` happens at t=75ms.
 * The second call is then delayed by 50ms and executes at t=125ms with the inputs [2].
 */
