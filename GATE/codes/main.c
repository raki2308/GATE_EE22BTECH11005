#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_TRIALS 100000

char toss_coin() {
    char outcomes[] = {'H', 'T'};  // 'H' for heads, 'T' for tails
    return outcomes[rand() % 2];   // obtain H or T randomly
}

int main() {
    srand(time(NULL));  // Initialize random seed

    int count_all_tails = 0; // counts number of trails with all three tails
    int count_at_least_two_tails = 0; // counts number of trails with atleast two tails

    for (int i = 0; i < NUM_TRIALS; i++) {
    	int count=0; // counts number of tails in a trail
        char outcomes[3] = {toss_coin(), toss_coin(), toss_coin()}; // outcome array for all three coins
	for (int i = 0; i < 3; i++){
	if (outcomes[i] == 'T'){
	count++;
	}
	}
        if (count == 3) {
            count_all_tails++;
        }
        if (count == 2) {
            count_at_least_two_tails++;
        }
        }
    double probability = (double)count_all_tails / count_at_least_two_tails; 

    printf("Simulated Probability: %.4f\n", probability);
    printf("Theoretical Probability: 1/4 = 0.25\n");

    return 0;
}
