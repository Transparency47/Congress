# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5882?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5882
- Title: No Tricks on Treats Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5882
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2025-11-21T15:10:34Z
- Update date including text: 2025-11-21T15:10:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-10-31: Introduced in House

## Actions

- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5882",
    "number": "5882",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "J000305",
        "district": "51",
        "firstName": "Sara",
        "fullName": "Rep. Jacobs, Sara [D-CA-51]",
        "lastName": "Jacobs",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "No Tricks on Treats Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-21T15:10:34Z",
    "updateDateIncludingText": "2025-11-21T15:10:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
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
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-31",
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
          "date": "2025-10-31T17:03:25Z",
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
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5882ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5882\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Ms. Jacobs (for herself and Mrs. Luna ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to include food containing dyes, flavoring, and sweeteners as misbranded unless the packaging of such food states such fact.\n#### 1. Short title\nThis Act may be cited as the No Tricks on Treats Act of 2025 .\n#### 2. Inclusion of food containing dyes, flavoring, and sweeteners as misbranded\nSection 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ) is amended by adding at the end the following:\n(z) (1) If, in the case of food other than a dietary supplement, such food bears or contains any synthetic dye, or any added artificial or natural flavoring, unless such fact is prominently stated on the principal display panel of the packaging of such food. (2) For the purposes of this paragraph, the term synthetic dye means a batch-certified dye subject to certification under part 74 of title 21, Code of Federal Regulations (or any successor regulations). (aa) If, in the case of food other than a dietary supplement, such food bears or contains any nonnutritive sweetener, unless such fact is prominently stated on the principal display panel of the packaging of such food. .",
      "versionDate": "2025-10-31",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-11-21T15:10:34Z"
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
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5882ih.xml"
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
      "title": "No Tricks on Treats Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-07T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Tricks on Treats Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-07T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to include food containing dyes, flavoring, and sweeteners as misbranded unless the packaging of such food states such fact.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-07T12:18:14Z"
    }
  ]
}
```
