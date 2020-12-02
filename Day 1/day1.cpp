#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <iomanip>
#include <conio.h>
#include <fstream>
#include <stdio.h>
using namespace std;
void bacafile();
void cekdatabase();
void tampilkan();
void cari();

int nomor[999],batas;


int main(){
	//cout<<"hallo";
	cekdatabase();
	bacafile();
	tampilkan();
	cari();
}

void cekdatabase(){
	ofstream data;
	data.open("data.txt",ios::app);
	data.close();
}

void bacafile(){
	ifstream baca;											//baca data
	baca.open("data.txt");
	int batasmax;
	for(batasmax=0;batasmax<1000;batasmax++){
		baca>>nomor[batasmax];
		if(baca.eof()){
			break;
		}
	}
	batas=batasmax;
	//cout<<"batas"<<batasmax;
	baca.close();
}

void tampilkan(){
	//int i=0;
	//while(i<=batas){
	//	cout<<nomor[i]<<endl;
	//	i++;
//}
//cout<<"batas"<<batas<<endl;	
}

void cari(){
	for(int i=0;i<=batas;i++){
		for(int y=0;y<=batas;y++){
			for(int z=0;z<=batas;z++){
				if(nomor[i]+nomor[y]+nomor[z]==2020){
					cout<<nomor[i]<<endl;
					cout<<nomor[y]<<endl;
					cout<<nomor[z]<<endl;
					cout<<"-----"<<endl;
					cout<<nomor[i]*nomor[y]*nomor[z]<<endl;
				}
			//cout<<nomor[i]+nomor[y]<<endl;
			}
		}
	}
	
	
}
