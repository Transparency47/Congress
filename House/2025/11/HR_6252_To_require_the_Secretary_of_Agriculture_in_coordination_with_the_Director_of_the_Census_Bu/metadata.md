# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6252?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6252
- Title: Food Assurance and Security Act
- Congress: 119
- Bill type: HR
- Bill number: 6252
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2026-05-16T08:07:14Z
- Update date including text: 2026-05-16T08:07:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-21: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-21 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-13 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-11-21: Introduced in House

## Actions

- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-21 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-13 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-21",
    "latestAction": {
      "actionDate": "2025-11-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6252",
    "number": "6252",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001324",
        "district": "1",
        "firstName": "Wesley",
        "fullName": "Rep. Bell, Wesley [D-MO-1]",
        "lastName": "Bell",
        "party": "D",
        "state": "MO"
      }
    ],
    "title": "Food Assurance and Security Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:14Z",
    "updateDateIncludingText": "2026-05-16T08:07:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-21",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-21",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-11-21T14:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T19:59:24Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-21T14:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "IN"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "DC"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "OR"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6252ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6252\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Mr. Bell (for himself and Ms. Barrag\u00e1n ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Secretary of Agriculture, in coordination with the Director of the Census Bureau, to maintain an interagency food security measurement program to coordinate the annual collection, analysis, and reporting of data on food insecurity and hunger.\n#### 1. Short title\nThis Act may be cited as the Food Assurance and Security Act .\n#### 2. Interagency food security measurement program\n##### (a) Interagency food security measurement program\nThe Secretary of Agriculture, in coordination with the Director of the Census Bureau, shall establish and maintain an interagency food security measurement program to coordinate the annual collection, analysis, and reporting of data on food insecurity and hunger.\n##### (b) Reporting\n**(1) Population Survey**\nThe Current Population Survey conducted by the Bureau of the Census shall include a food security supplement consistent with the questionnaire issued in 2023 that includes the questions described in paragraph (3) for the years 2026 through 2028 and continuing thereafter with questions substantially similar to those described in paragraph (3) with any amendments to the questions predicated upon robust testing, and thorough review, public input, and Office of Management and Budget clearance.\n**(2) Agriculture annual reports**\nThe Secretary of Agriculture shall, with respect to the annual report issued pursuant to subsection (a)\u2014\n**(A)**\ninclude the findings related to the questions described in paragraph (3);\n**(B)**\nmake the report publicly available on the website of the Department; and\n**(C)**\nsubmit such report to Congress.\n**(3) Questions described**\nThe questions described in this paragraph are as follows:\n**(A)**\nWas the answer often, sometimes, or never true for you in the last 12 months for each of the following:\n**(i)**\nWe worried whether our food would run out before we got money to buy more.\n**(ii)**\nThe food that we bought just didn\u2019t last and we didn\u2019t have money to get more.\n**(iii)**\nWe couldn\u2019t afford to eat balanced meals.\n**(B)**\nIn the last 12 months, did you or other adults in the household ever cut the size of your meals or skip meals because there wasn\u2019t enough money for food?\n**(C)**\nIf the answer is yes with respect to subparagraph (B), how often did this happen\u2014almost every month, some months but not every month, or in only 1 or 2 months?\n**(D)**\nIn the last 12 months, did you ever eat less than you felt you should because there wasn\u2019t enough money for food?\n**(E)**\nIn the last 12 months, were you ever hungry, but didn\u2019t eat, because there wasn\u2019t enough money for food?\n**(F)**\nIn the last 12 months, did you lose weight because there wasn\u2019t enough money for food?\n**(G)**\nIn the last 12 months, did you or other adults in your household ever not eat for a whole day because there wasn\u2019t enough money for food?\n**(H)**\nIf the answer is yes to subparagraph (G), how often did this happen\u2014almost every month, some months but not every month, or in only 1 or 2 months?\n**(I)**\nIn the case of a household that includes children ages 0 to 17, the following additional questions:\n**(i)**\nWas the answer often, sometimes, or never true for you in the last 12 months for each of the following:\n**(I)**\nWe relied on only a few kinds of low-cost food to feed our children because we were running out of money to buy food.\n**(II)**\nWe couldn\u2019t feed our children a balanced meal, because we couldn\u2019t afford that.\n**(III)**\nThe children were not eating enough because there wasn\u2019t enough money for food.\n**(ii)**\nIn the last 12 months, did you ever cut the size of any of the children\u2019s meals because there wasn\u2019t enough money for food?\n**(iii)**\nIn the last 12 months, were the children ever hungry because there wasn\u2019t enough money for food?\n**(iv)**\nIn the last 12 months, did any of the children ever skip a meal because there wasn\u2019t enough money for food?\n**(v)**\nIf the answer is yes to clause (iv), how often did this happen\u2014almost every month, some months but not every month, or in only 1 or 2 months?\n**(vi)**\nIn the last 12 months, did any of the children ever not eat for a whole day because there wasn\u2019t enough money for food?\n##### (c) Funding\n**(1) Appropriation**\nThere is appropriated to the Secretary of Agriculture such sums as may be necessary to carry out this section.\n**(2) Transfer**\nOf the funds appropriated under paragraph (1), the Secretary of Agriculture shall provide funding for the costs incurred by the Census Bureau in conducting the annual food security supplement.",
      "versionDate": "2025-11-21",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-12-12T14:27:52Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6252ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Agriculture, in coordination with the Director of the Census Bureau, to maintain an interagency food security measurement program to coordinate the annual collection, analysis, and reporting of data on food insecurity and hunger.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-12T17:24:33Z"
    },
    {
      "title": "Food Assurance and Security Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-12T14:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Food Assurance and Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-12T14:23:19Z"
    }
  ]
}
```
