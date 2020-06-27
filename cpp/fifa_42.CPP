#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<graphics.h>
#include<dos.h>
#include<stdlib.h>
#include<bios.h>
#define PI 3.14159
					     //min=3
long double p_pos=1,ai_pos=0;
double p__pos=1,ai__pos=1,s_p=1,s_ai=1;
int c12=1,m12=0,k12=0,cf=0,tg=0,tmp=0,tmp1=0,minus=0,g_p=0,g_ai=0,aI=0,pass_r=75,s=0,pass_rp=42,pass_rf=10,pr=7,ai_r=75,X=639,Y=479,r=75,x=250,y=250,br=5,gx=10,gy=250,Arr[9]={42,42,42,42,42,42,42,42,42};
double vx1=0,vy1=0,vx[9]={0,0,0,0,0,0,0,0,0},vy[9]={0,0,0,0,0,0,0,0,0};
int x1=X/2,y1=100,px=X/2,py=100;
double px1[9]={200,25,200,X-250,X-250,250,150,150,X-225},py1[9]={50,250,450,50,450,250,175,325,250};
double fx1[9]={X-175,X-25,X-175,350,350,X-250,200,X-150,200},fy1[9]={100,250,400,125,375,250,125,250,375};

double fx2[9]={X-200,X-25,X-200,250,250,X-250,X-150,X-150,225},fy2[9]={50,250,450,50,450,250,175,325,250};
double px2[9]={175,25,175,X-350,X-350,250,X-200,150,X-200},py2[9]={100,250,400,125,375,250,125,250,375};

char name[20];

double px3[9]={250,25,150,X-250,X-250,250,150,150,X-225},py3[9]={150,250,425,50,450,350,75,250,250};
double fx3[9]={X-175,X-25,X-175,325,325,X-325,200,X-150,200},fy3[9]={100,250,400,75,425,250,175,250,325};


double fx4[9]={X-250,X-25,X-150,250,250,X-250,X-150,X-150,225},fy4[9]={150,250,425,50,450,350,75,250,250};
double px4[9]={175,25,175,X-325,X-325,325,X-200,150,X-200},py4[9]={100,250,400,75,425,250,175,250,325};

class form
{ public:

  double px[9],py[9];
  double xc[9],yc[9];
  double fx[9],fy[9];
  double a1[9],b1[9];

  void change(int i);

} frmtn[4];

void form::change(int i)
{ int j;
 if (i==0)
 { for (j=0;j<9;j++)
   { px[j]=px1[j];
     py[j]=py1[j];
     fx[j]=fx1[j];
     fy[j]=fy1[j];
     xc[j]=px1[j];
     yc[j]=py1[j];
     a1[j]=fx1[j];
     b1[j]=fy1[j];
   }
 }
 if (i==1)
 { for (j=0;j<9;j++)
   { px[j]=px2[j];
     py[j]=py2[j];
     fx[j]=fx2[j];
     fy[j]=fy2[j];
     xc[j]=px2[j];
     yc[j]=py2[j];
     a1[j]=fx2[j];
     b1[j]=fy2[j];
   }
 }

 if (i==2)
 { for (j=0;j<9;j++)
   { px[j]=px3[j];
      py[j]=py3[j];
     fx[j]=fx3[j];
     fy[j]=fy3[j];
     xc[j]=px3[j];
     yc[j]=py3[j];
     a1[j]=fx3[j];
     b1[j]=fy3[j];
   }
 }

 if (i==3)
 { for (j=0;j<9;j++)
   { px[j]=px4[j];
     py[j]=py4[j];
     fx[j]=fx4[j];
     fy[j]=fy4[j];
     xc[j]=px4[j];
     yc[j]=py4[j];
     a1[j]=fx4[j];
     b1[j]=fy4[j];
   }
 }

}

int changeform();

void cmenu(int m12,int k1)
{ A:

  setcolor(WHITE);
  line(0,100,700,100);
  line(0,101,700,101);
  line(0,102,700,102);
  line(0,105,700,105);
  line(0,106,700,106);
  line(0,107,700,107);

  settextstyle(0,0,7);
  outtextxy(100,25,"FIFA '42");

  int poly[6],poly1[6];

  poly[0]=75;   poly1[0]=575;
  poly[1]=275;  poly1[1]=275;

  poly[2]=75;   poly1[2]=575;
  poly[3]=375;  poly1[3]=375;

  poly[4]=25;   poly1[4]=625;
  poly[5]=325;  poly1[5]=325;

  if (c12==1 || (c12==0 && k1!=1 && k1!=2) )
  { setcolor(15);
    setfillstyle(SOLID_FILL,15);
    fillpoly(3,poly);
    fillpoly(3,poly1);
  }
  if (c12==0 && k1==1)
  { setcolor(15);
    setfillstyle(SOLID_FILL,15);
    fillpoly(3,poly);
    setcolor(CYAN);
    setfillstyle(SOLID_FILL,CYAN);
    fillpoly(3,poly1);
  }
  if (c12==0 && k1==2)
  { setcolor(15);
    setfillstyle(SOLID_FILL,15);
    fillpoly(3,poly1);
    setcolor(CYAN);
    setfillstyle(SOLID_FILL,CYAN);
    fillpoly(3,poly);
  }

  if (m12==0)
  { setcolor(15);
    rectangle(99,249,551,401);
    rectangle(100,250,550,400);
    setcolor(GREEN);
    rectangle(100,250,550,400);
    setfillstyle(SOLID_FILL,GREEN);
    floodfill(105,251,GREEN);
    setcolor(WHITE);
    settextstyle(0,0,10);
    outtextxy(135,290,"START");
  }

  if (m12==1)
  { setcolor(15);
    rectangle(99,249,551,401);
    rectangle(100,250,550,400);
    setcolor(LIGHTBLUE);
    rectangle(100,250,550,400);
    setfillstyle(SOLID_FILL,LIGHTBLUE);
    floodfill(105,251,LIGHTBLUE);
    setcolor(YELLOW);
    settextstyle(0,0,4);
    outtextxy(130,300,"INSTRUCTIONS");

  }

  if (m12==2)
  { setcolor(15);
    rectangle(99,249,551,401);
    rectangle(100,250,550,400);
    setcolor(GREEN);
    rectangle(100,250,550,400);
    setfillstyle(SOLID_FILL,GREEN);
    floodfill(105,251,GREEN);
    setcolor(BLACK);
    settextstyle(0,0,6);
    outtextxy(113,300,"FORMATION");

  }

  if (m12==3)
  { setcolor(15);
    rectangle(99,249,551,401);
    rectangle(100,250,550,400);
    setcolor(6);
    rectangle(100,250,550,400);
    setfillstyle(SOLID_FILL,6);
    floodfill(105,251,6);
    setcolor(11);
    settextstyle(0,0,5);
    outtextxy(125,300,"HIGH SCORE");
   }

  if (m12==4)
  { setcolor(15);
    rectangle(99,249,551,401);
    rectangle(100,250,550,400);
    setcolor(RED);
    rectangle(100,250,550,400);
    setfillstyle(SOLID_FILL,RED);
    floodfill(105,251,RED);
    setcolor(YELLOW);
    settextstyle(0,0,10);
    outtextxy(175,290,"QUIT");

  }
  if (c12==0 )
  { c12++; delay(150); goto A; }
  if (c12==1)
  { c12=0; }

}


class score
{
  char nm[20];
  int sc;
  public:
  void getdata();
  void input();
  void process();
  void display();
}obj,m;

void score::getdata()
{
  cout<<"NAME: ";
  gets(obj.nm);
  obj.sc=g_p;
  cout<<endl;
}

