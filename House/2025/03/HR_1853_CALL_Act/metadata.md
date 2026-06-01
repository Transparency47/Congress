# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1853?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1853
- Title: CALL Act
- Congress: 119
- Bill type: HR
- Bill number: 1853
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2025-06-09T15:02:12Z
- Update date including text: 2025-06-09T15:02:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1853",
    "number": "1853",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "CALL Act",
    "type": "HR",
    "updateDate": "2025-06-09T15:02:12Z",
    "updateDateIncludingText": "2025-06-09T15:02:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-28",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:06:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-28T20:49:24Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "OR"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1853ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1853\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Ms. Brownley (for herself, Ms. Salinas , and Ms. Stansbury ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo require a study of the barriers to conservation practice adoption on leased agricultural land, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Conservation for Agricultural Leased Land Act or the CALL Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAccording to a 2016 study by the Economic Research Service of the Department of Agriculture, 39 percent of agricultural land in the United States is leased, including the majority (53 percent) of cropland.\n**(2)**\nThe participation of landowners and tenants in Federal, State, and local conservation programs, and the adoption of conservation practices on land that they own or manage, can be limited by a wide range of factors that are not fully understood.\n**(3)**\nMuch of the limited information that is known comes from the Tenure, Ownership, and Transition of Agricultural Land (TOTAL) Survey conducted by the National Agricultural Statistics Service, in collaboration with the Economic Research Service; regularly recurring data collection through the TOTAL Survey and other Department of Agriculture reports is vital to understanding land tenure trends, challenges, and opportunities.\n**(4)**\nSome of the potential barriers to such participation and adoption include the structure or term of the lease or rental agreement, the level of independence given to the operator, the awareness of the landowner of both conservation practice and program opportunities and the costs and benefits associated with those opportunities, and other policy or market factors.\n**(5)**\nThe solutions to these issues are unlikely to be one size fits all and must be better understood.\n#### 3. Study\n##### (a) In general\nThe Secretary shall carry out a study of the participation in conservation programs of, and the adoption of conservation practices on, leased agricultural land.\n##### (b) Collaboration\nThe study under this section shall be carried out in collaboration with the Economic Research Service.\n##### (c) Contents\nThe study carried out under this section shall include\u2014\n**(1)**\na review of relevant existing research literature, including\u2014\n**(A)**\nthe Tenure, Ownership, and Transition of Agricultural Land (TOTAL) Survey conducted by the National Agricultural Statistics Service, in collaboration with the Economic Research Service; and\n**(B)**\nthe report titled Understanding and Activating Non-Operating Landlords , published by the American Farmland Trust in September, 2020;\n**(2)**\na review of initiatives conducted by the Cooperative Extension System to increase the adoption of conservation practices on leased agricultural land;\n**(3)**\nidentification and quantification of the various types and structures of current agricultural land leasing relationships;\n**(4)**\nresearch on the history, and estimation of future trends, of agricultural land ownership;\n**(5)**\nexamination of what leasing models have been effective in encouraging the adoption of conservation practices;\n**(6)**\nconsideration of regional variations;\n**(7)**\nexamination of existing Federal incentives for adopting conservation practices, and the degree to which such incentives are currently utilized with respect to leased agricultural lands;\n**(8)**\nresearch on State and local incentive programs that are encouraging conservation practice adoption on leased agricultural land;\n**(9)**\nresearch on the benefits of transitioning from land leasing to land ownership on conservation practice adoption and Federal conservation program participation;\n**(10)**\nexamination of the effects of competition in cash rents on the adoption of conservation practices on leased agricultural lands;\n**(11)**\nexamination of what happens to conservation practices currently underway on leased agricultural land when new tenants take over such land; and\n**(12)**\nresearch on how the Department of Agriculture communicates regarding conservation practice adoption to farmers and ranchers who do not own the land they operate and to landowners who lease out their agricultural land.\n##### (d) Consideration\nThe study under this section shall be carried out with particular consideration of farmers and ranchers who are people of color, including Black and indigenous farmers and ranchers, and beginning farmers and ranchers.\n##### (e) Report\nNot later than December 31, 2026, the Secretary shall submit to Congress a report containing\u2014\n**(1)**\nthe results of the study conducted under this section; and\n**(2)**\nrecommendations, based on such study, for addressing the barriers unique to various agricultural land leasing relationships to adopting conservation practices on leased agricultural land, including\u2014\n**(A)**\nrecommendations that can be implemented under existing statutory authorities;\n**(B)**\nrecommendations that would require congressional authorization in order to be implemented; and\n**(C)**\nrecommendations for outreach.\n##### (f) Implementation\nThe Secretary may enter into an agreement with a non-Federal entity (such as a nonprofit entity or university), selected through an application process, to carry out this section.\n##### (g) Definitions\nIn this section:\n**(1) Leased agricultural land**\nThe term leased agricultural land means agricultural land that is operated, under a lease or other rental agreement, by a farmer or rancher who does not own the land.\n**(2) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the National Agricultural Statistics Service.",
      "versionDate": "2025-03-05",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-14T12:28:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
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
          "measure-id": "id119hr1853",
          "measure-number": "1853",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-05",
          "originChamber": "HOUSE",
          "update-date": "2025-06-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1853v00",
            "update-date": "2025-06-09"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Conservation for Agricultural Leased Land Act or the</strong> <strong>CALL Act</strong></p><p>This bill directs the National Agricultural Statistics Service (NASS) of the Department of Agriculture to carry out a study and make recommendations regarding conservation practices on leased agricultural land.</p><p>The study must (1) address issues such as participation in conservation programs and barriers to adopting conservation practices; and (2) be carried out with particular consideration of farmers and ranchers who are people of color, including Black and indigenous farmers and ranchers, and beginning farmers and ranchers.</p><p>NASS may enter into an agreement with a nonfederal entity (e.g., a nonprofit entity or university) to carry out the study.</p>"
        },
        "title": "CALL Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1853.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Conservation for Agricultural Leased Land Act or the</strong> <strong>CALL Act</strong></p><p>This bill directs the National Agricultural Statistics Service (NASS) of the Department of Agriculture to carry out a study and make recommendations regarding conservation practices on leased agricultural land.</p><p>The study must (1) address issues such as participation in conservation programs and barriers to adopting conservation practices; and (2) be carried out with particular consideration of farmers and ranchers who are people of color, including Black and indigenous farmers and ranchers, and beginning farmers and ranchers.</p><p>NASS may enter into an agreement with a nonfederal entity (e.g., a nonprofit entity or university) to carry out the study.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119hr1853"
    },
    "title": "CALL Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Conservation for Agricultural Leased Land Act or the</strong> <strong>CALL Act</strong></p><p>This bill directs the National Agricultural Statistics Service (NASS) of the Department of Agriculture to carry out a study and make recommendations regarding conservation practices on leased agricultural land.</p><p>The study must (1) address issues such as participation in conservation programs and barriers to adopting conservation practices; and (2) be carried out with particular consideration of farmers and ranchers who are people of color, including Black and indigenous farmers and ranchers, and beginning farmers and ranchers.</p><p>NASS may enter into an agreement with a nonfederal entity (e.g., a nonprofit entity or university) to carry out the study.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119hr1853"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1853ih.xml"
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
      "title": "CALL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CALL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Conservation for Agricultural Leased Land Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a study of the barriers to conservation practice adoption on leased agricultural land, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:34:02Z"
    }
  ]
}
```
