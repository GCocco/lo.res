#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#define NULLCHAR '\''


char* getCharPointer(){
  return (char*) malloc(sizeof(char));
}

void freePointer(char* pt){
  free(pt);
}

typedef struct{
  int flag;
  pthread_t thread;
  char* ptr;
}Thread;


void* scanner_func(void* tp){
  Thread* t = (Thread*) tp;
  while(t->flag){
    *t->ptr = NULLCHAR;
    *t->ptr = getchar();
    sleep(1);
  }
  return NULL;
}


Thread* run_scan(char* pter){
  Thread* t = malloc(sizeof(Thread));
  t->ptr = pter;
  t->flag = 1; 
  
  pthread_create(&t->thread, NULL, &scanner_func, t);
  
  return t;
}

void killThread(Thread* t){
  t->flag = 0;
  pthread_join(t->thread, NULL);
  free(t);
  return;
}


int main(){
  char c = 'c';
  Thread* t;

  t = run_scan(&c);

  while (c!='q'){
    printf("%c\n", c);
  }

  killThread(t);
  
  return 0;
}
