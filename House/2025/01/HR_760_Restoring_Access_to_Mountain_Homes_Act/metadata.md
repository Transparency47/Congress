# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/760?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/760
- Title: Restoring Access to Mountain Homes Act
- Congress: 119
- Bill type: HR
- Bill number: 760
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-12-05T22:50:40Z
- Update date including text: 2025-12-05T22:50:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-29 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-29 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/760",
    "number": "760",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "E000246",
        "district": "11",
        "firstName": "Chuck",
        "fullName": "Rep. Edwards, Chuck [R-NC-11]",
        "lastName": "Edwards",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Restoring Access to Mountain Homes Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:50:40Z",
    "updateDateIncludingText": "2025-12-05T22:50:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-29",
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
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:08:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-29T15:43:09Z",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "NC"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NC"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr760ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 760\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Edwards (for himself, Mr. Davis of North Carolina , and Mr. Moore of North Carolina ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo make certain repairs, replacements, and restorations of private roads and bridges eligible for reimbursement under the Robert T. Stafford Disaster Relief and Emergency Assistance Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restoring Access to Mountain Homes Act .\n#### 2. Reimbursement for repair, replacement, and restoration work on private roads and bridges impacted by Tropical Storm Helene\n##### (a) Eligibility for reimbursement\nNotwithstanding any provision of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ) or the regulations governing the public assistance program of the Federal Emergency Management Agency under such Act, the State, Indian Tribal, and local governments in North Carolina covered under major disaster declaration FEMA\u20134827\u2013DR\u2013NC (relating to Tropical Storm Helene) shall be eligible for reimbursement for the cost of repairs, replacements, or restoration to private roads and bridges, without regard to pre-existing condition, under section 428 of such Act that\u2014\n**(1)**\nare used as the sole means of access to primary residences or essential community services;\n**(2)**\nare significantly damaged or destroyed as a direct result of Tropical Storm Helene as identified in FEMA\u20134827\u2013DR\u2013NC; and\n**(3)**\ndoes not duplicate work that has already been completed.\n##### (b) Conditions of reimbursement\nReimbursement under this section shall be subject to the following conditions:\n**(1)**\nPrivate roads or bridges shall be inspected by appropriate State, Indian Tribal, or local government officials or their designees to verify the scope, need, and cost-effectiveness of any mitigation measures for the proposed repair, replacement, or restoration.\n**(2)**\nThe State, Indian Tribal, or local governments requesting assistance shall ensure that the private roads or bridges being repaired, replaced, or restored remain open for disaster recovery activities for the duration of the repair, replacement, or restoration process.\n**(3)**\nThe State or Indian Tribal governments shall be responsible for documenting all costs associated with repairs, replacements, or restorations within their jurisdiction in accordance with Federal Emergency Management Agency policy.\n**(4)**\nThe State, Indian Tribal, or local government applying for public assistance funding shall obtain authority or permission to perform the work to permanently repair, replace, or restore the private roads and bridges.\n**(5)**\nThe State, Indian Tribal, or local government applying for public assistance funding shall ensure the work under this section is performed in compliance with all applicable State and Federal regulations and requirements that pertain to work that is permanent in nature.\n##### (c) Duplication of benefits\n**(1) In general**\nAny individual or household that has received assistance prior to the date of enactment of this section pursuant to section 408 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5174 ) for the purposes of repairing a private road or bridge eligible under this section may proceed with such repairs or return any such assistance to have such repair eligible pursuant to this section.\n**(2) Calculation**\nIn the event the individual or household chooses to proceed with such repairs utilizing assistance provided pursuant to section 408 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5174 ) for a private road or bridge, such assistance shall not be counted against the maximum amount of assistance for such individual or household under such section.\n##### (d) Eligible costs\nIn determining eligible costs, the Administrator shall base such determinations on properly conducted and certified cost estimates prepared by professionally licensed engineers (mutually agreed upon by the Administrator and the applicant). Once certified by a professionally licensed engineer and accepted by the Administrator, the estimates on which grants made pursuant to this section are based shall be presumed to be reasonable and eligible costs, as long as there is no evidence of fraud.",
      "versionDate": "2025-01-28",
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
        "actionDate": "2025-01-28",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "267",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Restoring Access to Mountain Homes Act",
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
        "name": "Emergency Management",
        "updateDate": "2025-05-01T21:19:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr760",
          "measure-number": "760",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-05-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr760v00",
            "update-date": "2025-05-14"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Restoring Access to Mountain Homes Act</strong></p><p>This bill authorizes the Federal Emergency Management Agency (FEMA) to provide Public Assistance (PA) grant funding, under certain conditions, to reimburse government entities covered under the major disaster declaration for North Carolina relating to Tropical Storm Helene for the costs of repairing, replacing, or restoring private roads and bridges damaged by Helene.</p><p>Under current law, the PA program provides grants for repairing disaster damage to infrastructure owned or legally maintained by government entities (or certain\u00a0nonprofits). The bill authorizes PA funding for permanent repair work on privately\u00a0owned and maintained roads and bridges significantly damaged by Helene in North Carolina, as costs incurred by state, tribal, or local governments for such work are eligible for reimbursement. \u00a0\u00a0</p><p>Also, under current law, the costs of repairing damage that existed before the disaster are generally ineligible for PA. The bill makes the repair, replacement, or restoration costs eligible for reimbursement under PA regardless of pre-existing condition.</p><p>Additionally, the bill contains criteria and conditions for reimbursement, including that to be eligible a road or bridge must be used as the sole means of accessing primary residences or essential community services. Reimbursement is under PA\u2019s alternative procedures, and the bill requires\u00a0FEMA to determine eligible costs based on estimates prepared by engineers.</p><p>Recipients of funds from\u00a0FEMA\u2019s Individuals and Households Program (IHP) before the bill\u2019s enactment may use IHP funds for repairs eligible under the bill without those costs counting against their maximum amount of IHP assistance.</p>"
        },
        "title": "Restoring Access to Mountain Homes Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr760.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Restoring Access to Mountain Homes Act</strong></p><p>This bill authorizes the Federal Emergency Management Agency (FEMA) to provide Public Assistance (PA) grant funding, under certain conditions, to reimburse government entities covered under the major disaster declaration for North Carolina relating to Tropical Storm Helene for the costs of repairing, replacing, or restoring private roads and bridges damaged by Helene.</p><p>Under current law, the PA program provides grants for repairing disaster damage to infrastructure owned or legally maintained by government entities (or certain\u00a0nonprofits). The bill authorizes PA funding for permanent repair work on privately\u00a0owned and maintained roads and bridges significantly damaged by Helene in North Carolina, as costs incurred by state, tribal, or local governments for such work are eligible for reimbursement. \u00a0\u00a0</p><p>Also, under current law, the costs of repairing damage that existed before the disaster are generally ineligible for PA. The bill makes the repair, replacement, or restoration costs eligible for reimbursement under PA regardless of pre-existing condition.</p><p>Additionally, the bill contains criteria and conditions for reimbursement, including that to be eligible a road or bridge must be used as the sole means of accessing primary residences or essential community services. Reimbursement is under PA\u2019s alternative procedures, and the bill requires\u00a0FEMA to determine eligible costs based on estimates prepared by engineers.</p><p>Recipients of funds from\u00a0FEMA\u2019s Individuals and Households Program (IHP) before the bill\u2019s enactment may use IHP funds for repairs eligible under the bill without those costs counting against their maximum amount of IHP assistance.</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119hr760"
    },
    "title": "Restoring Access to Mountain Homes Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Restoring Access to Mountain Homes Act</strong></p><p>This bill authorizes the Federal Emergency Management Agency (FEMA) to provide Public Assistance (PA) grant funding, under certain conditions, to reimburse government entities covered under the major disaster declaration for North Carolina relating to Tropical Storm Helene for the costs of repairing, replacing, or restoring private roads and bridges damaged by Helene.</p><p>Under current law, the PA program provides grants for repairing disaster damage to infrastructure owned or legally maintained by government entities (or certain\u00a0nonprofits). The bill authorizes PA funding for permanent repair work on privately\u00a0owned and maintained roads and bridges significantly damaged by Helene in North Carolina, as costs incurred by state, tribal, or local governments for such work are eligible for reimbursement. \u00a0\u00a0</p><p>Also, under current law, the costs of repairing damage that existed before the disaster are generally ineligible for PA. The bill makes the repair, replacement, or restoration costs eligible for reimbursement under PA regardless of pre-existing condition.</p><p>Additionally, the bill contains criteria and conditions for reimbursement, including that to be eligible a road or bridge must be used as the sole means of accessing primary residences or essential community services. Reimbursement is under PA\u2019s alternative procedures, and the bill requires\u00a0FEMA to determine eligible costs based on estimates prepared by engineers.</p><p>Recipients of funds from\u00a0FEMA\u2019s Individuals and Households Program (IHP) before the bill\u2019s enactment may use IHP funds for repairs eligible under the bill without those costs counting against their maximum amount of IHP assistance.</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119hr760"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr760ih.xml"
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
      "title": "Restoring Access to Mountain Homes Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Restoring Access to Mountain Homes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To make certain repairs, replacements, and restorations of private roads and bridges eligible for reimbursement under the Robert T. Stafford Disaster Relief and Emergency Assistance Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:20Z"
    }
  ]
}
```
