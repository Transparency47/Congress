# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3252?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3252
- Title: Disaster Housing Flexibility Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3252
- Origin chamber: House
- Introduced date: 2025-05-07
- Update date: 2025-06-12T08:07:06Z
- Update date including text: 2025-06-12T08:07:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-07 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-05-07: Introduced in House

## Actions

- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-07 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3252",
    "number": "3252",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "M001217",
        "district": "23",
        "firstName": "Jared",
        "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
        "lastName": "Moskowitz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Disaster Housing Flexibility Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-12T08:07:06Z",
    "updateDateIncludingText": "2025-06-12T08:07:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-07",
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
      "actionDate": "2025-05-07",
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
      "actionDate": "2025-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-07",
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
          "date": "2025-05-07T14:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-07T21:15:26Z",
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
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "TN"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "GU"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3252ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3252\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2025 Mr. Moskowitz (for himself and Mr. Burchett ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to provide for an alternative block grant program for funding temporary housing in response to a major disaster, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disaster Housing Flexibility Act of 2025 .\n#### 2. Alternative block grant program\nTitle IV of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 et seq. ) is amended by adding at the end the following:\n431. Alternative block grant program for temporary housing assistance (a) Establishment The President, acting through the Administrator of the Federal Emergency Management Agency, shall establish an alternative block grant program for providing funds for temporary housing assistance for individuals and households in the event of a major disaster declared by the President under this title. (b) Assessment of cost of temporary housing assistance (1) Assessment required In the event of a major disaster described in subsection (a), the Administrator shall assess the cost of providing temporary housing assistance in each impacted State in which individuals and households would otherwise eligible for temporary housing assistance, including reasonable administrative expenses incurred by the State necessary to manage and distribute a block grant under this section. (2) Consultation In making an assessment under paragraph (1), the Administrator shall consult with each applicable State to ensure that the amount of the assessment reflects a reasonable estimate of the amount necessary to provide for temporary housing assistance in an amount that would otherwise be provided under\u2014 (A) section 408(c); or (B) other housing assistance programs identified as needed by the State. (c) Program requirements In carrying out the program under this section, the President shall\u2014 (1) establish a process for a State to elect to apply for a block under this section grant in lieu of the eligibility of individuals and households to apply for assistance under section 408(c); and (2) ensure that a State may request a single adjustment to the amount provided in such block grant if the initial amount is insufficient to provide individuals and households assistance equivalent to the assistance otherwise provided under such section. (d) Application To be eligible for a block grant under this section, a State shall submit to the President an application in such manner and containing such information as the President may require. (e) Applicability In any case in which a State receives a block grant under this section, an individual or household located in the area covered by a disaster declaration made by the President under section 401 and covered by such grant shall not be eligible for temporary housing assistance under section 408(c). (f) Remaining funds Any funds provided under this section that remain after the completion of recovery activities for which such funds are provided may be used for preparedness or mitigation activities in the State that are eligible for assistance under this Act. (g) Reports (1) State reports A State that receives a block grant under this section shall submit to the Administrator\u2014 (A) not later than 120 days after the date on which such grant was received, an initial disbursement plan outlining anticipated uses of funds; (B) not later than 1 year after the submission of the report under subparagraph (A), and annually thereafter until all funds provided under the grant are expended, a report containing\u2014 (i) a description of each individual or household for which funds were spent; (ii) in any case in which the State has remaining funds described under subsection (f), the proposed use of such funds; and (iii) an assessment of the impact and effectiveness of any expenditures of such funds; and (C) not later than 180 days after all funds provided under the grant have been expended, a final report containing\u2014 (i) a description of all assistance provided with such funds; and (ii) an analysis of the overall effectiveness of the assistance provided under such grant. (2) Report to Congress Not later than 12 months after the date of enactment of this section, and annually thereafter, the Administrator shall submit to Congress a report on the implementation of the program established under this section that includes\u2014 (A) a list of States that have elected to participate in such program; (B) a description of how the Administrator has implemented the program, including administrative procedures and timelines; (C) an assessment of any challenges and barriers to State participation and program implementation; (D) an evaluation of the accuracy and timeliness of cost estimates used to determine grant amounts; (E) the average length of time required to make cost estimates and disburse grant funds following a declaration of a major disaster; (F) a review of the administrative impact on the Administration and participating States, including staffing and oversight capacity; and (G) recommendations for statutory, regulatory, or administrative changes needed to\u2014 (i) improve delivery under such program; (ii) support administration of the program; or (iii) enhance effectiveness of the program. (h) Temporary housing assistance defined The term temporary housing assistance means any assistance provided to individuals and households under section 408(c). .",
      "versionDate": "2025-05-07",
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
        "updateDate": "2025-06-09T14:51:13Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3252ih.xml"
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
      "title": "To amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to provide for an alternative block grant program for funding temporary housing in response to a major disaster, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T03:59:38Z"
    },
    {
      "title": "Disaster Housing Flexibility Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T03:39:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Disaster Housing Flexibility Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T03:38:25Z"
    }
  ]
}
```
