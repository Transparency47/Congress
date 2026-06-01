# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5515?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5515
- Title: Indian Trust Asset Reform Amendment Act
- Congress: 119
- Bill type: HR
- Bill number: 5515
- Origin chamber: House
- Introduced date: 2025-09-19
- Update date: 2026-01-14T19:50:14Z
- Update date including text: 2026-01-14T19:50:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-19: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-11-12 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2025-11-19 - Committee: Subcommittee Hearings Held
- Latest action: 2025-09-19: Introduced in House

## Actions

- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-11-12 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2025-11-19 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-19",
    "latestAction": {
      "actionDate": "2025-09-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5515",
    "number": "5515",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "H001100",
        "district": "3",
        "firstName": "Jeff",
        "fullName": "Rep. Hurd, Jeff [R-CO-3]",
        "lastName": "Hurd",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Indian Trust Asset Reform Amendment Act",
    "type": "HR",
    "updateDate": "2026-01-14T19:50:14Z",
    "updateDateIncludingText": "2026-01-14T19:50:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
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
      "actionDate": "2025-11-12",
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
      "actionDate": "2025-09-19",
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
      "actionDate": "2025-09-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-19",
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
          "date": "2025-09-19T13:05:00Z",
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
                "date": "2025-11-19T15:15:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-11-12T21:41:40Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "WA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "WA"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "OR"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5515ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5515\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 19, 2025 Mr. Hurd of Colorado (for himself and Ms. Randall ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Indian Trust Asset Reform Act.\n#### 1. Short title\nThis Act may be cited as the Indian Trust Asset Reform Amendment Act .\n#### 2. Amendments to Indian Trust Asset Reform Act\n##### (a) Definitions\nSection 202 of the Indian Trust Asset Reform Act ( 25 U.S.C. 5611 ) is amended\u2014\n**(1)**\nby amending paragraph (1) to read as follows:\n(1) Indian tribe The term Indian tribe means an Indian or Alaska Native tribe, band, nation, pueblo, village, or community identified, including parenthetically, on the list published by the Secretary pursuant to Section 104 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5131 ). ; and\n**(2)**\nby adding at the end the following:\n(4) Tribal organization (A) In general The term tribal organization means any legally established organization of Indians which is controlled, sanctioned, or chartered by the governing body of an Indian Tribe or which is democratically elected by the adult members of the Indian community to be served by such organization and which includes the maximum participation of Indians in all phases of its activities. (B) Multiple tribes In any case where a contract is let or grant made to an organization to perform services benefiting more than one Indian tribe, the approval of each such Indian tribe shall be a prerequisite to the letting or making of such contract or grant. .\n##### (b) Indian Trust Asset Management Project\nSection 203 of the Indian Trust Asset Reform Act ( 25 U.S.C. 5612 ) is amended to read as follows:\n203. Indian Trust Asset Management Project (a) In general The Secretary shall carry out an Indian trust asset management project in accordance with this title. (b) Participation (1) In general To participate in the project, an Indian tribe shall submit to the Secretary a proposed Indian trust asset management plan as described in section 204 of this title, and a copy of a resolution or other appropriate action by the governing body of the Indian tribe in support of or authorizing the submission. (2) Tribal organizations A tribal organization may participate in the Project on behalf of an Indian tribe if the tribal organization\u2014 (A) submits a proposed Indian trust asset management plan that identifies the Indian tribe, the trust assets of which are included in the plan; (B) submits a copy of a resolution or other appropriate action by the governing body of the Indian tribe that is the owner of the trust assets included in the Indian trust asset management plan that supports or authorizes the tribal organization to carry out the plan; and (C) complies with the other provisions of this title. .\n##### (c) Indian trust asset management plan\nSection 204 of the Indian Trust Asset Reform Act ( 25 U.S.C. 5613 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking paragraph (1);\n**(B)**\nby redesignating paragraphs (2) and (3) as paragraphs (1) and (2) respectively; and\n**(C)**\nin paragraph (1), as so redesignated\u2014\n**(i)**\nin subparagraph (D)(i), by striking may include and inserting may include, but are not limited to, ; and\n**(ii)**\nin subparagraph (G), by striking plan and inserting plan, including regulations administered by the head of another Federal department or agency ;\n**(2)**\nin subsection (b)(1)(B)(i), by striking (a)(2) and inserting (a)(1) ;\n**(3)**\nby redesignating subsection (d) as subsection (e);\n**(4)**\nby inserting after subsection (c) the following:\n(d) Amendment of approved plan (1) In general An Indian tribe, or a tribal organization participating in an Indian trust asset management plan on behalf of an Indian tribe under section 203(b)(2) of this title, may propose amendments to the Indian trust asset management plan that the Secretary has approved or that is otherwise in effect pursuant to this title; and (2) Applicable provisions The Secretary shall review any proposal by an Indian tribe, or a tribal organization administering an Indian trust asset management plan pursuant to section 203(b)(2), using the criteria set forth in subsections (b) and (c) of this section. ; and\n**(5)**\nby adding at the end the following:\n(f) Eligibility for funding An Indian tribe operating under an approved Indian trust asset management plan shall continue to be eligible for, and shall not be disqualified from receiving, Federal funding to support the Indian tribe\u2019s activities under an approved Indian trust asset management plan, in the same manner and subject to the same considerations as Indian tribes without an Indian trust asset management plan. .\n##### (d) Trust asset management\nSection 205 of the Indian Trust Asset Reform Act ( 25 U.S.C. 5614 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby redesignating paragraphs (2) and (3) as paragraphs (3) and (4) respectively;\n**(B)**\nby inserting after paragraph (1) the following:\n(2) Forest management plan The term forest management plan has the meaning given the term in Section 304 of the National Indian Forest Resources Management Act of 1990 ( 25 U.S.C. 3103 ). ; and\n**(C)**\nby adding at the end the following:\n(5) Trust assets The term trust assets means\u2014 (A) trust lands, natural resources, trust funds, or other assets held by the Federal Government in trust for Indian tribes and individual Indians; or (B) any resource that is, or has previously been, included in an integrated resources management plan or other management plan approved by the Secretary. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby striking carry out and all that follows through would require and inserting carry out any transaction or activity related to management of that Indian tribe\u2019s trust assets, including, but not limited to, a surface leasing transaction, adoption or amendment of a forest management plan, or forest land management activity without approval of the Secretary, regardless of whether the trust asset management transaction or activity would require ;\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby striking with respect to forest and inserting with respect to forest management plans and forest ;\n**(ii)**\nin clause (ii)(II)(aa), by striking the public is and all that follows through the proposed and inserting interested parties are informed of, and have a reasonable opportunity to comment on a proposed forest management plan, and any significant environmental impacts of a proposed ; and\n**(iii)**\nin clause (ii)(II)(bb)\u2014\n**(I)**\nby striking public comments and inserting comments from interested parties ; and\n**(II)**\nby striking forest land and inserting forest management plan or forest land ;\n**(3)**\nby amending subsection (c) to read as follows:\n(c) Types of transactions At the discretion of the applicable Indian tribe, an Indian trust asset management plan may authorize the Indian tribe to manage any and all of that Indian tribe\u2019s trust assets, and undertake any transactions and activities related thereto, including but not limited to adopting or amending a forest management plan, carrying out a surface leasing transaction, and carrying out a forest land management activity, and the Secretary shall defer to any such discretionary trust asset management decision by the Indian tribe to the extent such decision is consistent with both the Indian trust asset management plan and this section. .\n**(4)**\nin subsection (f)\u2014\n**(A)**\nby striking executes a surface and all that follows through pursuant to tribal regulations and inserting undertakes an activity or transaction related to a trust asset, pursuant to the Indian tribe\u2019s trust asset management plan and tribal regulations ;\n**(B)**\nin paragraph (1), by striking the surface leasing transaction or forest land management activity documents and inserting activity or transaction documents ; and\n**(C)**\nin paragraph (2), by striking a surface leasing transaction, or forest land management activities and inserting or an activity or transaction related to a trust asset ; and\n**(5)**\nin subsection (g)(1)(A), by striking the execution of any forest land management activity and inserting any activity or transaction related to a trust asset and undertaken by the Indian tribe .\n##### (e) Trust responsibility\nSection 206(f) of the Indian Trust Asset Reform Act ( 25 U.S.C. 5615(f) ) is amended to read as follows:\n(f) Trust responsibility Nothing in this title enhances, diminishes, or otherwise affects the trust responsibility of the United States to Indian tribes. .",
      "versionDate": "2025-09-19",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Federal-Indian relations",
            "updateDate": "2026-01-14T19:50:00Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2026-01-14T19:50:14Z"
          },
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2026-01-14T19:50:05Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-01-14T19:50:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-12-04T21:37:08Z"
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
      "date": "2025-09-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5515ih.xml"
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
      "title": "Indian Trust Asset Reform Amendment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Indian Trust Asset Reform Amendment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Indian Trust Asset Reform Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T04:48:25Z"
    }
  ]
}
```
