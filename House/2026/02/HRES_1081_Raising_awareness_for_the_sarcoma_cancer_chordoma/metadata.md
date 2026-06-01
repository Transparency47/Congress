# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1081?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1081
- Title: Raising awareness for the sarcoma cancer chordoma.
- Congress: 119
- Bill type: HRES
- Bill number: 1081
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-03-02T20:28:35Z
- Update date including text: 2026-03-02T20:28:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-02-25 - IntroReferral: Submitted in House
- 2026-02-25 - IntroReferral: Submitted in House
- Latest action: 2026-02-25: Submitted in House

## Actions

- 2026-02-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-02-25 - IntroReferral: Submitted in House
- 2026-02-25 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1081",
    "number": "1081",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "J000288",
        "district": "4",
        "firstName": "Henry",
        "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
        "lastName": "Johnson",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Raising awareness for the sarcoma cancer chordoma.",
    "type": "HRES",
    "updateDate": "2026-03-02T20:28:35Z",
    "updateDateIncludingText": "2026-03-02T20:28:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
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
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T14:01:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1081ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1081\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Mr. Johnson of Georgia submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nRaising awareness for the sarcoma cancer chordoma.\nThat it is the sense of the House of Representatives that chordoma patients and families need increased funding and support for\u2014\n**(1)**\naccurate and early diagnosis;\n**(2)**\nthe development of new treatments, diagnostics, and cures;\n**(3)**\nfewer hurdles between research and new treatments; and\n**(4)**\npatient-centric approaches to drug discovery and development.",
      "versionDate": "2026-02-25",
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
        "actionDate": "2025-02-27",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "172",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Raising awareness for the sarcoma cancer chordoma.",
      "type": "HRES"
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
        "updateDate": "2026-03-02T20:28:34Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1081ih.xml"
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
      "title": "Raising awareness for the sarcoma cancer chordoma.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T09:18:26Z"
    },
    {
      "title": "Raising awareness for the sarcoma cancer chordoma.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T09:06:47Z"
    }
  ]
}
```
