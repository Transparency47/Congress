# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2341?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2341
- Title: Duplications of Benefits Victims Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 2341
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2025-06-12T08:07:04Z
- Update date including text: 2025-06-12T08:07:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2341",
    "number": "2341",
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
    "title": "Duplications of Benefits Victims Relief Act",
    "type": "HR",
    "updateDate": "2025-06-12T08:07:04Z",
    "updateDateIncludingText": "2025-06-12T08:07:04Z"
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
          "date": "2025-03-25T14:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-25T20:45:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2341ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2341\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Mr. Rouzer (for himself and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to waive certain prohibitions on duplication of benefits, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Duplications of Benefits Victims Relief Act .\n#### 2. Duplication of benefits\n##### (a) In general\n**(1) Authority**\nSection 312(b) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5155(b) ) is amended by adding at the end the following:\n(4) Waiver of general prohibition (A) In general The President may waive the general prohibition provided in subsection (a) upon request of a Governor on behalf of the State or on behalf of a person, business concern, or any other entity suffering losses as a result of a major disaster or emergency, if the President finds such waiver is in the public interest and will not result in waste, fraud, or abuse. In making this decision, the President may consider the following: (i) The recommendations of the Administrator of the Federal Emergency Management Agency made in consultation with the Federal agency or agencies administering the duplicative program. (ii) If a waiver is granted, the assistance to be funded is cost effective. (iii) Equity and good conscience. (iv) Other matters of public policy considered appropriate by the President. (B) Grant or denial of waiver A request under subparagraph (A) shall be granted or denied not later than 45 days after submission of such request. (C) Prohibition on determination that loan is a duplication Notwithstanding subsection (c), in carrying out subparagraph (A), the President may not determine that a loan is a duplication of assistance, provided that all Federal assistance is used toward a loss suffered as a result of the major disaster or emergency. (D) Prohibition on income threshold In carrying out this paragraph, no income threshold may be applied to limit the eligibility of a recipient from qualifying for a waiver under this paragraph. (E) Applicability This paragraph shall apply to any major disaster or emergency declared by the President under section 401 or 501, respectively, on or after January 1, 2016. .\n**(2) Statutory construction**\nThis subsection, including the amendment made by paragraph (1), shall not be construed to apply to section 406 or 408 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5172 , 5174).\n**(3) Report**\n**(A) In general**\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Federal Emergency Management Agency, in coordination with other relevant Federal agencies, shall submit to the congressional committees of jurisdiction a report conducted by all relevant Federal agencies to improve the comprehensive delivery of disaster assistance to individuals following a major disaster or emergency declaration under the Robert T. Stafford Disaster Relief and Emergency Assistance Act.\n**(B) Contents**\nThe report required under subparagraph (A) shall include both administrative actions taken, or planned to be taken, by the agencies as well as legislative proposals, where appropriate, of the following:\n**(i)**\nEfforts to improve coordination between the Agency and other relevant Federal agencies when delivering disaster assistance to individuals.\n**(ii)**\nClarify the sequence of delivery of disaster assistance to individuals from the Agency, and other relevant Federal agencies.\n**(iii)**\nClarify the interpretation and implementation of section 312 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5155 ) when providing disaster assistance to individuals, including providing a common interpretation across the Agency, and other relevant Federal agencies, of the definitions and requirements under such section 312.\n**(iv)**\nIncrease the effectiveness of communication to applicants for assistance programs for individuals after a disaster declaration, including the breadth of programs available and the potential impacts of utilizing one program versus another.\n**(C) Report update**\nNot later than 4 years after the date of enactment of this subsection, the Administrator, in coordination with other relevant Federal agencies, shall submit to the congressional committees of jurisdiction an update to the report required under subparagraph (A).",
      "versionDate": "2025-03-25",
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
        "updateDate": "2025-05-13T21:16:31Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2341ih.xml"
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
      "title": "Duplications of Benefits Victims Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Duplications of Benefits Victims Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to waive certain prohibitions on duplication of benefits, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:19Z"
    }
  ]
}
```
