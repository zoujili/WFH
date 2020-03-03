while true
do nvidia-smi --query-gpu=utilization.gpu,utilization.memory,memory.total,memory.free,memory.used,temperature.gpu --format=csv >> gpu220.log; sleep 1;
done
