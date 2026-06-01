# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2521?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2521
- Title: Provider Training in Palliative Care Act
- Congress: 119
- Bill type: S
- Bill number: 2521
- Origin chamber: Senate
- Introduced date: 2025-07-29
- Update date: 2026-01-07T12:03:26Z
- Update date including text: 2026-01-07T12:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in Senate
- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-29: Introduced in Senate

## Actions

- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2521",
    "number": "2521",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacky",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Provider Training in Palliative Care Act",
    "type": "S",
    "updateDate": "2026-01-07T12:03:26Z",
    "updateDateIncludingText": "2026-01-07T12:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-29",
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
            "date": "2025-07-29T21:07:59Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-29T21:07:59Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "AK"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2521is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2521\nIN THE SENATE OF THE UNITED STATES\nJuly 29, 2025 Ms. Rosen (for herself and Ms. Murkowski ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo allow participants in the National Health Service Corps to defer their obligated service in order to receive training in palliative care services.\n#### 1. Short title\nThis Act may be cited as the Provider Training in Palliative Care Act .\n#### 2. Deferral of obligated services for training in palliative care\nSection 331 of the Public Health Service Act ( 42 U.S.C. 254d ) is amended\u2014\n**(1)**\nby redesignating subsection (j) as subsection (k); and\n**(2)**\nby inserting after subsection (i) the following:\n(j) In carrying out subpart III, the Secretary may issue deferrals of the period of obligated service to individuals who have entered into a contract for obligated service under the Scholarship Program or the Loan Repayment Program and who apply for such a deferral in order to receive training in palliative care. The Secretary may grant such a deferral to such an individual for a period of up to 1 year. .",
      "versionDate": "2025-07-29",
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
        "name": "Health",
        "updateDate": "2025-09-18T17:49:05Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2521is.xml"
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
      "title": "Provider Training in Palliative Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-07T12:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Provider Training in Palliative Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to allow participants in the National Health Service Corps to defer their obligated service in order to receive training in palliative care services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:31Z"
    }
  ]
}
```
