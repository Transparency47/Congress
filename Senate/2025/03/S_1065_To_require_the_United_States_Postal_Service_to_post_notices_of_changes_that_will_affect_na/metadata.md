# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1065?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1065
- Title: INFORM Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1065
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2025-12-05T22:56:46Z
- Update date including text: 2025-12-05T22:56:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1065",
    "number": "1065",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "INFORM Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:56:46Z",
    "updateDateIncludingText": "2025-12-05T22:56:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
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
      "actionDate": "2025-03-13",
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
          "date": "2025-03-13T22:31:29Z",
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1065is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1065\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Rounds (for himself and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require the United States Postal Service to post notices of changes that will affect nationwide postal services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Instituting Notification Formalities On Reorganizing Mail Act of 2025 or the INFORM Act of 2025 .\n#### 2. Requiring notices relating to changes in nature of postal services\nSection 3661 of title 39, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking The and inserting In General.\u2014 The ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby inserting Change in Nature of Postal Services .\u2014 before When ; and\n**(B)**\nby striking When and all that follows, and inserting the following:\n(1) In General When the Postal Service determines that there should be a change in the nature of postal services which will generally affect service on a nationwide or substantially nationwide basis, it shall\u2014 (A) submit a proposed change, within a reasonable time prior to the effective date of the change, to the Postal Regulatory Commission requesting an advisory opinion on the change; and (B) on the date such proposed change is submitted to the Postal Regulatory Commission, post a notice of the change within affected storefront postal facilities, to remain posted for not fewer than 30 days after the change has gone into effect, and such notice shall include\u2014 (i) relevant details of the change; (ii) associated timelines relating to the implementation of the change; (iii) anticipated impacts on nationwide postal services; (iv) details of any public meetings and opportunities for public comment; (v) contact information for public comment; and (vi) other helpful resources as determined necessary by the Postal Service. ;\n**(3)**\nby redesignating subsection (c) as paragraph (2) of subsection (b); and\n**(4)**\nin paragraph (2) of subsection (b), as so redesignated\u2014\n**(A)**\nby inserting Hearing and Opinion of Commission.\u2014 before The Commission ; and\n**(B)**\nby striking proposal and inserting proposed change .",
      "versionDate": "2025-03-13",
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
        "actionDate": "2025-02-12",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "1249",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "INFORM Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Government information and archives",
            "updateDate": "2025-05-02T15:09:35Z"
          },
          {
            "name": "Postal Regulatory Commission",
            "updateDate": "2025-05-02T15:09:35Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-05-02T15:09:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-20T15:20:14Z"
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
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1065is.xml"
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
      "title": "INFORM Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "INFORM Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Instituting Notification Formalities On Reorganizing Mail Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the United States Postal Service to post notices of changes that will affect nationwide postal services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:40Z"
    }
  ]
}
```
