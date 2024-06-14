#!/bin/bash

kill -9 $(ps auwx | grep bench | awk '{print $2}')

