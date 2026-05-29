#include <iostream>
#include <string>
#include <vector>

using namespace std;

void split(const string& s, vector<string>& tokens, const string& delimiters = " ")
{
	string::size_type lastPos = s.find_first_not_of(delimiters, 0);
	string::size_type pos = s.find_first_of(delimiters, lastPos);

	while (string::npos != lastPos) {
		if (string::npos == pos)
			tokens.push_back(s.substr(lastPos));
		else
			tokens.push_back(s.substr(lastPos, pos - lastPos));
		lastPos = s.find_first_not_of(delimiters, pos);
		if (string::npos == lastPos)
			break;
		pos = s.find_first_of(delimiters, lastPos);
	}
}

void testcase()
{
	vector<string> seps;
	string S = "I love apples, you want eat with me ?";
	split(S, seps);
	int n = seps.size();

	for (int i = 0; i < n; i++)
		cout << seps[i] << endl;
}

int main()
{
	testcase();
	cout << "test end..." << endl;
}
