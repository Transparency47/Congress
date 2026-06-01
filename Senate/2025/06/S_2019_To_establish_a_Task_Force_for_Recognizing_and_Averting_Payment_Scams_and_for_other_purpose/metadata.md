# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2019?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2019
- Title: TRAPS Act
- Congress: 119
- Bill type: S
- Bill number: 2019
- Origin chamber: Senate
- Introduced date: 2025-06-10
- Update date: 2026-04-23T11:03:25Z
- Update date including text: 2026-04-23T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-10: Introduced in Senate
- 2025-06-10 - IntroReferral: Introduced in Senate
- 2025-06-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-06-10: Introduced in Senate

## Actions

- 2025-06-10 - IntroReferral: Introduced in Senate
- 2025-06-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2019",
    "number": "2019",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "C000880",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Crapo, Mike [R-ID]",
        "lastName": "Crapo",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "TRAPS Act",
    "type": "S",
    "updateDate": "2026-04-23T11:03:25Z",
    "updateDateIncludingText": "2026-04-23T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-10",
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
      "actionDate": "2025-06-10",
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
        "item": [
          {
            "date": "2025-06-10T21:06:40Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-10T21:06:40Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "VA"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "KS"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "GA"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-07-08",
      "state": "LA"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "GA"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "NH"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "OR"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "MN"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "DE"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2026-03-10",
      "state": "AR"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2019is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2019\nIN THE SENATE OF THE UNITED STATES\nJune 10, 2025 Mr. Crapo (for himself, Mr. Warner , Mr. Moran , and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo establish a Task Force for Recognizing and Averting Payment Scams, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Taskforce for Recognizing and Averting Payment Scams Act or the TRAPS Act .\n#### 2. Definitions\nIn this Act:\n**(1) Payment**\nThe term payment means any mechanism through which an individual can electronically transfer funds to another individual via a platform or intermediary.\n**(2) Secretary**\nThe term Secretary means the Secretary of the Treasury.\n**(3) Task Force**\nThe term Task Force means the Task Force on Payment Scams established under section 3(a).\n#### 3. Task Force on Payment Scams\n##### (a) Establishment\nNot later than 90 days after the date of enactment of this Act, the Secretary shall establish a task force, to be known as the Task Force for Recognizing and Averting Payment Scams.\n##### (b) Membership\n**(1) Composition**\nThe Task Force shall be chaired by the Secretary or a designee thereof, and shall consist of representatives from the following:\n**(A)**\nThe Bureau of Consumer Financial Protection.\n**(B)**\nThe Federal Communications Commission.\n**(C)**\nThe Federal Trade Commission.\n**(D)**\nThe Department of Justice.\n**(E)**\nThe Office of the Comptroller of the Currency.\n**(F)**\nThe Board of Governors of the Federal Reserve System.\n**(G)**\nThe National Credit Union Administration.\n**(H)**\nThe Federal Deposit Insurance Corporation.\n**(I)**\nThe Financial Crimes Enforcement Network.\n**(J)**\nA representative, appointed by the Secretary in consultation with the Task Force, from a financial institution with expertise in identifying, preventing, and combating payment scams.\n**(K)**\nA representative, appointed by the Secretary in consultation with the Task Force, from a credit union with expertise in identifying, preventing, and combating payment scams.\n**(L)**\nA representative, appointed by the Secretary in consultation with the Task Force, from a digital payment network with expertise in identifying, preventing, and combating payment scams.\n**(M)**\nA representative, appointed by the Secretary in consultation with the Task Force, from a community bank.\n**(N)**\nA representative, appointed by the Secretary in consultation with the Task Force, from a consumer group.\n**(O)**\nA representative, appointed by the Secretary in consultation with the Task Force, from an industry association representing technology or online platforms.\n**(P)**\nNot more than 5 representatives appointed by the Secretary to represent victims, scam support networks, and other relevant stakeholders in order to better assist consumers and stakeholders.\n**(2) Term of appointment**\nThe term of a member of the Task Force shall continue until the termination of the Task Force.\n**(3) Vacancy**\nAny vacancy occurring in the membership of the Task Force shall be filled in the same manner in which the original appointment was made.\n##### (c) Purpose\nThe Task Force shall\u2014\n**(1)**\nexamine current trends and developments in payment scams, identify effective methods for preventing such scams, and issue recommendations to enhance efforts to identify and prevent such activities;\n**(2)**\nadopt a cross-sector approach to ensure its recommendations reflect the full scope of the issue, given that scams impact individuals across a wide range of industries, including financial services, telecommunications, and technology; and\n**(3)**\ninclude representation from stakeholders with direct experience supporting victims of scams, as well as industry participants with insight into scam tactics and prevention strategies.\n##### (d) Meetings\nThe Task Force shall meet not less than 3 times during the 1-year period beginning on the date of enactment of this Act, and thereafter at such times and places, and by such means, as the Chair of the Task Force determines to be appropriate, which may include the use of remote conference technology.\n##### (e) Duties\nThe duties of the Task Force shall include\u2014\n**(1)**\nevaluating best practices for combating methods used by scammers, including spoofed calls, scam text messages, and malicious advertisements, pop-ups, and websites;\n**(2)**\nassessing how international jurisdictions have tried to prevent payment scams;\n**(3)**\nidentifying and reviewing current methods used to scam a consumer through payment platforms;\n**(4)**\ndetermining a strategy for education programs that better equip consumers to identify, avoid, and report payment scam attempts to the appropriate authorities;\n**(5)**\ncoordinating efforts to ensure perpetrators of payment scams can be identified and pursued by law enforcement;\n**(6)**\nconsulting with other relevant stakeholders, including State, local, and Tribal agencies and financial services providers;\n**(7)**\ndetermining whether any additional Federal legislation would be beneficial for law enforcement and industry in mitigating payment scams; and\n**(8)**\nidentifying potential solutions to payment scams involving business email compromise.\n##### (f) Compensation\nEach member of the Task Force who is a civilian or employee of the United States shall serve without compensation, other than compensation to which entitled as an employee of the United States, as the case may be.\n##### (g) Report\n**(1) In general**\nNot later than 1 year after the date on which the Secretary establishes the Task Force, the Task Force shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives and make publicly available online a report detailing\u2014\n**(A)**\nthe results of the reviews and evaluations of the Task Force under subsection (e);\n**(B)**\nthe strategy identified under subsection (e);\n**(C)**\nany legislative or regulatory recommendations that would enhance the ability to detect and prevent payment scams described in subsection (e); and\n**(D)**\nrecommendations to enhance cooperation among Federal, State, local, and Tribal authorities in the investigation and prosecution of scams and other financial crimes, including harmonizing data collection, improving reporting mechanisms and streams, estimating the number of complaints and consumers affected, and evaluating the effectiveness of anti-scam training programs.\n**(2) Annual updates**\nAfter submitting an initial report required under paragraph (1), the Task Force shall, on an annual basis, submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives and make publicly available online an updated version of the report.\n##### (h) Applicable law\nChapter 4 of title 5, United States Code, shall not apply to the Task Force.\n##### (i) Sunset\nThe Task Force shall terminate on the date that is 3 years after the date on which the Task Force submits the report required under subsection (h)(1).",
      "versionDate": "2025-06-10",
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
        "actionDate": "2025-08-08",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "4936",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "TRAPS Act",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-07-02T18:31:03Z"
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
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2019is.xml"
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
      "title": "TRAPS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TRAPS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Taskforce for Recognizing and Averting Payment Scams Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a Task Force for Recognizing and Averting Payment Scams, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T02:48:25Z"
    }
  ]
}
```
