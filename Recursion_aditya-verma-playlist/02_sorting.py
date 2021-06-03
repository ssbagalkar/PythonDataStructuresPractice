"""
Video link--> https://www.youtube.com/watch?v=AZ4jEY_JAVc&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=6&ab_channel=AdityaVermaAdityaVerma
Aditya's cpp code form patreon

#include<bits/stdc++.h>
using namespace std;
#define ll long long unsigned int
void push(vector<int>& v,int temp)
{
    if(v.size()==0 || v[v.size()-1]<=temp)
    {
        v.push_back(temp);
        return;
    }
    int val=v[v.size()-1];
    v.pop_back();
    push(v,temp);
    v.push_back(val);
    return;
}
void sort(vector<int>& v)
{
    if(v.size()==1)
    {
        return;
    }
    int temp=v[v.size()-1];
    v.pop_back();
    sort(v);
    push(v,temp);
    return;

}
int main()
{
    //programming_lord
    int tc;
    cin>>tc;
    while(tc--)
    {
        int size;
        cin>>size;
        vector<int> v;
        for(int i=0;i<size;i++)
        {
            int a;
            cin>>a;
            v.push_back(a);
        }
        sort(v);

        for(int i=0;i<v.size();i++)
        {
            cout<<v[i]<<" ";
        }
        cout<<endl;


    }
return 0;
}
"""


def recursive_sort(arr, n):
	# base condition
	if n == 1:
		return n

	# hypothesis( generally code to make input smaller and smaller )
	temp = arr.pop()# --> keep track of popped element
	recursive_sort(arr, n - 1)

	# induction
	return insert(arr, temp, n - 1)


def insert(arr, el, n):
	# base condition
	if n == 0 or el >= arr[n - 1]:
		arr.append(el)
		return arr

	temp_val = arr.pop()
	insert(arr, el, n - 1)
	arr.append(temp_val)
	return arr


# driver code

arr = [3, 2, 1]
print(recursive_sort(arr, len(arr)))
