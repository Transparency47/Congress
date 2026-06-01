# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5341?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5341
- Title: LOCAL Foods Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5341
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2026-03-27T08:06:39Z
- Update date including text: 2026-03-27T08:06:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5341",
    "number": "5341",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "LOCAL Foods Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-27T08:06:39Z",
    "updateDateIncludingText": "2026-03-27T08:06:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:06:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "IN"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "TX"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "CO"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "VA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "VT"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5341ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5341\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Mr. Vindman (for himself and Mr. Baird ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Federal Meat Inspection Act to exempt certain owners of livestock from inspection requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Livestock Owned by Communities to Advance Local Foods Act of 2025 or the LOCAL Foods Act of 2025 .\n#### 2. Exemptions from inspection\nSection 23(a) of the Federal Meat Inspection Act ( 21 U.S.C. 623(a) ) is amended by striking the slaughtering by any person of animals of his own raising, and the preparation by him and transportation in commerce of the carcasses, parts thereof, meat and meat food products of such animals exclusively for use by him and members of his household and his nonpaying guests and employees and inserting the slaughtering of animals by any person that is an owner of the animals in whole or in part, or the preparation or transportation in commerce of the carcasses or parts thereof or meat and meat food products from those animals by an owner, if such slaughter, preparation, or transportation is exclusively for the use of an owner or the household, nonpaying guests, or employees of an owner, subject to the condition that if an owner designates an agent to assist in such slaughter, preparation, or transportation, the owner shall maintain custody and specific identification of the carcasses or parts thereof or meat and meat food products, as determined by the Secretary .",
      "versionDate": "2025-09-11",
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
        "actionDate": "2025-03-31",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1212",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "LOCAL Foods Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-09-24T15:10:39Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5341ih.xml"
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
      "title": "LOCAL Foods Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-24T06:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LOCAL Foods Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-24T06:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Livestock Owned by Communities to Advance Local Foods Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-24T06:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Meat Inspection Act to exempt certain owners of livestock from inspection requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-24T06:33:17Z"
    }
  ]
}
```
