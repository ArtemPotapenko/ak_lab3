number a = 1;
number b = 1;
number sum = 0;
while (b < 4000000){
     if (b % 2 == 0){
        sum = sum + b;
     }
     b = a + b;
     a = b - a;
}
print(sum);