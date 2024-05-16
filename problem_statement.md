Problem Statement
===

## Title, Authors, Project Type ##

Title: Pseudorandom Number Generator with a Chaotic System
Authors: Nathan Lee and Quentin Adolphe

## Problem Statement ##

Generating random numbers especially in the context of computers is extremely difficult. We want to explore a simulated technique of using chaotic systems to generate pseudorandom numbers from a computer.

## Motivation and related work ##

Pseudorandom number generators are the backbone of modern encryption algorithms, without them, it is impossible to securely create keys used in block ciphers. However, randomness is extremely hard to come by within a computer setting since computers are made to be deterministic. 

Companies have resorted to using the imprecision of measurements of real-world systems to create unpredictable data. Cloudflare for example uses a camera feed pointing at 100 lava lamps and uses each pixel as an unpredictable input to a pseudorandom number generator. We would like to create pseudorandomes with a similar approach. Instead of using lava lamps, we will be using double pendulums which are a deterministic but chaotic system. Since creating many double pendulums impractical we will be simulating them. Having a pseudorandom generator that can be simulated on a computer is not secure, but for the purposes of the project, we just want to test the viability of using a deterministic but chaotic system to simulate randomness.

https://blog.cloudflare.com/randomness-101-lavarand-in-production
