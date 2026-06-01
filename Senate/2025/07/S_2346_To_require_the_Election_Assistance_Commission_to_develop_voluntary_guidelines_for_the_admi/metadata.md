# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2346?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2346
- Title: Preparing Election Administrators for AI Act
- Congress: 119
- Bill type: S
- Bill number: 2346
- Origin chamber: Senate
- Introduced date: 2025-07-17
- Update date: 2025-10-09T11:03:14Z
- Update date including text: 2025-10-09T11:03:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in Senate
- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2025-07-17: Introduced in Senate

## Actions

- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2346",
    "number": "2346",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Preparing Election Administrators for AI Act",
    "type": "S",
    "updateDate": "2025-10-09T11:03:14Z",
    "updateDateIncludingText": "2025-10-09T11:03:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Rules and Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T19:46:54Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "ME"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "AZ"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2346is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2346\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Ms. Klobuchar (for herself, Ms. Collins , and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Rules and Administration\nA BILL\nTo require the Election Assistance Commission to develop voluntary guidelines for the administration of elections that address the use and risks of artificial intelligence technologies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preparing Election Administrators for AI Act .\n#### 2. Voluntary guidelines for administration of elections that address the use and risks of artificial intelligence technologies\n##### (a) Report and voluntary guidelines\nNot later than 60 days after the date of the enactment of this Act, the Election Assistance Commission shall, in consultation with the National Institute of Standards and Technology, submit to Congress, issue to State and local election offices, and make available to the public a report with voluntary guidelines for election offices that address the use and risks of artificial intelligence technologies in the administration of elections.\n##### (b) Contents\nThe report submitted and made available pursuant to subsection (a) shall include voluntary guidelines that address\u2014\n**(1)**\nthe risks and benefits associated with using artificial intelligence technologies to conduct election administration activities;\n**(2)**\nthe cybersecurity risks of artificial intelligence technologies to election administration;\n**(3)**\nhow information generated and distributed by artificial intelligence technologies can affect the sharing of accurate election information and how election offices should respond; and\n**(4)**\nhow information generated and distributed by artificial intelligence technologies can affect the spreading of election disinformation that undermines public trust and confidence in elections.\n#### 3. Study on use of artificial intelligence technologies in the 2024 elections\n##### (a) In general\nNot later than July 31, 2026, the Election Assistance Commission, in consultation with the National Institute of Standards and Technology, shall study and submit to Congress, issue to State and local election offices, and make available to the public a report on the use and impacts of artificial intelligence technologies in the elections for Federal office held in 2024, including how information generated by artificial intelligence technologies was shared and the use of artificial intelligence technologies by election offices.\n##### (b) Review and update of voluntary guidelines\nTaking into consideration the results of the study conducted under subsection (a), the Election Assistance Commission shall review and update the voluntary guidelines issued under section 2(a) as appropriate.",
      "versionDate": "2025-07-17",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-08-01T16:16:49Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2346is.xml"
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
      "title": "Preparing Election Administrators for AI Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-09T11:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preparing Election Administrators for AI Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Election Assistance Commission to develop voluntary guidelines for the administration of elections that address the use and risks of artificial intelligence technologies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:18:33Z"
    }
  ]
}
```
