# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3759?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3759
- Title: Streamlined FEMA Cost Exemption Act
- Congress: 119
- Bill type: HR
- Bill number: 3759
- Origin chamber: House
- Introduced date: 2025-06-05
- Update date: 2026-02-09T16:30:58Z
- Update date including text: 2026-02-09T16:30:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-05: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-06 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-06-05: Introduced in House

## Actions

- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-06 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3759",
    "number": "3759",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "D000628",
        "district": "2",
        "firstName": "Neal",
        "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
        "lastName": "Dunn",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Streamlined FEMA Cost Exemption Act",
    "type": "HR",
    "updateDate": "2026-02-09T16:30:58Z",
    "updateDateIncludingText": "2026-02-09T16:30:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-06",
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
      "actionDate": "2025-06-05",
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
      "actionDate": "2025-06-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T14:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-06T20:27:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3759ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3759\nIN THE HOUSE OF REPRESENTATIVES\nJune 5, 2025 Mr. Dunn of Florida introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo provide for streamlined cost exemptions for public assistance projects by the Federal Emergency Management Agency, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Streamlined FEMA Cost Exemption Act .\n#### 2. Recoupment of certain assistance prohibited\nSection 705(a)(1) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5205(a)(1) ) is amended by striking 3 years and inserting 2 years .\n#### 3. Restoration of waiver authority\n##### (a) Authority\nSection 312(b) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5155(b) ) is amended by adding at the end the following:\n(4) Waiver of general prohibition (A) In general The President may waive the general prohibition provided in subsection (a) upon request of a Governor on behalf of the State or on behalf of a person, business concern, or any other entity suffering losses as a result of a major disaster or emergency, if the President finds such waiver is in the public interest and will not result in waste, fraud, or abuse. In making this decision, the President may consider the following: (i) The recommendations of the Administrator of the Federal Emergency Management Agency made in consultation with the Federal agency or agencies administering the duplicative program. (ii) If a waiver is granted, the assistance to be funded is cost effective. (iii) Equity and good conscience. (iv) Other matters of public policy considered appropriate by the President. (B) Grant or denial of waiver A request under subparagraph (A) shall be granted or denied not later than 45 days after submission of such request. (C) Prohibition on determination that loan is a duplication Notwithstanding subsection (c), in carrying out subparagraph (A), the President may not determine that a loan is a duplication of assistance, provided that all Federal assistance is used toward a loss suffered as a result of the major disaster or emergency. .\n##### (b) Limitation\nThis subsection, including the amendment made by subsection (a), shall not be construed to apply to section 406 or 408 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5172 , 5174).\n##### (c) Applicability\nThe amendment made by subsection (a) shall apply to any major disaster or emergency declared by the President under section 401 or 501, respectively, of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 , 5191) on or after the date of enactment of this Act.\n#### 4. Waiver of certain recoupment of funds\nTitle VII of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ) is amended by adding at the end the following:\n707. Waiver of certain recoupment of funds (a) In general Notwithstanding subchapter IV of chapter 33 of title 31, United States Code, the Administrator may waive recoupment of funds provided for a covered project that\u2014 (1) are otherwise eligible to be recouped by a provision of this Act; and (2) that exceed the total cost of a covered project by not greater than 5 percent. (b) Covered project In this section, the term covered project means a project for which financial assistance was provided under section 403, 406, 407, 428, or 502. .\n#### 5. Acceptable error ratio\nTitle VII of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ) is further amended by adding at the end the following:\n708. Acceptable error ratio (a) Establishment Notwithstanding subchapter IV of chapter 33 of title 31, United States Code, the Administrator of the Federal Emergency Management Agency shall develop and establish an acceptable error ratio for allocations during eligibility negotiations relating to financial assistance provided under this Act. (b) Use of funds The Administrator shall ensure that any amount provided under this Act that the Administrator considers to be within the error ratio established under subsection (a) is used for an eligible purpose for which the assistance is provided. .",
      "versionDate": "2025-06-05",
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
        "updateDate": "2025-07-15T14:52:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-05",
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
          "measure-id": "id119hr3759",
          "measure-number": "3759",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-05",
          "originChamber": "HOUSE",
          "update-date": "2026-02-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3759v00",
            "update-date": "2026-02-09"
          },
          "action-date": "2025-06-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Streamlined FEMA Cost Exemption Act</strong></p><p>This bill reduces to two years the statute of limitations for the Federal Emergency Management Agency (FEMA) to recoup disaster funding. It also requires FEMA to establish a ratio of acceptable error in its grants payments and authorizes the waiver of certain recoupment and duplication of benefits requirements.</p><p>The bill reduces from three years to two the time period (starting from the final report of project completion) during which\u00a0FEMA may take action to recover emergency or disaster assistance FEMA has provided to a state, Indian tribal, or local government.\u00a0</p><p>Also, under current law, FEMA generally must reduce and recover improper payments (i.e., payments that should not have been made or were made in an incorrect amount)\u00a0and maintain an error rate below 10%. The bill requires\u00a0FEMA to establish its own acceptable error ratio for providing emergency or disaster assistance funds for eligible purposes. It also authorizes\u00a0FEMA to waive recoupment of certain emergency or disaster assistance (e.g., Public Assistance funding) when the provided funds exceed the total cost of the relevant project by no more than 5%.</p><p>Additionally, the bill reauthorizes the President to waive the prohibition on the duplication of benefits upon request from the governor of a state if the President determines certain criteria are met. In exercising such authority, the President may not determine that a loan is a duplication. This authority is not applicable to FEMA\u2019s Individual Assistance program or Public Assistance for repair and replacement.</p>"
        },
        "title": "Streamlined FEMA Cost Exemption Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3759.xml",
    "summary": {
      "actionDate": "2025-06-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Streamlined FEMA Cost Exemption Act</strong></p><p>This bill reduces to two years the statute of limitations for the Federal Emergency Management Agency (FEMA) to recoup disaster funding. It also requires FEMA to establish a ratio of acceptable error in its grants payments and authorizes the waiver of certain recoupment and duplication of benefits requirements.</p><p>The bill reduces from three years to two the time period (starting from the final report of project completion) during which\u00a0FEMA may take action to recover emergency or disaster assistance FEMA has provided to a state, Indian tribal, or local government.\u00a0</p><p>Also, under current law, FEMA generally must reduce and recover improper payments (i.e., payments that should not have been made or were made in an incorrect amount)\u00a0and maintain an error rate below 10%. The bill requires\u00a0FEMA to establish its own acceptable error ratio for providing emergency or disaster assistance funds for eligible purposes. It also authorizes\u00a0FEMA to waive recoupment of certain emergency or disaster assistance (e.g., Public Assistance funding) when the provided funds exceed the total cost of the relevant project by no more than 5%.</p><p>Additionally, the bill reauthorizes the President to waive the prohibition on the duplication of benefits upon request from the governor of a state if the President determines certain criteria are met. In exercising such authority, the President may not determine that a loan is a duplication. This authority is not applicable to FEMA\u2019s Individual Assistance program or Public Assistance for repair and replacement.</p>",
      "updateDate": "2026-02-09",
      "versionCode": "id119hr3759"
    },
    "title": "Streamlined FEMA Cost Exemption Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Streamlined FEMA Cost Exemption Act</strong></p><p>This bill reduces to two years the statute of limitations for the Federal Emergency Management Agency (FEMA) to recoup disaster funding. It also requires FEMA to establish a ratio of acceptable error in its grants payments and authorizes the waiver of certain recoupment and duplication of benefits requirements.</p><p>The bill reduces from three years to two the time period (starting from the final report of project completion) during which\u00a0FEMA may take action to recover emergency or disaster assistance FEMA has provided to a state, Indian tribal, or local government.\u00a0</p><p>Also, under current law, FEMA generally must reduce and recover improper payments (i.e., payments that should not have been made or were made in an incorrect amount)\u00a0and maintain an error rate below 10%. The bill requires\u00a0FEMA to establish its own acceptable error ratio for providing emergency or disaster assistance funds for eligible purposes. It also authorizes\u00a0FEMA to waive recoupment of certain emergency or disaster assistance (e.g., Public Assistance funding) when the provided funds exceed the total cost of the relevant project by no more than 5%.</p><p>Additionally, the bill reauthorizes the President to waive the prohibition on the duplication of benefits upon request from the governor of a state if the President determines certain criteria are met. In exercising such authority, the President may not determine that a loan is a duplication. This authority is not applicable to FEMA\u2019s Individual Assistance program or Public Assistance for repair and replacement.</p>",
      "updateDate": "2026-02-09",
      "versionCode": "id119hr3759"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3759ih.xml"
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
      "title": "Streamlined FEMA Cost Exemption Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-17T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Streamlined FEMA Cost Exemption Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for streamlined cost exemptions for public assistance projects by the Federal Emergency Management Agency, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-17T04:18:21Z"
    }
  ]
}
```
