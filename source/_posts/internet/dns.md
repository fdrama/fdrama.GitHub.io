---
title: DNS
tags: [internet, dns]
categories: 互联网
---


> DNS（Domain Name System）是互联网的电话簿，人类通过域名访问网上信息，如 nytimes.com 或 espn.com。网络浏览器通过互联网协议（IP）地址进行交互。DNS 将域名转换为 IP 地址，以便浏览器加载互联网资源。

<!-- more -->

1. DNS 服务器的作用是什么？

    DNS 服务器的作用是将域名转换为 IP 地址，以便于计算机之间的通信。

2. DNS 服务器的工作原理是什么？

> 根域名服务器列表^[<https://www.iana.org/domains/root/servers>]

 Hostname           | IP Addresses                      | Operator
--------------------|-----------------------------------|------------------------------------------------------------------
 a.root-servers.net | 198.41.0.4, 2001:503:ba3e::2:30   | Verisign, Inc.
 b.root-servers.net | 199.9.14.201, 2001:500:200::b     | University of Southern California,Information Sciences Institute
 c.root-servers.net | 192.33.4.12, 2001:500:2::c        | Cogent Communications
 d.root-servers.net | 199.7.91.13, 2001:500:2d::d       | University of Maryland
 e.root-servers.net | 192.203.230.10, 2001:500:a8::e    | NASA (Ames Research Center)
 f.root-servers.net | 192.5.5.241, 2001:500:2f::f       | Internet Systems Consortium, Inc.
 g.root-servers.net | 192.112.36.4, 2001:500:12::d0d    | US Department of Defense (NIC)
 h.root-servers.net | 198.97.190.53, 2001:500:1::53     | US Army (Research Lab)
 i.root-servers.net | 192.36.148.17, 2001:7fe::53       | Netnod
 j.root-servers.net | 192.58.128.30, 2001:503:c27::2:30 | Verisign, Inc.
 k.root-servers.net | 193.0.14.129, 2001:7fd::1         | RIPE NCC
 l.root-servers.net | 199.7.83.42, 2001:500:9f::42      | ICANN
 m.root-servers.net | 202.12.27.33, 2001:dc3::35        | WIDE Project


[^]:[What is DNS](https://www.cloudflare.com/en-gb/learning/dns/what-is-dns/)