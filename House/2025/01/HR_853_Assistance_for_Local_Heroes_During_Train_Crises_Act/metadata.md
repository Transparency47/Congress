# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/853?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/853
- Title: Assistance for Local Heroes During Train Crises Act
- Congress: 119
- Bill type: HR
- Bill number: 853
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-03-10T15:11:30Z
- Update date including text: 2025-03-10T15:11:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-01 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-01 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/853",
    "number": "853",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "D000530",
        "district": "17",
        "firstName": "Christopher",
        "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
        "lastName": "Deluzio",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Assistance for Local Heroes During Train Crises Act",
    "type": "HR",
    "updateDate": "2025-03-10T15:11:30Z",
    "updateDateIncludingText": "2025-03-10T15:11:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-01",
      "committees": {
        "item": {
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:08:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-01T15:44:32Z",
              "name": "Referred to"
            }
          },
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr853ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 853\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Deluzio (for himself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo authorize the declaration of a hazardous train event, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Assistance for Local Heroes During Train Crises Act .\n#### 2. Hazardous train events\n##### (a) In general\nChapter 209 of title 49, United States Code, is amended by adding at the end the following:\n20904. Hazardous train events (a) Definitions In this section: (1) Administrator The term Administrator means the Administrator of the Federal Railroad Administration. (2) Eligible entity The term eligible entity means a State or local emergency response group, including a law enforcement agency, a fire department, and an emergency response agency, located in an area affected by a hazardous train event. (3) Fund The term Fund means the Hazardous Train Event Emergency Reimbursement Fund established under subsection (c). (4) Hazardous train event The term hazardous train event means a train incident that the Administrator has declared to be a hazardous train event pursuant to subsection (b). (b) Declaration (1) In general The Administrator, in consultation with the Administrator of the Federal Emergency Management Agency and the Administrator of the Environmental Protection Agency, may declare that a hazardous train event has occurred not later than 3 days after the occurrence of a train derailment, train crash, or other incident involving a train carrying hazardous materials, hazardous waste, or other materials that pose a threat to public health, safety, and the environment, as determined by the Administrator. (2) Effect of declaration Upon a declaration pursuant to subsection (a), the Administrator shall immediately award at least $250,000 from the Fund to 1 or more eligible entities pursuant to subsection (d). (3) Additional funding award Not later than 5 days after a declaration pursuant to subsection (a), the Administrator may award additional amounts to the initially awarded entities for further costs or other eligible entities from the Fund, not to exceed $3,000,000 per hazardous train event. Amounts awarded pursuant to this paragraph shall be allocated based on additional needs, as determined by the Administrator. (c) Hazardous Train Event Emergency Reimbursement Fund There is established within the Treasury of the United States a fund, which\u2014 (1) shall be known as the Hazardous Train Event Emergency Reimbursement Fund ; and (2) shall be administered by the Administrator. (d) Assistance for eligible entities (1) In general The Administrator may use amounts from the Fund to reimburse eligible entities, in accordance with subsection (b)\u2014 (A) for the cost of replacing equipment that is damaged, contaminated, or otherwise rendered unusable as a result of the response of the eligible entity to a hazardous train event; (B) for overtime pay for firefighters, law enforcement officers, or other emergency responders who work at the scene of a hazardous train event; (C) for operational costs for actions taken to respond to a hazardous train event; (D) for any other purpose related to a hazardous train event, as determined by the Administrator; and (E) to retroactively cover a cost described in any of subparagraphs (A) through (D) that is incurred after the date of a hazardous train event or within 30 days of the receipt of amounts under this subsection. (2) Documentation of costs (A) In general Not later than 120 days after the date on which the Administrator declares a hazardous train event for which an eligible entity receives assistance under this subsection, the eligible entity shall submit documentation to the Administrator for each item for which such assistance is used through procurement or reimbursement. (B) Reimbursement If the Administrator determines that an eligible entity has used assistance received under this subsection in violation of this subsection, the eligible entity shall reimburse the Fund for the amount of such assistance. Reimbursements to the Fund shall be made eligible for future hazardous train events. .\n##### (b) Clerical amendment\nThe analysis for chapter 209 of title 49, United States Code, is amended by adding at the end the following:\n20904. Hazardous train events. .\n#### 3. Advance warning requirement\nThe Secretary of Transportation, in consultation with the Administrator of the Transportation Security Administration, shall issue regulations requiring any railroad that transports hazardous materials by train through any community in the United States to provide county and local emergency response groups in such community, including police departments, fire departments, and emergency response agencies, with\u2014\n**(1)**\nadvance warning of such train\u2019s load and timing; and\n**(2)**\nreal-time location information on such a train when it enters and exits its service area the applicable service area.\n#### 4. Hazardous materials emergency reimbursement fee\n##### (a) In general\nSection 5108(g) of title 49, United States Code, is amended by adding at the end the following:\n(4) Hazardous materials emergency reimbursement fee for shippers and carriers of hazardous material (A) Schedule of fees The Secretary shall prescribe a schedule of annual fees for shippers and carriers of hazardous materials by rail that have total annual collections of not less than $10,000,000. (B) Deposits into trust fund Fees collected pursuant to subparagraph (A) shall be deposited into the Hazardous Train Event Emergency Reimbursement Fund established under section 20904. .\n##### (b) Deposits into trust fund\nAmounts collected from shippers and carriers pursuant to section 5108(g)(4), United States Code, as added by subsection (a), shall be regularly deposited into the Hazardous Train Event Emergency Reimbursement Fund established under section 20904 of title 49, United States Code, as added by section 2.",
      "versionDate": "2025-01-31",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-03-04T14:42:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr853",
          "measure-number": "853",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-03-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr853v00",
            "update-date": "2025-03-10"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Assistance for Local Heroes During Train Crises Act</strong></p><p>This bill establishes a Hazardous Train Event Emergency Reimbursement Fund for state and local emergency response groups.</p><p>Upon a declaration by the Federal Railroad Administration (FRA) that a hazardous train event has occurred, the FRA must immediately award at least $250,000 from the emergency fund to one or more eligible groups (e.g., law enforcement agencies and fire departments). Additional amounts may be awarded, but may not exceed $3 million per hazardous train event. The FRA may declare a hazardous train event has occurred following a derailment or crash involving a train carrying hazardous materials, hazardous waste, or other materials that pose a threat to public health, safety, and the environment.</p><p>Costs associated with a response to a hazardous train event that are eligible for reimbursement include (1) replacing damaged or contaminated equipment, (2) overtime pay for firefighters\u00a0or law enforcement officers, and (3) retroactively covering these types of incurred costs after the event date.</p><p>The FRA must also (1) establish annual fees for shippers and carriers of hazardous materials by rail that have total annual collections of at least $10 million, and (2) deposit the fees into the reimbursement fund.</p><p>Further, the Department of Transportation must issue regulations requiring railroads that transport hazardous materials by train to provide county and local emergency response groups with (1) advance warning of the train's load and timing, and (2) real-time location information on the train when it enters and exits the community's service area.</p>"
        },
        "title": "Assistance for Local Heroes During Train Crises Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr853.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Assistance for Local Heroes During Train Crises Act</strong></p><p>This bill establishes a Hazardous Train Event Emergency Reimbursement Fund for state and local emergency response groups.</p><p>Upon a declaration by the Federal Railroad Administration (FRA) that a hazardous train event has occurred, the FRA must immediately award at least $250,000 from the emergency fund to one or more eligible groups (e.g., law enforcement agencies and fire departments). Additional amounts may be awarded, but may not exceed $3 million per hazardous train event. The FRA may declare a hazardous train event has occurred following a derailment or crash involving a train carrying hazardous materials, hazardous waste, or other materials that pose a threat to public health, safety, and the environment.</p><p>Costs associated with a response to a hazardous train event that are eligible for reimbursement include (1) replacing damaged or contaminated equipment, (2) overtime pay for firefighters\u00a0or law enforcement officers, and (3) retroactively covering these types of incurred costs after the event date.</p><p>The FRA must also (1) establish annual fees for shippers and carriers of hazardous materials by rail that have total annual collections of at least $10 million, and (2) deposit the fees into the reimbursement fund.</p><p>Further, the Department of Transportation must issue regulations requiring railroads that transport hazardous materials by train to provide county and local emergency response groups with (1) advance warning of the train's load and timing, and (2) real-time location information on the train when it enters and exits the community's service area.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr853"
    },
    "title": "Assistance for Local Heroes During Train Crises Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Assistance for Local Heroes During Train Crises Act</strong></p><p>This bill establishes a Hazardous Train Event Emergency Reimbursement Fund for state and local emergency response groups.</p><p>Upon a declaration by the Federal Railroad Administration (FRA) that a hazardous train event has occurred, the FRA must immediately award at least $250,000 from the emergency fund to one or more eligible groups (e.g., law enforcement agencies and fire departments). Additional amounts may be awarded, but may not exceed $3 million per hazardous train event. The FRA may declare a hazardous train event has occurred following a derailment or crash involving a train carrying hazardous materials, hazardous waste, or other materials that pose a threat to public health, safety, and the environment.</p><p>Costs associated with a response to a hazardous train event that are eligible for reimbursement include (1) replacing damaged or contaminated equipment, (2) overtime pay for firefighters\u00a0or law enforcement officers, and (3) retroactively covering these types of incurred costs after the event date.</p><p>The FRA must also (1) establish annual fees for shippers and carriers of hazardous materials by rail that have total annual collections of at least $10 million, and (2) deposit the fees into the reimbursement fund.</p><p>Further, the Department of Transportation must issue regulations requiring railroads that transport hazardous materials by train to provide county and local emergency response groups with (1) advance warning of the train's load and timing, and (2) real-time location information on the train when it enters and exits the community's service area.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr853"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr853ih.xml"
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
      "title": "Assistance for Local Heroes During Train Crises Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T09:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Assistance for Local Heroes During Train Crises Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T09:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the declaration of a hazardous train event, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T09:03:28Z"
    }
  ]
}
```
