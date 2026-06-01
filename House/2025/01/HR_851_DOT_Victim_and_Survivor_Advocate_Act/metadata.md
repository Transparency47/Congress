# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/851?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/851
- Title: DOT Victim and Survivor Advocate Act
- Congress: 119
- Bill type: HR
- Bill number: 851
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-12-05T22:08:36Z
- Update date including text: 2025-12-05T22:08:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-01 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-01 - Committee: Referred to the Subcommittee on Highways and Transit.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/851",
    "number": "851",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "DOT Victim and Survivor Advocate Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:08:36Z",
    "updateDateIncludingText": "2025-12-05T22:08:36Z"
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
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
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
          "date": "2025-01-31T15:06:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-01T15:44:13Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr851ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 851\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Cohen introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo establish the position of National Roadway Safety Advocate within the Department of Transportation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the DOT Victim and Survivor Advocate Act .\n#### 2. Position of National Roadway Safety Advocate\n##### (a) Definitions\nIn this section:\n**(1) Department**\nThe term Department means the Department of Transportation.\n**(2) Secretary**\nThe term Secretary means the Secretary of Transportation.\n**(3) Stakeholder**\n**(A) In general**\nThe term stakeholder means\u2014\n**(i)**\na victim or survivor of a road crash; and\n**(ii)**\na family member of a victim or survivor of a road crash.\n**(B) Family member**\nFor purposes of subparagraph (A)(ii), the term family member shall not be limited to a parent, parent-in-law, grandparent, grandparent-in-law, sibling, spouse, child, or step-child of a victim or survivor of a road crash.\n##### (b) Establishment\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish within the Office of the Under Secretary of Transportation for Policy of the Department a position, to be known as the National Roadway Safety Advocate .\n**(2) Career position**\nThe position of National Roadway Safety Advocate shall be filled by a career appointment.\n##### (c) Purposes of the position\nThe purposes of the position of the National Roadway Safety Advocate are\u2014\n**(1)**\nto document and communicate recommendations from stakeholders to the Secretary on needs, objectives, plans, approaches, content, and accomplishments of the programs and activities carried out by the Department relating to roadway safety; and\n**(2)**\nto serve as a resource and point of contact for stakeholders on relevant roadway safety issues.\n##### (d) Authority and limitations\n**(1) Authority**\nThe National Roadway Safety Advocate may\u2014\n**(A)**\nprovide\u2014\n**(i)**\neducation on Department activities to stakeholders; and\n**(ii)**\nmeans for stakeholders to provide the perspective of the stakeholders on roadway safety issues to the Department;\n**(B)**\nexplain Department processes, procedures, scientific principles, and technical information to victims of roadway safety incidents and advocates in plain language;\n**(C)**\ncommunicate the perspective of stakeholders within Department processes;\n**(D)**\nprovide aggregated feedback on the regulatory agenda and activities of the Department from stakeholders to the Secretary;\n**(E)**\nbuild relationships with individual stakeholders, through establishing consistent outreach and dialogue for feedback, to enhance the engagement in the mission of the Department;\n**(F)**\npublish educational materials for enhancing stakeholder understanding of activities and procedures of the Department in accessible formats and venues, with clear and easy to understand wording, consistent with Department policy, in multiple languages;\n**(G)**\nconsult with and make recommendations to the Secretary relating to the appointment of stakeholders who may be appropriate for roles in advisory roadway safety committees, in accordance with chapter 10 of title 5, United States Code;\n**(H)**\nmeet not less frequently than once per quarter with the Secretary to highlight issues, make recommendations for resolving problems and alleviating stakeholder roadway safety concerns, and summarize input from stakeholders on proposed roadway safety initiatives;\n**(I)**\nrefer questions to the Office of the General Counsel or the Office of the Under Secretary of Transportation for Policy, as appropriate;\n**(J)**\nwork collaboratively with other offices in the Department that are working to educate and communicate with stakeholders on roadway safety issues; and\n**(K)**\nperform such other duties as may be determined by the Secretary.\n**(2) Limitations**\nThe National Roadway Safety Advocate may not\u2014\n**(A)**\nprovide legal notice, counsel, or determinations of any kind;\n**(B)**\nset or delay any agency deadlines;\n**(C)**\nmake Department decisions;\n**(D)**\ncreate or authorize Department policies, priorities, or activities;\n**(E)**\nmodify or interfere with any laws, regulations, related policies, practices, or procedures followed or enforced by the Department;\n**(F)**\nprevent other Department staff from working directly with stakeholders;\n**(G)**\ndisclose or discuss any enforcement matters that are under investigation, in litigation, or the subject of a civil penalty investigation or any other pre-litigation or litigation proceeding; or\n**(H)**\ndisclose or discuss any human resource matters with individuals outside of the Department.\n##### (e) Report to Office of the Under Secretary of Transportation for Policy\nThe National Roadway Safety Advocate shall report within the Office of the Under Secretary of Transportation for Policy of the Department.\n##### (f) Support\nThe Office of the Under Secretary of Transportation for Policy of the Department shall provide necessary funding, logistics, and administrative support to the National Roadway Safety Advocate as necessary.\n##### (g) Access to documents\nThe Department shall ensure that the National Roadway Safety Advocate has full and timely access to the documents of the Department, as necessary, to carry out the functions of the National Roadway Safety Advocate.\n##### (h) Reports required\n**(1) Annual report**\nNot later than November 15 of each year, the National Roadway Safety Advocate shall submit to the Secretary an annual report\u2014\n**(A)**\nhighlighting systemic issues relating to roadway safety based on information provided by stakeholders; and\n**(B)**\nmaking recommendations on how to remedy the issues highlighted under subparagraph (A).\n**(2) Additional reports**\nIn addition to the annual report required under paragraph (1), the National Roadway Safety Advocate may submit to the Secretary such additional reports, as determined necessary by the National Roadway Safety Advocate, in accordance with the requirements of that paragraph.",
      "versionDate": "2025-01-31",
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
        "actionDate": "2025-02-05",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "415",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "DOT Victim and Survivor Advocate Act",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-03-03T20:03:34Z"
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
          "measure-id": "id119hr851",
          "measure-number": "851",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr851v00",
            "update-date": "2025-03-27"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>DOT Victim and Survivor Advocate Act</strong></p><p>This bill directs the Department of Transportation (DOT) to establish the position of National Roadway Safety Advocate to work directly with victims and survivors of road crashes and their families (i.e., stakeholders).</p><p>Specifically, the purposes of the advocate are to (1) document and communicate recommendations from stakeholders to DOT on the needs, objectives, plans, approaches, content, and accomplishments of DOT's roadway safety programs and activities; and (2) serve as a resource and point of contact for stakeholders on relevant roadway safety issues.</p><p>The bill specifies that the advocate position must be filled by a career appointment.</p><p>The bill prohibits the advocate from taking certain actions, such as</p><ul><li>creating or authorizing DOT policies, priorities, or activities; or</li><li>disclosing or discussing any enforcement matters that are under investigation or in litigation.</li></ul><p>The advocate must submit an annual report to DOT highlighting systemic issues relating to roadway safety based on information provided by stakeholders. The report must include recommendations on how to remedy the issues.</p>"
        },
        "title": "DOT Victim and Survivor Advocate Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr851.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>DOT Victim and Survivor Advocate Act</strong></p><p>This bill directs the Department of Transportation (DOT) to establish the position of National Roadway Safety Advocate to work directly with victims and survivors of road crashes and their families (i.e., stakeholders).</p><p>Specifically, the purposes of the advocate are to (1) document and communicate recommendations from stakeholders to DOT on the needs, objectives, plans, approaches, content, and accomplishments of DOT's roadway safety programs and activities; and (2) serve as a resource and point of contact for stakeholders on relevant roadway safety issues.</p><p>The bill specifies that the advocate position must be filled by a career appointment.</p><p>The bill prohibits the advocate from taking certain actions, such as</p><ul><li>creating or authorizing DOT policies, priorities, or activities; or</li><li>disclosing or discussing any enforcement matters that are under investigation or in litigation.</li></ul><p>The advocate must submit an annual report to DOT highlighting systemic issues relating to roadway safety based on information provided by stakeholders. The report must include recommendations on how to remedy the issues.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr851"
    },
    "title": "DOT Victim and Survivor Advocate Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>DOT Victim and Survivor Advocate Act</strong></p><p>This bill directs the Department of Transportation (DOT) to establish the position of National Roadway Safety Advocate to work directly with victims and survivors of road crashes and their families (i.e., stakeholders).</p><p>Specifically, the purposes of the advocate are to (1) document and communicate recommendations from stakeholders to DOT on the needs, objectives, plans, approaches, content, and accomplishments of DOT's roadway safety programs and activities; and (2) serve as a resource and point of contact for stakeholders on relevant roadway safety issues.</p><p>The bill specifies that the advocate position must be filled by a career appointment.</p><p>The bill prohibits the advocate from taking certain actions, such as</p><ul><li>creating or authorizing DOT policies, priorities, or activities; or</li><li>disclosing or discussing any enforcement matters that are under investigation or in litigation.</li></ul><p>The advocate must submit an annual report to DOT highlighting systemic issues relating to roadway safety based on information provided by stakeholders. The report must include recommendations on how to remedy the issues.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr851"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr851ih.xml"
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
      "title": "DOT Victim and Survivor Advocate Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DOT Victim and Survivor Advocate Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the position of National Roadway Safety Advocate within the Department of Transportation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T05:18:37Z"
    }
  ]
}
```
