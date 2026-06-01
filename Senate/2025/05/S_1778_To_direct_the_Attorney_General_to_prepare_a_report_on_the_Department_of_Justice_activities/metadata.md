# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1778?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1778
- Title: Countering Chinese Espionage Reporting Act
- Congress: 119
- Bill type: S
- Bill number: 1778
- Origin chamber: Senate
- Introduced date: 2025-05-15
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in Senate
- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-05-15: Introduced in Senate

## Actions

- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1778",
    "number": "1778",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Countering Chinese Espionage Reporting Act",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T16:36:21Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "DE"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "PA"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-06-12",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1778is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1778\nIN THE SENATE OF THE UNITED STATES\nMay 15, 2025 Mrs. Blackburn (for herself and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo direct the Attorney General to prepare a report on the Department of Justice activities related to countering Chinese national security threats, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Countering Chinese Espionage Reporting Act .\n#### 2. Report on Department of Justice activities related to countering national security threats from the Chinese Communist Party\n##### (a) Requirement\nNot later than 90 days after the date of enactment of this Act, and each year thereafter for 7 years, the Attorney General shall submit to the Committees on the Judiciary of the Senate and of the House of Representatives, and make publicly available on the website of the Department of Justice, a report on activities conducted by the Department of Justice related to countering national security threats from and espionage in the United States by the Chinese Communist Party, including\u2014\n**(1)**\na description of the activities and operations of the Department of Justice related to countering Chinese national security threats and espionage in the United States, including\u2014\n**(A)**\ntheft of United States intellectual property (including trade secrets) and research; and\n**(B)**\nthreats from non-traditional collectors, such as researchers in laboratories, at universities, and at defense industrial base facilities (as that term is defined in section 2208(u)(3) of title 10, United States Code);\n**(2)**\nan accounting of the resources of the Department of Justice that are dedicated to programs aimed at combating national security threats posed by the Chinese Communist Party, and any supporting information as to the efficacy of each such program; and\n**(3)**\na detailed description of the measures used to ensure the protection of civil rights, civil liberties, and privacy rights of United States persons in carrying out the activities, operations, and programs described in paragraphs (1) and (2).\n##### (b) Form\nThe report under subsection (a) shall be submitted in unclassified form, but may include a classified annex.\n##### (c) Consultation\nIn preparing the report under subsection (a), the Attorney General shall collaborate with the Director of National Intelligence, the Secretary of Homeland Security, the Secretary of Defense, and any other appropriate officials.",
      "versionDate": "2025-05-15",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-30T14:21:10Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1778is.xml"
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
      "title": "Countering Chinese Espionage Reporting Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-13T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Countering Chinese Espionage Reporting Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Attorney General to prepare a report on the Department of Justice activities related to countering Chinese national security threats, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T02:03:27Z"
    }
  ]
}
```
