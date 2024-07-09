/**
Input: customers = [[1,2],[2,5],[4,3]]
Output: 5.00000
Explanation:
1) The first customer arrives at time 1, the chef takes his order and starts preparing it immediately at time 1, and finishes at time 3, so the waiting time of the first customer is 3 - 1 = 2.
2) The second customer arrives at time 2, the chef takes his order and starts preparing it at time 3, and finishes at time 8, so the waiting time of the second customer is 8 - 2 = 6.
3) The third customer arrives at time 4, the chef takes his order and starts preparing it at time 8, and finishes at time 11, so the waiting time of the third customer is 11 - 4 = 7.
So the average waiting time = (2 + 6 + 7) / 3 = 5.

problem states tha we need to find the average timing time of customer who cam to eat the resturant where there is only one 
person as chef.

step 1 : 
    let interval = 0;
    let initially = true;
    let totalTime = 0;  we need interval to store the interval time to store and initially varible to keep trak of frist 
    element of customers to handle the edge case and totalTime is use to store the total amount of time taken.

step 2 : if initially is true then we are traversing the frist element in the customer array so er need to sum the arrival, ordertaken
for the order make sure it runs only once at the time of beginning. 
      if (initially) {
            interval = arrival + ordertaken;
            initially = false;
        }
step 3 : next we need to check  whether interval is less the arrival if it is there means we need to add interval = arrival + ordertaken;
if not means we need to add interval with ordertaken.

        else {
            if (interval < arrival) {
                interval = arrival + ordertaken;
            } else {
                interval += ordertaken;
            }
        }
step 4 : wait_time can be calculted by using interval - arrival and adding the wait_time to totalTime to find the average time taken
for waiting 
 const wait_time = interval - arrival;
        totalTime += wait_time;
        
step 5 :  finally we need to return the avrage time taken for in wating 
return totalTime / customers.length;

 */


function averageWaitingTime(customers) {
    let interval = 0;
    let initially = true;
    let totalTime = 0;

    for (let i = 0; i < customers.length; i++) {
        const [arrival, ordertaken] = customers[i];
        if (initially) {
            interval = arrival + ordertaken;
            initially = false;
        } else {
            if (interval < arrival) {
                interval = arrival + ordertaken;
            } else {
                interval += ordertaken;
            }
        }
        const wait_time = interval - arrival;
        totalTime += wait_time;
    }
    
    return totalTime / customers.length;
}
