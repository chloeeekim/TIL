// https://algospot.com/judge/problem/read/JOSEPHUS

#include <iostream>
#include <vector>
using namespace std;

int main() {
	int testcase;
	int n, k;

	cin >> testcase;

	while (testcase--) {
		cin >> n >> k;
		vector<int> v;

		for (int i = 1; i <= n; i++) {
			v.push_back(i);
		}
		
		int index = 0;
		while(n > 2) {
			v.erase(v.begin() + index);
			n--;
			index = (index + k - 1) % n;
		}

		cout << v[0] << " " << v[1] << endl;
	}

	return 0;
}