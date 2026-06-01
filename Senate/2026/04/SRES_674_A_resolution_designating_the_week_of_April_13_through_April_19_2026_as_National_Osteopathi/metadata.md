# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/674?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/674
- Title: A resolution designating the week of April 13 through April 19, 2026, as "National Osteopathic Medicine Week".
- Congress: 119
- Bill type: SRES
- Bill number: 674
- Origin chamber: Senate
- Introduced date: 2026-04-16
- Update date: 2026-04-22T15:02:57Z
- Update date including text: 2026-04-22T15:02:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in Senate
- 2026-04-16 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1824)
- 2026-04-16 - IntroReferral: Submitted in Senate
- Latest action: 2026-04-16: Submitted in Senate

## Actions

- 2026-04-16 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1824)
- 2026-04-16 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/674",
    "number": "674",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000437",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Wicker, Roger F. [R-MS]",
        "lastName": "Wicker",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "A resolution designating the week of April 13 through April 19, 2026, as \"National Osteopathic Medicine Week\".",
    "type": "SRES",
    "updateDate": "2026-04-22T15:02:57Z",
    "updateDateIncludingText": "2026-04-22T15:02:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S1824)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
          "date": "2026-04-16T15:12:07Z",
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
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres674is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 674\nIN THE SENATE OF THE UNITED STATES\nApril 16 (legislative day, April 14), 2026 Mr. Wicker (for himself and Mr. Heinrich ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating the week of April 13 through April 19, 2026, as National Osteopathic Medicine Week .\nThat the Senate\u2014\n**(1)**\ndesignates the week of April 13 through April 19, 2026, as National Osteopathic Medicine Week ;\n**(2)**\nrecognizes the contributions of osteopathic physicians to the healthcare system of the United States; and\n**(3)**\ncelebrates the role that colleges of osteopathic medicine play in training the next generation of physicians.",
      "versionDate": "2026-04-16",
      "versionType": "IS"
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
        "name": "Health",
        "updateDate": "2026-04-22T15:02:57Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres674is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution designating the week of April 13 through April 19, 2026, as \"National Osteopathic Medicine Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T05:48:26Z"
    },
    {
      "title": "A resolution designating the week of April 13 through April 19, 2026, as \"National Osteopathic Medicine Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T14:15:19Z"
    }
  ]
}
```
