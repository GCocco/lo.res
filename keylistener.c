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

typedef struct{
  pthread_t thread;
  char* c;
  int wait;
}Thread;


char getch_(Thread* t){
  char ch;
  ch = *t->c;
  printf("retrieving scanned char %c, %c \n", *t->c, ch);
  t->wait = 0;
  return ch;
}


void* scanner_func(void* tp){
  Thread* t = (Thread*) tp;
  initTermios();
  
  while(1){
    t->wait = 1;
    printf("scanning...\b");
    *t->c = NULLCHAR;
    *t->c = getchar();
    printf("scanned %c, waiting...\n",*t->c);
    while(t->wait){usleep(200000);}
  }
  return NULL;
}


Thread* run_scan(){
  Thread* t = malloc(sizeof(Thread));
  t->c = malloc(sizeof(char));
  pthread_create(&t->thread, NULL, &scanner_func, t);  
  return t;
}

void killThread(Thread* t){
  pthread_kill(t->thread, 0);
  //pthread_join(t->thread, NULL);
  free(t->c);
  free(t);
  resetTermios();
  return;
}


int main(){
  Thread* t;
  char ch = ' ';
  t = run_scan();
  
  while (ch!='Q'){
    ch = getch_(t);
    printf("%c\n", ch);
    sleep(1);
  }

  killThread(t);
  
  return 0;
}
