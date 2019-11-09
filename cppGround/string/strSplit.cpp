#include <iostream>
#include <string>
#include <map>
#include <vector> 



using namespace std;

void split(const string& s, vector<string>& tokens, const string& delimiters=" ")
{
	string::size_type lastPos = s.find_first_not_of(delimiters, 0);
	string::size_type pos = s.find_first_of(delimiters, lastPos);
	while (string::npos != pos || string::npos != lastPos) {
		tokens.push_back(s.substr(lastPos, pos-lastPos));
		lastPos = s.find_first_not_of(delimiters, pos);


	}


}


void testcase(){
	vector<string> seps;
	string S = "I love apples, you want eat with me ?";
	split(S, seps);
	int n = seps.size();

	for(int i=0;i<n;i++){
	cout << seps[i] << endl;

	}


}






int main(){
	testcase();
	cout << "test end..." << endl;
}
