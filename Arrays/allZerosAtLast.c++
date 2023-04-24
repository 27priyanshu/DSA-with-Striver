
vector<int> moveZeros(int n, vector<int> a) {
    // Write your code here.
    //step1
    vector <int> temp;
    for(int i=0;i<n;i++){
        if(a[i]!=0){
            temp.push_back(a[i]);//numbers are getting added into new array named temp
        }
    }
    //step 2
    int nz= temp.size();
    for(int i =0;i<nz;i++){
        a[i]=temp[i];//numbers are added into main array 
    }
    //step3
    for(int i =nz;i<n;i++){
        a[i]=0;//zeros are getting added into the last of the array

    }
    return a;
}
