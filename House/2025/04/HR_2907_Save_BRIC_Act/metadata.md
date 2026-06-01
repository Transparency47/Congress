# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2907?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2907
- Title: Save BRIC Act
- Congress: 119
- Bill type: HR
- Bill number: 2907
- Origin chamber: House
- Introduced date: 2025-04-14
- Update date: 2026-03-18T19:06:15Z
- Update date including text: 2026-03-18T19:06:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-14: Introduced in House
- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-14 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-04-14: Introduced in House

## Actions

- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-14 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-14",
    "latestAction": {
      "actionDate": "2025-04-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2907",
    "number": "2907",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "S001211",
        "district": "4",
        "firstName": "Greg",
        "fullName": "Rep. Stanton, Greg [D-AZ-4]",
        "lastName": "Stanton",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Save BRIC Act",
    "type": "HR",
    "updateDate": "2026-03-18T19:06:15Z",
    "updateDateIncludingText": "2026-03-18T19:06:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-14",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-14",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-14",
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
          "date": "2025-04-14T13:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-14T21:12:05Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-04-14",
      "state": "PA"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "PA"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2907ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2907\nIN THE HOUSE OF REPRESENTATIVES\nApril 14, 2025 Mr. Stanton (for himself and Mr. Bresnahan ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend section 203 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act to require the President to provide assistance for predisaster hazard mitigation measures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Save Building Resilient Infrastructure and Communities Act or the Save BRIC Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nPredisaster mitigation enables actions to be taken proactively to reduce loss of life and property by lessening the impact of future disasters.\n**(2)**\nEffective mitigation minimizes the potential loss of life and property from a disaster based on identifying and understanding the risks in a given area or community.\n**(3)**\nThe United States experienced 27 weather and climate disasters with damages exceeding $1,000,000,000 in 2024.\n**(4)**\nMitigation can encompass a wide variety of activities, including preparation and planning, elevating or moving structures prone to flooding, reducing loss of life during extreme heat, and hardening structures to mitigate the effects of hurricanes or earthquakes.\n**(5)**\nScientific research has proven that every $1 invested in predisaster mitigation saves up to $13 in disaster recovery costs.\n**(6)**\nIn 2019, President Trump created the predisaster mitigation program known as Building Resilient Communities and Infrastructure (BRIC) because it is prudent from a business and insurance perspective.\n**(7)**\nIn 2025, the BRIC program was wrongfully cancelled and over $4,000,000,000 of predisaster mitigation grants were clawed back from communities vulnerable to disaster damage.\n#### 3. Mandatory mitigation\nSection 203 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5133 ) is amended\u2014\n**(1)**\nin subsection (b) by striking may and inserting shall ; and\n**(2)**\nin subsection (c) by striking may and inserting shall .",
      "versionDate": "2025-04-14",
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
        "name": "Emergency Management",
        "updateDate": "2025-05-27T16:52:17Z"
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
      "date": "2025-04-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2907ih.xml"
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
      "title": "Save BRIC Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-02T03:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Save BRIC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-02T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Save Building Resilient Infrastructure and Communities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-02T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 203 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act to require the President to provide assistance for predisaster hazard mitigation measures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-02T03:03:32Z"
    }
  ]
}
```
