# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/691?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/691
- Title: A resolution supporting the designation of April 2026 as the "Month of the Military Child".
- Congress: 119
- Bill type: SRES
- Bill number: 691
- Origin chamber: Senate
- Introduced date: 2026-04-28
- Update date: 2026-05-12T10:56:30Z
- Update date including text: 2026-05-12T10:56:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in Senate
- 2026-04-28 - IntroReferral: Referred to the Committee on Armed Services. (text: CR S2083)
- 2026-04-28 - IntroReferral: Submitted in Senate
- Latest action: 2026-04-28: Submitted in Senate

## Actions

- 2026-04-28 - IntroReferral: Referred to the Committee on Armed Services. (text: CR S2083)
- 2026-04-28 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/691",
    "number": "691",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001111",
        "district": "",
        "firstName": "Patty",
        "fullName": "Sen. Murray, Patty [D-WA]",
        "lastName": "Murray",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "A resolution supporting the designation of April 2026 as the \"Month of the Military Child\".",
    "type": "SRES",
    "updateDate": "2026-05-12T10:56:30Z",
    "updateDateIncludingText": "2026-05-12T10:56:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-28",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Armed Services. (text: CR S2083)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-04-28",
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
          "date": "2026-04-28T15:03:44Z",
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
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "AR"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres691is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 691\nIN THE SENATE OF THE UNITED STATES\nApril 28, 2026 Mrs. Murray (for herself and Mr. Boozman ) submitted the following resolution; which was referred to the Committee on Armed Services\nRESOLUTION\nSupporting the designation of April 2026 as the Month of the Military Child .\nThat the Senate\u2014\n**(1)**\nsupports the designation of April 2026 as the Month of the Military Child ; and\n**(2)**\nurges the people of the United States to observe the Month of the Military Child with appropriate ceremonies and activities that honor, support, and show appreciation for military children.",
      "versionDate": "2026-04-28",
      "versionType": "IS"
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
        "actionDate": "2025-04-30",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2710; text: CR S2718)"
      },
      "number": "191",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution supporting the designation of April 2025 as the \"Month of the Military Child\".",
      "type": "SRES"
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
        "updateDate": "2026-05-07T02:21:09Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres691is.xml"
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
      "title": "A resolution supporting the designation of April 2026 as the \"Month of the Military Child\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-01T06:48:33Z"
    },
    {
      "title": "A resolution supporting the designation of April 2026 as the \"Month of the Military Child\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T10:56:35Z"
    }
  ]
}
```
