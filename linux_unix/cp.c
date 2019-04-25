#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <stdio.h>
#include <utime.h>
#include <string.h>

//공통사항
int mv_file(int rf, int wf, char* file_1, char* file_2, struct stat rf_stat){
	rf = open(file_1, O_RDONLY); //원본파일
	fstat(rf, &rf_stat); //원본파일의 속성을 받아옴
	wf = open(file_2, O_WRONLY|O_CREAT, rf_stat.st_mode); //이동파일, 원본파일퍼미션

	int n; //이동하면서 나타나는 한줄의 크기
	char buf[1024]; //이동을 위한 버퍼
	while(n = read(rf, buf, 1024)){ //한줄씩 읽어서
		write(wf, buf, n); //이동파일에 저장
	}
}

int mv_stat(int wf, char* file_2, struct stat rf_stat){
	struct utimbuf rf_time;
	rf_time.actime = rf_stat.st_atime;
	rf_time.modtime = rf_stat.st_mtime;
	utime(file_2, &rf_time); //생성시간
	chmod(file_2, rf_stat.st_mode); //퍼미션
	fchown(wf, rf_stat.st_uid, rf_stat.st_gid); //소유자
}

//옵션이 없을때
int no_opt(int argc, char **argv){
	char* file_1 = argv[1];
	char* file_2 = argv[2];
	int rf, wf;
	struct stat rf_stat;
	mv_file(rf, wf, file_1, file_2, rf_stat);
	mv_stat(wf, file_2, rf_stat);
	close(rf); //닫아주기
	close(wf); //닫아주기
}

//옵션이 있을때
int switch_opt(char* opt, char* file_2){
	if(access(file_2, F_OK) == 0){ //file2가 이미 존재한다면
		if(strcmp(opt, "-i") == 0){ //물어보고 진행
			while(1){
				printf("Excute?(y/n)\n");
				scanf("%s", opt);
				if(strcmp(opt, "y") == 0){break;}
				else if(strcmp(opt, "n") == 0){exit(1);}
				else{}
			}
		}
		else if(strcmp(opt, "-f") == 0){}//강제로 진행
		else{ //다른 옵션이면 종료
			exit(1);
		}
	}
	unlink(file_2); //존재하는 복사파일 삭제
}

int yes_opt(int argc, char **argv){
	char* opt = argv[1];
	char* file_1 = argv[2];
	char* file_2 = argv[3];
	int rf, wf;
	struct stat rf_stat;
	switch_opt(opt, file_2);
	mv_file(rf, wf, file_1, file_2, rf_stat);
	mv_stat(wf, file_2, rf_stat);
	close(rf); //닫아주기
	close(wf); //닫아주기
}

int main(int argc, char **argv)
{
	if(argc == 3){no_opt(argc, argv);}
	else if(argc == 4){yes_opt(argc, argv);}
	else{printf("mv -opt file_1 file_2 \n");}
	exit(1);
}
