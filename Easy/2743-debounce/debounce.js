let callTime = -1
let timeoutId = undefined

/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    return function(...args) {
        const currentTime = Date.now();

        if (timeoutId !== undefined) {
            if (callTime <= currentTime && callTime + t >= currentTime) {
                clearTimeout(timeoutId);
            }
        }

        callTime = currentTime
        timeoutId = setTimeout(() => fn(...args), t)
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */