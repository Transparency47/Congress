# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7691?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7691
- Title: Fight Book Bans Act
- Congress: 119
- Bill type: HR
- Bill number: 7691
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-03-16T16:38:07Z
- Update date including text: 2026-03-16T16:38:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7691",
    "number": "7691",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "F000476",
        "district": "10",
        "firstName": "Maxwell",
        "fullName": "Rep. Frost, Maxwell [D-FL-10]",
        "lastName": "Frost",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Fight Book Bans Act",
    "type": "HR",
    "updateDate": "2026-03-16T16:38:07Z",
    "updateDateIncludingText": "2026-03-16T16:38:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T14:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "MD"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7691ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7691\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Mr. Frost (for himself, Mr. Raskin , and Ms. Wilson of Florida ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo authorize the Secretary of Education to provide grants to local educational agencies to cover the costs of challenges to determinations not to discontinue the use of specific instructional materials, or the availability of specific school library materials, in public elementary and secondary schools, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fight Book Bans Act .\n#### 2. Grants to reimburse certain costs of challenges to continued use of instructional and library materials\n##### (a) Definitions\nFor purposes of this section:\n**(1) Applicable program**\nThe term applicable program means any program for which the Secretary of Education has administrative responsibility as provided by law or by delegation of authority pursuant to law.\n**(2) Covered local educational agency**\nThe term covered local educational agency means a local educational agency that has the duty and responsibility under law\u2014\n**(A)**\nto select and provide instructional materials and school library materials for students attending public elementary schools or public secondary schools under the jurisdiction of the agency;\n**(B)**\nto provide, or participate in, a process\u2014\n**(i)**\nto provide for resolution of an objection by a parent or other person to\u2014\n**(I)**\nthe use of a specific instructional material; or\n**(II)**\nthe availability of a specific school library material; and\n**(ii)**\nto discontinue the use of the instructional material, or the availability of the school library material, for any grade level or age group if the local educational agency determines that the material is inappropriate or unsuitable; and\n**(C)**\nto provide, or participate in, a process (including any administrative proceeding or court case) under which a parent or other person who disagrees with a determination made by the covered local educational agency pursuant to subparagraph (B)(ii) to discontinue or not to discontinue the use of an instructional material, or the availability of a school library material, may appeal, or otherwise request reconsideration of, the determination.\n**(3) ESEA terms**\nThe terms elementary school , parent , secondary school , and Secretary have the meaning given those terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(4) Instructional material**\nThe term instructional material means instructional content that is provided to a student, regardless of its format, including printed or representational materials, audio-visual materials, and materials in electronic or digital formats (such as materials accessible through the internet). The term does not include academic tests or academic assessments.\n**(5) Local educational agency**\nThe term local educational agency means a public elementary school, public secondary school, school district, or local board of education that is the recipient of funds under an applicable program.\n**(6) School library material**\nThe term school library material means any material available to a student via the student\u2019s school library, regardless of its format, including printed or representational materials, audio-visual materials, and materials in electronic or digital formats (such as materials accessible through the internet).\n**(7) Student**\nThe term student means any public elementary school or public secondary school student.\n##### (b) Grants\n**(1) In general**\nThe Secretary of Education is authorized to make grants to covered local educational agencies to reimburse such agencies for the costs (including costs such as attorneys\u2019 fees and court costs) incurred in connection with a process described in subsection (a)(2)(C), if\u2014\n**(A)**\nsuch costs are not reimbursed by the State or any other person; and\n**(B)**\nsuch process was initiated due to a determination by the covered local educational agency not to discontinue the use of an instructional material or the availability of a school library material.\n**(2) Application**\nA covered local educational agency desiring to receive an award under paragraph (1) shall submit an application to the Secretary at such time and in such manner as the Secretary shall require.\n**(3) Maximum amount**\nThe maximum amount that a covered local educational agency is eligible to receive under this subsection is $100,000 for each determination described in paragraph (1)(B).\n**(4) Award process**\nIn awarding grants under this subsection, the Secretary shall ensure that the award process is based on content-neutral and viewpoint-neutral criteria and does not take into account the content of the instructional material or school library material concerned.\n##### (c) Authorization of appropriations\nTo carry out this section, there are authorized to be appropriated a total of $15,000,000 for fiscal years 2027 through 2031.",
      "versionDate": "2026-02-25",
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
        "name": "Education",
        "updateDate": "2026-03-16T16:38:06Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7691ih.xml"
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
      "title": "Fight Book Bans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-13T11:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fight Book Bans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-13T11:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Education to provide grants to local educational agencies to cover the costs of challenges to determinations not to discontinue the use of specific instructional materials, or the availability of specific school library materials, in public elementary and secondary schools, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-13T11:48:17Z"
    }
  ]
}
```