void score::input()
{ fstream fi;
  fi.open("SC.txt",ios::out);

   getdata();

   fi.write((char*)&obj,sizeof(obj));

   fi.close();
}

void score::process()
{ int max=0;
  char m_nm[20];
  fstream f1;
  f1.open("SC.txt",ios::in);

  while( !f1.eof() )
  {
   f1.read((char*)&obj,sizeof(obj));
   if( obj.sc>=max )
   { max=obj.sc;
     strcpy(m_nm,obj.nm);
   }
  }
  strcpy(m.nm,m_nm);
  m.sc=max;
  f1.close();
}

void score::display()
{ cleardevice();
  clrscr();
  setcolor(YELLOW);
  settextstyle(0,0,7);
  outtextxy(42,42,"HIGHSCORE");
//  closegraph();
//  clrscr();
  fstream f1;
  f1.open("SC.txt",ios::in);
  f1.seekg(0);
  while ( !f1.eof() )
  { f1.read((char*)&obj,sizeof(obj));
    if (obj.sc==m.sc && strcmp(obj.nm,m.nm)==0 )
    { gotoxy(21,15);
      cout<<"NAME: ";puts(obj.nm);
      gotoxy(42,15);
      cout<<"SCORE: "<<obj.sc;
    }
  }
  f1.close();
}

void highscore()
{ clrscr();
  obj.process();
  obj.display();
  getch();
}

int instr();

int menu()
{ A:
  int key;

  cmenu(m12,k12);
  getch();

  while (bioskey(1)==0)
  { key=bioskey(0);

    if (key==19712)
    { m12++; k12=1; }

    if (key==19200)
    { m12--; k12=2; }

    if (key==7181)
    { break; }

    if (m12<0)
    { m12=2-m12; }

    m12=m12%5;

    cleardevice();
    cmenu(m12,k12);
  }
    if (m12<0)
    { m12=2-m12; }

    m12=m12%5;

  if (m12==0)
  { return 0; }

  if (m12==1)
  { instr(); goto A; }

  if (m12==2)
  { changeform(); }

  if (m12==3)
  { highscore(); goto A; }

  if (m12==4)
  {
   obj.input();
   getch();
   exit(0);
  }

  return 0;
}


void pass1 (int k1)
{ float a=5.5;
  if (k1==1)
  { x1-=a; y1-=a; }
  if (k1==2)
  { y-=a; }
  if (k1==3)
  { x1+=a; y1-=a; }
  if (k1==4)
  { x1-=a; }
  if (k1==5)
  { x1+=a; }
  if (k1==6)
  { x1-=a; y1+=a; }
  if (k1==7)
  { y1+=a; }
  if (k1==8)
  { x1+=a; y1+=a; }
}

int instr()
{ int k1=0,key,t=0,t1=5;

 // setbkcolor(LIGHTGREEN);

  for (t=0;t<t1;t++)
  {
    setcolor(WHITE);
    line(0,(Y/2)-1,X,(Y/2)-1 );
    line(0,Y/2,X,Y/2);
    line(0,(Y/2)+1,X,(Y/2)+1 );

    line (X/3,Y/2,X/3,Y);
    line (2*X/3,Y/2,2*X/3,Y);

    setcolor(CYAN);
    settextstyle(0,0,3);
    outtextxy(56,3*Y/4,"PASS");
    outtextxy(56+(X/3),3*Y/4,"MISC");
    outtextxy(56+(2*X/3),3*Y/4,"MOVE");

    setcolor(RED);
    settextstyle(0,0,5);
    outtextxy(4,270,"Q");
    outtextxy(87,270,"W");
    outtextxy(169,270,"E");

    outtextxy(4,345,"A");
    outtextxy(169,345,"D");

    outtextxy(4,420,"Z");
    outtextxy(87,420,"X");
    outtextxy(169,420,"C");

    outtextxy(4+(2*X/3),345,"<");
    outtextxy(169+(2*X/3),345,">");
    settextstyle(0,1,5);
    outtextxy(122+(2*X/3),420,"<");
    outtextxy(122+(2*X/3),260,">");

    settextstyle(0,0,2);
    outtextxy(1+(X/3),280,"<spacebar>");
    outtextxy(1+(X/3),390,"<escape>");
    outtextxy(1+(X/3),440,"<backspace>");
    setcolor(YELLOW);
    settextstyle(11,0,3);
    outtextxy(2+(X/3),303,"TOGGLE ON=>Holds Formation");
    outtextxy(2+(X/3),318,"TOGGLE OFF=>Holds Position");
    outtextxy(2+(X/3),413,"Open Pause Menu");
    outtextxy(2+(X/3),463,"To Exit");

    while (bioskey(1)!=0)
    { key=bioskey(0);
      if (key==18432)
      { py-=1; }
      if (key==20480)
      { py+=1; }
      if (key==19712)
      { px+=1; }
      if (key==19200)
      { px-=1; }

      if (key==283)
      { return 0; }
     if ( (x1-px)*(x1-px)+(y1-py)*(y1-py)<=7 )
     {if (key==4209 || key==4177)
      { k1=1; }
      if (key==4471 || key==4439)
      { k1=2; }
      if (key==4709 || key==4677)
      { k1=3; }
      if (key==7777 || key==7745)
      { k1=4; }
      if (key==8292 || key==8260)
      { k1=5; }
      if (key==11386 || key==11354)
      { k1=6; }
      if (key==11640 || key==11608)
      { k1=7; }
      if (key==11875 || key==11843)
      { k1=8; }
     }
    }

    if (x1<=5)
    { if (k1==1)
      { k1=3; }

      if (k1==4)
      { k1=5; }

      if (k1==6)
      { k1=8; }
     }

    if (x1>=X-5)
    { if (k1==3)
      { k1=1; }

      if (k1==5)
      { k1=4; }

      if (k1==8)
      { k1=6; }
     }

    if (y1<=5)
    { if (k1==1)
      { k1=6; }

      if (k1==2)
      { k1=7; }

      if (k1==3)
      { k1=8; }
     }

    if (y1>=(Y/2)-5)
    { if (k1==6)
      { k1=1; }

      if (k1==7)
      { k1=2; }

      if (k1==8)
      { k1=3; }
     }

      pass1(k1);

      if ( (x1-px)*(x1-px)+(y1-py)*(y1-py)<=7*7 && k1==0)
      { x1=px; y1=py; }

      if (t==42)
      { t1=5; x1=px; y1=py; k1=0; t=0; }

      setcolor(YELLOW);
      setfillstyle(SOLID_FILL,YELLOW);
      circle(px,py,7);
      floodfill(px,py,YELLOW);
      setcolor(LIGHTGREEN);
      setfillstyle(11,LIGHTGREEN);
      circle(x1,y1,5);
      floodfill(x1,y1,LIGHTGREEN);

      delay(175);
      cleardevice();

      t1++;
   }
  cleardevice();
  return 0;
}


void lose()
{ randomize();

  int i,A[7]={3,7,9,10,11,14,15};

   for (i=0;i<=7;i++)
   { setbkcolor(A[i]);
     setcolor(RED);
     settextstyle(4,0,7);
     outtextxy(225,150,"YOU");
     setcolor(RED);
     settextstyle(0,0,7);
     outtextxy(50,250,"LOSE(R)!!!");
     delay(1000);
   }
   exit(0);
}

void draw()
{ randomize();

  int i,A[7]={3,7,9,10,11,14,15};

   for (i=0;i<=7;i++)
   { setbkcolor(A[i]);
     setcolor(RED);
     settextstyle(0,0,7);
     outtextxy(200,200,"DRAW");
     delay(1000);
   }
   exit(0);
}

