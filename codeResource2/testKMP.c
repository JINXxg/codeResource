#include<stdio.h>
#include<string.h>

void KMParray(char *pat,int M,int   *lps){//ws sb

    int len=0;
    int i=1;
    lps[0]=0;
    while(i<M){
        if(pat[i]==pat[len]){
            len++;
            lps[i]=len;
            i++;
        }
        else {
            if(len!=0)
                len=lps[len-1];
        
            else{
                lps[i]=0;
                i++;
            }
        }
    }
}
int main(){
    char pat[]="getgett";
    int M=strlen(pat);
    int lps[M];
    KMParray(pat,M,lps);
    for(int i=0;i<M;i++){
        printf("%d\t",lps[i]);

    }
    return 0;
}