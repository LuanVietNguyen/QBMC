
%time_safe8 = [1.6 1.1 8.3 6.9 76.1 40.1 344.8 288.8];
time_safe8 = [1.6 8.3 76.1 344.8];
time_unsafe8 = [ 1.1 6.9 40.1 288.8];
hycomp_time_safe8 = [0.5 2.2 9.9 172.4];
hycomp_time_unsafe8 = [ 0.4 2.1 13.3 109.1];
dreach_time_safe8 = [64.1 2.7 4.63 16.69];
dreach_time_unsafe8 = [ 48.4 2.7 4.93 17];
%%%%%
mem_safe8 = [25.2 48.7 74.1 254.4];
mem_unsafe8 = [24.7 48.7 73.2 249.9];
hycomp_mem_safe8 = [101.4 131.8 319.1 1405.9];
hycomp_mem_unsafe8 = [ 100.9 131.8 318.2 1345.4];
dreach_mem_safe8 = [120.8 26.4 96.7 469.6];
dreach_mem_unsafe8 = [28.9 26.8 119.8 506.6];
%%%%%

N = [ 2 3 4 5 ];
% plot runtime at k <= 8
figure
%plot(time_safe8, N, 'LineWidth',1.3); 
%plot(N,time_safe8,'-.ro',N,time_unsafe8,'-.b','LineWidth',2);
%plot(N,time_safe8,'-.o',N,time_unsafe8,'-.s',N,hycomp_time_safe8,'-+',N,hycomp_time_unsafe8,'-d',...
    %N,dreach_time_safe8,':^',N,dreach_time_unsafe8,':>','LineWidth',2);
plot(N,time_safe8,'-.o',N,time_unsafe8,'-.s',N,hycomp_time_safe8,'-+',N,hycomp_time_unsafe8,'-d',...
    N,dreach_time_safe8,':^',N,dreach_time_unsafe8,':>','LineWidth',2);
%plot(N,time_safe8,'-ro',N,time_unsafe8,'-.b','LineWidth',2);
%hold on;
%plot(N,hycomp_time_safe8,'-+g',N,hycomp_time_unsafe8,'-dy','LineWidth',2);
ax = gca;
set(ax,'XTick',[ 2 3 4 5 ]);
%
xlabel('Number of Processes');
ylabel('Runtime (s)');
%legend('QBMC-safe','QBMC-unsafe','HyComp-safe','HyComp-unsafe','dReach-safe','dReach-unsafe','Location','northwest');
title('k \leq 8');
% plot memmory at k <= 8
figure
plot(N,mem_safe8,'-.o',N,mem_unsafe8,'-.s',N,hycomp_mem_safe8,'-+',N,hycomp_mem_unsafe8,'-d',...
    N,dreach_mem_safe8,':^',N,dreach_mem_unsafe8,':>','LineWidth',2);
ax = gca;
set(ax,'XTick',[ 2 3 4 5 ]);
xlabel('Number of Processes');
ylabel('Memory Usage (MB)');
%legend('QBMC-safe','QBMC-unsafe','HyComp-safe','HyComp-unsafe','dReach-safe','dReach-unsafe','Location','northwest');
title('k \leq 8');