# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2817?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2817
- Title: Fed Integrity and Independence Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2817
- Origin chamber: Senate
- Introduced date: 2025-09-16
- Update date: 2025-09-29T13:44:11Z
- Update date including text: 2025-09-29T13:44:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in Senate
- 2025-09-16 - IntroReferral: Introduced in Senate
- 2025-09-16 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-09-16: Introduced in Senate

## Actions

- 2025-09-16 - IntroReferral: Introduced in Senate
- 2025-09-16 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2817",
    "number": "2817",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "G000574",
        "district": "",
        "firstName": "Ruben",
        "fullName": "Sen. Gallego, Ruben [D-AZ]",
        "lastName": "Gallego",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Fed Integrity and Independence Act of 2025",
    "type": "S",
    "updateDate": "2025-09-29T13:44:11Z",
    "updateDateIncludingText": "2025-09-29T13:44:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-16",
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
      "actionDate": "2025-09-16",
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
          "date": "2025-09-16T19:06:42Z",
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
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NJ"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MD"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MD"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NV"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "DE"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "GA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2817is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2817\nIN THE SENATE OF THE UNITED STATES\nSeptember 16, 2025 Mr. Gallego (for himself, Mr. Kim , Ms. Warren , Ms. Alsobrooks , Mr. Van Hollen , Ms. Cortez Masto , Ms. Blunt Rochester , and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Federal Reserve Act to prohibit dual appointments of employees of the Federal Reserve System, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fed Integrity and Independence Act of 2025 .\n#### 2. Sense of Congress\n##### (a) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe Federal Reserve System plays a critical role in maintaining the stability of the economy of the United States by conducting monetary policy, supervising and regulating financial institutions, and supporting the payments system;\n**(2)**\nhistorically, the insulation of the Federal Reserve System from political interference has been essential in preventing an electoral consideration or partisan agenda from driving any monetary policy decision;\n**(3)**\nthe credibility and effectiveness of the Federal Reserve System depend on the ability of the Federal Reserve System to operate independently of any short-term political pressure, particularly from an elected official or individual in a position of public trust;\n**(4)**\nthe presence of a current government official, Member of Congress, or other politically affiliated individual in a role within the Federal Reserve System raises legitimate concerns about conflict of interest and undue influence; and\n**(5)**\nthe purpose of this Act, and the amendments made by this Act, is to strengthen the institutional integrity and independence of the Federal Reserve System by more categorically prohibiting dual appointments, preventing conflicts of interest, and ensuring a clear separation between a political actor and a monetary policy decision.\n#### 3. Prohibition of Dual Appointment\n##### (a) Board of Governors\nThe fourth sentence of the first undesignated paragraph of section 10 of the Federal Reserve Act ( 12 U.S.C. 241 ) is amended by striking business of the Board and shall each receive and inserting business of the Board, may not simultaneously hold any other office, position, or employment for which the member is appointed by the President, including under a leave of absence from such other office, position, or employment, and shall each receive .\n##### (b) Federal Reserve Bank Presidents, Vice Presidents, Officers, and Employees\nThe fifth subparagraph of the fourth undesignated paragraph of section 4 of the Federal Reserve Act ( 12 U.S.C. 341 ) is amended by adding at the end the following: A president, vice president, officer, or employee of the bank may not simultaneously hold any other office, position, or employment for which the president, vice president, officer, or employee is appointed by the President, including under a leave of absence from such other office, position, or employment. .\n##### (c) Federal Reserve Bank Board of Directors\nThe ninth undesignated paragraph of section 4 of the Federal Reserve Act ( 12 U.S.C. 302 ) is amended by adding at the end the following: A member of such board of directors may not simultaneously hold any other office, position, or employment for which the member is appointed by the President, including under a leave of absence from such other office, position, or employment. .",
      "versionDate": "2025-09-16",
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
        "updateDate": "2025-09-29T13:44:11Z"
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
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2817is.xml"
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
      "title": "Fed Integrity and Independence Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-27T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fed Integrity and Independence Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-27T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Reserve Act to prohibit dual appointments of employees of the Federal Reserve System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-27T03:48:22Z"
    }
  ]
}
```
