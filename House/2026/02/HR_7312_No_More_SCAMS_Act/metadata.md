# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7312?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7312
- Title: No More SCAMS Act
- Congress: 119
- Bill type: HR
- Bill number: 7312
- Origin chamber: House
- Introduced date: 2026-02-02
- Update date: 2026-04-22T08:07:33Z
- Update date including text: 2026-04-22T08:07:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-02: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-02-02: Introduced in House

## Actions

- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-02",
    "latestAction": {
      "actionDate": "2026-02-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7312",
    "number": "7312",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "K000397",
        "district": "40",
        "firstName": "Young",
        "fullName": "Rep. Kim, Young [R-CA-40]",
        "lastName": "Kim",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "No More SCAMS Act",
    "type": "HR",
    "updateDate": "2026-04-22T08:07:33Z",
    "updateDateIncludingText": "2026-04-22T08:07:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-02",
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
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-02",
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
          "date": "2026-02-02T14:02:15Z",
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
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "MN"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "SC"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "NY"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7312ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7312\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 2, 2026 Mrs. Kim (for herself and Mr. Stauber ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo establish a national task force to investigate and combat fraud involving Federal dollars.\n#### 1. Short title\nThis Act may be cited as the No More SCAMS Act or the No More Shielding Corruption and Misuse in Spending Act .\n#### 2. Federal Fraud Interagency Task Force\n##### (a) Establishment\nNot later than 90 days after enactment of this Act, the President shall establish the Federal Fraud Interagency Task Force (hereinafter referred to as the Task Force ) to investigate and combat fraud involving Federal dollars, enhance interagency anti-fraud coordination, and recover misused funds.\n##### (b) Appointment\n**(1) Director**\n**(A) In general**\nNot later than 180 days after the date of the enactment of this Act, the President shall appoint a Director of the Task Force to a 4 year term.\n**(B) Qualifications**\nThe Director appointed under subparagraph (A) shall have 10 years of experience in fraud investigation or Federal law enforcement.\n**(2) Members**\n**(A) In general**\nNot later than 180 days after the date of the enactment of this Act, the President shall appoint members of the Task Force from each covered agency.\n**(B) Qualifications**\nA member appointed under subparagraph (A) shall be a subject matter expert with familiarity and technical expertise regarding Federal financial management, grants and procurement administration, auditing and compliance, forensic accounting, payment integrity, or fraud risk management, or in-depth knowledge of the schemes, methods, and typologies commonly used to defraud Federal programs and interagency funding streams.\n**(3) Vacancy**\nA vacancy occurring in the membership of the Task Force shall be filled in the same manner in which the original appointment was made.\n##### (c) Duties\nThe Task Force shall\u2014\n**(1)**\ninvestigate fraud allegations involving Federal dollars;\n**(2)**\ncoordinate with State and local law enforcement for fraud investigations;\n**(3)**\ndevelop best practices for Federal agencies to prevent and identify fraud, including training programs;\n**(4)**\nfacilitate interagency cooperation through data and resource sharing to expedite and streamline fraud investigation; and\n**(5)**\nutilize and integrate existing Federal initiatives and resources for detecting and combatting Federal fraud.\n##### (d) Reporting and oversight\n**(1) Annual report**\nNot later than 1 year after the date of the enactment of this Act, and annually thereafter, the Director of the Task Force, in consultation with the covered agencies, shall submit a report to the President, the Committee on Oversight and Government Reform of the House of Representatives, and the Committee on Homeland Security and Governmental Affairs of the Senate, including\u2014\n**(A)**\nthe number of investigations initiated, cases referred for prosecution, and funds recovered;\n**(B)**\ncontributions and activities relating to fraud carried out by covered agencies;\n**(C)**\nan analysis of fraud trends by sector and by covered agency; and\n**(D)**\nrecommendations for improving fraud prevention and detection specific to covered agencies.\n**(2) GAO audit**\nNot later than one year after the date of the enactment of this Act, and annually thereafter, the Comptroller General shall conduct and audit of the operations and spending of the Task Force.\n##### (e) Definitions\nIn this section:\n**(1) Fraud**\nThe term fraud means the intentional perversion of the truth for the purpose of inducing another person in reliance upon it to part with something of value or to surrender a legal right.\n**(2) Covered agency**\nThe term covered agency includes the following:\n**(A)**\nThe Department of State.\n**(B)**\nThe Department of the Treasury.\n**(C)**\nThe Department of Defense.\n**(D)**\nThe Department of Justice.\n**(E)**\nThe Department of the Interior.\n**(F)**\nThe Department of Labor.\n**(G)**\nThe Department of Health and Human Services.\n**(H)**\nThe Department of Housing and Urban Development.\n**(I)**\nThe Department of Transportation.\n**(J)**\nThe Department of Energy.\n**(K)**\nThe Department of Education.\n**(L)**\nThe Department of Veterans Affairs.\n**(M)**\nThe Department of Homeland Security.\n**(N)**\nAny other Federal agency, designated by the President.",
      "versionDate": "2026-02-02",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-20T17:40:15Z"
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
      "date": "2026-02-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7312ih.xml"
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
      "title": "No More SCAMS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T07:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No More Shielding Corruption and Misuse in Spending Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T07:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No More SCAMS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T07:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a national task force to investigate and combat fraud involving Federal dollars.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T07:48:31Z"
    }
  ]
}
```