void win()
{ randomize();

  int i1,j1,x1,y1,a1,b1,c1;
  x1=getmaxx();
  y1=getmaxy();

  for (i1=0;i1<=10;i1++)
  { setbkcolor(random(16));

    for (j1=1;j1<=2000;j1++)
     { a1=random(x1);b1=random(y1);
       c1=random(16);
       setcolor(c1);
       circle(a1,b1,3);
       setfillstyle(1,c1);
       floodfill(a1,b1,c1);
     }
      setcolor(BLUE);
      settextstyle(0,0,11);
      outtextxy(150,200,"WIN");
  delay(100);
   //cleardevice();
  }
  exit(0);
}


int changeform()
{ cleardevice();
  setbkcolor(LIGHTGREEN);
  int key=0;
  while (bioskey(1)==0)
  {
    key=bioskey(0);
    if (key==19712)
    { cf++;
      cleardevice(); }
    if (key==19200)
    { cf--;
      if (cf<0)
      { cf=3-cf; }
      cleardevice(); }
    cf=cf%4;
    if (key==7181)
    { cleardevice();
      return 0;
    }
    for (int i=0;i<9;i++)
    { gotoxy(2,2);
      cout<<(cf+1);
      setcolor(WHITE);
      rectangle(1,1,X-1,Y-1);
      rectangle(0,0,X,Y);
      setfillstyle(7,WHITE);
      rectangle(0,100,10,Y-100);
      floodfill(5,Y/2,WHITE);
      rectangle(X-0,100,X-10,Y-100);
      floodfill(X-5,Y/2,WHITE);
      line (X/2,0,X/2,Y);
      circle(X/2,Y/2,100);
      rectangle(0,50,100,Y-50);
      ellipse(100,Y/2,-90,90,50,75);
      //arc(0,Y/2,-90,90,218);

      rectangle(X-0,50,X-100,Y-50);
      ellipse(X-100,Y/2,90,-90,50,75);

      setcolor(WHITE);
      circle(frmtn[cf].xc[i],frmtn[cf].yc[i],7);
      setfillstyle(SOLID_FILL,WHITE);
      floodfill(frmtn[cf].xc[i],frmtn[cf].yc[i],WHITE);
      setcolor(BLUE);
      circle(frmtn[cf].a1[i],frmtn[cf].b1[i],7);
      setfillstyle(11,BLUE);
      floodfill(frmtn[cf].a1[i],frmtn[cf].b1[i],BLUE);
    }
  }
  return 1;
}

void goal(int g,int pos,int minus)
{
 if(g==0)
 { outtextxy(pos-minus,15,"0"); }
 if(g==1)
 { outtextxy(pos-minus,15,"1"); }

 if(g==2)
 { outtextxy(pos-minus,15,"2"); }

 if(g==3)
 { outtextxy(pos-minus,15,"3"); }

 if(g==4)
 { outtextxy(pos-minus,15,"4"); }

 if(g==5)
 { outtextxy(pos-minus,15,"5"); }

 if(g==6)
 { outtextxy(pos-minus,15,"6"); }

 if(g==7)
 { outtextxy(pos-minus,15,"7"); }

 if(g==8)
 { outtextxy(pos-minus,15,"8"); }

 if(g==9)
 { outtextxy(pos-minus,15,"9"); }

}

int ai_shoot(int ai)
{
  class shoot
  { public:
    double dist;
    int ind,pk;
  }S[5],temp;

  int i,j,ret;

   S[0].ind=frmtn[0].fx[ai]-frmtn[0].fy[ai];             //135
   S[1].ind=X-640+frmtn[0].fy[ai]+frmtn[0].fx[ai];       //45
   S[2].ind=frmtn[0].fy[ai];                             //0

   S[3].ind=X-640+frmtn[0].fy[ai]-frmtn[0].fx[ai];       //135 R
   S[4].ind=frmtn[0].fy[ai]+frmtn[0].fx[ai]-640+X-Y;     //45 R

   S[0].pk=1;
   S[1].pk=6;
   S[2].pk=4;
   S[3].pk=1;
   S[4].pk=6;

  S[0].dist=sqrt(pow((frmtn[0].py[1]-S[0].ind),2));
  S[1].dist=sqrt(pow((frmtn[0].py[1]-S[1].ind),2));
  S[2].dist=sqrt(pow((frmtn[0].py[1]-S[2].ind),2));

  S[3].dist=sqrt(pow((frmtn[0].py[1]-S[3].ind),2));
  S[4].dist=sqrt(pow((frmtn[0].py[1]-S[4].ind),2));

  for (j=0;j<5;j++)
  { for (i=0;i<4;i++)
    { if (S[i].dist<=S[i+1].dist)
      { temp=S[i];
	S[i]=S[i+1];
	S[i+1]=temp;
      }
    }
  }

  ret=42;
  for (i=0;i<5;i++)
  { if (S[i].ind<=Y-110 && S[i].ind>=110)
    { ret=i; break; }
  }

  s_ai++;

  if (ret==42)
  { aI=0;
    return 0;
  }

  else
  { aI=1;
    ret=S[ret].pk;
    return ret;
  }
}

