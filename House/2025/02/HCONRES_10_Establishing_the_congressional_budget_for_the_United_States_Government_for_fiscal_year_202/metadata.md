# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/10?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hconres/10
- Title: Emergency Border Control Resolution
- Congress: 119
- Bill type: HCONRES
- Bill number: 10
- Origin chamber: House
- Introduced date: 2025-02-10
- Update date: 2025-06-13T18:49:21Z
- Update date including text: 2025-06-13T18:49:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-10: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the House Committee on the Budget.
- 2025-02-10 - IntroReferral: Sponsor introductory remarks on measure. (CR H607)
- 2025-02-10 - Committee: Submitted in House
- Latest action: 2025-02-10: Sponsor introductory remarks on measure. (CR H607)

## Actions

- 2025-02-10 - IntroReferral: Referred to the House Committee on the Budget.
- 2025-02-10 - IntroReferral: Sponsor introductory remarks on measure. (CR H607)
- 2025-02-10 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-10",
    "latestAction": {
      "actionDate": "2025-02-10",
      "text": "Sponsor introductory remarks on measure. (CR H607)"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hconres/10",
    "number": "10",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "H001052",
        "district": "1",
        "firstName": "Andy",
        "fullName": "Rep. Harris, Andy [R-MD-1]",
        "lastName": "Harris",
        "party": "R",
        "state": "MD"
      }
    ],
    "title": "Emergency Border Control Resolution",
    "type": "HCONRES",
    "updateDate": "2025-06-13T18:49:21Z",
    "updateDateIncludingText": "2025-06-13T18:49:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-10",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Budget.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H607)",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-02-10T17:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "TX"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "AZ"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "MO"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "GA"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "AZ"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "LA"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "SC"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "TN"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "TX"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres10ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. CON. RES. 10\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2025 Mr. Harris of Maryland (for himself, Mr. Cloud , Mr. Biggs of Arizona , Mr. Burlison , Mr. Clyde , Mr. Crane , Mr. Higgins of Louisiana , Mr. Norman , Mr. Ogles , Mr. Perry , and Mr. Roy ) submitted the following concurrent resolution; which was referred to the Committee on the Budget\nCONCURRENT RESOLUTION\nEstablishing the congressional budget for the United States Government for fiscal year 2025 and setting forth the appropriate budgetary levels for fiscal years 2026 through 2034.\n#### 1. Short title\nThis concurrent resolution may be cited as the Emergency Border Control Resolution .\n#### 2. Concurrent resolution on the budget for fiscal year 2025\n##### (a) Declaration\nThe Congress determines and declares that prior concurrent resolutions on the budget are replaced as of fiscal year 2025 and that this concurrent resolution establishes the budget for fiscal year 2025 and sets forth the appropriate budgetary levels for fiscal years 2026 through 2034.\n##### (b) Table of Contents\nThe table of contents for this concurrent resolution is as follows:\nSec. 1. Short title.\nSec. 2. Concurrent resolution on the budget for fiscal year 2025.\nTitle I\u2014Recommended levels and amounts\nSec. 101. Recommended levels and amounts.\nSec. 102. Major functional categories.\nTitle II\u2014Budget enforcement in the House of Representatives\nSec. 201. Reconciliation in the House.\nTitle III\u2014Policy Statements in the House of Representatives\nSec. 301. Policy statement on Federal spending.\nI\nRecommended levels and amounts\n#### 101. Recommended levels and amounts\nThe following budgetary levels are appropriate for each of fiscal years 2025 through 2034:\n**(1) Federal revenues**\nFor purposes of the enforcement of this concurrent resolution:\n**(A)**\nThe recommended levels of Federal revenues are as follows:\nFiscal year 2025: $3,859,000,000,000.\nFiscal year 2026: $4,217,000,000,000.\nFiscal year 2027: $4,516,000,000,000.\nFiscal year 2028: $4,637,000,000,000.\nFiscal year 2029: $4,760,000,000,000.\nFiscal year 2030: $4,959,000,000,000.\nFiscal year 2031: $5,180,000,000,000.\nFiscal year 2032: $5,389,000,000,000.\nFiscal year 2033: $5,623,000,000,000.\nFiscal year 2034: $5,860,000,000,000.\n**(B)**\nThe amounts by which the aggregate levels of Federal revenues should be changed are as follows:\nFiscal year 2025: $0.\nFiscal year 2026: $0.\nFiscal year 2027: $0.\nFiscal year 2028: $0.\nFiscal year 2029: $0.\nFiscal year 2030: $0.\nFiscal year 2031: $0.\nFiscal year 2032: $0.\nFiscal year 2033: $0.\nFiscal year 2034: $0.\n**(2) New budget authority**\nFor purposes of the enforcement of this concurrent resolution, the appropriate levels of total new budget authority are as follows:\nFiscal year 2025: $5,524,029,000,000.\nFiscal year 2026: $5,898,943,000,000.\nFiscal year 2027: $6,107,613,000,000.\nFiscal year 2028: $6,367,856,000,000.\nFiscal year 2029: $6,499,320,000,000.\nFiscal year 2030: $6,835,261,000,000.\nFiscal year 2031: $7,106,512,000,000.\nFiscal year 2032: $7,425,923,000,000.\nFiscal year 2033: $7,841,068,000,000.\nFiscal year 2034: $8,043,297,000,000.\n**(3) Budget outlays**\nFor purposes of the enforcement of this concurrent resolution, the appropriate levels of total budget outlays are as follows:\nFiscal year 2025: $5,499,209,000,000.\nFiscal year 2026: $5,796,590,000,000.\nFiscal year 2027: $6,040,474,000,000.\nFiscal year 2028: $6,335,771,000,000.\nFiscal year 2029: $6,392,586,000,000.\nFiscal year 2030: $6,748,328,000,000.\nFiscal year 2031: $7,016,004,000,000.\nFiscal year 2032: $7,311,102,000,000.\nFiscal year 2033: $7,761,565,000,000.\nFiscal year 2034: $7,922,559,000,000.\n**(4) Deficits (on-budget)**\nFor purposes of the enforcement of this concurrent resolution, the amounts of the deficits (on-budget) are as follows:\nFiscal year 2025: $1,640,075,000,000.\nFiscal year 2026: $1,579,298,000,000.\nFiscal year 2027: $1,524,337,000,000.\nFiscal year 2028: $1,698,827,000,000.\nFiscal year 2029: $1,633,067,000,000.\nFiscal year 2030: $1,789,582,000,000.\nFiscal year 2031: $1,836,021,000,000.\nFiscal year 2032: $1,922,423,000,000.\nFiscal year 2033: $2,138,607,000,000.\nFiscal year 2034: $2,062,575,000,000.\n**(5) Debt subject to limit**\nThe appropriate levels of debt subject to limit are as follows:\nFiscal year 2025: $37,105,075,000,000.\nFiscal year 2026: $39,038,373,000,000.\nFiscal year 2027: $40,791,710,000,000.\nFiscal year 2028: $42,678,537,000,000.\nFiscal year 2029: $44,670,604,000,000.\nFiscal year 2030: $46,675,186,000,000.\nFiscal year 2031: $48,713,207,000,000.\nFiscal year 2032: $50,840,630,000,000.\nFiscal year 2033: $53,300,237,000,000.\nFiscal year 2034: $56,056,812,000,000.\n**(6) Debt held by the public**\nThe appropriate levels of debt held by the public are as follows:\nFiscal year 2025: $29,999,075,000,000.\nFiscal year 2026: $31,791,373,000,000.\nFiscal year 2027: $33,555,710,000,000.\nFiscal year 2028: $35,531,537,000,000.\nFiscal year 2029: $37,470,604,000,000.\nFiscal year 2030: $39,595,186,000,000.\nFiscal year 2031: $41,795,207,000,000.\nFiscal year 2032: $44,129,630,000,000.\nFiscal year 2033: $46,695,237,000,000.\nFiscal year 2034: $49,216,812,000,000.\n#### 102. Major functional categories\nThe Congress determines and declares that the appropriate levels of new budget authority and outlays for fiscal years 2025 through 2034 for each major functional category are:\n**(1)**\nNational Defense (050):\nFiscal year 2025:\n**(A)**\nNew budget authority, $888,044,000,000.\n**(B)**\nOutlays, $883,821,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $913,263,000,000.\n**(B)**\nOutlays, $895,830,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $935,345,000,000.\n**(B)**\nOutlays, $913,493,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, $956,694,000,000.\n**(B)**\nOutlays, $940,299,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, $979,049,000,000.\n**(B)**\nOutlays, $950,598,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, $1,002,337,000,000.\n**(B)**\nOutlays, $977,233,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, $1,026,119,000,000.\n**(B)**\nOutlays, $996,535,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, $1,050,408,000,000.\n**(B)**\nOutlays, $1,016,235,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, $1,076,299,000,000.\n**(B)**\nOutlays, $1,050,728,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, $1,101,659,000,000.\n**(B)**\nOutlays, $1,067,701,000,000.\n**(2)**\nInternational Affairs (150):\nFiscal year 2025:\n**(A)**\nNew budget authority, $65,962,000,000.\n**(B)**\nOutlays, $69,206,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $64,270,000,000.\n**(B)**\nOutlays, $68,458,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $64,856,000,000.\n**(B)**\nOutlays, $68,013,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, $66,169,000,000.\n**(B)**\nOutlays, $64,433,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, $67,655,000,000.\n**(B)**\nOutlays, $65,177,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, $69,175,000,000.\n**(B)**\nOutlays, $65,601,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, $70,699,000,000.\n**(B)**\nOutlays, $66,643,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, $72,220,000,000.\n**(B)**\nOutlays, $67,916,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, $73,809,000,000.\n**(B)**\nOutlays, $69,332,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, $75,431,000,000.\n**(B)**\nOutlays, $70,768,000,000.\n**(3)**\nGeneral Science, Space, and Technology (250):\nFiscal year 2025:\n**(A)**\nNew budget authority, $42,084,000,000.\n**(B)**\nOutlays, $41,734,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $43,056,000,000.\n**(B)**\nOutlays, $42,483,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $44,011,000,000.\n**(B)**\nOutlays, $43,166,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, $44,881,000,000.\n**(B)**\nOutlays, $43,781,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, $45,834,000,000.\n**(B)**\nOutlays, $44,611,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, $46,835,000,000.\n**(B)**\nOutlays, $45,450,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, $47,840,000,000.\n**(B)**\nOutlays, $46,405,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, $48,853,000,000.\n**(B)**\nOutlays, $47,377,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, $49,907,000,000.\n**(B)**\nOutlays, $48,391,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, $50,997,000,000.\n**(B)**\nOutlays, $49,436,000,000.\n**(4)**\nEnergy (270):\nFiscal year 2025:\n**(A)**\nNew budget authority, $39,842,000,000.\n**(B)**\nOutlays, $37,587,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $40,172,000,000.\n**(B)**\nOutlays, $44,518,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $43,579,000,000.\n**(B)**\nOutlays, $52,928,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, $44,493,000,000.\n**(B)**\nOutlays, $52,542,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, $45,633,000,000.\n**(B)**\nOutlays, $51,237,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, $44,014,000,000.\n**(B)**\nOutlays, $47,297,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, $45,460,000,000.\n**(B)**\nOutlays, $46,521,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, $50,176,000,000.\n**(B)**\nOutlays, $48,864,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, $35,184,000,000.\n**(B)**\nOutlays, $34,040,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, $27,122,000,000.\n**(B)**\nOutlays, $26,021,000,000.\n**(5)**\nNatural Resources and Environment (300):\nFiscal year 2025:\n**(A)**\nNew budget authority, $88,219,000,000.\n**(B)**\nOutlays, $90,074,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $89,760,000,000.\n**(B)**\nOutlays, $90,428,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $83,830,000,000.\n**(B)**\nOutlays, $91,282,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, $85,498,000,000.\n**(B)**\nOutlays, $91,754,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, $87,319,000,000.\n**(B)**\nOutlays, $92,172,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, $88,970,000,000.\n**(B)**\nOutlays, $92,442,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, $91,016,000,000.\n**(B)**\nOutlays, $92,640,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, $92,975,000,000.\n**(B)**\nOutlays, $91,686,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, $95,254,000,000.\n**(B)**\nOutlays, $93,640,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, $97,211,000,000.\n**(B)**\nOutlays, $94,831,000,000.\n**(6)**\nAgriculture (350):\nFiscal year 2025:\n**(A)**\nNew budget authority, $58,457,000,000.\n**(B)**\nOutlays, $41,846,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $59,875,000,000.\n**(B)**\nOutlays, $58,018,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $64,092,000,000.\n**(B)**\nOutlays, $61,792,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, $66,014,000,000.\n**(B)**\nOutlays, $64,140,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, $66,999,000,000.\n**(B)**\nOutlays, $63,775,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, $65,213,000,000.\n**(B)**\nOutlays, $62,065,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, $65,516,000,000.\n**(B)**\nOutlays, $62,226,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, $66,979,000,000.\n**(B)**\nOutlays, $63,432,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, $68,738,000,000.\n**(B)**\nOutlays, $64,825,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, $70,130,000,000.\n**(B)**\nOutlays, $66,347,000,000.\n**(7)**\nCommerce and Housing Credit (370):\nFiscal year 2025:\n**(A)**\nNew budget authority, $12,477,000,000.\n**(B)**\nOutlays, -$18,175,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $33,817,000,000.\n**(B)**\nOutlays, -$207,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $29,807,000,000.\n**(B)**\nOutlays, $8,387,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, -$55,092,000,000.\n**(B)**\nOutlays, -$64,213,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, $27,308,000,000.\n**(B)**\nOutlays, $17,149,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, $27,501,000,000.\n**(B)**\nOutlays, $14,043,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, $27,776,000,000.\n**(B)**\nOutlays, $9,486,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, $28,233,000,000.\n**(B)**\nOutlays, $6,788,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, $22,118,000,000.\n**(B)**\nOutlays, -$2,412,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, $31,836,000,000.\n**(B)**\nOutlays, $4,308,000,000.\n**(8)**\nTransportation (400):\nFiscal year 2025:\n**(A)**\nNew budget authority, $173,158,000,000.\n**(B)**\nOutlays, $144,771,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $176,249,000,000.\n**(B)**\nOutlays, $154,625,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $178,411,000,000.\n**(B)**\nOutlays, $162,925,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, $180,607,000,000.\n**(B)**\nOutlays, $171,610,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, $182,610,000,000.\n**(B)**\nOutlays, $175,967,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, $179,144,000,000.\n**(B)**\nOutlays, $174,442,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, $181,099,000,000.\n**(B)**\nOutlays, $178,314,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, $189,966,000,000.\n**(B)**\nOutlays, $187,367,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, $192,692,000,000.\n**(B)**\nOutlays, $191,213,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, $195,495,000,000.\n**(B)**\nOutlays, $194,754,000,000.\n**(9)**\nCommunity and Regional Development (450):\nFiscal year 2025:\n**(A)**\nNew budget authority, $87,762,000,000.\n**(B)**\nOutlays, $78,752,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $89,366,000,000.\n**(B)**\nOutlays, $69,845,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $91,267,000,000.\n**(B)**\nOutlays, $74,426,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, $92,897,000,000.\n**(B)**\nOutlays, $75,604,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, $94,812,000,000.\n**(B)**\nOutlays, $77,850,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, $96,811,000,000.\n**(B)**\nOutlays, $82,903,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, $98,774,000,000.\n**(B)**\nOutlays, $86,364,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, $100,621,000,000.\n**(B)**\nOutlays, $88,685,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, $102,711,000,000.\n**(B)**\nOutlays, $90,723,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, $104,818,000,000.\n**(B)**\nOutlays, $93,005,000,000.\n**(10)**\nEducation, Training, Employment, and Social Services (500):\nFiscal year 2025:\n**(A)**\nNew budget authority, $149,303,000,000.\n**(B)**\nOutlays, $171,916,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $152,714,000,000.\n**(B)**\nOutlays, $151,605,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $155,153,000,000.\n**(B)**\nOutlays, $150,979,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, $157,971,000,000.\n**(B)**\nOutlays, $152,819,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, $160,952,000,000.\n**(B)**\nOutlays, $155,502,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, $163,865,000,000.\n**(B)**\nOutlays, $158,383,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, $166,854,000,000.\n**(B)**\nOutlays, $161,312,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, $170,223,000,000.\n**(B)**\nOutlays, $164,486,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, $173,784,000,000.\n**(B)**\nOutlays, $167,792,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, $176,834,000,000.\n**(B)**\nOutlays, $170,876,000,000.\n**(11)**\nHealth (550):\nFiscal year 2025:\n**(A)**\nNew budget authority, $945,070,000,000.\n**(B)**\nOutlays, $961,180,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $992,460,000,000.\n**(B)**\nOutlays, $976,705,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $1,021,428,000,000.\n**(B)**\nOutlays, $1,021,884,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, $1,056,522,000,000.\n**(B)**\nOutlays, $1,053,318,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, $1,099,999,000,000.\n**(B)**\nOutlays, $1,095,100,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, $1,144,066,000,000.\n**(B)**\nOutlays, $1,133,456,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, $1,177,723,000,000.\n**(B)**\nOutlays, $1,176,648,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, $1,228,051,000,000.\n**(B)**\nOutlays, $1,218,203,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, $1,278,134,000,000.\n**(B)**\nOutlays, $1,267,299,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, $1,311,280,000,000.\n**(B)**\nOutlays, $1,300,233,000,000.\n**(12)**\nMedicare (570):\nFiscal year 2025:\n**(A)**\nNew budget authority, $950,891,000,000.\n**(B)**\nOutlays, $950,641,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $1,007,431,000,000.\n**(B)**\nOutlays, $1,009,161,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $1,067,229,000,000.\n**(B)**\nOutlays, $1,066,832,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, $1,210,420,000,000.\n**(B)**\nOutlays, $1,208,952,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, $1,126,357,000,000.\n**(B)**\nOutlays, $1,125,928,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, $1,276,602,000,000.\n**(B)**\nOutlays, $1,276,291,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, $1,358,554,000,000.\n**(B)**\nOutlays, $1,358,476,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, $1,445,982,000,000.\n**(B)**\nOutlays, $1,445,966,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, $1,664,590,000,000.\n**(B)**\nOutlays, $1,664,595,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, $1,667,328,000,000.\n**(B)**\nOutlays, $1,667,321,000,000.\n**(13)**\nIncome Security (600):\nFiscal year 2025:\n**(A)**\nNew budget authority, $712,446,000,000.\n**(B)**\nOutlays, $709,132,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $702,007,000,000.\n**(B)**\nOutlays, $699,086,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $703,592,000,000.\n**(B)**\nOutlays, $698,238,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, $722,280,000,000.\n**(B)**\nOutlays, $721,948,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, $724,420,000,000.\n**(B)**\nOutlays, $710,279,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, $743,824,000,000.\n**(B)**\nOutlays, $735,068,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, $757,021,000,000.\n**(B)**\nOutlays, $747,723,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, $775,456,000,000.\n**(B)**\nOutlays, $765,416,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, $796,775,000,000.\n**(B)**\nOutlays, $793,408,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, $805,597,000,000.\n**(B)**\nOutlays, $795,238,000,000.\n**(14)**\nSocial Security (650):\nFiscal year 2025:\n**(A)**\nNew budget authority, $67,259,000,000.\n**(B)**\nOutlays, $67,259,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $81,690,000,000.\n**(B)**\nOutlays, $81,690,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $89,447,000,000.\n**(B)**\nOutlays, $89,447,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, $94,419,000,000.\n**(B)**\nOutlays, $94,419,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, $100,138,000,000.\n**(B)**\nOutlays, $100,138,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, $106,208,000,000.\n**(B)**\nOutlays, $106,208,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, $112,114,000,000.\n**(B)**\nOutlays, $112,114,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, $118,485,000,000.\n**(B)**\nOutlays, $118,485,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, $125,325,000,000.\n**(B)**\nOutlays, $125,325,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, $132,539,000,000.\n**(B)**\nOutlays, $132,539,000,000.\n**(15)**\nVeterans Benefits and Services (700):\nFiscal year 2025:\n**(A)**\nNew budget authority, $361,349,000,000.\n**(B)**\nOutlays, $357,760,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $382,625,000,000.\n**(B)**\nOutlays, $378,862,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $404,665,000,000.\n**(B)**\nOutlays, $401,379,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, $427,402,000,000.\n**(B)**\nOutlays, $444,309,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, $447,832,000,000.\n**(B)**\nOutlays, $422,387,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, $466,693,000,000.\n**(B)**\nOutlays, $461,795,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, $486,796,000,000.\n**(B)**\nOutlays, $481,715,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, $507,269,000,000.\n**(B)**\nOutlays, $502,734,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, $528,816,000,000.\n**(B)**\nOutlays, $548,814,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, $550,747,000,000.\n**(B)**\nOutlays, $547,878,000,000.\n**(16)**\nAdministration of Justice (750):\nFiscal year 2025:\n**(A)**\nNew budget authority, $83,111,000,000.\n**(B)**\nOutlays, $85,235,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $90,002,000,000.\n**(B)**\nOutlays, $87,682,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $89,047,000,000.\n**(B)**\nOutlays, $87,256,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, $91,066,000,000.\n**(B)**\nOutlays, $89,499,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, $93,553,000,000.\n**(B)**\nOutlays, $91,849,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, $96,019,000,000.\n**(B)**\nOutlays, $94,292,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, $98,328,000,000.\n**(B)**\nOutlays, $96,277,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, $105,979,000,000.\n**(B)**\nOutlays, $103,293,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, $108,710,000,000.\n**(B)**\nOutlays, $105,827,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, $111,020,000,000.\n**(B)**\nOutlays, $108,460,000,000.\n**(17)**\nGeneral Government (800):\nFiscal year 2025:\n**(A)**\nNew budget authority, $10,089,000,000.\n**(B)**\nOutlays, $37,960,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $30,678,000,000.\n**(B)**\nOutlays, $38,289,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $32,078,000,000.\n**(B)**\nOutlays, $38,267,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, $33,007,000,000.\n**(B)**\nOutlays, $37,965,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, $33,784,000,000.\n**(B)**\nOutlays, $37,804,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, $34,628,000,000.\n**(B)**\nOutlays, $37,998,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, $35,261,000,000.\n**(B)**\nOutlays, $37,038,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, $36,204,000,000.\n**(B)**\nOutlays, $36,321,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, $36,975,000,000.\n**(B)**\nOutlays, $36,772,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, $37,697,000,000.\n**(B)**\nOutlays, $37,281,000,000.\n**(18)**\nNet Interest (900):\nFiscal year 2025:\n**(A)**\nNew budget authority, $1,017,513,000,000.\n**(B)**\nOutlays, $1,017,513,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $1,068,222,000,000.\n**(B)**\nOutlays, $1,068,222,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $1,132,963,000,000.\n**(B)**\nOutlays, $1,132,963,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, $1,220,157,000,000.\n**(B)**\nOutlays, $1,220,157,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, $1,298,170,000,000.\n**(B)**\nOutlays, $1,298,170,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, $1,370,842,000,000.\n**(B)**\nOutlays, $1,370,842,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, $1,451,680,000,000.\n**(B)**\nOutlays, $1,451,680,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, $1,536,261,000,000.\n**(B)**\nOutlays, $1,536,261,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, $1,615,954,000,000.\n**(B)**\nOutlays, $1,615,954,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, $1,705,576,000,000.\n**(B)**\nOutlays, $1,705,576,000,000.\n**(19)**\nAllowances (920):\nFiscal year 2025:\n**(A)**\nNew budget authority, $0.\n**(B)**\nOutlays, $0.\nFiscal year 2026:\n**(A)**\nNew budget authority, $0.\n**(B)**\nOutlays, $0.\nFiscal year 2027:\n**(A)**\nNew budget authority, $0.\n**(B)**\nOutlays, $0.\nFiscal year 2028:\n**(A)**\nNew budget authority, $0.\n**(B)**\nOutlays, $0.\nFiscal year 2029:\n**(A)**\nNew budget authority, $0.\n**(B)**\nOutlays, $0.\nFiscal year 2030:\n**(A)**\nNew budget authority, $0.\n**(B)**\nOutlays, $0.\nFiscal year 2031:\n**(A)**\nNew budget authority, $0.\n**(B)**\nOutlays, $0.\nFiscal year 2032:\n**(A)**\nNew budget authority, $0.\n**(B)**\nOutlays, $0.\nFiscal year 2033:\n**(A)**\nNew budget authority, $0.\n**(B)**\nOutlays, $0.\nFiscal year 2034:\n**(A)**\nNew budget authority, $0.\n**(B)**\nOutlays, $0.\n**(20)**\nGovernment-wide Savings and Adjustments (930):\nFiscal year 2025:\n**(A)**\nNew budget authority, -$103,925,000,000.\n**(B)**\nOutlays, -$103,925,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, $12,298,000,000.\n**(B)**\nOutlays, $12,298,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, $11,337,000,000.\n**(B)**\nOutlays, $11,337,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, $10,827,000,000.\n**(B)**\nOutlays, $10,827,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, -$40,933,000,000.\n**(B)**\nOutlays, -$40,933,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, -$42,418,000,000.\n**(B)**\nOutlays, -$42,418,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, -$43,979,000,000.\n**(B)**\nOutlays, -$43,979,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, -$45,577,000,000.\n**(B)**\nOutlays, -$45,577,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, -$47,393,000,000.\n**(B)**\nOutlays, -$47,393,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, -$49,425,000,000.\n**(B)**\nOutlays, -$49,425,000,000.\n**(21)**\nUndistributed Offsetting Receipts (950):\nFiscal year 2025:\n**(A)**\nNew budget authority, -$127,603,000,000.\n**(B)**\nOutlays, -$127,603,000,000.\nFiscal year 2026:\n**(A)**\nNew budget authority, -$135,110,000,000.\n**(B)**\nOutlays, -$135,110,000,000.\nFiscal year 2027:\n**(A)**\nNew budget authority, -$137,883,000,000.\n**(B)**\nOutlays, -$137,883,000,000.\nFiscal year 2028:\n**(A)**\nNew budget authority, -$141,145,000,000.\n**(B)**\nOutlays, -$141,165,000,000.\nFiscal year 2029:\n**(A)**\nNew budget authority, -$145,400,000,000.\n**(B)**\nOutlays, -$145,407,000,000.\nFiscal year 2030:\n**(A)**\nNew budget authority, -$149,582,000,000.\n**(B)**\nOutlays, -$149,581,000,000.\nFiscal year 2031:\n**(A)**\nNew budget authority, -$154,014,000,000.\n**(B)**\nOutlays, -$154,013,000,000.\nFiscal year 2032:\n**(A)**\nNew budget authority, -$160,114,000,000.\n**(B)**\nOutlays, -$160,113,000,000.\nFiscal year 2033:\n**(A)**\nNew budget authority, -$166,102,000,000.\n**(B)**\nOutlays, -$166,101,000,000.\nFiscal year 2034:\n**(A)**\nNew budget authority, -$171,015,000,000.\n**(B)**\nOutlays, -$171,014,000,000.\nII\nReconciliation in the House of Representatives\n#### 201. Reconciliation in the House\n##### (a) Spending reconciliation instructions\n**(1) Committee on armed services**\nThe Committee on Armed Services of the House of Representatives shall submit changes in laws within its jurisdiction that increase the deficit by not more than $100,000,000,000 for the period of fiscal years 2025 through 2028, and $0 for the period of fiscal years 2029 through 2034.\n**(2) Committee on homeland security**\nThe Committee on Homeland Security of the House of Representatives shall submit changes in laws within its jurisdiction that increase the deficit by not more than $50,000,000,000 for the period of fiscal years 2025 through 2028, and $0 for the period of fiscal years 2029 through 2034.\n**(3) Committee on the judiciary**\nThe Committee on the Judiciary of the House of Representatives shall submit changes in laws within its jurisdiction that increase the deficit by not more than $50,000,000,000 for the period of fiscal years 2025 through 2028, and $0 for the period of fiscal years 2029 through 2034.\n##### (b) Deficit Reduction Reconciliation Instructions\n**(1) Committee on agriculture**\nThe Committee on Agriculture of the House of Representatives shall submit changes in laws within its jurisdiction that reduce the deficit by not less than $5,000,000,000 for the period of fiscal years 2025 through 2034.\n**(2) Committee on education and workforce**\nThe Committee on Education and Workforce of the House of Representatives shall submit changes in laws within its jurisdiction that reduce the deficit by not less than $246,800,000,000 for the period of fiscal years 2025 through 2034.\n**(3) Committee on energy and commerce**\nThe Committee on Energy and Commerce of the House of Representatives shall submit changes in laws within its jurisdiction to reduce the deficit by not less than $200,000,000,000 for the period of fiscal years 2025 through 2034.\n**(4) Committee on the judiciary**\nThe Committee on the Judiciary of the House of Representatives shall submit changes in laws within its jurisdiction that reduce the deficit by not less than $10,000,000,000 for the period of fiscal years 2025 through 2034.\n**(5) Committee on ways and means**\nThe Committee on Ways and Means of the House of Representatives shall submit changes in laws within its jurisdiction that reduce the deficit by not less than $24,500,000,000 for the period of fiscal years 2025 through 2034.\n##### (c) Increase in the statutory debt limit\nThe Committee on Ways and Means of the House of Representatives shall submit changes in laws within its jurisdiction that increases the statutory debt limit by $4,000,000,000,000.\n##### (d) Submissions\nNot later than February 27, 2025, the committees named in subsections (a), (b), and (c) shall submit their recommendations to the Committee on the Budget of the House of Representatives to carry out this section.\nIII\nPolicy Statements in the House of Representatives\n#### 301. Policy statement on Federal spending\n##### (a) Findings\nThe House finds the following:\n**(1)**\nThe United States faces a dire fiscal crisis that poses a threat to our national security and economic wellbeing.\n**(2)**\nGross Federal debt has surpassed $36 trillion and is now 122.94 percent of our national gross domestic product. Left on its current course, the Congressional Budget Office estimates it will reach nearly $60 trillion by fiscal year 2035.\n**(3)**\nPrior to the COVID\u201319 pandemic, Federal spending was already irresponsible with a Federal deficit of $983.6 billion and $5.46 trillion in total outlays in fiscal year 2019, which then skyrocketed to $7.94 trillion the following year.\n**(4)**\nEven now, years after the pandemic, fiscal year 2024 Federal outlays were $6.8 trillion and continue to significantly outpace pre-COVID levels. This is unsustainable.\n**(5)**\nIt is critical that the United States rein in the Federal Government\u2019s out-of-control spending to set our nation on a better fiscal path.\n**(6)**\nPresident Trump\u2019s fiscal year 2021 budget, released just before the pandemic, projected total budget outlays would reach $5.451 trillion this year. If adjusted to protect current Social Security and Medicare spending, as well as reflect existing debt service obligations, total budget outlays would be $6.057 trillion.\n##### (b) Policy on Federal spending\nIt is the policy of this concurrent resolution that restoring Federal spending levels that existed prior to the COVID\u201319 pandemic, adjusted to protect current Social Security and Medicare spending and reflect existing debt service obligations, and that it shall be the objective of the House to reach total budget outlays of $6.057 trillion this fiscal year or less.",
      "versionDate": "2025-02-10",
      "versionType": "IH"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Budget deficits and national debt",
            "updateDate": "2025-06-13T18:49:10Z"
          },
          {
            "name": "Budget process",
            "updateDate": "2025-06-13T18:49:06Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-06-13T18:49:21Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-06-13T18:49:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Economics and Public Finance",
        "updateDate": "2025-05-02T15:15:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-10",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hconres10",
          "measure-number": "10",
          "measure-type": "hconres",
          "orig-publish-date": "2025-02-10",
          "originChamber": "HOUSE",
          "update-date": "2025-05-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hconres10v00",
            "update-date": "2025-05-02"
          },
          "action-date": "2025-02-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Emergency Border Control Resolution</strong></p><p>This concurrent resolution establishes the congressional budget for the federal government for FY2025, sets forth budgetary levels for FY2026-FY2034, and provides reconciliation instructions for legislation that increases or decreases the deficit and increases the statutory debt limit by specified amounts.\u00a0</p><p>The resolution recommends levels and amounts for FY2025-FY2034 for</p><ul><li>federal revenues,</li><li>new budget authority,</li><li>budget outlays,</li><li>deficits (on-budget),</li><li>debt subject to limit,\u00a0</li><li>debt held by the public, and</li><li>the major functional categories of spending.</li></ul><p>The resolution includes reconciliation instructions that direct several\u00a0House committees to submit legislation that will increase or decrease the deficit and increase the statutory debt limit by specified amounts. The committees must submit the legislation to the House Budget Committee by February 27, 2025.\u00a0</p><p>(Under current law, reconciliation bills are considered by Congress using expedited legislative procedures that prevent a filibuster and restrict amendments in the Senate.)</p><p>Finally, the resolution specifies that it is the policy of this resolution that (1) federal spending levels should be restored to the levels that existed prior to the COVID-19 pandemic, adjusted to protect current Social Security and Medicare spending and reflect existing debt service obligations; and (2) it shall be the objective of the House to reach total budget outlays of $6.057 trillion or less this fiscal year.</p>"
        },
        "title": "Emergency Border Control Resolution"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hconres/BILLSUM-119hconres10.xml",
    "summary": {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Emergency Border Control Resolution</strong></p><p>This concurrent resolution establishes the congressional budget for the federal government for FY2025, sets forth budgetary levels for FY2026-FY2034, and provides reconciliation instructions for legislation that increases or decreases the deficit and increases the statutory debt limit by specified amounts.\u00a0</p><p>The resolution recommends levels and amounts for FY2025-FY2034 for</p><ul><li>federal revenues,</li><li>new budget authority,</li><li>budget outlays,</li><li>deficits (on-budget),</li><li>debt subject to limit,\u00a0</li><li>debt held by the public, and</li><li>the major functional categories of spending.</li></ul><p>The resolution includes reconciliation instructions that direct several\u00a0House committees to submit legislation that will increase or decrease the deficit and increase the statutory debt limit by specified amounts. The committees must submit the legislation to the House Budget Committee by February 27, 2025.\u00a0</p><p>(Under current law, reconciliation bills are considered by Congress using expedited legislative procedures that prevent a filibuster and restrict amendments in the Senate.)</p><p>Finally, the resolution specifies that it is the policy of this resolution that (1) federal spending levels should be restored to the levels that existed prior to the COVID-19 pandemic, adjusted to protect current Social Security and Medicare spending and reflect existing debt service obligations; and (2) it shall be the objective of the House to reach total budget outlays of $6.057 trillion or less this fiscal year.</p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119hconres10"
    },
    "title": "Emergency Border Control Resolution"
  },
  "summaries": [
    {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Emergency Border Control Resolution</strong></p><p>This concurrent resolution establishes the congressional budget for the federal government for FY2025, sets forth budgetary levels for FY2026-FY2034, and provides reconciliation instructions for legislation that increases or decreases the deficit and increases the statutory debt limit by specified amounts.\u00a0</p><p>The resolution recommends levels and amounts for FY2025-FY2034 for</p><ul><li>federal revenues,</li><li>new budget authority,</li><li>budget outlays,</li><li>deficits (on-budget),</li><li>debt subject to limit,\u00a0</li><li>debt held by the public, and</li><li>the major functional categories of spending.</li></ul><p>The resolution includes reconciliation instructions that direct several\u00a0House committees to submit legislation that will increase or decrease the deficit and increase the statutory debt limit by specified amounts. The committees must submit the legislation to the House Budget Committee by February 27, 2025.\u00a0</p><p>(Under current law, reconciliation bills are considered by Congress using expedited legislative procedures that prevent a filibuster and restrict amendments in the Senate.)</p><p>Finally, the resolution specifies that it is the policy of this resolution that (1) federal spending levels should be restored to the levels that existed prior to the COVID-19 pandemic, adjusted to protect current Social Security and Medicare spending and reflect existing debt service obligations; and (2) it shall be the objective of the House to reach total budget outlays of $6.057 trillion or less this fiscal year.</p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119hconres10"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres10ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Emergency Border Control Resolution",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T04:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Emergency Border Control Resolution",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Establishing the congressional budget for the United States Government for fiscal year 2025 and setting forth the appropriate budgetary levels for fiscal years 2026 through 2034.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T04:18:53Z"
    }
  ]
}
```
