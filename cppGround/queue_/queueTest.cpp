// queue_back.cpp
// compile with: /EHsc
#include <queue>
#include <iostream>




int main( ) {
	using namespace std;
	queue <int> q1;
 
	q1.push( 10 );
	q1.push( 11 );
	q1.push(100);

 
	int& i = q1.back( );
	const int& ii = q1.front( );
 
	cout << "The integer at the back of queue q1 is " << i << "." << endl;
	cout << "The integer at the front of queue q1 is " << ii << "." << endl;
	q1.pop();

        cout << "after pop The integer at the back of queue q1 is " << q1.back() << "." << endl;
        cout << "after pop The integer at the front of queue q1 is " << q1.front() << "." << endl;

	return 0;

}
