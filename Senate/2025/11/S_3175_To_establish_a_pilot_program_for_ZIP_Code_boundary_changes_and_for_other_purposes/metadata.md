# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3175?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3175
- Title: CIPZIP Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3175
- Origin chamber: Senate
- Introduced date: 2025-11-18
- Update date: 2026-04-29T11:03:32Z
- Update date including text: 2026-04-29T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in Senate
- 2025-11-18 - IntroReferral: Introduced in Senate
- 2025-11-18 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-11-18: Introduced in Senate

## Actions

- 2025-11-18 - IntroReferral: Introduced in Senate
- 2025-11-18 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3175",
    "number": "3175",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "CIPZIP Act of 2025",
    "type": "S",
    "updateDate": "2026-04-29T11:03:32Z",
    "updateDateIncludingText": "2026-04-29T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-18",
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
      "actionDate": "2025-11-18",
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
            "date": "2025-11-18T20:29:52Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-18T20:29:52Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3175is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3175\nIN THE SENATE OF THE UNITED STATES\nNovember 18, 2025 Mr. Lankford introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo establish a pilot program for ZIP Code boundary changes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Community Involvement in Zone Improvement Plans Act of 2025 or the CIPZIP Act of 2025 .\n#### 2. Pilot postal service program for ZIP Code boundary changes\n##### (a) In general\nNotwithstanding any other provision of title 39, United States Code, the United States Postal Service (referred to in this section as the Postal Service ) shall establish a pilot program through which the Postal Service may consider entering into an agreement with an agency of a State government, local government, or Tribal government to receive money, property, or services to defray part or all of the net costs, if any, in conjunction with a request for a ZIP Code boundary change or realignment.\n##### (b) Denial of ZIP Code boundary change or realignment requests\n**(1) In general**\nIf the Postal Service denies a request from a State government, local government, or Tribal government for a ZIP Code boundary change or realignment on the basis of a net cost to the Postal Service, the Postal Service shall\u2014\n**(A)**\nnotify the requestor in writing of the existence of the program established under subsection (a);\n**(B)**\nprovide the requestor with an estimate of the net cost to the Postal Service of the implementation of the request;\n**(C)**\nallow not less than 30 days for the requestor to propose an agreement meeting the requirements of the pilot program established under subsection (a); and\n**(D)**\ngive due consideration to a proposed agreement under subparagraph (C).\n**(2) Cost as only dispositive factor for a denial**\nIf a net cost to the Postal Service is the only dispositive factor in a denial of a request under paragraph (1), and the requestor is able to defray that cost under an agreement described in subsection (a), the Postal Service shall accept the agreement and grant the request.\n##### (c) Reports\n**(1) Annual reports**\nNot later than 360 days after the date of enactment of this Act, and annually thereafter, the Postal Regulatory Commission shall submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Government Reform of the House of Representatives a report on the pilot program under subsection (a), including\u2014\n**(A)**\nthe number of requests the United States Postal Service has received for a ZIP Code boundary change or realignment, including the number of requests granted and denied;\n**(B)**\nthe number of agreements entered into under the pilot program established under subsection (a), and with respect to each such agreement, the total value of the costs defrayed; and\n**(C)**\nwith respect to each denial of a request for a ZIP Code boundary change or realignment\u2014\n**(i)**\nwhether a notification was provided pursuant to subsection (b)(1)(A); and\n**(ii)**\nthe estimated net cost provided pursuant to subsection (b)(1)(B).\n**(2) By member request**\nThe Postal Service shall submit to any Member of Congress, upon request, a report of the factors contributing to the denial of a request from a State government, local government, or Tribal government for a ZIP Code boundary change or realignment.\n##### (d) Sunset\nThe pilot program established under this section shall terminate on the date that is 7 years after the date of enactment of this Act.",
      "versionDate": "2025-11-18",
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
        "updateDate": "2025-12-09T21:11:01Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3175is.xml"
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
      "title": "CIPZIP Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CIPZIP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T03:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Community Involvement in Zone Improvement Plans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T03:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a pilot program for ZIP Code boundary changes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T03:33:26Z"
    }
  ]
}
```
