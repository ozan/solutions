#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXOP 100
#define NUMBER '0'
#define EXP '1'
#define SIN '2'

int getop(char *);
void push(double);
double pop(void);
double peek(void);

/* reverse Polish calculator */
int main() {
  int type;
  double op2;
  char s[MAXOP];

  while ((type = getop(s)) != EOF) {
    switch (type) {
    case NUMBER:
      push(atof(s));
      break;
    case EXP:
      push(exp(pop()));
      break;
    case SIN:
      push(sin(pop()));
      break;
    case '+':
      push(pop() + pop());
      break;
    case '*':
      push(pop() * pop());
      break;
    case '-':
      op2 = pop();
      push(pop() - op2);
      break;
    case '/':
      op2 = pop();
      if (op2 != 0.0)
        push(pop() / op2);
      else
        printf("error: zero divisor\n");
      break;
    case '%':
      op2 = pop();
      push((int)pop() % (int)op2);
      break;
    case '^':
      op2 = pop();
      push(pow(pop(), op2));
      break;
    case '\n':
      printf("\t%.8g\n", pop());
      break;
    default:
      printf("error: unknown command %s\n", s);
      break;
    }
  }
  return 0;
}

#define MAXVAL 100

int sp = 0;
double val[MAXVAL];

/* push: push f onto value stack */
void push(double f) {
  if (sp < MAXVAL)
    val[sp++] = f;
  else
    printf("error: stack full, can't push%g\n", f);
}

/* pop: pop and return top value from stack */
double pop(void) {
  if (sp > 0)
    return val[--sp];
  else {
    printf("error: stack empty\n");
    return 0.0;
  }
}

double peek(void) {
  if (sp > 0)
    return val[sp - 1];
  else {
    printf("error: stack empty\n");
    return 0.0;
  }
}

void duptop(void) { push(peek()); }
void swap(void) {
  double a, b;
  a = pop();
  b = pop();
  push(a);
  push(b);
}
void clear(void) { sp = 0; }

int getch(void);
void ungetch(int);

/* getop: get next operator or numeric operand */
int getop(char *s) {
  char token[MAXOP], c, head;
  int i = 1;

  while ((token[0] = head = getch()) == ' ' || head == '\t')
    ;
  if (head == '\n')
    return '\n';
  while ((c = getch()) != ' ' && c != EOF && c != '\n')
    token[i++] = c;
  token[i] = '\0';

  if (c == '\n')
    ungetch('\n');

  if (!isdigit(head) && i == 1)
    return head;
  if (strcmp(s, "sin") == 0)
    return SIN;
  if (strcmp(s, "exp") == 0)
    return EXP;

  strcpy(s, token);
  return NUMBER;
}

#define BUFSIZE 100

char buf[BUFSIZE];
int bufp = 0;

int getch(void) { return (bufp > 0) ? buf[--bufp] : getchar(); }

void ungetch(int c) {
  if (bufp >= BUFSIZE)
    printf("ungetch: too many characters\n");
  else
    buf[bufp++] = c;
}
