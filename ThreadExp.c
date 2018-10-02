#include <jni.h>
#include <stdio.h>
#include "ThreadExp.h"
#include "time.h"

void delay(int number_of_seconds) 
{ 
    int milli_seconds = 1000 * number_of_seconds; 
    clock_t start_time = clock();  
    while (clock() < start_time + milli_seconds) 
        ; 
}

JNIEXPORT void JNICALL Java_ThreadExp_sleep (JNIEnv *env, jclass class, jlong milli){
	delay(milli);
	printf("Time exhausted\n");
	return;
}