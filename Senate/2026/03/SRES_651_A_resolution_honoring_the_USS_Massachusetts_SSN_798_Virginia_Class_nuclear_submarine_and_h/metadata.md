# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/651?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/651
- Title: A resolution honoring the USS Massachusetts (SSN-798) Virginia Class nuclear submarine and her crew on the historic occasion of her commissioning, on March 28, 2026.
- Congress: 119
- Bill type: SRES
- Bill number: 651
- Origin chamber: Senate
- Introduced date: 2026-03-19
- Update date: 2026-03-31T20:35:49Z
- Update date including text: 2026-03-31T20:35:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in Senate
- 2026-03-19 - IntroReferral: Referred to the Committee on Armed Services. (text: CR S1380-1381)
- 2026-03-19 - IntroReferral: Submitted in Senate
- Latest action: 2026-03-19: Submitted in Senate

## Actions

- 2026-03-19 - IntroReferral: Referred to the Committee on Armed Services. (text: CR S1380-1381)
- 2026-03-19 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/651",
    "number": "651",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "A resolution honoring the USS Massachusetts (SSN-798) Virginia Class nuclear submarine and her crew on the historic occasion of her commissioning, on March 28, 2026.",
    "type": "SRES",
    "updateDate": "2026-03-31T20:35:49Z",
    "updateDateIncludingText": "2026-03-31T20:35:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Armed Services. (text: CR S1380-1381)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
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
          "date": "2026-03-19T16:45:31Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres651is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 651\nIN THE SENATE OF THE UNITED STATES\nMarch 19, 2026 Ms. Warren (for herself and Mr. Markey ) submitted the following resolution; which was referred to the Committee on Armed Services\nRESOLUTION\nHonoring the USS Massachusetts (SSN\u2013798) Virginia Class nuclear submarine and her crew on the historic occasion of her commissioning, on March 28, 2026.\nThat\n\u2014\n**(1)**\nthe Senate\u2014\n**(A)**\nagain would like to recognize the profound historical significance of the commissioning of warship USS Massachusetts (SSN\u2013798); and\n**(B)**\nextends its best wishes for good fortune for all those that sail aboard her, for fair winds and following seas during her service to the United States; and\n**(2)**\nservice of the USS Massachusetts (SSN\u2013798) shall commence with her commissioning in the Commonwealth of Massachusetts on March 28, 2026, in Boston Harbor.",
      "versionDate": "2026-03-19",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-03-31T20:35:49Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres651is.xml"
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
      "title": "A resolution honoring the USS Massachusetts (SSN-798) Virginia Class nuclear submarine and her crew on the historic occasion of her commissioning, on March 28, 2026.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:39Z"
    },
    {
      "title": "A resolution honoring the USS Massachusetts (SSN-798) Virginia Class nuclear submarine and her crew on the historic occasion of her commissioning, on March 28, 2026.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T10:56:24Z"
    }
  ]
}
```
