
%time_safe8 = [1.6 1.1 8.3 6.9 76.1 40.1 344.8 288.8];
time_safe2 = [1.11 1.6 6.4 60];
time_unsafe2 = [ 0.7 1.1 1.52 6.1];
hycomp_time_safe2 = [0.2 0.51 2.8 14.1];
hycomp_time_unsafe2 = [ 0.2 0.4 0.5 0.53];
dreach_time_safe2 = [1.2 64.1];
dreach_time_unsafe2 = [ 1.2 48.4 50.3 55.8];
%%%%%
mem_safe2 = [22.3 25.2 30 45.2];
mem_unsafe2 = [21.73 24.5 28.2 40.2];
hycomp_mem_safe2 = [90.6 101.4 107.3 123.4];
hycomp_mem_unsafe2 = [89.3 100.9 101.4 101.5];
dreach_mem_safe2 = [2.5 120.8];
dreach_mem_unsafe2 = [ 2.5 28.9 30.7 31.4];
%%%%%

N = [ 4 8 16 32 ];
N_2 = [ 4 8]; 
N_3 = [ 4 8 16];
% plot runtime at k <= 8
figure
%plot(time_safe2, N, 'LineWidth',1.3); 
%plot(N,time_safe2,'-.ro',N,time_unsafe2,'-.b','LineWidth',2);
plot(N,time_safe2,'-.o',N,time_unsafe2,'-.s',N,hycomp_time_safe2,'-+',N,hycomp_time_unsafe2,'-d',...
    N_2,dreach_time_safe2,':^',N,dreach_time_unsafe2,':>','LineWidth',2);
%plot(N,time_safe2,'-ro',N,time_unsafe2,'-.b','LineWidth',2);
%hold on;
%plot(N,hycomp_time_safe2,'-+g',N,hycomp_time_unsafe2,'-dy','LineWidth',2);
ax = gca;
set(ax,'XTick',[ 4 8 12 16 20 24 28 32]);
%
xlabel('k');
ylabel('Runtime (s)');
%legend('QBMC-safe','QBMC-unsafe','HyComp-safe','HyComp-unsafe','dReach-safe','dReach-unsafe','Location','northwest');
title('N = 2');
% plot memmory at k <= 8 [ 4 8 12 16 20 24 28 32]
figure
plot(N,mem_safe2,'-.o',N,mem_unsafe2,'-.s',N,hycomp_mem_safe2,'-+',N,hycomp_mem_unsafe2,'-d',...
    N_2,dreach_mem_safe2,':^',N,dreach_mem_unsafe2,':>','LineWidth',2);
ax = gca;
set(ax,'XTick',[ 4 8 12 16 20 24 28 32]);
xlabel('k');
ylabel('Memory Usage (MB)');
%legend('QBMC-safe','QBMC-unsafe','HyComp-safe','HyComp-unsafe','dReach-safe','dReach-unsafe','Location','northwest');
title('N = 2');