from bots.botsconfig import *
from records004010 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA  to send
        'functionalgroup'    :  'RA',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BPR', MIN: 1, MAX: 1},
    {ID: 'NTE', MIN: 0, MAX: 99999},
    {ID: 'TRN', MIN: 0, MAX: 1},
    {ID: 'CUR', MIN: 0, MAX: 1},
    #~ {ID: 'REF', MIN: 0, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 99},
    {ID: 'DTM', MIN: 0, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 200, LEVEL: [   #ADDED
        {ID: 'N2', MIN: 0, MAX: 2},   #ADDED
        {ID: 'N3', MIN: 0, MAX: 2},   #ADDED
        {ID: 'N4', MIN: 0, MAX: 99999},   #ADDED
        {ID: 'REF', MIN: 0, MAX: 12},   #ADDED
        {ID: 'PER', MIN: 0, MAX: 99999},   #ADDED
    ]},
    {ID: 'ENT', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 99999},
            {ID: 'N3', MIN: 0, MAX: 99999},
            {ID: 'N4', MIN: 0, MAX: 1},
            #~ {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 99999},
        ]},
        {ID: 'ADX', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'NTE', MIN: 0, MAX: 99999},
            {ID: 'PER', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99999},
        ]},
        {ID: 'IT1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 1},
            ]},
            {ID: 'SAC', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'TXI', MIN: 0, MAX: 99999},
            ]},
            {ID: 'SLN', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 99999},
                ]},
                {ID: 'SAC', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'TXI', MIN: 0, MAX: 99999},
                ]},
            ]},
        ]},
        {ID: 'RMR', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'NTE', MIN: 0, MAX: 99999},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'IT1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 1},
                ]},
                {ID: 'SAC', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'TXI', MIN: 0, MAX: 99999},
                ]},
                {ID: 'SLN', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'DTM', MIN: 0, MAX: 99999},
                    ]},
                    {ID: 'SAC', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'TXI', MIN: 0, MAX: 99999},
                    ]},
                ]},
            ]},
            {ID: 'ADX', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'NTE', MIN: 0, MAX: 99999},
                {ID: 'PER', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 99999},
                ]},
                {ID: 'IT1', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'DTM', MIN: 0, MAX: 1},
                    ]},
                    {ID: 'SAC', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'TXI', MIN: 0, MAX: 99999},
                    ]},
                    {ID: 'SLN', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'REF', MIN: 0, MAX: 99999, LEVEL: [
                            {ID: 'DTM', MIN: 0, MAX: 99999},
                        ]},
                        {ID: 'SAC', MIN: 0, MAX: 99999, LEVEL: [
                            {ID: 'TXI', MIN: 0, MAX: 99999},
                        ]},
                    ]},
                ]},
            ]},
        ]},
    ]},
    {ID: 'TXP', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'TXI', MIN: 0, MAX: 99999},
    ]},
    {ID: 'DED', MIN: 0, MAX: 99999},
    {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'TRN', MIN: 0, MAX: 99999},
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'G53', MIN: 0, MAX: 1},
            {ID: 'AIN', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'QTY', MIN: 0, MAX: 99999},
                {ID: 'DTP', MIN: 0, MAX: 99999},
            ]},
            {ID: 'PEN', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'AMT', MIN: 0, MAX: 99999},
                {ID: 'DTP', MIN: 0, MAX: 99999},
                {ID: 'INV', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'DTP', MIN: 0, MAX: 99999},
                ]},
            ]},
        ]},
    ]},
    {ID: 'N9', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'AMT', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
        ]},
        {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'EMS', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'ATN', MIN: 0, MAX: 99999},
                {ID: 'AIN', MIN: 0, MAX: 99999},
                {ID: 'PYD', MIN: 0, MAX: 99999},
            ]},
        ]},
    ]},
    {ID: 'RYL', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'NM1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'PID', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'DTM', MIN: 0, MAX: 1},
                    {ID: 'PCT', MIN: 0, MAX: 99999, LEVEL: [
                        {ID: 'QTY', MIN: 0, MAX: 1},
                        {ID: 'AMT', MIN: 0, MAX: 99999, LEVEL: [
                            {ID: 'ADX', MIN: 0, MAX: 99999},
                        ]},
                    ]},
                ]},
            ]},
            {ID: 'ASM', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'ADX', MIN: 0, MAX: 1},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 0, MAX: 1},
]}
]
