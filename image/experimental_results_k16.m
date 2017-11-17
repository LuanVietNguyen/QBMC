
%time_safe8 = [1.6 1.1 8.3 6.9 76.1 40.1 344.8 288.8];
time_safe16 = [6.4 117.8];
time_unsafe16 = [ 1.52 22.7 119.1 21456];
hycomp_time_safe16 = [2.8 55.8 788];
hycomp_time_unsafe16 = [0.5 6.7 569.4];
dreach_time_unsafe16 = [50.3 959.3];
%%%%%
mem_safe16 = [30 52.4];
mem_unsafe16 = [28.2 49.7 156.2 473.8];
hycomp_mem_safe16 = [107.3 214.4 1010.8];
hycomp_mem_unsafe16 = [101.4 149.6 895.4];
dreach_mem_unsafe16 = [30.5 235.3];
%%%%%

N = [ 2 3 4 5 ];
N_2 = [2 3];
N_3 = [ 2 3 4];
% plot runtime at k <= 8
figure
%plot(time_safe8, N, 'LineWidth',1.3); 
%plot(N,time_safe8,'-ro',N,time_unsafe8,'-.b','LineWidth',2);
plot(N_2,time_safe16,'-.o',N,time_unsafe16,'-.s',N_3,hycomp_time_safe16,'-+',N_3,hycomp_time_unsafe16,'-d',N_2,dreach_time_unsafe16,':>','LineWidth',2);
%plot(N,time_safe8,'-ro',N,time_unsafe8,'-.b','LineWidth',2);
%hold on;
%plot(N,hycomp_time_safe8,'-+g',N,hycomp_time_unsafe8,'-dy','LineWidth',2);
ax = gca;
set(ax,'XTick',[ 2 3 4 5 ]);
%
xlabel('Number of Processes');
ylabel('Runtime (s)');
%legend('QBMC-safe','QBMC-unsafe','HyComp-safe','HyComp-unsafe','dReach-unsafe','Location','northwest');
title('k \leq 16');
% plot memmory at k <= 8
figure
plot(N_2,mem_safe16,'-.o',N,mem_unsafe16,'-.s',N_3,hycomp_mem_safe16,'-+',N_3,hycomp_mem_unsafe16,'-d',N_2,dreach_mem_unsafe16,':>','LineWidth',2);
ax = gca;
set(ax,'XTick',[ 2 3 4 5 ]);
xlabel('Number of Processes');
ylabel('Memory Usage (MB)');
%legend('QBMC-safe','QBMC-unsafe','HyComp-safe','HyComp-unsafe','dReach-unsafe','Location','northwest');
title('k \leq 16');