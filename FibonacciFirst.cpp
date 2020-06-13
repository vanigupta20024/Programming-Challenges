/*	
    FIBONACCI
	Challenge #1, Difficulty #1 (beginner-friendly) 	
	Suggested language: Java, C++, Python
	Languages you shouldnt use: Assembler :P

	void task() {
		Take two integers as input by the user.

		Now calculate atleast 10 iterations of the Fibonacci-sequence with the two integers as starting point.

		Output those calculations.
	}

	void extraTask () {
		1) ask the user how many iterations of the Fibonacci sequence the program should calculate

		2) If one number in the sequence is divisible by x (let the user input that too), output "FIZZ" instead of it
	}
*/

#include<bits/stdc++.h>
#define ll long long int

using namespace std;

// using memoization ~ TopToBottom
ll dp[200] = {0};

int fibRec(ll s, ll e, ll n){
	
	if (n == s || n == e){
		dp[n] = n;
		return n;
	}
	
	if(dp[n]!=0){
		return dp[n];
	}
	
	ll answer = fibRec(s, e, n-1) + fibRec(s, e, n-2);
	dp[n] = answer;
	return answer;
	
}

void printFib(ll s, ll e, ll n, ll d){
	
	ll count = 0;
	ll a = s, b = e, c;
	
	while(count < n){
		
		c = a + b;
		a = b;
		b = c;
		
		if (c%d == 0) cout<<"FIZZ ";
		else cout<<c<<" ";
		
		count++;
	}
}

int main(){
//	#ifndef ONLINE_JUDGE
//		freopen("input.txt", "r", stdin);
//		freopen("output.txt", "w", stdout);
//	#endif
	
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	ll start, end, num, div;
	
	cin>>start>>end>>num>>div;

	cout<< fibRec(start, end, num) <<endl;
	
	// extended task
	printFib(start, end, num, div);
	
	return 0;	
}
