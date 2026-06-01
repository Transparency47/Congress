# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/918?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/918
- Title: Protect Our Probationary Employees Act
- Congress: 119
- Bill type: S
- Bill number: 918
- Origin chamber: Senate
- Introduced date: 2025-03-10
- Update date: 2026-02-26T12:03:17Z
- Update date including text: 2026-02-26T12:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in Senate
- 2025-03-10 - IntroReferral: Introduced in Senate
- 2025-03-10 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-03-10: Introduced in Senate

## Actions

- 2025-03-10 - IntroReferral: Introduced in Senate
- 2025-03-10 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/918",
    "number": "918",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Protect Our Probationary Employees Act",
    "type": "S",
    "updateDate": "2026-02-26T12:03:17Z",
    "updateDateIncludingText": "2026-02-26T12:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
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
            "date": "2025-03-10T22:18:52Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-10T22:18:52Z",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "VA"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "VA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "MD"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "DE"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s918is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 918\nIN THE SENATE OF THE UNITED STATES\nMarch 10, 2025 Mr. Van Hollen (for himself and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo allow Federal employees who are involuntarily separated from Government service while serving a probationary or trial period to resume that period upon reinstatement, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect Our Probationary Employees Act .\n#### 2. Resumption of probationary period\n##### (a) Definitions\nIn this section:\n**(1) Covered appointment**\nThe term covered appointment means an appointment of a covered probationary employee to a position in the former employing agency of that covered probationary employee that, to the extent practicable, is the same as the previous Federal position occupied by that covered probationary employee.\n**(2) Covered probationary employee**\nThe term covered probationary employee means an individual who\u2014\n**(A)**\nis, or was, involuntarily separated from Government service during the period beginning on January 20, 2025, and ending on the date described in subsection (c); and\n**(B)**\nimmediately before the involuntary separation described in subparagraph (A), occupied a position in an Executive agency under which the individual served a probationary or trial period under an initial appointment.\n**(3) Executive agency**\nThe term Executive agency has the meaning given the term in section 105 of title 5, United States Code.\n**(4) Former employing agency**\nWith respect to a covered probationary employee, the term former employing agency means the Executive agency from which the involuntary separation of that individual made that individual a covered probationary employee.\n**(5) Previous Federal position**\nThe term previous Federal position means, with respect to a covered probationary employee, the position in an Executive agency occupied by the covered probationary employee immediately before becoming a covered probationary employee.\n##### (b) Resumption of probationary period\nNotwithstanding any other provision of law, the duration of the probationary or trial period for a covered appointment of a covered probationary employee to become final shall be equal to the difference between\u2014\n**(1)**\nthe duration of that probationary or trial period that, but for this Act, would apply to that covered appointment; and\n**(2)**\nthe duration of the probationary or trial period that the covered probationary employee served in the previous Federal position of that covered probationary employee, to the extent that such duration does not exceed the duration described in paragraph (1).\n##### (c) Sunset\nThis Act shall terminate on January 20, 2029.",
      "versionDate": "2025-03-10",
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
        "updateDate": "2025-05-21T14:57:48Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s918is.xml"
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
      "title": "Protect Our Probationary Employees Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protect Our Probationary Employees Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to allow Federal employees who are involuntarily separated from Government service while serving a probationary or trial period to resume that period upon reinstatement, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:41Z"
    }
  ]
}
```
