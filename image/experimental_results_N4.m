
%time_safe8 = [1.6 1.1 8.3 6.9 76.1 40.1 344.8 288.8];
time_safe4 = [9.97  76.1];
time_unsafe4 = [ 8.44 40.1 119.1 4197.1];
hycomp_time_safe4 = [2.78 9.9 788];
hycomp_time_unsafe4 = [ 2.53 13.3 569.4 568.4];
dreach_time_safe4 = [2.1 4.63];
dreach_time_unsafe4 = [ 1.6 4.93];
%%%%%
mem_safe4 = [56.9 74.1];
mem_unsafe4 = [57 73.2 156.2 254.1];
hycomp_mem_safe4 = [255.2 319.1 1010.4];
hycomp_mem_unsafe4 = [255 318.2 895.4 897.1];
dreach_mem_safe4 = [ 9.8 96.7];
dreach_mem_unsafe4 = [ 2.5 119.8];
%%%%%

N = [ 4 8 16 32 ];
N_2 = [ 4 8]; 
N_3 = [ 4 8 16];
% plot runtime at k <= 8
figure
%plot(time_safe4, N, 'LineWidth',1.3); 
%plot(N,time_safe4,'-.ro',N,time_unsafe4,'-.b','LineWidth',2);
plot(N_2,time_safe4,'-.o',N,time_unsafe4,'-.s',N_3,hycomp_time_safe4,'-+',N,hycomp_time_unsafe4,'-d',...
    N_2,dreach_time_safe4,':^',N_2,dreach_time_unsafe4,':>','LineWidth',2);
%plot(N,time_safe4,'-ro',N,time_unsafe4,'-.b','LineWidth',2);
%hold on;
%plot(N,hycomp_time_safe4,'-+g',N,hycomp_time_unsafe4,'-dy','LineWidth',2);
ax = gca;
set(ax,'XTick',[ 4 8 12 16 20 24 28 32]);
%
xlabel('k');
ylabel('Runtime (s)');
%legend('QBMC-safe','QBMC-unsafe','HyComp-safe','HyComp-unsafe','dReach-safe','dReach-unsafe','Location','northwest');
title('N = 4');
% plot memmory at k <= 8 [ 4 8 12 16 20 24 28 32]
figure
plot(N_2,mem_safe4,'-.o',N,mem_unsafe4,'-.s',N_3,hycomp_mem_safe4,'-+',N,hycomp_mem_unsafe4,'-d',...
    N_2,dreach_mem_safe4,':^',N_2,dreach_mem_unsafe4,':>','LineWidth',2);
ax = gca;
set(ax,'XTick',[ 4 8 12 16 20 24 28 32]);
xlabel('k');
ylabel('Memory Usage (MB)');
%legend('QBMC-safe','QBMC-unsafe','HyComp-safe','HyComp-unsafe','dReach-safe','dReach-unsafe','Location','northwest');
title('N = 4');