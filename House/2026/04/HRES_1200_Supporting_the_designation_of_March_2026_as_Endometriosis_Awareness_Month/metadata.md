# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1200?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1200
- Title: Supporting the designation of March 2026 as Endometriosis Awareness Month.
- Congress: 119
- Bill type: HRES
- Bill number: 1200
- Origin chamber: House
- Introduced date: 2026-04-20
- Update date: 2026-04-24T19:13:08Z
- Update date including text: 2026-04-24T19:13:08Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1200",
    "number": "1200",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001157",
        "district": "13",
        "firstName": "David",
        "fullName": "Rep. Scott, David [D-GA-13]",
        "lastName": "Scott",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Supporting the designation of March 2026 as Endometriosis Awareness Month.",
    "type": "HRES",
    "updateDate": "2026-04-24T19:13:08Z",
    "updateDateIncludingText": "2026-04-24T19:13:08Z"
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
          "date": "2026-04-20T16:04:35Z",
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
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "IA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "GA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1200ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1200\nIN THE HOUSE OF REPRESENTATIVES\nApril 20, 2026 Mr. David Scott of Georgia (for himself, Mrs. Miller-Meeks , Ms. Williams of Georgia , and Mr. Crenshaw ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nSupporting the designation of March 2026 as Endometriosis Awareness Month.\nThat the House of Representatives\u2014\n**(1)**\nstrongly supports the goals and ideals of Endometriosis Awareness Month;\n**(2)**\nrecognizes the need for early detection and treatment of endometriosis, increased education for health care providers, and more culturally competent care;\n**(3)**\nremains committed to supporting and funding endometriosis research for more effective treatments, increasing fertility, and, ultimately, a cure; and\n**(4)**\nencourages the people of the United States to observe the month with appropriate awareness and educational activities.",
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
        "actionDate": "2025-03-26",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "256",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Supporting the designation of March 2025 as Endometriosis Awareness Month.",
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
        "updateDate": "2026-04-24T19:13:08Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1200ih.xml"
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
      "title": "Supporting the designation of March 2026 as Endometriosis Awareness Month.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T08:19:08Z"
    },
    {
      "title": "Supporting the designation of March 2026 as Endometriosis Awareness Month.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T08:06:29Z"
    }
  ]
}
```
