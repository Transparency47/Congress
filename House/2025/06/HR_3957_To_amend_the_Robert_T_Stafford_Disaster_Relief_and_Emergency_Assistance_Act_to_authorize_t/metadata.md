# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3957?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3957
- Title: To amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to authorize the President to provide certain fire management assistance to Indian Tribal Governments, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 3957
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2025-12-05T21:51:47Z
- Update date including text: 2025-12-05T21:51:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-13 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-13 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3957",
    "number": "3957",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "D000629",
        "district": "3",
        "firstName": "Sharice",
        "fullName": "Rep. Davids, Sharice [D-KS-3]",
        "lastName": "Davids",
        "party": "D",
        "state": "KS"
      }
    ],
    "title": "To amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to authorize the President to provide certain fire management assistance to Indian Tribal Governments, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-12-05T21:51:47Z",
    "updateDateIncludingText": "2025-12-05T21:51:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-13",
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
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-13T20:52:18Z",
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
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "SD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3957ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3957\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Ms. Davids of Kansas (for herself and Mr. Johnson of South Dakota ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to authorize the President to provide certain fire management assistance to Indian Tribal Governments, and for other purposes.\n#### 1. Indian tribal government eligibility\n##### (a) In general\nSection 420 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5187 ) is amended\u2014\n**(1)**\nin subsection (a), by inserting , Indian Tribal Government, before or local government ;\n**(2)**\nby redesignating subsections (b) through (e) as subsections (c) through (f), respectively;\n**(3)**\nby inserting after subsection (a) the following:\n(b) Procedure for request The Governor of a State or the Chief Executive of an Indian Tribal Government affected by a fire described in subsection (a) may directly submit a request to authorize assistance under this section. ; and\n**(4)**\nby adding at the end the following:\n(g) Savings provision Nothing in this section shall prohibit an Indian Tribal Government from receiving assistance under this section pursuant to an authorization made at the request of a State under subsection (b) if assistance is not authorized under this section for the same incident based on a request by the Indian Tribal Government under subsection (b). .\n##### (b) Regulations\n**(1) Update**\nNot later than 1 year after the date of enactment of this Act, the President shall issue regulations updating part 204 of title 44, Code of Federal Regulations, to carry out the amendments made by subsection (a).\n**(2) Contents**\nIn issuing the regulations required under paragraph (1), the President shall\u2014\n**(A)**\nauthorize the Federal Emergency Management Agency to directly receive a request for a fire management assistance declaration from an Indian Tribal Government and directly provide related grants and resources to Indian Tribal Governments;\n**(B)**\nclarify that Indian Tribal Governments for which the President does not grant a request described in subparagraph (A) remain eligible to receive assistance under section 420 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5187 ) through assistance granted under a fire management assistance declaration made at the request of a State;\n**(C)**\nconsider the unique conditions that affect the general welfare of Indian Tribal Governments; and\n**(D)**\nenter into government-to-government consultation with Indian Tribal Governments regarding the regulations.\n**(3) Fire management assistance declaration defined**\nIn this subsection, the term fire management assistance declaration means a declaration approved under section 204.21(a) of title 44, Code of Federal Regulations.",
      "versionDate": "2025-06-12",
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
        "actionDate": "2025-02-06",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "443",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Fire Management Assistance Grants for Tribal Governments Act",
      "type": "S"
    },
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
        "updateDate": "2025-07-30T21:50:16Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3957ih.xml"
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
      "title": "To amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to authorize the President to provide certain fire management assistance to Indian Tribal Governments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T02:48:33Z"
    },
    {
      "title": "To amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to authorize the President to provide certain fire management assistance to Indian Tribal Governments, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-13T08:06:56Z"
    }
  ]
}
```
