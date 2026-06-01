# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4415?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4415
- Title: Office of Fossil Energy and Carbon Management Relocation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4415
- Origin chamber: House
- Introduced date: 2025-07-15
- Update date: 2026-04-01T17:52:04Z
- Update date including text: 2026-04-01T17:52:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-15: Introduced in House

## Actions

- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4415",
    "number": "4415",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "R000610",
        "district": "14",
        "firstName": "Guy",
        "fullName": "Rep. Reschenthaler, Guy [R-PA-14]",
        "lastName": "Reschenthaler",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Office of Fossil Energy and Carbon Management Relocation Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-01T17:52:04Z",
    "updateDateIncludingText": "2026-04-01T17:52:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-15",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-07-15T14:00:05Z",
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
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "PA"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "PA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4415ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4415\nIN THE HOUSE OF REPRESENTATIVES\nJuly 15, 2025 Mr. Reschenthaler (for himself, Mr. Deluzio , and Mr. Joyce of Pennsylvania ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Secretary of Energy to relocate the Office of Fossil Energy and Carbon Management to Pittsburgh, Pennsylvania.\n#### 1. Short title\nThis Act may be cited as the Office of Fossil Energy and Carbon Management Relocation Act of 2025 .\n#### 2. Relocation of Office of Fossil Energy and Carbon Management\n##### (a) In general\nNotwithstanding section 72 of title 4, United States Code, not later than December 31, 2026, the Secretary of Energy shall relocate the Office of Fossil Energy and Carbon Management (referred to in this section as the Office ) from Washington, DC, to Pittsburgh, Pennsylvania.\n##### (b) Report\nNot later than 1 year after the relocation required under subsection (a) is completed, the Secretary of Energy shall submit to Congress a report describing\u2014\n**(1)**\nany attrition of employees from the Office during and after that relocation;\n**(2)**\nthe extent to which that attrition is attributable to that relocation;\n**(3)**\nhow the Secretary of Energy will address that attrition; and\n**(4)**\nhow that relocation affected the ability of employees of the Office to negotiate through representatives regarding conditions of employment.",
      "versionDate": "2025-07-15",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-06-12",
        "text": "Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "2044",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Office of Fossil Energy and Carbon Management Relocation Act of 2025",
      "type": "S"
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
        "name": "Energy",
        "updateDate": "2025-09-11T14:45:51Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4415ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Office of Fossil Energy and Carbon Management Relocation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T11:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Office of Fossil Energy and Carbon Management Relocation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T11:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Energy to relocate the Office of Fossil Energy and Carbon Management to Pittsburgh, Pennsylvania.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T11:48:18Z"
    }
  ]
}
```
