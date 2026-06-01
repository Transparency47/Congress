# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/191?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/191
- Title: A resolution supporting the designation of April 2025 as the "Month of the Military Child".
- Congress: 119
- Bill type: SRES
- Bill number: 191
- Origin chamber: Senate
- Introduced date: 2025-04-30
- Update date: 2026-05-07T02:21:01Z
- Update date including text: 2026-05-07T02:21:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in Senate
- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-04-30 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2710; text: CR S2718)
- Latest action: 2025-04-30: Introduced in Senate

## Actions

- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-04-30 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2710; text: CR S2718)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/191",
    "number": "191",
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
    "title": "A resolution supporting the designation of April 2025 as the \"Month of the Military Child\".",
    "type": "SRES",
    "updateDate": "2026-05-07T02:21:01Z",
    "updateDateIncludingText": "2026-05-07T02:21:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2710; text: CR S2718)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-30",
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
      "sponsorshipDate": "2025-04-30",
      "state": "AR"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NV"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres191ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 191\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2025 Mrs. Murray (for herself, Mr. Boozman , Ms. Rosen , and Mr. Hoeven ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nSupporting the designation of April 2025 as the Month of the Military Child .\nThat the Senate\u2014\n**(1)**\nsupports the designation of April 2025 as the Month of the Military Child ; and\n**(2)**\nurges the people of the United States to observe the Month of the Military Child with appropriate ceremonies and activities that honor, support, and show appreciation for military children.",
      "versionDate": "2025-04-30",
      "versionType": "ATS"
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
        "actionDate": "2026-04-28",
        "text": "Referred to the Committee on Armed Services. (text: CR S2083)"
      },
      "number": "691",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution supporting the designation of April 2026 as the \"Month of the Military Child\".",
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
            "name": "Commemorative events and holidays",
            "updateDate": "2025-06-02T14:40:12Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-06-02T14:39:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-29T17:57:58Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres191ats.xml"
        }
      ],
      "type": "ATS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A resolution supporting the designation of April 2025 as the \"Month of the Military Child\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-01T10:56:22Z"
    },
    {
      "title": "A resolution supporting the designation of April 2025 as the \"Month of the Military Child\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-01T10:56:22Z"
    }
  ]
}
```