int ai_pass(int ai, int X)  //D= (-2x1+2mc-2my1)^2 - 4*(1+m*m)(x1*x1+c*c+y1*y1-r*r-2mcy) for y=mx+c and (x-x1)^2+(y-y1)^2=r*r
{
  int p,r=0,max=0,w,i,j,a,A[8]={0,0,0,0,0,0,0,0};

  for (w=1;w<=8;w++)
   { if (w==1 || w==8)   //i=frmtn[0].fy[ai] ==> a=0,b=1,c=-frmtn[0].fy[ai]
     { for (a=0;a<9;a++)
       { if ( (frmtn[0].py[a]-frmtn[0].fy[ai])*(frmtn[0].py[a]-frmtn[0].fy[ai])<=(pass_rp*pass_rp) )
	 { if (frmtn[0].px[a]<=frmtn[0].fx[ai])
	   { A[0]--; }
	   else
	   { A[7]--; }
	 }
       }
       for (a=0;a<9;a++)
       { if ( (frmtn[0].fy[a]-frmtn[0].fy[ai])*(frmtn[0].fy[a]-frmtn[0].fy[ai])<=(pass_rf*pass_rf) && a!=ai )
	 {
	   if (frmtn[0].fx[a]<=frmtn[0].fx[ai])
	   { A[0]+=5; }
	   else
	   { A[7]+=5; }
	 }
       }
     }

     if (w==4 || w==5)   //j=frmtn[0].fx[ai] ==> a=1,b=0,c=-frmtn[0].fx[ai]
     { for (a=0;a<9;a++)
       { if ( (frmtn[0].px[a]-frmtn[0].fx[ai])*(frmtn[0].px[a]-frmtn[0].fx[ai])<=(pass_rp*pass_rp) )
	 {
	   if (frmtn[0].py[a]<frmtn[0].fy[ai])
	   { A[4]--; }
	   else
	   { A[3]--; }
	 }
       }
       for (a=0;a<9;a++)
       { if ( (frmtn[0].fx[a]-frmtn[0].fx[ai])*(frmtn[0].fx[a]-frmtn[0].fx[ai])<=(pass_rf*pass_rf) && a!=ai )
	 {
	   if (frmtn[0].fy[a]<=frmtn[0].fy[ai])
	   { A[4]+=5; }
	   else
	   { A[3]+=5; }

	 }
       }
     }

     if (w==3 || w==6) //i+frmtn[0].fy[ai]=j+frmtn[0].fx[ai] ==> a=1,b=-1,c=frmtn[0].fy[ai]-frmtn[0].fx[ai]
     { for (a=0;a<9;a++)
       { if ( (frmtn[0].py[a]-frmtn[0].px[a]-frmtn[0].fy[ai]+frmtn[0].fx[ai])*(frmtn[0].py[a]-frmtn[0].px[a]-frmtn[0].fy[ai]+frmtn[0].fx[ai])<=2*(pass_rp*pass_rp) )
	 {
	   if (frmtn[0].px[a]<=frmtn[0].fx[ai])
	   { A[2]--; }
	   else
	   { A[5]--; }
	 }
	 if ( (-frmtn[0].py[a]+frmtn[0].px[a]+(j+X+frmtn[0].fx[ai]+frmtn[0].fy[ai]-640))*(-frmtn[0].py[a]+frmtn[0].px[a]+(j+X+frmtn[0].fx[ai]+frmtn[0].fy[ai]-640))<=2*(pass_rp*pass_rp) )
	 {
	   if (frmtn[0].px[a]<=X+frmtn[0].fx[ai]+frmtn[0].fy[ai]-640)
	   { A[2]--; }                          //j=X+frmtn[0].fx[ai]+frmtn[0].fy[ai]-640
	   else                                 //i=0
	   { A[5]--; }                          //i=j+X+frmtn[0].fx[ai]+frmtn[0].fy[ai]-640
	 }
       }
       for (a=0;a<9;a++)
       { if ( (frmtn[0].fx[a]-frmtn[0].fy[a]+frmtn[0].fy[ai]-frmtn[0].fx[ai])*(frmtn[0].fx[a]-frmtn[0].fy[a]+frmtn[0].fy[ai]-frmtn[0].fx[ai])<=2*(pass_rf*pass_rf) && a!=ai)
	 {
	   if (frmtn[0].fx[a]<=X+frmtn[0].fx[ai]+frmtn[0].fy[ai]-640)
	   { A[2]+=5; }
	   else
	   { A[5]+=5; }
	 }
	 if ( (-frmtn[0].fy[a]+frmtn[0].fx[a]+(j+X+frmtn[0].fx[ai]+frmtn[0].fy[ai]-640))*(-frmtn[0].fy[a]+frmtn[0].fx[a]+(j+X+frmtn[0].fx[ai]+frmtn[0].fy[ai]-640))<=2*(pass_rf*pass_rf) )
	 {
	   if (frmtn[0].px[a]<=frmtn[0].fx[ai])
	   { A[2]+=5; }                          //j=X+frmtn[0].fx[ai]+frmtn[0].fy[ai]-640
	   else                                  //i=0
	   { A[5]+=5; }                          //i=j+X+frmtn[0].fx[ai]+frmtn[0].fy[ai]-640
	 }

       }
     }

     if (w==2 || w==7) //i+j+640=X+frmtn[0].fx[ai]+frmtn[0].fy[ai] ==> a=1,b=1,c=640-(X+frmtn[0].fx[ai]+frmtn[0].fy[ai])
     { for (a=0;a<9;a++)
       { if ( (frmtn[0].px[a]+frmtn[0].py[a]+640-(X+frmtn[0].fx[ai]+frmtn[0].fy[ai]))*(frmtn[0].px[a]+frmtn[0].py[a]+640-(X+frmtn[0].fx[ai]+frmtn[0].fy[ai]))<=2*(pass_rp*pass_rp) )
	 {
	   if (frmtn[0].py[a]<frmtn[0].fy[ai])                       //frmtn[0].fy[ai]-frmtn[0].fx[ai]+X=j
	   { A[1]--; }
	   else
	   { A[6]--; }
	 }
	 if ( (frmtn[0].px[a]+frmtn[0].py[a]+640-(X+frmtn[0].fy[ai]-frmtn[0].fx[ai]+Y))*(frmtn[0].px[a]+frmtn[0].py[a]+640-(X+Y+frmtn[0].fy[ai]-frmtn[0].fx[ai]))<=2*pass_rp*pass_rp )
	 {  if (frmtn[0].py[a]<0)                       //frmtn[0].fy[ai]-frmtn[0].fx[ai]+X=j
	   { A[1]--; }
	   else
	   { A[6]--; }
	 }
       }
       for (a=0;a<9;a++)
       { if ( (frmtn[0].fx[a]+frmtn[0].fy[a]+640-(X+frmtn[0].fx[ai]+frmtn[0].fy[ai]))*(frmtn[0].fx[a]+frmtn[0].fy[a]+640-(X+frmtn[0].fx[ai]+frmtn[0].fy[ai]))<=2*(pass_rf*pass_rf) && a!=ai)
	 {
	   if (frmtn[0].fy[a]<frmtn[0].fy[ai])
	   { A[1]+=5; }
	   else
	   { A[6]+=5; }

	 }
	  if ( (frmtn[0].fx[a]+frmtn[0].fy[a]+640-(X+frmtn[0].fy[ai]-frmtn[0].fx[ai]+Y))*(frmtn[0].fx[a]+frmtn[0].fy[a]+640-(X+Y+frmtn[0].fy[ai]-frmtn[0].fx[ai]))<=2*pass_rp*pass_rp )
	 {  if (frmtn[0].fy[a]<0)                       //frmtn[0].fy[ai]-frmtn[0].fx[ai]+X=j
	   { A[1]+=5; }
	   else
	   { A[6]+=5; }
	 }

       }
     }
   }

  for (i=0;i<8;i++)
  { if (max<=A[i])
    { max=A[i]; }
  }

  for (i=0;i<8;i++)
  { if (A[i]==max && A[i]!=0)  //return 0 if no value found
    { r=i+1; break; }
  }

  if (r==2)
  { p=1; }

  if (r==5)
  { p=2; }

  if (r==6)
  { p=3; }

  if (r==1)
  { p=4; }

  if (r==8)
  { p=5; }

  if (r==3)
  { p=6; }

  if (r==4)
  { p=7; }

  if (r==7)
  { p=8; }

  if (r==0)
  { p=0; }
 if (ai!=1)
 { return p; }
 else
 { if (p==3 || p==5 || p==8)
   { return 0; }
   else
   { return p; }
 }


}

class point
{ public:
  int C,pt;
  point()
  { C=0;pt=0; }

  ~point()
  { ; }

} p[380];        //479-100

void choose(int i1)
{ int i,j,gy1;

for (i=100;i<Y-100;i++)
{ if (frmtn[0].py[1]!=i)
  { p[i-100].C=(frmtn[0].py[1]-i)/(frmtn[0].fy[i1]-i); }
  else
  { p[i-100].C=0; }
  p[i-100].pt=i;
}

int max;

for (i=0;i<Y-200;i++)
{ if (max<=p[i].C)
  { max=p[i].C; }
}

for (i=0;i<Y-200;i++)
{ if (max==p[i].C)
  { gy1=i; break; }
}

gy=p[gy1].pt;

}


void ai_move1(int ai)
{ double th,a,b,d,s,c;

  if (gx!=frmtn[0].fx[ai])
  {
    a=gy-frmtn[0].fy[ai]; b=gx-frmtn[0].fx[ai]; c=a/b;
    th=atan(c);
  }

  if (gx==frmtn[0].fx[ai])
  { th=PI/2; }

  if (gx<frmtn[0].fx[ai])
  { th=th-PI; }

  s=sin(th);
  c=cos(th);

 if ( ((gx-frmtn[0].fx[ai])*(gx-frmtn[0].fx[ai]))+((gy-frmtn[0].fy[ai])*(gy-frmtn[0].fy[ai]))<=6400 )
 {
  vx1+=3*c/2;
  vy1+=3*s/2;
 }
 else
 {
  vx1+=c;
  vy1+=s;
 }
}

