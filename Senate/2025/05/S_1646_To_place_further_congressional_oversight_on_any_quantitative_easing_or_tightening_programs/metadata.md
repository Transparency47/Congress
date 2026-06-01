# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1646?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1646
- Title: Rein in the Federal Reserve Act
- Congress: 119
- Bill type: S
- Bill number: 1646
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2025-05-27T13:08:19Z
- Update date including text: 2025-05-27T13:08:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1646",
    "number": "1646",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Rein in the Federal Reserve Act",
    "type": "S",
    "updateDate": "2025-05-27T13:08:19Z",
    "updateDateIncludingText": "2025-05-27T13:08:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-05-07T20:53:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1646is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1646\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mr. Scott of Florida (for himself and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo place further congressional oversight on any quantitative easing or tightening programs or any emergency lending programs of the Board of Governors of the Federal Reserve System, to require reports to Congress relating to those programs, to require congressional approval of the extension of those programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rein in the Federal Reserve Act .\n#### 2. Federal Reserve programs\n##### (a) Reporting required for certain programs\n**(1) In general**\nUpon initiating any quantitative easing or tightening program or any emergency lending program under the first or third undesignated paragraph of section 13 of the Federal Reserve Act ( 12 U.S.C. 342 , 343), the Board of Governors of the Federal Reserve System (referred to in this section as the Board of Governors ) shall submit to Congress, the Committee on Banking, Housing, and Urban Affairs of the Senate , and the Committee on Ways and Means of the House of Representatives , and make publicly available, a report on the program.\n**(2) Report frequency**\nWith respect to a report under paragraph (1), the Board of Governors shall submit an updated report not less frequently than once every 90 days until\u2014\n**(A)**\nthe program to which the report applies ends; and\n**(B)**\nall assets purchased under the program described in subparagraph (A) have been removed from the balance sheet indicating the total assets of the Board of Governors.\n**(3) Report contents**\nA report described in paragraph (1) shall include, with respect to the program to which the report applies\u2014\n**(A)**\nthe rationale for initiating the program;\n**(B)**\nan estimated projection of\u2014\n**(i)**\nmark-to-market losses;\n**(ii)**\nany addition of funds to the money supply;\n**(iii)**\nany impact on the amount of the public debt of the Federal Government; and\n**(iv)**\nany potential losses to the taxpayers of the United States;\n**(C)**\nif applicable, an economic impact assessment and projections on the interaction of the program with domestic and global markets;\n**(D)**\nan outline of the pace, size, and specific financial products purchased and anticipated to be purchased under the program;\n**(E)**\na plan with a specific timeline for ending the program by a date that is not later than 3 years after the date on which the Board of Governors initiates the program, such that the program does not become part of the standard operations of the Board of Governors, including, if applicable, a description of the rationale for why the program should extend beyond 1 year; and\n**(F)**\nan assessment of any potential risks to price stability that may result from the program.\n##### (b) Limitation on duration and renewal of programs\nThe Board of Governors shall not engage in any program described in subsection (a)(1) for a period longer than 1 year without authorization from Congress.\n##### (c) Disapproval of standing programs\nWith respect to any program described in subsection (a)(1)\u2014\n**(1)**\nthe report submitted under that subsection shall be considered to be the report required under section 801(a)(1)(A) of title 5, United States Code; and\n**(2)**\nthe program shall be subject to the procedure for congressional disapproval under chapter 8 of title 5, United States Code.",
      "versionDate": "2025-05-07",
      "versionType": "Introduced in Senate"
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-27T13:08:19Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1646is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Rein in the Federal Reserve Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T04:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rein in the Federal Reserve Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to place further congressional oversight on any quantitative easing or tightening program or any emergency lending programs of the Board of Governors of the Federal Reserve System, to require reports to Congress relating to those programs, to require congressional approval of the extension of those programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:33:21Z"
    }
  ]
}
```
