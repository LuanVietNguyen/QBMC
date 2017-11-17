
%time_safe8 = [1.6 1.1 8.3 6.9 76.1 40.1 344.8 288.8];
time_safe4 = [1.11 4.02 9.97 77.51];
time_unsafe4 = [ 0.7 3.97 8.44 63.93];
hycomp_time_safe4 = [0.2 0.51 2.78 17.13];
hycomp_time_unsafe4 = [ 0.2 0.51 2.53 16.56];
dreach_time_safe4 = [1.2 1.4 2.1 7.7];
dreach_time_unsafe4 = [ 1.2 1.3 1.6 7.7];
%%%%%
mem_safe4 = [22.3 48.7 56.9 263];
mem_unsafe4 = [21.73 48.7 57 249.9];
hycomp_mem_safe4 = [90.6 120.2 255.2 1067];
hycomp_mem_unsafe4 = [ 89.3 121.5 255 1066.7];
dreach_mem_safe4 = [2.5 2.5 9.8 167.2];
dreach_mem_unsafe4 = [ 2.5 2.5 2.5 153.9];
%%%%%

N = [ 2 3 4 5 ];
% plot runtime at k <= 8
figure
%plot(time_safe4, N, 'LineWidth',1.3); 
%plot(N,time_safe4,'-.ro',N,time_unsafe4,'-.b','LineWidth',2);
plot(N,time_safe4,'-.o',N,time_unsafe4,'-.s',N,hycomp_time_safe4,'-+',N,hycomp_time_unsafe4,'-d',...
    N,dreach_time_safe4,':^',N,dreach_time_unsafe4,':>','LineWidth',2);
%plot(N,time_safe4,'-ro',N,time_unsafe4,'-.b','LineWidth',2);
%hold on;
%plot(N,hycomp_time_safe4,'-+g',N,hycomp_time_unsafe4,'-dy','LineWidth',2);
ax = gca;
set(ax,'XTick',[ 2 3 4 5 ]);
%
xlabel('Number of Processes');
ylabel('Runtime (s)');
%legend('QBMC-safe','QBMC-unsafe','HyComp-safe','HyComp-unsafe','dReach-safe','dReach-unsafe','Location','northwest');
title('k \leq 4');
% plot memmory at k <= 8
figure
plot(N,mem_safe4,'-.o',N,mem_unsafe4,'-.s',N,hycomp_mem_safe4,'-+',N,hycomp_mem_unsafe4,'-d',...
    N,dreach_mem_safe4,':^',N,dreach_mem_unsafe4,':>','LineWidth',2);
ax = gca;
set(ax,'XTick',[ 2 3 4 5 ]);
xlabel('Number of Processes');
ylabel('Memory Usage (MB)');
%legend('QBMC-safe','QBMC-unsafe','HyComp-safe','HyComp-unsafe','dReach-safe','dReach-unsafe','Location','northwest');
title('k \leq 4');