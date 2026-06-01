# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5067?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5067
- Title: Rapid Disaster Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 5067
- Origin chamber: House
- Introduced date: 2025-08-29
- Update date: 2025-10-07T08:05:36Z
- Update date including text: 2025-10-07T08:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-29: Introduced in House
- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-08-30 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-08-29: Introduced in House

## Actions

- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-08-30 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-29",
    "latestAction": {
      "actionDate": "2025-08-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5067",
    "number": "5067",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "M001237",
        "district": "8",
        "firstName": "Kristen",
        "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
        "lastName": "McDonald Rivet",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Rapid Disaster Relief Act",
    "type": "HR",
    "updateDate": "2025-10-07T08:05:36Z",
    "updateDateIncludingText": "2025-10-07T08:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-30",
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
      "actionDate": "2025-08-29",
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
      "actionDate": "2025-08-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-29",
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
          "date": "2025-08-29T17:32:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-08-30T21:37:35Z",
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
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5067ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5067\nIN THE HOUSE OF REPRESENTATIVES\nAugust 29, 2025 Ms. McDonald Rivet (for herself and Mr. Moolenaar ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act with respect to the disbursement of certain reimbursements provided under such Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rapid Disaster Relief Act .\n#### 2. Expedited funding for emergency work\nSection 403 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170b ) is amending by adding at the end the following:\n(e) Disbursement Reimbursements provided under this section shall be disbursed to the applicant not later than 120 days after the applicant submits a request for reimbursement if the President determines at least 90 percent of estimated costs are eligible for such reimbursement. .",
      "versionDate": "2025-08-29",
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
        "actionDate": "2025-09-03",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 57 - 3."
      },
      "number": "4669",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FEMA Act of 2025",
      "type": "HR"
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
        "updateDate": "2025-09-17T20:02:25Z"
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
      "date": "2025-08-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5067ih.xml"
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
      "title": "Rapid Disaster Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-03T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rapid Disaster Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-03T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act with respect to the disbursement of certain reimbursements provided under such Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-03T05:18:22Z"
    }
  ]
}
```
