# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2342?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2342
- Title: State-Managed Disaster Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 2342
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2025-09-17T14:43:46Z
- Update date including text: 2025-09-17T14:43:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-25 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-03-25: Introduced in House

## Actions

- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-25 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2342",
    "number": "2342",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "R000603",
        "district": "7",
        "firstName": "David",
        "fullName": "Rep. Rouzer, David [R-NC-7]",
        "lastName": "Rouzer",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "State-Managed Disaster Relief Act",
    "type": "HR",
    "updateDate": "2025-09-17T14:43:46Z",
    "updateDateIncludingText": "2025-09-17T14:43:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T14:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-25T20:45:35Z",
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2342ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2342\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Mr. Rouzer (for himself and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo establish alternate procedures for lump sum payments for certain covered small disasters, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the State-Managed Disaster Relief Act .\n#### 2. Alternative procedures for covered small disasters\nThe Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ) is amended by adding at the end the following:\nVIII Alternative Procedures for Covered Small Disasters 801. Alternative procedures for covered small disasters (a) In general The Governor of a State or the governing body of an Indian tribal government for the area in which a covered small disaster occurs may request a lump sum payment of the estimated damages calculated under subsection (b) for such disaster in lieu of any assistance under the Public Assistance Program for such disaster. (b) Calculation Notwithstanding the requirements of section 206.47(b) of title 44, Code of Federal Regulations, a payment under subsection (a) shall be equal to the amount that is 80 percent of the total estimated cost of assistance under the Public Assistance Program for a covered small disaster in the area of jurisdiction of the State or Indian tribal government requesting such payment. (c) Limitations (1) In general A State or Indian tribal government receiving a payment under this section may not receive assistance under the Public Assistance Program with respect to the covered small disaster for which a payment was accepted under this section. (2) Final payment (A) In general A payment under this section may not be increased or decreased based on actual costs calculated for a covered small disaster. (B) Exception Notwithstanding subparagraph (A), the Administrator may adjust a payment under this section in the event of unforeseen circumstances at no fault of the applicant. (3) Selection of option A State or Indian tribal government may designate to the Federal Emergency Management Agency on an annual basis the interest of such State or Indian tribal government in participating in the small disaster authority. (4) Indication A State or Indian tribal government shall indicate at the time of the submission of a request for a major disaster declaration that such State or Indian tribal government is requesting assistance for such incident under this section. (5) Timing requirement The Administrator and the State or Indian tribal government shall\u2014 (A) reach an agreement on the amount under subsection (b) not later than 90 days after the incident; or (B) administer the incident under the procedures and authorities for the Public Assistance Program. (6) Administrative plan To be eligible for assistance under this section, a State or Indian tribal government shall have an approved administrative plan in place at the time of the obligation of funds provided under this section. (d) Use of funds A State or Indian tribal government receiving a payment under this section may use such payment for recovery for the covered small disaster in any manner determined appropriate by the respective Governor or governing body of such State or Indian tribal government if such funds\u2014 (1) address impacts and needs resulting from the declared disaster incident; (2) are provided to State, Indian tribal government, territorial and local government agencies, and private non-profit entities eligible for Public Assistance Program funding; and (3) are used in a manner that complies with applicable environmental, historic preservation, and civil rights laws (including the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) and the National Historic Preservation Act of 1966 ( 54 U.S.C. 300101 et seq. )) and any applicable resiliency standards under section 203. (e) Compliance with other laws and regulations A State or Indian tribal government shall be responsible for ensuring compliance under subsection (d)(3). (f) Rule of construction Nothing in this section shall be construed to affect the eligibility of a State or Indian tribal government for assistance under section 404. (g) Report to FEMA A State or governing body of an Indian tribal government shall submit to the Federal Emergency Management Agency an annual report of expenses for a covered small disaster in the area of jurisdiction of the respective State or Indian tribal government. (h) Savings clause Nothing in this section shall be construed to affect any program in title IV or V that is not a Public Assistance Program. (i) Definitions In this section: (1) Covered small disaster The term covered small disaster means a major disaster declared under section 401 or an emergency declared under section 501 with estimated damage eligible under the Public Assistance Program of less than or equal to 125 percent of the State\u2019s per capita indicator. (2) Public Assistance Program The term Public Assistance Program means the programs under sections 403, 406, 407, and 502. .",
      "versionDate": "2025-03-25",
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
        "updateDate": "2025-05-21T17:59:46Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2342ih.xml"
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
      "title": "State-Managed Disaster Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-05T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "State-Managed Disaster Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-05T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish alternate procedures for lump sum payments for certain covered small disasters, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-05T04:18:14Z"
    }
  ]
}
```
