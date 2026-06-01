# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/105?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/105
- Title: A joint resolution redesignating the Robert E. Lee Memorial in Arlington National Cemetery as the "Arlington House National Historic Site".
- Congress: 119
- Bill type: SJRES
- Bill number: 105
- Origin chamber: Senate
- Introduced date: 2026-02-04
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in Senate
- 2026-02-04 - IntroReferral: Introduced in Senate
- 2026-02-04 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2026-02-04: Introduced in Senate

## Actions

- 2026-02-04 - IntroReferral: Introduced in Senate
- 2026-02-04 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/105",
    "number": "105",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "A joint resolution redesignating the Robert E. Lee Memorial in Arlington National Cemetery as the \"Arlington House National Historic Site\".",
    "type": "SJRES",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T17:46:13Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres105is.xml",
      "text": "IIA\n119th CONGRESS\n2d Session\nS. J. RES. 105\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2026 Mr. Kaine introduced the following joint resolution; which was read twice and referred to the Committee on Energy and Natural Resources\nJOINT RESOLUTION\nRedesignating the Robert E. Lee Memorial in Arlington National Cemetery as the Arlington House National Historic Site .\nThat\u2014\n**(1)**\nthe site administered by the National Park Service and dedicated as a memorial to Robert E. Lee pursuant to the joint resolution of June 29, 1955 ( Public Law 84\u2013107 ; 69 Stat. 190), as amended by the joint resolution of June 30, 1972 ( Public Law 92\u2013333 ; 86 Stat. 401), shall after the date of the enactment of this joint resolution be redesignated and known as the Arlington House National Historic Site ;\n**(2)**\nany reference in any law, regulation, map, document, paper, or other record of the United States to the site referred to in paragraph (1) shall be considered to be a reference to the Arlington House National Historic Site; and\n**(3)**\nthe joint resolution of June 29, 1955 ( Public Law 84\u2013107 ; 69 Stat. 190), and the joint resolution of June 30, 1972 ( Public Law 92\u2013333 ; 86 Stat. 401), are repealed.",
      "versionDate": "2026-02-04",
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
        "actionDate": "2025-02-27",
        "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "63",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Redesignating the Robert E. Lee Memorial as the \"Arlington House National Historic Site\".",
      "type": "HJRES"
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
        "updateDate": "2026-02-11T21:16:28Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres105is.xml"
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
      "title": "A joint resolution redesignating the Robert E. Lee Memorial in Arlington National Cemetery as the \"Arlington House National Historic Site\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-06T03:18:40Z"
    },
    {
      "title": "A joint resolution redesignating the Robert E. Lee Memorial in Arlington National Cemetery as the \"Arlington House National Historic Site\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T11:56:23Z"
    }
  ]
}
```
