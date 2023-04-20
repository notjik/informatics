#include <iostream>
#include <vector>
using namespace std;

int main() {
	freopen("27-131b.txt", "r", stdin);
	
	int n, m, k;
	cin >> n >> m >> k;
	vector<vector<int> > a(n, vector<int> (m));
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cin >> a[i][j];
		}
	}
	
	vector<vector<long long> > pref(n, vector<long long>(m));
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (i == 0 && j == 0) {
				pref[i][j] = a[i][j];
			} else if (i == 0) {
				pref[i][j] = pref[i][j - 1] + a[i][j];
			} else if (j == 0) {
				pref[i][j] = pref[i - 1][j] + a[i][j];
			} else {
				pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + a[i][j];
			}
		}
	}
	long long ans = 0;
	for (int i = k - 1; i < n; ++i) {
		for (int j = k - 1; j < m; ++j) {
			long long ctz = pref[i][j];
			if (i == k - 1 && j == k - 1) {
				// ...
			} else if (i == k - 1) {
				ctz -= pref[i][j - k];
			} else if (j == k - 1) {
				ctz -= pref[i - k][j];
			} else {
				ctz = ctz - pref[i - k][j] - pref[i][j - k] + pref[i - k][j - k];
			}
			ans = max(ans, ctz);
		}
	}
	cout << ans << '\n';
	return 0;
}
