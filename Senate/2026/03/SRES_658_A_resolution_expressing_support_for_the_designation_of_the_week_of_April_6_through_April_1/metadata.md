# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/658?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/658
- Title: A resolution expressing support for the designation of the week of April 6 through April 10, 2026, as "National Assistant Principals Week".
- Congress: 119
- Bill type: SRES
- Bill number: 658
- Origin chamber: Senate
- Introduced date: 2026-03-23
- Update date: 2026-04-01T21:09:30Z
- Update date including text: 2026-04-01T21:09:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-23: Introduced in Senate
- 2026-03-23 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1546)
- 2026-03-23 - IntroReferral: Submitted in Senate
- Latest action: 2026-03-23: Submitted in Senate

## Actions

- 2026-03-23 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1546)
- 2026-03-23 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-23",
    "latestAction": {
      "actionDate": "2026-03-23",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/658",
    "number": "658",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "A resolution expressing support for the designation of the week of April 6 through April 10, 2026, as \"National Assistant Principals Week\".",
    "type": "SRES",
    "updateDate": "2026-04-01T21:09:30Z",
    "updateDateIncludingText": "2026-04-01T21:09:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-23",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1546)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-03-23",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
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
          "date": "2026-03-23T22:18:53Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-23",
      "state": "HI"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-03-23",
      "state": "NM"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres658is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 658\nIN THE SENATE OF THE UNITED STATES\nMarch 23, 2026 Mr. Durbin (for himself, Ms. Hirono , Mr. Heinrich , and Mr. Luj\u00e1n ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nExpressing support for the designation of the week of April 6 through April 10, 2026, as National Assistant Principals Week .\nThat the Senate\u2014\n**(1)**\nsupports the designation of National Assistant Principals Week ;\n**(2)**\nhonors the contributions of assistant principals to the success of students in the United States; and\n**(3)**\nencourages the people of the United States to observe National Assistant Principals Week with appropriate ceremonies and activities that promote awareness of the role played by assistant principals in school leadership and ensuring that every child has access to a high-quality education.",
      "versionDate": "2026-03-23",
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
        "actionDate": "2025-04-07",
        "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2459)"
      },
      "number": "161",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution expressing support for the designation of the week of April 7 through April 11, 2025, as \"National Assistant Principals Week\".",
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
        "name": "Education",
        "updateDate": "2026-04-01T21:09:29Z"
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
      "date": "2026-03-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres658is.xml"
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
      "title": "A resolution expressing support for the designation of the week of April 6 through April 10, 2026, as \"National Assistant Principals Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T05:33:40Z"
    },
    {
      "title": "A resolution expressing support for the designation of the week of April 6 through April 10, 2026, as \"National Assistant Principals Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T10:56:23Z"
    }
  ]
}
```
