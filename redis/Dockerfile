FROM redis

COPY redis_data.txt /

RUN redis-server --appendonly yes && sleep 5s && cat /redis_data.txt | redis-cli --pipe && redis-cli save && redis-cli shutdown

CMD ["redis-server"]
