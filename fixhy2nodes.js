function operator(proxies = []){
  newProxies = proxies.map(proxie => 
    proxie.type === 'hysteria2'
      ? { ...proxie,  up: "120 Mbps", down: "600 Mbps" }
      : { ...proxie }
  );
  return newProxies;
}
