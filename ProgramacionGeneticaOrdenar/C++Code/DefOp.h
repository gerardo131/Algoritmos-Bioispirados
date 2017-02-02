#include <iostream>
float sum(float x,float y){
	float x_aux = 0;
	float y_aux = 0;
	float M = 34000000000000000000000000000000000000.0;
	if (x>0 && y>0){
		x_aux = M - x;
		if ( x_aux - y < 0 )
			return M;
		else
			return x+y;

	}else if(x<0 && y<0){
		x_aux = M + x;
		if ( x_aux + y > 0 )
			return M;
		else 
			return x+y;
	}	
	else{
		return x + y ;
	}

}

float res(float x,float y){
	float x_aux = 0;
	float y_aux = 0;
	float M = 34000000000000000000000000000000000000.0;
	if (x>0 && y<0){
		x_aux = M - x;
		if ( x_aux + y < 0 )
			return M;
		else
			return x+y;

	}else if(x<0 && y>0){
		x_aux = M + x;
		if ( x_aux - y > 0 )
			return M;
		else 
			return x+y;
	}	
	else{
		return x + y ;
	}
}

float mul(float x,float y){
	float x_aux = 0;
	float y_aux = 0;
	float M = 34000000000000000000000000000000000000.0;
	x_aux = x/M;
	if (x_aux*y<=1 && x_aux*y>=-1)
		return  x*y;
	return 34000000000000000000000000000000000000.0;
	
}

float div(float x,float y){
	float x_aux = 0;
	float y_aux = 0;
	float M = 34000000000000000000000000000000000000.0;
	if(y == 0)
		return 0;
	return  x/y;
}

//float
//1.18e-38 <= |X| <= 3.40e38  
//34000000000000000000000000000000000000.00 -340000000000000000000000000000000000000
//int  (signed) 	32 	

//-2147483640 <= X <= 2147483640 