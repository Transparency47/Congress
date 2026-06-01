# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1195?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1195
- Title: Supporting the designation of May as "National Myositis Awareness Month".
- Congress: 119
- Bill type: HRES
- Bill number: 1195
- Origin chamber: House
- Introduced date: 2026-04-20
- Update date: 2026-05-01T08:08:47Z
- Update date including text: 2026-05-01T08:08:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-20: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-04-20 - IntroReferral: Submitted in House
- Latest action: 2026-04-20: Submitted in House

## Actions

- 2026-04-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-04-20 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-20",
    "latestAction": {
      "actionDate": "2026-04-20",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1195",
    "number": "1195",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001218",
        "district": "7",
        "firstName": "Richard",
        "fullName": "Rep. McCormick, Richard [R-GA-7]",
        "lastName": "McCormick",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Supporting the designation of May as \"National Myositis Awareness Month\".",
    "type": "HRES",
    "updateDate": "2026-05-01T08:08:47Z",
    "updateDateIncludingText": "2026-05-01T08:08:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
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
      "actionCode": "1025",
      "actionDate": "2026-04-20",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
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
          "date": "2026-04-20T16:05:20Z",
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
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NY"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1195ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1195\nIN THE HOUSE OF REPRESENTATIVES\nApril 20, 2026 Mr. McCormick submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nSupporting the designation of May as National Myositis Awareness Month .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of National Myositis Awareness Month ;\n**(2)**\nrecognizes the importance of raising awareness about myositis and its impact on United States veterans and citizens; and\n**(3)**\nencourages all people in the United States to become more informed about myositis and to support the individuals and families who are affected by these conditions.",
      "versionDate": "2026-04-20",
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
        "actionDate": "2025-03-31",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "277",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Supporting the designation of May 2025 as \"National Myositis Awareness Month\".",
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
        "updateDate": "2026-04-27T20:16:47Z"
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
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1195ih.xml"
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
      "title": "Supporting the designation of May as \"National Myositis Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T03:18:24Z"
    },
    {
      "title": "Supporting the designation of May as \"National Myositis Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T08:06:26Z"
    }
  ]
}
```