void ai_move2(int i, int ai)
{ double th,a,b,d,s,c;

  if (frmtn[0].px[i]!=frmtn[0].fx[ai])
  {
    a=(frmtn[0].py[i]-frmtn[0].fy[ai]); b=(frmtn[0].px[i]-frmtn[0].fx[ai]); c=a/b;
    th=atan(c);
  }

  if (frmtn[0].px[i]==frmtn[0].fx[ai])
  { th=PI/2; }

  if (frmtn[0].px[i]<frmtn[0].fx[ai])
  { th=th-PI; }

  s=sin(th);
  c=cos(th);

if ( (((frmtn[0].px[i]-frmtn[0].fx[ai])*(frmtn[0].px[i]-frmtn[0].fx[ai]))+((frmtn[0].py[i]-frmtn[0].fy[ai])*(frmtn[0].py[i]-frmtn[0].fy[ai])))<=3600 && frmtn[0].px[i]<=frmtn[0].fx[ai])
 {

  vx[i]-=3*c/4;
  vy[i]-=3*s/4;
 }
 else
 {
  vx[i]-=c/2;
  vy[i]-=s/2;
 }


}

void ai_move(int ai)
{ int i;

   ai_move1(ai);

 for (i=0;i<9;i++)
 { if (Arr[i]!=42)
   { int a=Arr[i];
     ai_move2(a,ai);
   }
 }

   frmtn[0].fx[ai]+=(vx1+vx[0]+vx[1]+vx[2]+vx[3]+vx[4]+vx[5]+vx[6]+vx[7]+vx[8]);
   frmtn[0].fy[ai]+=(vy1+vy[0]+vy[1]+vy[2]+vy[3]+vy[4]+vy[5]+vy[6]+vy[7]+vy[8]);

   vx1=0; vy1=0;

 for (i=0;i<9;i++)
 { vx[i]=0; vy[i]=0; }

}

void pass (int k)
{ float a=5.5;
  if (k==1)
  { x-=a; y-=a; }
  if (k==2)
  { y-=a; }
  if (k==3)
  { x+=a; y-=a; }
  if (k==4)
  { x-=a; }
  if (k==5)
  { x+=a; }
  if (k==6)
  { x-=a; y+=a; }
  if (k==7)
  { y+=a; }
  if (k==8)
  { x+=a; y+=a; }
}

class plyr
{ public:
  double D;
  int p;
}P[9];

int decide()
{ int i,j,a;
  plyr temp;

  for (i=0;i<9;i++)
  { P[i].D=(((x-frmtn[0].px[i])*(x-frmtn[0].px[i]))+((y-frmtn[0].py[i])*(y-frmtn[0].py[i]))); }

  for (i=0;i<9;i++)
  { P[i].p=i; }

  for (i=0;i<9;i++)                      //better min value algorithm
  { for (j=0;j<8;j++)
    { if (P[j].D>P[j+1].D)
      { temp=P[j+1];
	P[j+1]=P[j];
	P[j]=temp;
      }
    }
  }
  for (i=0;i<9;i++)
  { if ( P[0].p==i )
    { a=i; break; }
  }

  return a;
}

void check(int i, int j)
{ int a=2;
  if ( (((frmtn[0].fx[i]-frmtn[0].fx[j])*(frmtn[0].fx[i]-frmtn[0].fx[j]))+((frmtn[0].fy[i]-frmtn[0].fy[j])*(frmtn[0].fy[i]-frmtn[0].fy[j])))<=4*(pr*pr) )
  { if (frmtn[0].fx[i]>=frmtn[0].fx[j] && frmtn[0].fy[i]>=frmtn[0].fy[j])
    { frmtn[0].fx[i]+=a; frmtn[0].fy[i]+=a; frmtn[0].fx[j]-=a; frmtn[0].fy[j]-=a;}

    if (frmtn[0].fx[i]>=frmtn[0].fx[j] && frmtn[0].fy[i]<=frmtn[0].fy[j])
    { frmtn[0].fx[i]+=a; frmtn[0].fy[i]-=a; frmtn[0].fx[j]-=a; frmtn[0].fy[j]+=a;}

    if (frmtn[0].fx[i]<=frmtn[0].fx[j] && frmtn[0].fy[i]>=frmtn[0].fy[j])
    { frmtn[0].fx[i]-=a; frmtn[0].fy[i]+=a; frmtn[0].fx[j]+=a; frmtn[0].fy[j]-=a;}

    if (frmtn[0].fx[i]<=frmtn[0].fx[j] && frmtn[0].fy[i]<=frmtn[0].fy[j])
    { frmtn[0].fx[i]-=a; frmtn[0].fy[i]-=a; frmtn[0].fx[j]+=a; frmtn[0].fy[j]+=a;}
  }

  if ( (((frmtn[0].px[i]-frmtn[0].px[j])*(frmtn[0].px[i]-frmtn[0].px[j]))+((frmtn[0].py[i]-frmtn[0].py[j])*(frmtn[0].py[i]-frmtn[0].py[j])))<=4*(pr*pr) )
  {
    if (frmtn[0].px[i]>=frmtn[0].px[j] && frmtn[0].py[i]>=frmtn[0].py[j])
    { frmtn[0].px[i]+=a; frmtn[0].py[i]+=a; frmtn[0].px[j]-=a; frmtn[0].py[j]-=a;}

    if (frmtn[0].px[i]>=frmtn[0].px[j] && frmtn[0].py[i]<=frmtn[0].py[j])
    { frmtn[0].px[i]+=a; frmtn[0].py[i]-=a; frmtn[0].px[j]-=a; frmtn[0].py[j]+=a;}

    if (frmtn[0].px[i]<=frmtn[0].px[j] && frmtn[0].py[i]>=frmtn[0].py[j])
    { frmtn[0].px[i]-=a; frmtn[0].py[i]+=a; frmtn[0].px[j]+=a; frmtn[0].py[j]-=a;}

    if (frmtn[0].px[i]<=frmtn[0].px[j] && frmtn[0].py[i]<=frmtn[0].py[j])
    { frmtn[0].px[i]-=a; frmtn[0].py[i]-=a; frmtn[0].px[j]+=a; frmtn[0].py[j]+=a;}
  }
}

void check_t(int i)
{ int a,b=15;
  for (a=0;a<9;a++)
  { if ( (((frmtn[0].px[i]-frmtn[0].fx[a])*(frmtn[0].px[i]-frmtn[0].fx[a]))+((frmtn[0].py[i]-frmtn[0].fy[a])*(frmtn[0].py[i]-frmtn[0].fy[a])))<=4*(pr*pr) )
   {
    if (frmtn[0].px[i]>=frmtn[0].fx[a] && frmtn[0].py[i]>=frmtn[0].fy[a])
    { frmtn[0].px[i]+=b; frmtn[0].py[i]+=b; frmtn[0].fx[a]-=3*b/2; frmtn[0].fy[a]-=3*b/2;}

    if (frmtn[0].px[i]>=frmtn[0].fx[a] && frmtn[0].py[i]<=frmtn[0].fy[a])
    { frmtn[0].px[i]+=b; frmtn[0].py[i]-=b; frmtn[0].fx[a]-=3*b/2; frmtn[0].fy[a]+=3*b/2;}

    if (frmtn[0].px[i]<=frmtn[0].fx[a] && frmtn[0].py[i]>=frmtn[0].fy[a])
    { frmtn[0].px[i]-=b; frmtn[0].py[i]+=b; frmtn[0].fx[a]+=3*b/2; frmtn[0].fy[a]-=3*b/2;}

    if (frmtn[0].px[i]<=frmtn[0].fx[a] && frmtn[0].py[i]<=frmtn[0].fy[a])
    { frmtn[0].px[i]-=b; frmtn[0].py[i]-=b; frmtn[0].fx[a]+=3*b/2; frmtn[0].fy[a]+=3*b/2;}
   }
  }
}

