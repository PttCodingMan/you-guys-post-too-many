---
title: 404
date: 2021-12-20 15:28:39
permalink: /404.html
comments: false
---
<!-- markdownlint-disable MD039 MD033 -->

## 很抱歉，你目前存取的頁面並不存在。

預計將在約 <span id="timeout">6</span> 秒後返回首頁。

<script>
let countTime = 6;

function count() {
  
  document.getElementById('timeout').textContent = countTime;
  countTime -= 1;
  if(countTime === 0){
    location.href = '/you-guys-post-too-many'; // 記得改成自己網址 Url
  }
  setTimeout(() => {
    count();
  }, 1000);
}

count();
</script>