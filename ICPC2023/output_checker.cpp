#include "testlib.h"
#include <vector>
#include <algorithm>
using namespace std; 
using vi=std::vector<int>;
using vvi=std::vector<vi>;
using pii=std::pair<int,int>;

const int MIN_N = 0, MAX_N = 50;

vvi getMat(int n,InStream&ins){ int nn=n*n;
	vvi a(n,vi(n)); vi chk;
	for(int i=0;i<n;i++){
		a[i][0]=ins.readInt(1,nn); chk.push_back(a[i][0]);
		for(int j=1;j<n;j++){
			a[i][j]=ins.readInt(1,nn); chk.push_back(a[i][j]);
		}
		if (!ins.seekEoln())
		  quit(_pe, "Expected EOLN");
	}
	std::sort(chk.begin(),chk.end());
	for(int i=0;i<n*n;i++) {
		//cout<<"chk["<<i<<"]="<<chk[i]<<endl;
		ensuref(chk[i]==i+1,"chk[i]==i+1");
	}
	return a;
}
int dist(vector<pii>& pos,int k,int kk){
	return abs(pos[k].first-pos[kk].first)+abs(pos[k].second-pos[kk].second);
}
void check(int n,vvi& in, vvi& out){int n2=n/2;
	vector<pii> o2pos(n*n+1);
	for(int i=0;i<n;i++)for(int j=0;j<n;j++){int k=out[i][j];o2pos[k]=pii(i,j);}
	for(int i=0;i<n;i++)for(int j=0;j<n;j++){
		int k=in[i][j],kk;
		//cout<<"k="<<k<<endl; cout.flush();
		if(j>0){kk=in[i][j-1];ensuref(dist(o2pos,k,kk)>=n2,"distance>=n2");}
		if(j<n-1){kk=in[i][j+1];ensuref(dist(o2pos,k,kk)>=n2,"distance>=n2");}
		if(i>0){kk=in[i-1][j];ensuref(dist(o2pos,k,kk)>=n2,"distance>=n2");}
		if(i<n-1){kk=in[i+1][j];ensuref(dist(o2pos,k,kk)>=n2,"distance>=n2");}
	}
}

int main(int argc, char* argv[]) {
  registerTestlibCmd(argc, argv);

	for(;;)
	{
		int n = inf.readInt(MIN_N,MAX_N);
		inf.readEoln();
		if(n==0) break;
		//cout<<"n="<<n<<endl;
		vvi m_in=getMat(n,inf);
		vvi m_ans=getMat(n,ans);
		vvi m_out=getMat(n,ouf);
		check(n,m_in,m_out);
	}
	if (!inf.seekEof()) quit(_pe, "Expected EOF");
	if (!ans.seekEof()) quit(_pe, "Expected EOF");
	if (!ouf.seekEof()) quit(_pe, "Expected EOF");
	quitf(_ok,"correct");
	return 0;
}
