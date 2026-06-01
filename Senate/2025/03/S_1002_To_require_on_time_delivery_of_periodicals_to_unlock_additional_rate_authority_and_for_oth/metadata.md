# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1002?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1002
- Title: Deliver for Democracy Act
- Congress: 119
- Bill type: S
- Bill number: 1002
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2025-12-05T22:05:43Z
- Update date including text: 2025-12-05T22:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1002",
    "number": "1002",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "Deliver for Democracy Act",
    "type": "S",
    "updateDate": "2025-12-05T22:05:43Z",
    "updateDateIncludingText": "2025-12-05T22:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-12",
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
          "date": "2025-03-12T21:10:29Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "SD"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MN"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "ND"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "OR"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "OR"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MN"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-03-12",
      "state": "VT"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1002is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1002\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mr. Welch (for himself, Mr. Rounds , Ms. Klobuchar , Mr. Hoeven , Mr. Wyden , Mr. Merkley , Ms. Smith , Mr. Sanders , and Ms. Baldwin ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require on-time delivery of periodicals to unlock additional rate authority, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Deliver for Democracy Act .\n#### 2. Additional rate authority for periodicals\nNot later than 1 year after the date of enactment of this Act, the Postal Regulatory Commission shall amend section 3030.222 of title 39, Code of Federal Regulations, to provide that, for any fiscal year ending after the date of enactment of this Act, the Commission shall not authorize the United States Postal Service any additional rate authority with respect to periodicals under that section for the following fiscal year, unless the Commission determines that the United States Postal Service achieved\u2014\n**(1)**\na 95 percent on-time delivery performance for periodicals during the fiscal year of the determination, as measured by the service standards in effect on the date of enactment of this Act; or\n**(2)**\nan increase in the on-time delivery performance for periodicals during the fiscal year of the determination, as measured by the service standards in effect on the date of enactment of this Act, of not less than 2 percentage points, as compared to the on-time delivery performance percentage in the fiscal year before, on, or after the date of enactment of this Act in which the on-time delivery performance percentage is the highest measured, as measured by such service standards.\n#### 3. Annual progress report\n##### (a) Report required\n**(1) In general**\nSubject to subsections (c) and (d), the Postmaster General shall submit to the Postal Regulatory Commission and make publicly available an annual report on the progress of the United States Postal Service in including in the periodical service performance measurements of the Postal Service on-time performance data for in-county and out-of-county newspaper mail that is entered and accepted at each delivery unit for delivery.\n**(2) Stakeholder input**\nIn carrying out the report requirement under paragraph (1), the Postmaster General shall solicit feedback from relevant stakeholders.\n##### (b) Implementation of report requirement\nIf the relevant information is not available for each individually-addressed piece of mail for purposes of a report required under subsection (a), the Postal Regulatory Commission, in consultation with the Postmaster General, shall develop a system for generating service performance data for use in the report by producing digital information for relevant mail bundles.\n##### (c) Termination of report requirement\nThe Postmaster General shall submit and make publicly available the report described in subsection (a) annually until the date on which the Postal Regulatory Commission determines that the United States Postal Service has incorporated the categories of mail described in subsection (a), or any other relevant mail categories used in the report in accordance with subsection (d), into the existing applicable service performance measurements.\n##### (d) Proxy information\n**(1) In general**\nIf the Postal Regulatory Commission and the Postmaster General jointly determine that identifying newspaper mail within the periodicals mail category is not practicable for purposes of a report under subsection (a), the Postal Regulatory Commission may determine what information with respect to the closest relevant mail category the Postmaster General may use in the report.\n**(2) Public report on determination**\nIf the Postal Regulatory Commission and the Postmaster General make the determination described in paragraph (1), the Postal Regulatory Commission and the Postmaster General shall make publicly available a report describing the process and rationale for the determination, including a description of\u2014\n**(A)**\nthe potential costs for the United States Postal Service and applicable businesses resulting from the report requirement under subsection (a);\n**(B)**\nthe ability of the Postmaster General to ascertain accurate results for inclusion in the report under subsection (a); and\n**(C)**\nany other factor contributing to the determination.\n#### 4. GAO study and report\n##### (a) Study\nThe Comptroller General of the United States shall conduct a study of alternative pricing schemes and other options for the United States Postal Service that would improve the financial position of periodicals and other products that do not cover their costs and evaluate the potential impact of such alternative pricing schemes and other options.\n##### (b) Report\nNot later than 2 years after the date of enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Government Reform of the House of Representatives a report on the study conducted under subsection (a).",
      "versionDate": "2025-03-12",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-14",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "2098",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Deliver for Democracy Act",
      "type": "HR"
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-20T15:18:19Z"
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
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1002is.xml"
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
      "title": "Deliver for Democracy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Deliver for Democracy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require on-time delivery of periodicals to unlock additional rate authority, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:34Z"
    }
  ]
}
```
