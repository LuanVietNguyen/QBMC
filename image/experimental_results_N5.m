
%time_safe8 = [1.6 1.1 8.3 6.9 76.1 40.1 344.8 288.8];
time_safe5 = [77.51 344.4];
time_unsafe5 = [63.93 288.8 21456];
hycomp_time_safe5 = [17.13 172.4];
hycomp_time_unsafe5 = [16.56 109.1];
dreach_time_safe5 = [7.7 16.69];
dreach_time_unsafe5 = [7.7 17];
%%%%%
mem_safe5 = [254.3 254.4];
mem_unsafe5 = [249.9 249.9 473.8];
hycomp_mem_safe5 = [1067 1405.9];
hycomp_mem_unsafe5 = [1066.7 1345.4];
dreach_mem_safe5 = [167.2 469.6];
dreach_mem_unsafe5 = [153.9 506.5];
%%%%%

N = [ 4 8 16 32];
N_2 = [ 4 8]; 
N_3 = [ 4 8 16];
% plot runtime at k <= 8
figure
%plot(time_safe5, N, 'LineWidth',1.3); 
%plot(N,time_safe5,'-.ro',N,time_unsafe5,'-.b','LineWidth',2);
plot(N_2,time_safe5,'-.o',N_3,time_unsafe5,'-.s',N_2,hycomp_time_safe5,'-+',N_2,hycomp_time_unsafe5,'-d',...
    N_2,dreach_time_safe5,':^',N_2,dreach_time_unsafe5,':>','LineWidth',2);
%plot(N,time_safe5,'-ro',N,time_unsafe5,'-.b','LineWidth',2);
%hold on;
%plot(N,hycomp_time_safe5,'-+g',N,hycomp_time_unsafe5,'-dy','LineWidth',2);
ax = gca;
set(ax,'XTick',[ 4 8 12 16]);
%
xlabel('k');
ylabel('Runtime (s)');
%legend('QBMC-safe','QBMC-unsafe','HyComp-safe','HyComp-unsafe','dReach-safe','dReach-unsafe','Location','northwest');
title('N = 5');
% plot memmory at k <= 8 [ 4 8 12 16 20 24 28 32]
figure
plot(N_2,mem_safe5,'-.o',N_3,mem_unsafe5,'-.s',N_2,hycomp_mem_safe5,'-+',N_2,hycomp_mem_unsafe5,'-d',...
    N_2,dreach_mem_safe5,':^',N_2,dreach_mem_unsafe5,':>','LineWidth',2);
ax = gca;
set(ax,'XTick',[ 4 8 12 16]);
xlabel('k');
ylabel('Memory Usage (MB)');
%legend('QBMC-safe','QBMC-unsafe','HyComp-safe','HyComp-unsafe','dReach-safe','dReach-unsafe','Location','northwest');
title('N = 5');