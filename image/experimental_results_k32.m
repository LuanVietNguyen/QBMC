
%time_safe8 = [1.6 1.1 8.3 6.9 76.1 40.1 344.8 288.8];
time_safe32 = [60 19452];
time_unsafe32 = [ 6.1 94.31 4197.1];
hycomp_time_safe32 = [14.1 539.7];
hycomp_time_unsafe32 = [0.53 6.5 568.4];
dreach_time_unsafe32 = [55.8 966.8];
%%%%%
mem_safe32 = [45.2 115.6];
mem_unsafe32 = [40.2 74.6 254.1];
hycomp_mem_safe32 = [101.5 713.4];
hycomp_mem_unsafe32 = [101.4 167.1 897.1];
dreach_mem_unsafe32 = [30.7 241.2];
%%%%%

N = [ 2 3 4 5 ];
N_2 = [ 2 3];
N_3 = [ 2 3 4];
% plot runtime at k <= 8
figure
%plot(time_safe8, N, 'LineWidth',1.3); 
%plot(N,time_safe8,'-ro',N,time_unsafe8,'-.b','LineWidth',2);
plot(N_2,time_safe32,'-.o',N_3,time_unsafe32,'-.s',N_2,hycomp_time_safe32,'-+',N_3,hycomp_time_unsafe32,'-d',N_2,dreach_time_unsafe32,':>','LineWidth',2);
%plot(N,time_safe8,'-ro',N,time_unsafe8,'-.b','LineWidth',2);
%hold on;
%plot(N,hycomp_time_safe8,'-+g',N,hycomp_time_unsafe8,'-dy','LineWidth',2);
ax = gca;
set(ax,'XTick',[2:1:5]);
%
xlabel('Number of Processes');
ylabel('Runtime (s)');
%legend('QBMC-safe','QBMC-unsafe','HyComp-safe','HyComp-unsafe','dReach-unsafe','Location','northwest');
title('k \leq 32');
% plot memmory at k <= 8
figure
plot(N_2,mem_safe32,'-.o',N_3,mem_unsafe32,'-.s',N_2,hycomp_mem_safe32,'-+',N_3,hycomp_mem_unsafe32,'-d',N_2,dreach_mem_unsafe32,':>','LineWidth',2);
ax = gca;
set(ax,'XTick',[ 2 3 4 5 ]);
xlabel('Number of Processes');
ylabel('Memory Usage (MB)');
%legend('QBMC-safe','QBMC-unsafe','HyComp-safe','HyComp-unsafe','dReach-unsafe','Location','northwest');
title('k \leq 32');