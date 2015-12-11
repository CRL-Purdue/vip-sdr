#include <stdio.h>

int main() {
    
    FILE * fptr = fopen("sdr.in", "r");
while(!feof(fptr)) {
   int count = 0;
   int ch = 0;
   for(count  = 0; count < 8; count++) {
       int bit = fgetc(fptr);
       if(bit == EOF) break;
       ch = (ch << 1) | bit;
   }
   printf("%c", ch);
}
fclose(fptr);
return 0;

}

