# Secure File Sync

I know what you are think, "Dude, just use scp, FTPS, SFTP, rsync..." and you are right.  There are a lot of other tools that would work just fine.  But I am trying to learn python and become better and being able to script my own solutions instead of surviving off of someone elses work.  

## Purpose

I have a pi3 that sits on a span port running zeek.  I like to use RITA to be able to analyse the zeek logs.  However, RITA does not install nicely on a pi.  And so, I have rita install on the server running my SIEM.  The intent is to have a python script that will package the logs, ship them to the server running RITA.  

## Goals

The script will need to: 

1. Be able to establish connections with client and server without human intervention on a set schedule.  
2. Be able to use TLS or some other form of encryption.  You know, Zero trust and all.
3. Ship the logs fast and efficiently


## Final Thoughts

Keep in mind that my python scripting skills as this point are dismal.  The goal of these projects are to use python to solve needs, and to do so in a way where I am forced to learned python. 