# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1265?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1265
- Title: Expressing support for the designation of the week of May 3, 2026, through May 9, 2026, as "Tardive Dyskinesia Awareness Week".
- Congress: 119
- Bill type: HRES
- Bill number: 1265
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-21T14:27:16Z
- Update date including text: 2026-05-21T14:27:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-07 - IntroReferral: Submitted in House
- Latest action: 2026-05-07: Submitted in House

## Actions

- 2026-05-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-07 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1265",
    "number": "1265",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000608",
        "district": "50",
        "firstName": "Scott",
        "fullName": "Rep. Peters, Scott H. [D-CA-50]",
        "lastName": "Peters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing support for the designation of the week of May 3, 2026, through May 9, 2026, as \"Tardive Dyskinesia Awareness Week\".",
    "type": "HRES",
    "updateDate": "2026-05-21T14:27:16Z",
    "updateDateIncludingText": "2026-05-21T14:27:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
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
      "actionDate": "2026-05-07",
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
          "date": "2026-05-07T13:08:25Z",
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
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "FL"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "CA"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1265ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1265\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Peters (for himself, Mr. Bilirakis , Mr. Mullin , and Mr. Bean of Florida ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of the week of May 3, 2026, through May 9, 2026, as Tardive Dyskinesia Awareness Week .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of Tardive Dyskinesia Awareness Week ; and\n**(2)**\nencourages each individual in the United States to become better informed about and aware of tardive dyskinesia.",
      "versionDate": "2026-05-07",
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
        "actionDate": "2025-05-07",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "396",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for the designation of the week of May 4, 2025, through May 10, 2025, as \"Tardive Dyskinesia Awareness Week\".",
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
        "updateDate": "2026-05-21T14:27:15Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1265ih.xml"
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
      "title": "Expressing support for the designation of the week of May 3, 2026, through May 9, 2026, as \"Tardive Dyskinesia Awareness Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T08:18:50Z"
    },
    {
      "title": "Expressing support for the designation of the week of May 3, 2026, through May 9, 2026, as \"Tardive Dyskinesia Awareness Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T08:05:55Z"
    }
  ]
}
```
