clear all
close all

scrsz = get(0,'ScreenSize');

wf=8/10;
hf=4/5;
figsize=[0 0  0.7*scrsz(4) 0.7*scrsz(4)];

%Abaque tr en fonction de xi
w0=1;
xi=0.2;

%Estimation de la courbe
a1=-(log10(300)-log10(3))/(log10(0.7)-log10(0.01));
b1=log10(3)-a1*log10(0.7);
a2=(log10(600)-log10(3))/(log10(100)-log10(0.7));
b2=log10(3)-a2*log10(0.7);
varlogxi=-2:0.01:2;
vxi=10.^(varlogxi);
% vxi=0.01:0.01:100;
% vxi=[0.01,0.7,1,10,100];
%vxi=[10]


N=[1];
D=[1/w0^2,2*xi/w0,1];
if xi<=0.7
tr=exp(log(10)*(a1*log10(xi)+b1));
else
tr=exp(log(10)*(a2*log10(xi)+b2));
end
tsimu=2*tr;
if xi<1
dt=2*pi/(100*sqrt(1-xi^2)) 
else
dt=tsimu/100;
end



R=sim('reponse_2nd_ordre','AbsTol','1e-5','MaxStep',string(dt),...
'StopTime',string(tsimu),'SaveTime','on','TimeSaveName','tp');
tp=R.get('tp');
s=R.get('simout').data(:,1);


    
figure1=figure()
axes1=axes('parent',figure1,'fontsize',20);
plot(tp,s,'b-','LineWidth',3)
grid on
% yticks([0:0.1:1.6]);
% xticks([0:0.5:5]);

set(axes1,'FontSize',16);
xlabel('temps en s','FontSize',20)
ylabel('s(t)','FontSize',20)
print('2nd_ordre','-dpng')
