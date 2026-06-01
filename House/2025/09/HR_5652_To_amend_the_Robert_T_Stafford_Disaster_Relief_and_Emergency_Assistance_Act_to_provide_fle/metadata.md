# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5652?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5652
- Title: Wildfire Recovery Act
- Congress: 119
- Bill type: HR
- Bill number: 5652
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2026-03-26T16:52:35Z
- Update date including text: 2026-03-26T16:52:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-01 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-01 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5652",
    "number": "5652",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Wildfire Recovery Act",
    "type": "HR",
    "updateDate": "2026-03-26T16:52:35Z",
    "updateDateIncludingText": "2026-03-26T16:52:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-01",
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
      "actionDate": "2025-09-30",
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
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-01T19:25:47Z",
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
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CO"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "OR"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "DC"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CO"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NM"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "WA"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "AZ"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NV"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "FL"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5652ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5652\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. Neguse (for himself, Mr. LaMalfa , Ms. DeGette , Mr. Huffman , Mr. Swalwell , Ms. Bonamici , Ms. Norton , Mr. Carbajal , Mr. Garamendi , Mr. Costa , Mr. Lynch , Ms. Pettersen , Ms. Leger Fernandez , and Mr. Harder of California ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to provide flexibility with the cost share for fire management assistance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wildfire Recovery Act .\n#### 2. Fire management assistance cost share\n##### (a) In general\nSection 420 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act is amended\u2014\n**(1)**\nby redesignating subsection (e) as subsection (f); and\n**(2)**\nby inserting after subsection (d) the following:\n(e) Federal share The Federal share of assistance under this section shall be not less than 75 percent of the eligible cost of such assistance. .\n##### (b) Applicability\nThe amendment made by subsection (a) shall only apply to amounts appropriated on or after the date of enactment of this Act.\n#### 3. Rulemaking\nNot later than 3 years after the date of enactment of this Act, the President, acting through the Administrator of the Federal Emergency Management Agency, shall conduct and complete a rulemaking to provide criteria for the circumstances under which the Administrator may recommend the President increase the Federal cost share for section 420 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5187 ). Such criteria shall include a threshold metric that assesses the financial impact to a State or local government from responding to a fire for which fire management assistance is being provided.\n#### 4. Policy update\nThe Administrator of the Federal Emergency Management Agency shall update the policy for grants made under section 420 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5187 ), consistent with assistance provided under a major disaster and emergency declaration under such Act, to provide that predeployment of domestic assets by States, local, and Tribal governments may be eligible for reimbursement under such section 420.",
      "versionDate": "2025-09-30",
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
        "actionDate": "2025-01-16",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "133",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Fire Suppression and Response Funding Assurance Act",
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
        "updateDate": "2025-12-05T21:47:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-30",
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
          "measure-id": "id119hr5652",
          "measure-number": "5652",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-30",
          "originChamber": "HOUSE",
          "update-date": "2026-03-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5652v00",
            "update-date": "2026-03-26"
          },
          "action-date": "2025-09-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Wildfire Recovery Act</strong></p><p>This bill provides flexibility to increase the federal cost share for the Fire Management Assistance Grant (FMAG) program of the Federal Emergency Management Agency (FEMA). It also requires updates to FMAG policy to remove limitations on reimbursement for predeployment of firefighting assets.</p><p>Under current law, FEMA\u2019s regulations require a 75% federal cost share for FMAG assistance and do not permit adjustments. The bill establishes FMAG\u2019s 75% federal cost share as a minimum, providing flexibility for such percentage to be increased in certain instances. It also requires FEMA to establish by regulation criteria through which FEMA may recommend the President increase FMAG\u2019s federal cost share above 75%. Such criteria must include a financial threshold, relating to the costs of state or local government response to a fire triggering FMAG assistance, above which FEMA may recommend the President increase the federal cost share.\u00a0</p><p>Also, currently, FMAG may reimburse costs for pre-positioning firefighting resources into areas of higher fire danger up to 21 days before a declared fire. However, under current FMAG policy, costs for pre-positioning state or local government-owned resources within their own state are ineligible. The bill requires FEMA to update FMAG grants policy to allow reimbursement for predeployment of domestic assets by state, local, or Indian tribal governments in a manner consistent with other FEMA programs.</p>"
        },
        "title": "Wildfire Recovery Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5652.xml",
    "summary": {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Wildfire Recovery Act</strong></p><p>This bill provides flexibility to increase the federal cost share for the Fire Management Assistance Grant (FMAG) program of the Federal Emergency Management Agency (FEMA). It also requires updates to FMAG policy to remove limitations on reimbursement for predeployment of firefighting assets.</p><p>Under current law, FEMA\u2019s regulations require a 75% federal cost share for FMAG assistance and do not permit adjustments. The bill establishes FMAG\u2019s 75% federal cost share as a minimum, providing flexibility for such percentage to be increased in certain instances. It also requires FEMA to establish by regulation criteria through which FEMA may recommend the President increase FMAG\u2019s federal cost share above 75%. Such criteria must include a financial threshold, relating to the costs of state or local government response to a fire triggering FMAG assistance, above which FEMA may recommend the President increase the federal cost share.\u00a0</p><p>Also, currently, FMAG may reimburse costs for pre-positioning firefighting resources into areas of higher fire danger up to 21 days before a declared fire. However, under current FMAG policy, costs for pre-positioning state or local government-owned resources within their own state are ineligible. The bill requires FEMA to update FMAG grants policy to allow reimbursement for predeployment of domestic assets by state, local, or Indian tribal governments in a manner consistent with other FEMA programs.</p>",
      "updateDate": "2026-03-26",
      "versionCode": "id119hr5652"
    },
    "title": "Wildfire Recovery Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Wildfire Recovery Act</strong></p><p>This bill provides flexibility to increase the federal cost share for the Fire Management Assistance Grant (FMAG) program of the Federal Emergency Management Agency (FEMA). It also requires updates to FMAG policy to remove limitations on reimbursement for predeployment of firefighting assets.</p><p>Under current law, FEMA\u2019s regulations require a 75% federal cost share for FMAG assistance and do not permit adjustments. The bill establishes FMAG\u2019s 75% federal cost share as a minimum, providing flexibility for such percentage to be increased in certain instances. It also requires FEMA to establish by regulation criteria through which FEMA may recommend the President increase FMAG\u2019s federal cost share above 75%. Such criteria must include a financial threshold, relating to the costs of state or local government response to a fire triggering FMAG assistance, above which FEMA may recommend the President increase the federal cost share.\u00a0</p><p>Also, currently, FMAG may reimburse costs for pre-positioning firefighting resources into areas of higher fire danger up to 21 days before a declared fire. However, under current FMAG policy, costs for pre-positioning state or local government-owned resources within their own state are ineligible. The bill requires FEMA to update FMAG grants policy to allow reimbursement for predeployment of domestic assets by state, local, or Indian tribal governments in a manner consistent with other FEMA programs.</p>",
      "updateDate": "2026-03-26",
      "versionCode": "id119hr5652"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5652ih.xml"
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
      "title": "Wildfire Recovery Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-16T02:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wildfire Recovery Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T02:53:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to provide flexibility with the cost share for fire management assistance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T02:48:17Z"
    }
  ]
}
```
