#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <termios.h>

#define NULLCHAR '\''
static struct termios old, current;

/* Initializza terminale */
void initTermios() 
{
  tcgetattr(0, &old); /* grab old terminal i/o settings */
  current = old; /* make new settings same as old settings */
  current.c_lflag &= ~ICANON; /* disable buffered i/o */
  current.c_lflag &= ~ECHO; /* set no echo mode */
  tcsetattr(0, TCSANOW, &current); /* use these new terminal i/o settings now */
}

/* Restore old terminal i/o settings */
void resetTermios(void) 
{
  tcsetattr(0, TCSANOW, &old);
}

/* Read 1 character */
char getch_() 
{
  char ch;
  initTermios();
  ch = getchar();
  resetTermios();
  return ch;
}


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
    *t->ptr = getch_();
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
