# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1112?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1112
- Title: Supporting the goals and ideals of "Deep Vein Thrombosis and Pulmonary Embolism Awareness Month".
- Congress: 119
- Bill type: HRES
- Bill number: 1112
- Origin chamber: House
- Introduced date: 2026-03-12
- Update date: 2026-04-17T18:35:37Z
- Update date including text: 2026-04-17T18:35:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-03-12 - IntroReferral: Submitted in House
- 2026-03-12 - IntroReferral: Submitted in House
- Latest action: 2026-03-12: Submitted in House

## Actions

- 2026-03-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-03-12 - IntroReferral: Submitted in House
- 2026-03-12 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1112",
    "number": "1112",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001210",
        "district": "3",
        "firstName": "Gregory",
        "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
        "lastName": "Murphy",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Supporting the goals and ideals of \"Deep Vein Thrombosis and Pulmonary Embolism Awareness Month\".",
    "type": "HRES",
    "updateDate": "2026-04-17T18:35:37Z",
    "updateDateIncludingText": "2026-04-17T18:35:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-03-12T13:35:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1112ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1112\nIN THE HOUSE OF REPRESENTATIVES\nMarch 12, 2026 Mr. Murphy (for himself and Mr. Tonko ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nSupporting the goals and ideals of Deep Vein Thrombosis and Pulmonary Embolism Awareness Month .\nThat the Senate\u2014\n**(1)**\nsupports the goals and ideals of Deep Vein Thrombosis and Pulmonary Embolism Awareness Month ; and\n**(2)**\nrecognizes the importance of raising awareness of deep vein thrombosis and pulmonary embolisms.",
      "versionDate": "2026-03-12",
      "versionType": "IH"
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
        "actionDate": "2025-03-25",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S1839; text: CR S1838)"
      },
      "number": "138",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution supporting the goals and ideals of \"Deep Vein Thrombosis and Pulmonary Embolism Awareness Month\".",
      "type": "SRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-14",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S1745; text: CR S1744)"
      },
      "number": "669",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution supporting the goals and ideals of \"Deep Vein Thrombosis and Pulmonary Embolism Awareness Month\".",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Cardiovascular and respiratory health",
            "updateDate": "2026-04-10T12:05:15Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2026-04-10T12:05:15Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2026-04-10T12:05:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-03-16T16:31:41Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1112ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting the goals and ideals of \"Deep Vein Thrombosis and Pulmonary Embolism Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-13T08:19:29Z"
    },
    {
      "title": "Supporting the goals and ideals of \"Deep Vein Thrombosis and Pulmonary Embolism Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-13T08:05:28Z"
    }
  ]
}
```
