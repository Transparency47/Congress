# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1451?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1451
- Title: Quapaw Tribal Settlement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1451
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2025-12-05T22:03:55Z
- Update date including text: 2025-12-05T22:03:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-04-23 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2025-04-30 - Committee: Subcommittee Hearings Held
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-04-23 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2025-04-30 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1451",
    "number": "1451",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "B001317",
        "district": "2",
        "firstName": "Josh",
        "fullName": "Rep. Brecheen, Josh [R-OK-2]",
        "lastName": "Brecheen",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Quapaw Tribal Settlement Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:03:55Z",
    "updateDateIncludingText": "2025-12-05T22:03:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-23",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Indian and Insular Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:31:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-04-30T20:03:09Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-04-23T14:46:24Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "systemCode": "hsii00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1451ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1451\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Brecheen introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo authorize the Secretary of the Treasury to make payments to the Quapaw Nation and certain members of the Quapaw Nation in accordance with the recommendation of the United States Court of Federal Claims, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Quapaw Tribal Settlement Act of 2025 .\n#### 2. Quapaw Tribal settlement\n##### (a) Definitions\nIn this section:\n**(1) Claimant**\nThe term Claimant means each of\u2014\n**(A)**\nthe Quapaw Nation and the parties identified in paragraphs 1 through 10 of the complaint in Bear, et al. v. United States, No. 13\u201351X (Fed. Cl. Mar. 25, 2013); and\n**(B)**\nthe individual members of the Quapaw Nation identified in Exhibit A to the amended complaint in Bear, et al. v. United States, No. 13\u201351X (Fed. Cl. Mar. 25, 2013) filed on February 14, 2014.\n**(2) Report**\nThe term Report means the report of the Review Panel of the United States Court of Federal Claims in Congressional Reference Case No. 13\u201351X, Bear, et al. v. United States (Jan. 9, 2020), submitted to the House of Representatives on January 31, 2020.\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior (or a designee).\n##### (b) Establishment\nThere is established a Special Deposit Account in the Department of the Interior Bureau of Trust Funds Administration, to be known as the Quapaw Bear Settlement Trust Account .\n##### (c) Administration\nThe Secretary of the Interior by and through the Bureau of Trust Funds Administration shall administer all funds appropriated to the Quapaw Bear Settlement Trust Account.\n##### (d) Authorization of payment\nIn accordance with the Report, the Secretary of the Interior is authorized and directed to pay to the Claimants $137,500,000 out of any funds in the Treasury of the United States not otherwise appropriated. The Secretary of the Treasury shall transfer the single payment to the Quapaw Bear Settlement Trust Account established in subsection (b).\n##### (e) Payment in accordance with report\nThe payment under subsection (d) shall be made in accordance with the Report.\n##### (f) Distribution\nAfter the settlement proceeds are transferred to the Quapaw Bear Settlement Trust Account specified under subsection (b), the settlement proceeds shall be available for use, allocation, and distribution in accordance with the Claimants\u2019 distribution plan. The Claimants shall establish a distribution plan in accordance with subsection (d) and the procedures set forth in subsection (g).\n##### (g) Distribution of Funds in the Quapaw Bear Settlement Trust Account\n**(1) Mediation**\n**(A)**\nNo more than forty-five (45) days following enactment of the Act, the Claimants shall submit the issues of the allocation and distribution of the settlement proceeds to a mutually agreed upon third-party mediator.\n**(B)**\nIn the event the Claimants do not submit to a mutually agreed upon third-party mediation within forty-five (45) days pursuant to the preceding subparagraph, then any Claimant may initiate Secretarial Allocation procedures under paragraph (2) below.\n**(C)**\nAny mediation shall be confidential and non-binding on the Claimants without the written consent of the Claimants, provided that nothing in this paragraph shall be interpreted to bar the Quapaw Nation Business Committee from consulting with the Quapaw Nation Indian Council during mediation.\n**(D)**\nNo statements made or information exchanged during mediation shall be admissible in any future legal or dispute resolution proceedings without the written consent of the Claimants.\n**(E)**\nThe Claimants shall mutually agree to conduct mediation at a specified location. Each Claimant shall pay its own costs, plus an equal share of the costs of the mediator and the mediation facilities.\n**(F)**\nFollowing successful completion of any mediation under this section, the Claimants may submit a mutually agreed upon distribution plan to the Secretary.\n**(G)**\nUpon submission of a mutually agreed upon distribution plan to the Secretary, the Secretary shall distribute the funds in the Quapaw Bear Settlement Trust Account to the Claimants in accordance with their mutually agreed upon distribution plan.\n**(H)**\nIn the event the Claimants do not reach a mutually agreed upon distribution plan following mediation, then any Claimant, through written notification, may submit the matter to the Secretary who shall determine a final distribution plan allocating the funds in the Quapaw Bear Settlement Trust Account in accordance with the Report based on the procedures in paragraph (2).\n**(2) Secretarial Allocation**\n**(A)**\nFollowing an unsuccessful mediation pursuant to the procedures in paragraph (1), any Claimant may petition the Secretary to determine final allocations of settlement proceeds in accordance with subsection (d).\n**(B)**\nThe Secretary shall commence the Secretarial Allocation process in accordance with this paragraph (2) if the Claimants do not reach a mutually agreed upon allocation plan within 18 months following enactment of the Act.\n**(C)**\nUpon the receipt of such a petition by a Claimant, the Secretary or the Secretary\u2019s designee shall order an allocation of the settlement proceeds pursuant to the following steps:\n**(i)**\nWithin thirty (30) days following the Secretary\u2019s receipt of a petition to allocation settlement proceeds after failed mediation, the Secretary or the Secretary\u2019s designee shall issue a scheduling order to establish a schedule for a hearing and the issuance of a final decision by the Secretary of a final distribution plan.\n**(ii)**\nThe Secretary\u2019s decision determining a final distribution plan in accordance with subsection (d) shall be made following a hearing to be presided over by the Secretary or the Secretary\u2019s designee. The hearing shall occur no less than sixty (60) days following the issuance of the scheduling order.\n**(iii)**\nAt least fifteen (15) days prior to the hearing, each Claimant shall submit to the other Claimants and to the Secretary a copy of all exhibits on which such Claimant intends to rely at the hearing, a pre-hearing brief, and a proposed final decision by the Secretary. The proposed final decision shall include a proposed distribution plan to be submitted to the Secretary and shall be limited to proposed rulings and distributions for each Claimant.\n**(iv)**\nWithin fourteen (14) days after the close of the hearing, each Claimant may submit a post-hearing brief to the Secretary.\n**(v)**\nFollowing the hearing and post-hearing brief, the Secretary shall issue a final decision determining a final distribution plan in accordance with subsection (d) within sixty (60) calendar days. The Claimants may mutually agree upon a binding distribution plan at any time before the Secretary\u2019s decision is issued.\n**(vi)**\nWithin twenty (20) calendar days after transmittal of the Secretary\u2019s final decision to the Claimants, the Claimants may submit to the Secretary any information necessary for the implementation of the final distribution plan.\n**(vii)**\nWithin sixty (60) days of the Secretary\u2019s final decision determining a final distribution plan, the Secretary shall distribute the funds in the Quapaw Bear Settlement Trust Account to the Claimants pursuant to the terms of the final distribution plan.\n**(viii)**\nAny deadlines established in this section may be extended by unanimous mutual agreement of the Claimants.\n**(3) Federal Mediation & Conciliation Service**\nIn discharging any duties under this Act, the Secretary is authorized to utilize the Federal Mediation Conciliation Service to provide technical support and dispute resolution resources, provided, however, that the Secretary or the Secretary\u2019s designee is responsible for approving and implementing any mutually agreed-upon or binding distribution plan reached pursuant to this Act.",
      "versionDate": "2025-02-21",
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
        "actionDate": "2025-02-19",
        "text": "Read twice and referred to the Committee on Indian Affairs."
      },
      "number": "630",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Quapaw Tribal Settlement Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Alternative dispute resolution, mediation, arbitration",
            "updateDate": "2025-06-26T17:06:48Z"
          },
          {
            "name": "Federal-Indian relations",
            "updateDate": "2025-06-26T17:08:32Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2025-06-26T17:06:43Z"
          },
          {
            "name": "Indian claims",
            "updateDate": "2025-06-26T17:06:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-06-24T18:23:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-21",
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
          "measure-id": "id119hr1451",
          "measure-number": "1451",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-21",
          "originChamber": "HOUSE",
          "update-date": "2025-06-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1451v00",
            "update-date": "2025-06-27"
          },
          "action-date": "2025-02-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Quapaw Tribal Settlement Act of 2025</strong></p><p>This bill creates a trust account, funds the account,\u00a0and establishes a distribution process to settle certain claims between the federal government and the\u00a0Quapaw Nation (a tribe in Oklahoma).\u00a0</p><p>Specifically, the bill establishes\u00a0the\u00a0Quapaw Bear Settlement Trust Account and directs the Department of the Interior's Bureau of Trust Funds Administration to administer all funds appropriated to the trust account.\u00a0</p><p>Interior must make payments to the tribe and individual members of the tribe in accordance with the January 2020 recommendation of the review panel of the U.S. Court of Federal Claims.</p><p>The bill outlines the distribution process for the settlement funds in the trust account.</p>"
        },
        "title": "Quapaw Tribal Settlement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1451.xml",
    "summary": {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Quapaw Tribal Settlement Act of 2025</strong></p><p>This bill creates a trust account, funds the account,\u00a0and establishes a distribution process to settle certain claims between the federal government and the\u00a0Quapaw Nation (a tribe in Oklahoma).\u00a0</p><p>Specifically, the bill establishes\u00a0the\u00a0Quapaw Bear Settlement Trust Account and directs the Department of the Interior's Bureau of Trust Funds Administration to administer all funds appropriated to the trust account.\u00a0</p><p>Interior must make payments to the tribe and individual members of the tribe in accordance with the January 2020 recommendation of the review panel of the U.S. Court of Federal Claims.</p><p>The bill outlines the distribution process for the settlement funds in the trust account.</p>",
      "updateDate": "2025-06-27",
      "versionCode": "id119hr1451"
    },
    "title": "Quapaw Tribal Settlement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Quapaw Tribal Settlement Act of 2025</strong></p><p>This bill creates a trust account, funds the account,\u00a0and establishes a distribution process to settle certain claims between the federal government and the\u00a0Quapaw Nation (a tribe in Oklahoma).\u00a0</p><p>Specifically, the bill establishes\u00a0the\u00a0Quapaw Bear Settlement Trust Account and directs the Department of the Interior's Bureau of Trust Funds Administration to administer all funds appropriated to the trust account.\u00a0</p><p>Interior must make payments to the tribe and individual members of the tribe in accordance with the January 2020 recommendation of the review panel of the U.S. Court of Federal Claims.</p><p>The bill outlines the distribution process for the settlement funds in the trust account.</p>",
      "updateDate": "2025-06-27",
      "versionCode": "id119hr1451"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1451ih.xml"
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
      "title": "Quapaw Tribal Settlement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Quapaw Tribal Settlement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of the Treasury to make payments to the Quapaw Nation and certain members of the Quapaw Nation in accordance with the recommendation of the United States Court of Federal Claims, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:26Z"
    }
  ]
}
```