void move(int i)
{ double th,a,b,d,s,c;
 if (i==1)
 {
  if (X-30!=frmtn[0].fx[i])
  { a=(y-frmtn[0].fy[i]); b=(X-30-frmtn[0].fx[i]); c=a/b;
    th=atan(c);
  }

  if (X-30==frmtn[0].fx[i])
  { th=3.14159/2; }

  if (X-30<frmtn[0].fx[i])
  { th=th-PI; }

 }

 else
 {
  if (x!=frmtn[0].fx[i])
  { a=(y-frmtn[0].fy[i]); b=(x-frmtn[0].fx[i]); c=a/b;
    th=atan(c);
  }
  if (x==frmtn[0].fx[i])
  { th=3.14159/2; }

  if (x<frmtn[0].fx[i])
  { th=th-PI; }

 }
  s=sin(th);
  c=cos(th);
 if (i==1)
 { frmtn[0].fx[i]+=5.25*c;
   frmtn[0].fy[i]+=5.25*s;
 }
 else
 { frmtn[0].fx[i]+=3*c;
   frmtn[0].fy[i]+=3*s;
 }

}

void move1(int i)
{ double th,a,b,d,s,c;

  if (frmtn[cf].a1[i]!=frmtn[0].fx[i])
  {
    a=(frmtn[cf].b1[i]-frmtn[0].fy[i]); b=(frmtn[cf].a1[i]-frmtn[0].fx[i]); c=a/b;
    th=atan(c);
  }

  if (frmtn[cf].a1[i]==frmtn[0].fx[i])
  { th=3.14159/2; }

  if (frmtn[cf].a1[i]<frmtn[0].fx[i])
  { th=th-PI; }

  s=sin(th);
  c=cos(th);

  frmtn[0].fx[i]+=3*c;
  frmtn[0].fy[i]+=3*s;

}

 void p_move(int i)
{ double th,a,b,d,s,c;

  if (frmtn[cf].xc[i]!=frmtn[0].px[i])
  {
    a=(frmtn[cf].yc[i]-frmtn[0].py[i]); b=(frmtn[cf].xc[i]-frmtn[0].px[i]); c=a/b;
    th=atan(c);
  }

  if (frmtn[cf].xc[i]==frmtn[0].px[i])
  { th=3.14159/2; }

  s=sin(th);
  c=cos(th);

 if (frmtn[cf].xc[i]<frmtn[0].px[i])
 { frmtn[0].px[i]-=2*c;
   frmtn[0].py[i]-=2*s;
 }

 else
 { frmtn[0].px[i]+=2*c;
   frmtn[0].py[i]+=2*s;
 }
}

void print(int i)
{
  setcolor(WHITE);
  rectangle(1,1,X-1,Y-1);
  rectangle(0,0,X,Y);
  setfillstyle(7,WHITE);
  rectangle(0,100,10,Y-100);
  floodfill(5,Y/2,WHITE);
  rectangle(X-0,100,X-10,Y-100);
  floodfill(X-5,Y/2,WHITE);
  line (X/2,0,X/2,Y);
  circle(X/2,Y/2,100);
  rectangle(0,50,100,Y-50);
  ellipse(100,Y/2,-90,90,50,75);
  //arc(0,Y/2,-90,90,218);

  rectangle(X-0,50,X-100,Y-50);
  ellipse(X-100,Y/2,90,-90,50,75);

  //setcolor(GREEN);
  //setfillstyle(12,GREEN);
  //floodfill(2,2,GREEN);

  int a,j;
// setcolor(RED);             //HIDE
// circle(x,y,r);             //HIDE
// circle(frmtn[0].fx[1],frmtn[0].fy[1],125);           //HIDE(GK)

 if (aI==0)
 { j=decide(); }
 if (aI==1)
 { j=1; }

 int abc=15;

  for (a=0;a<9;a++)
  { abc=15;

    if (a==j)
    { abc=14;}

      setcolor(abc);
      circle(frmtn[0].px[a],frmtn[0].py[a],pr);
      setfillstyle(1,abc);
      floodfill(frmtn[0].px[a],frmtn[0].py[a],abc);
  }
  setcolor(BLUE);
  circle(frmtn[0].fx[i],frmtn[0].fy[i],pr);
  setfillstyle(11,BLUE);
  floodfill(frmtn[0].fx[i],frmtn[0].fy[i],BLUE);

  setcolor(RED);
  circle(x,y,br);
 // circle(X-30,y,br);
  setfillstyle(CLOSE_DOT_FILL,RED);
  floodfill(x,y,RED);

  setcolor(WHITE);
  rectangle(50,5,75,30);
  setfillstyle(SOLID_FILL,WHITE);
  floodfill(65,15,WHITE);
  setcolor(BLUE);
  rectangle(125,5,150,30);
  setfillstyle(SOLID_FILL,BLUE);
  floodfill(135,15,BLUE);
  setcolor(LIGHTGRAY);
  rectangle(2,4,151,31);
  rectangle(1,3,152,32);
  rectangle(3,5,150,30);
  setfillstyle(SOLID_FILL,LIGHTGRAY);
  floodfill(4,6,LIGHTGRAY);

  setcolor(WHITE);
  settextstyle(0,0,1);
  outtextxy(5,15," PLYR");
  setcolor(BLUE);
  outtextxy(80,15," COMP");

}

int pause()
{  int key12=0;
   A:
   setbkcolor(8);
   setcolor(GREEN);
   rectangle(1,1,60,60);
   settextstyle(0,0,2);
   outtextxy(8,10,"ESC");
   settextstyle(11,0,1);
   outtextxy(42,32,"to");
   outtextxy(11,50,"resume");

   rectangle(X-1,1,X-60,60);
   settextstyle(0,0,2);
   outtextxy(X-52,10,"BKS");
   settextstyle(11,0,1);
   outtextxy(X-20,32,"to");
   outtextxy(X-35,50,"exit");

   setcolor(YELLOW);
   settextstyle(0,0,5);
   outtextxy(121,10,"PAUSE MENU");
   line (121,53,X-121,53);
   line (115,55,X-115,55);

//   rectangle (25,150,X-25,175);
  // delay(1000);

   setcolor(CYAN);
   settextstyle(0,0,3);
   outtextxy(177,115,"POSSESSION");
   setcolor(WHITE);
   rectangle (25,150,(X-50)*(p__pos/100)-1,175);
   setfillstyle(SOLID_FILL,WHITE);
   floodfill((25+(X-50)*(p__pos/100)-1)/2,160,WHITE);
   setcolor(BLUE);
   rectangle ((X-50)*(p__pos/100)+1,150,X-25,175);
   setfillstyle(SOLID_FILL,BLUE);
   floodfill(((X-50)*(p__pos/100)+1+X-25)/2,160,BLUE);

   double b;
   b=(X-50)*(s_p/(s_p+s_ai));

   setcolor(CYAN);
   settextstyle(0,0,3);
   outtextxy(163,215,"   SHOTS  ");
   setcolor(WHITE);
   rectangle (25,250,b-1,275);
   setfillstyle(SOLID_FILL,WHITE);
   floodfill((25+b-1)/2,260,WHITE);
   setcolor(BLUE);
   rectangle (b+1,250,X-25,275);
   setfillstyle(SOLID_FILL,BLUE);
   floodfill((b+1+X-25)/2,260,BLUE);

   setcolor(CYAN);
   settextstyle(0,0,4);
   outtextxy(75,374,"CHANGE FORMATION");
   settextstyle(0,0,2);
   outtextxy(190,Y-75,"press spacebar");

  // delay(1000);

  while (bioskey(1)==0)
  {
    key12=bioskey(0);

   if (key12==283)
   { setbkcolor(LIGHTGREEN);
     return 0;
   }

   else if (key12==3592)
   { cleardevice();
     if (g_p==g_ai)
     {
      obj.input();
      getch();
      draw();
     }
     if (g_p>g_ai)
     {
      obj.input();
      getch();
      win();
     }
     if (g_p<g_ai)
     {
      obj.input();
      getch();
      lose();
     }
   }

   else if (key12==14624)
   { changeform(); goto A;}

   else
   goto A;
  }
  setbkcolor(LIGHTGREEN);

  return 2;
}


