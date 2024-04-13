#!/usr/bin/env node
const dns = require('dns');

function resolveDNS(domainName) {
    dns.resolve(domainName, (err, addresses) => {
        if (err) {
            console.error(`Failed to resolve DNS for ${domainName}: ${err}`);
        } else {
            console.log(`The IP addresses of ${domainName} are: ${addresses}`);
        }
    });
}

// Example usage
resolveDNS("google.com");

