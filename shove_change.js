/**
 * @param {number[]} bills
 * @return {boolean}
 */
var shovelChange = function(bills) {
    // implement function here
    let queue = [];
    for (let i=0; i < bills.length; i++) {
        if (i === 0 && bills[i] > 5) {
            return false;
        }
        pay = bills[i];
        if (pay > 5 && queue.length > 0) {
            c = 0;
            while (pay > 5 && queue.length > 0) {
                if (pay - queue[c] > 0) {
                    pay = pay - queue[c];
                    queue.splice(queue.indexOf(queue[c]), 1);
                }
                c = c + 1;
                if (c >= queue.length) {
                    break;
                }
            }
        }
        if (pay > 5) {
            return false;
        }
        queue = [...queue, bills[i]];
    }
    return true;
};