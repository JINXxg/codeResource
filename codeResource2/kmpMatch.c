#include<stdio.h>
#include<string.h>


//create a method to comput lps array
void computeLPS(char *pat,int M,int *lps){//here is the key code
    int len=0;
    int i=1;
    M=strlen(pat);
    lps[0]=0;
    while(i<M){
        if(lps[i]==lps[len]){//remember use simple example to write such as at 3 mismatch
            len++;
            lps[i]=len;
            i++;
        }
        else if(len!=0){
            len=lps[len-1];
        }
        else{
            lps[i]=0;
            i++;
        }
    }
}

//create a method to execute search
int KMPSearch(char *pat,char *text){
    int i=0;
    int j=0;
    int N=strlen(text);
    int M=strlen(pat);
    int lps[M];
    //before match compute the lps Array
    computeLPS(pat,M,lps);
    //match
    while(i<N){
        if(pat[j]==text[i]){
            i++;
            j++;
        }
        if(j==M){
            printf("Match succesfuly at inedex %d\n",i);
            printf("LPS NUMBER\n");
            for(int i=0;i<M;i++){
                printf("%d\t",lps[i]);
            }
            return 1;
        }
        else if(i<N&&pat[j]!=text[i]){
            if(j!=0){//j reprent the pat's position
                j=lps[j-1];
            }
            else{
                i++;//mean's j is back to the start then still unmatch so from the begian
            }
            
        }
       
    }
    return 0;//match failed
}

int main(){
    char package[]="https://GETGETt/index.html";
    char pat[]="GETGETt";
    if(KMPSearch(pat,package)){
        printf("fuck you damn\n");
        
    }
    else{
        printf("patten not found in packet\n");
    }
    return 0;
}