void main()
{ randomize();
  clrscr();

  int n=9,i,j,z;

  for (i=0;i<4;i++)
  { frmtn[i].change(i); }

  int gd=DETECT,gm;
  initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");

  menu();

  setbkcolor(LIGHTGREEN);

  int key,t,t1=5;

  int ai_f1=0,ai_f=0,qq=42,xx=0,a,b=0,c=42,flag=0,flag1=0,flag2=0,p_flag=0,k=0,s=0;

  for (t=0;t<t1;t++)
  {  int m=0;

    if (aI==0)
    { a=decide(); }
    if (aI==1)
    { a=1; }

     while (b==0)
     { c=a; b=b+1; }

     flag1=0;

     for (i=0;i<9;i++)
     { if ( (((x-frmtn[0].px[i])*(x-frmtn[0].px[i]))+((y-frmtn[0].py[i])*(y-frmtn[0].py[i]))<=(br+pr)*(br+pr)) && x!=frmtn[0].px[c] && y!=frmtn[0].py[c] )
       { flag1=1; break; }
     }
     if (flag1==1)
     { b=0; }

     float gkm=1;

   p__pos=100*(p_pos)/(p_pos+ai_pos);
   ai__pos=100-p__pos;
 /*
   gotoxy(8,3);
   cout<<g_p;
   gotoxy(8,4);
   cout<<s_p;
   gotoxy(8,5);
   cout<<int(p__pos)<<"%";
   gotoxy(18,3);
   cout<<g_ai;
   gotoxy(18,4);
   cout<<s_ai;
   gotoxy(18,5);
   cout<<int(ai__pos)<<"%";
 */

    while (bioskey(1)!=0)
    {
      gkm=1;
      if (a==1)
      { gkm=1.5; }

      key=bioskey(0);
      if (key==18432)
      { frmtn[0].py[a]-=gkm; }
      if (key==20480)
      { frmtn[0].py[a]+=gkm; }
      if (key==19712)
      { frmtn[0].px[a]+=gkm; }
      if (key==19200)
      { frmtn[0].px[a]-=gkm; }
      if (key==283)
      { pause(); }
      if (key==3592)
      { cleardevice();
	if (g_p==g_ai)
	{ obj.input();
          getch();
	  draw();
        }
	if (g_p>g_ai)
	{ obj.input();
          getch();
	  win();
        }
	if (g_p<g_ai)
	{ obj.input();
          getch();
	  lose();
        }
      }
      if (key==14624)
      { tg=tg+1;
	tg=tg%2;
      }

      if ( ((x-frmtn[0].px[c])*(x-frmtn[0].px[c]))+((y-frmtn[0].py[c])*(y-frmtn[0].py[c]))<=((pr+br)*(pr+br)) )
      { flag=1; }
      if ( ((x-frmtn[0].px[c])*(x-frmtn[0].px[c]))+((y-frmtn[0].py[c])*(y-frmtn[0].py[c]))>((pr+br)*(pr+br)) )
      { flag=0; }

      if (flag==1)
      { if (key==4209 || key==4177)
	{ k=1; }
	if (key==4471 || key==4439)
	{ k=2; }
	if (key==4709 || key==4677)
	{ k=3; }
	if (key==7777 || key==7745)
	{ k=4; }
	if (key==8292 || key==8260)
	{ k=5; }
	if (key==11386 || key==11354)
	{ k=6; }
	if (key==11640 || key==11608)
	{ k=7; }
	if (key==11875 || key==11843)
	{ k=8; }
       }
    }

   if (frmtn[0].px[a]>=X)
   { frmtn[0].px[a]=X-10; }
   if (frmtn[0].px[a]<=0)
   { frmtn[0].px[a]=10; }
   if (frmtn[0].py[a]>=Y)
   { frmtn[0].py[a]=Y-10; }
   if (frmtn[0].py[a]<=0)
   { frmtn[0].py[a]=10; }

   if ( x>=X )
   { x=frmtn[0].fx[1];
     y=frmtn[0].fy[1];
     k=0;
     s=0;
     s_p++;
     }
     if (y<=Y-100 && y>100 && x>=X-5)
     { g_p+=1; }

   if ( x<=0 )
   { x=frmtn[0].px[1];
     y=frmtn[0].py[1];
     k=0;
     s=0;
     aI=0;
     c=42;
   }
     if (y<=Y-100 && y>100 && x<=7)
     { g_ai+=1; }

   if (y>=Y || y<=0)
   { if (k==1)
     { k=6; goto M2; }
     if (k==6)
     { k=1; goto M2; }
     if (k==2)
     { k=7; goto M2; }
     if (k==7)
     { k=2; goto M2; }
     if (k==3)
     { k=8; goto M2; }
     if (k==8)
     { k=3; goto M2; }
   }
   M2:
   if (y>=Y || y<=0)
   { if (s==1)
     { s=6; goto M1; }
     if (s==6)
     { s=1; goto M1; }
     if (s==2)
     { s=7; goto M1; }
     if (s==7)
     { s=2; goto M1; }
     if (s==3)
     { s=8; goto M1; }
     if (s==8)
     { s=3; goto M1; }
   }
   M1:


 if( ((x-frmtn[0].px[a])*(x-frmtn[0].px[a]))+((y-frmtn[0].py[a])*(y-frmtn[0].py[a]))<=(pr+br)*(pr+br) && a!=c)
 { k=0; }


 flag2=0;
 for (i=0;i<9;i++)
  { if (((x-frmtn[0].px[i])*(x-frmtn[0].px[i]))+((y-frmtn[0].py[i])*(y-frmtn[0].py[i]))>((pr+br)*(pr+br)) && i!=c && k!=0)
    { flag2=1; }
  }

  if (flag2==1)
  { pass (k); }

  for (i=0;i<9;i++)
 { if ( ( ((frmtn[cf].xc[i]-frmtn[0].px[i])*(frmtn[cf].xc[i]-frmtn[0].px[i]))+((frmtn[cf].yc[i]-frmtn[0].py[i])*(frmtn[cf].yc[i]-frmtn[0].py[i]))>=4) && i!=a && ((((x-frmtn[0].px[i])*(x-frmtn[0].px[i]))+((y-frmtn[0].py[i])*(y-frmtn[0].py[i]))>=((br+pr)*(br+pr)))) )
   { if (i==1 || tg==0)
     { p_move(i); }
   }
 }

 if( ((x-frmtn[0].px[a])*(x-frmtn[0].px[a]))+((y-frmtn[0].py[a])*(y-frmtn[0].py[a]))<=(pr+br)*(pr+br) && k==0)
   { x=frmtn[0].px[a];
     y=frmtn[0].py[a];
     p_pos++;
   }
 int ai=42;
 for (i=0;i<9;i++)
 { if( ((x-frmtn[0].fx[i])*(x-frmtn[0].fx[i]))+((y-frmtn[0].fy[i])*(y-frmtn[0].fy[i]))<=(pr+br)*(pr+br) )
   {  //m=1;
      //k=0;
      ai=i;
      break;
   }
 }
 while (xx==0)
 { qq=ai; xx++; }

 for (i=0;i<9;i++)
 { if ( (x-frmtn[0].px[i])*(x-frmtn[0].px[i])+(y-frmtn[0].py[i])*(y-frmtn[0].py[i])<=(br+pr)*(br+pr) )
   { xx=0; break; }
 }

 for (i=0;i<9;i++)
 { if ( (x-frmtn[0].fx[i])*(x-frmtn[0].fx[i])+(y-frmtn[0].fy[i])*(y-frmtn[0].fy[i])<=(br+pr)*(br+pr) && i!=qq)
   { xx=0; break; }
 }

 for (i=0;i<9;i++)
 { if( ((x-frmtn[0].fx[i])*(x-frmtn[0].fx[i]))+((y-frmtn[0].fy[i])*(y-frmtn[0].fy[i]))<=(pr+br)*(pr+br) && i!=qq && aI==0)
    { x=frmtn[0].fx[i];
      y=frmtn[0].fy[i];
      m=1;
      k=0;
      ai_pos++;
    }
    if (i==ai && s==0 && aI==0)
    { x=frmtn[0].fx[i];
      y=frmtn[0].fy[i];
      ai_pos++;
      m=1;
      k=0;
    }
 }

 choose(ai);

  for (i=0;i<9;i++)
 { Arr[i]=42; vx[i]=0; vy[i]=0; }

 for (i=0;i<9;i++)
 { if (((frmtn[0].px[i]-frmtn[0].fx[ai])*(frmtn[0].px[i]-frmtn[0].fx[ai]))+((frmtn[0].py[i]-frmtn[0].fy[ai])*(frmtn[0].py[i]-frmtn[0].fy[ai]))<=((pr+ai_r)*(pr+ai_r)) )
   Arr[i]=i;
 }


   for (i=0;i<n;i++)
   { if (frmtn[0].fx[i]>=X)
     { frmtn[0].fx[i]=X-pr; }
     if (frmtn[0].fx[i]<=0)
     { frmtn[0].fx[i]=pr; }
     if (frmtn[0].fy[i]>=Y)
     { frmtn[0].fy[i]=Y-pr; }
     if (frmtn[0].fy[i]<=0)
     { frmtn[0].fy[i]=pr; }
   }
    for (i=0;i<n;i++)
   { if (frmtn[0].px[i]>=X)
     { frmtn[0].px[i]=X-pr; }
     if (frmtn[0].px[i]<=0)
     { frmtn[0].px[i]=pr; }
     if (frmtn[0].py[i]>=Y)
     { frmtn[0].py[i]=Y-pr; }
     if (frmtn[0].py[i]<=0)
     { frmtn[0].py[i]=pr; }
   }
   p_flag=0;

   for (i=0;i<9;i++)
   { if ( (frmtn[0].px[i]-frmtn[0].fx[qq])*(frmtn[0].px[i]-frmtn[0].fx[qq]) + (frmtn[0].py[i]-frmtn[0].fy[qq])*(frmtn[0].py[i]-frmtn[0].fy[qq])<=(pass_r+pr)*(pass_r+pr) )
     { p_flag=1; break; }
   }

   if (p_flag==1 && s==0)
   {
     s=ai_pass(ai,X);
   }

   ai_f=0;
   for (i=0;i<9;i++)
   { if ( (x-frmtn[0].fx[i])*(x-frmtn[0].fx[i])+(y-frmtn[0].fy[i])*(y-frmtn[0].fy[i])<=(br+pr)*(br+pr) )
     { ai_f=1; break; }
   }

   if ( frmtn[0].fx[ai]<=218 && aI==0 && ai_f==1)
   { k=ai_shoot(ai); }

   if (aI==0)
   { pass(s); }

   if (aI!=0)
   { pass(k); }

   ai_f1=0;
   for (i=0;i<9;i++)
   { if ( (x-frmtn[0].px[i])*(x-frmtn[0].px[i])+(y-frmtn[0].py[i])*(y-frmtn[0].py[i])<=(br+pr)*(br+pr) )
     { ai_f1=1; break; }
   }

   if (x<=0 || ai_f1==1)
   { aI=0; }

   for (i=0;i<9;i++)
   { if ( (frmtn[0].px[i]-x)*(frmtn[0].px[i]-x) + (frmtn[0].py[i]-y)*(frmtn[0].py[i]-y)<=(br+pr)*(br+pr) && aI==0)
     { s=0; }
   }

   for (i=0;i<9;i++)
   { if ( (frmtn[0].fx[i]-x)*(frmtn[0].fx[i]-x) + (frmtn[0].fy[i]-y)*(frmtn[0].fy[i]-y)<=(br+pr)*(br+pr) && i!=qq && aI==0)
     { s=0; }
   }

   for (i=0;i<n;i++)
   {
    if (aI==0)
    { a=decide(); }
    if (aI==1)
    { a=1; }

      if ( ((frmtn[0].fx[i]-x)*(frmtn[0].fx[i]-x))+((frmtn[0].fy[i]-y)*(frmtn[0].fy[i]-y))>(r+br)*(r+br) && aI==0)
      { move1(i); }

      if ( ((frmtn[0].fx[i]-x)*(frmtn[0].fx[i]-x))+((frmtn[0].fy[i]-y)*(frmtn[0].fy[i]-y))<=(r+br)*(r+br) && m==0 && i!=1 && aI==0)
      {
	if (i!=ai)
	{ move(i); }
	if (i==qq && s==0)
	{ move(i); }
	if (i==qq && s!=0)
	{ move1(i); }
      }

      if ( ((frmtn[0].fx[i]-x)*(frmtn[0].fx[i]-x)+((frmtn[0].fy[i]-y)*(frmtn[0].fy[i]-y))<=(125+br)*(125+br) && m==0 && i==1 && aI==0))
      {
	if (i!=ai)
	{ move(i); }
	if (i==qq && s==0)
	{ move(i); }
	if (i==qq && s!=0)
	{ move1(i); }
      }
      if (s==0)
      { ai_move(ai); }

      check_t(i);
    if (t%5==0)
    { for (j=0;j<n;j++)
     { check(i,j); }
    }
//    if(t%2==0)
   { print(i);

   if (tg==0)
   {  setcolor(5);
      settextstyle(0,0,2);
      outtextxy(X-50,10,"ON");
      setcolor(CYAN);
      settextstyle(0,0,1);
      outtextxy(X-111,15,"TOGGLE: ");
   }
   if (tg==1)
   {  setcolor(RED);
      settextstyle(0,0,2);
      outtextxy(X-50,10,"OFF");
      setcolor(CYAN);
      settextstyle(0,0,1);
      outtextxy(X-111,15,"TOGGLE: ");
   }

   }

      minus=0;
     int g__p=g_p;
     do
     { tmp=g__p%10;
       g__p=g__p/10;
       setcolor(BLUE);
       settextstyle(0,0,1);
       goal(tmp,65,minus);
       minus+=5;
     }while(g__p>0);

     minus=0;
     int g__ai=g_ai;
     do
     { tmp1=g__ai%10;
       g__ai=g__ai/10;
       setcolor(WHITE);
       settextstyle(0,0,1);
       goal(tmp1,137,minus);
       minus+=5;
     }while(g__ai>0);

   }
//if (t%2==0)
{  delay(50);
  cleardevice();
}
    t1++;
  }
  B:
  getch();
}
