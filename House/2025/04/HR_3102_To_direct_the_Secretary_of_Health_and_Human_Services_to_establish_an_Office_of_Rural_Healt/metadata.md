# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3102?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3102
- Title: To direct the Secretary of Health and Human Services to establish an Office of Rural Health, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 3102
- Origin chamber: House
- Introduced date: 2025-04-30
- Update date: 2026-02-12T09:06:29Z
- Update date including text: 2026-02-12T09:06:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-30: Introduced in House

## Actions

- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3102",
    "number": "3102",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000591",
        "district": "3",
        "firstName": "Michael",
        "fullName": "Rep. Guest, Michael [R-MS-3]",
        "lastName": "Guest",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "To direct the Secretary of Health and Human Services to establish an Office of Rural Health, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-02-12T09:06:29Z",
    "updateDateIncludingText": "2026-02-12T09:06:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
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
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T14:05:35Z",
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
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "WA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "VA"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3102ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3102\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2025 Mr. Guest (for himself and Ms. Perez ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services to establish an Office of Rural Health, and for other purposes.\n#### 1. CDC Office of Rural Health\n##### (a) In general\nThe Secretary of Health and Human Services, acting through the Director of the Centers for Disease Control and Prevention, shall establish within the Centers for Disease Control and Prevention an office to be known as the Office of Rural Health, to be headed by a director selected by the Director of the Centers for Disease Control and Prevention.\n##### (b) Duties and authorities\nThe duties and authorities of the Director of the Office of Rural Health shall be limited to the following:\n**(1)**\nServing as the primary point of contact in the Centers for Disease Control and Prevention on matters pertaining to rural health.\n**(2)**\nAssisting the Director of the Centers for Disease Control and Prevention in conducting, coordinating, and promoting research regarding public health issues affecting rural populations, and in disseminating the results of such research.\n**(3)**\nWorking with all personnel and offices of the Centers for Disease Control and Prevention to develop, refine, coordinate, and promulgate policies, best practices, lessons learned, and innovative, successful programs to improve care and services (including through telehealth) for rural populations.\n**(4)**\nCoordinating and supporting rural health research, conducting and supporting educational outreach, and disseminating evidence-based interventions related to health outcomes, access to health care, and lifestyle challenges, to prevent death, disease, injury, and disability, and promote healthy behaviors in rural populations.\n**(5)**\nImproving the understanding of the health challenges faced by rural populations.\n**(6)**\nIdentifying disparities in the availability of health care and public health interventions for rural populations.\n**(7)**\nAwarding and administering grants, cooperative agreements, and contracts to provide technical assistance and other activities as necessary to support activities related to improving health and health care in rural areas.\n**(8)**\nCoordinating with the Federal Office of Rural Health Policy of the Health Resources and Services Administration, as needed, to facilitate co-operation on rural health initiatives and avoid duplication of efforts.",
      "versionDate": "2025-04-30",
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
        "actionDate": "2025-02-05",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "403",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Rural Health Focus Act",
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
        "name": "Health",
        "updateDate": "2025-05-21T10:35:29Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3102ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services to establish an Office of Rural Health, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T06:18:41Z"
    },
    {
      "title": "To direct the Secretary of Health and Human Services to establish an Office of Rural Health, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-01T08:06:09Z"
    }
  ]
}
```
