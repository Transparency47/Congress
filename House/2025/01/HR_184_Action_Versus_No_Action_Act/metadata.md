# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/184?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/184
- Title: Action Versus No Action Act
- Congress: 119
- Bill type: HR
- Bill number: 184
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-05-27T08:05:52Z
- Update date including text: 2026-05-27T08:05:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-07 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- 2026-05-12 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-05-21 - Committee: Subcommittee Hearings Held
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-07 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- 2026-05-12 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-05-21 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/184",
    "number": "184",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "M001177",
        "district": "5",
        "firstName": "Tom",
        "fullName": "Rep. McClintock, Tom [R-CA-5]",
        "lastName": "McClintock",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Action Versus No Action Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:05:52Z",
    "updateDateIncludingText": "2026-05-27T08:05:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
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
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Federal Lands.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-07",
      "committees": {
        "item": {
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Forestry and Horticulture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:23:40Z",
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
                "date": "2026-05-21T14:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-05-12T21:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-03T16:23:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-07T17:48:09Z",
              "name": "Referred to"
            }
          },
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "systemCode": "hsag00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr184ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 184\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. McClintock introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require that only two alternatives be considered with respect to certain proposed collaborative forest management activities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Action Versus No Action Act .\n#### 2. Analysis of only two alternatives (action versus no action) in proposed collaborative forest management activities\n##### (a) Application to certain environmental assessments and environmental impact statements\nThis section shall apply whenever the Secretary concerned prepares an environmental assessment or an environmental impact statement pursuant to section 102 of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4332 ) for a forest management activity that\u2014\n**(1)**\nwill occur on lands identified as the Secretary concerned as suitable for timber production; and\n**(2)**\nmeets at least one of the following conditions:\n**(A)**\nThe forest management activity will occur on lands designated by the Secretary (or designee thereof) pursuant to section 602(b) of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6591a(b) ), notwithstanding whether such forest management activity is initiated prior to the date of enactment of this Act.\n**(B)**\nThe forest management activity is developed through a collaborative process.\n**(C)**\nThe forest management activity is proposed by a resource advisory committee.\n**(D)**\nThe forest management activity is covered by a community wildfire protection plan.\n##### (b) Consideration of alternatives\nIn the case of an environmental assessment or environmental impact statement described in subsection (a), the Secretary concerned shall study, develop, and describe only the following two alternatives:\n**(1)**\nThe forest management activity.\n**(2)**\nThe alternative of no action.\n##### (c) Elements of no action alternative\nIn the case of the alternative of no action described in subsection (b)(2), the Secretary concerned shall consider whether to evaluate\u2014\n**(1)**\nthe effect of no action on\u2014\n**(A)**\nforest health;\n**(B)**\npotential losses of life and property;\n**(C)**\nhabitat diversity;\n**(D)**\nwildfire potential;\n**(E)**\ninsect and disease potential; and\n**(F)**\ntimber production; and\n**(2)**\nthe implications of a resulting decline in forest health, loss of habitat diversity, wildfire, or insect or disease infestation (given fire and insect and disease historic cycles) on\u2014\n**(A)**\npotential losses of life and property;\n**(B)**\ndomestic water supply in the project area;\n**(C)**\nwildlife habitat loss; and\n**(D)**\nother economic and social factors.\n##### (d) Definitions\nIn this section:\n**(1) Collaborative process**\nThe term collaborative process means a process relating to the management of National Forest System lands or public lands by which a project or forest management activity is developed and implemented by the Secretary concerned through collaboration with interested persons, as described in section 603(b)(1)(C) of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6591b(b)(1)(C) ).\n**(2) Community wildfire protection plan**\nThe term community wildfire protection plan has the meaning given the term in section 101 of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6511 ).\n**(3) Resource advisory committee**\nThe term resource advisory committee has the meaning given the term in section 201 of the Secure Rural Schools and Community Self-Determination Act of 2000 ( 16 U.S.C. 7121 ).\n**(4) Secretary concerned**\nThe term Secretary concerned means\u2014\n**(A)**\nthe Secretary of Agriculture, with respect to National Forest System lands; and\n**(B)**\nthe Secretary of the Interior, with respect to public lands.",
      "versionDate": "2025-01-03",
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
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-02-28T18:57:05Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-02-28T18:57:05Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2025-02-28T18:57:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-02-26T20:53:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr184",
          "measure-number": "184",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-03-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr184v00",
            "update-date": "2025-03-10"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Action Versus No Action Act</strong></p><p>This bill limits the scope of an environmental assessment (EA)\u00a0or environmental impact statement (EIS) conducted under the National Environmental Policy Act of 1969 for forest management activity on certain public lands to only the following two alternatives: (1) the effects of the forest management activity, and (2) no action.</p><p>The bill applies to any EA or EIS prepared by the Forest Service or the Department of the Interior for a forest management activity on public land\u00a0that is suitable for timber production and that</p><ul><li>occurs on land designated as an insect and disease treatment area under the\u00a0Healthy Forests Restoration Act of 2003,</li><li>is developed through a collaborative process,</li><li>is proposed by a resource advisory committee, or</li><li>is covered by a community wildfire protection plan.</li></ul><p>In the case of the alternative of no action, the Forest Service or Interior must consider whether to evaluate</p><ul><li>the effect of no action on forest health, potential losses of life and property, habitat diversity, wildfire potential, insect and disease potential, and timber production; and</li><li>the implications of a resulting decline in forest health, loss of habitat diversity, wildfire, or insect or disease infestation on potential losses of life and property, domestic water supply in the project area, wildlife habitat loss, and other economic and social factors.</li></ul>"
        },
        "title": "Action Versus No Action Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr184.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Action Versus No Action Act</strong></p><p>This bill limits the scope of an environmental assessment (EA)\u00a0or environmental impact statement (EIS) conducted under the National Environmental Policy Act of 1969 for forest management activity on certain public lands to only the following two alternatives: (1) the effects of the forest management activity, and (2) no action.</p><p>The bill applies to any EA or EIS prepared by the Forest Service or the Department of the Interior for a forest management activity on public land\u00a0that is suitable for timber production and that</p><ul><li>occurs on land designated as an insect and disease treatment area under the\u00a0Healthy Forests Restoration Act of 2003,</li><li>is developed through a collaborative process,</li><li>is proposed by a resource advisory committee, or</li><li>is covered by a community wildfire protection plan.</li></ul><p>In the case of the alternative of no action, the Forest Service or Interior must consider whether to evaluate</p><ul><li>the effect of no action on forest health, potential losses of life and property, habitat diversity, wildfire potential, insect and disease potential, and timber production; and</li><li>the implications of a resulting decline in forest health, loss of habitat diversity, wildfire, or insect or disease infestation on potential losses of life and property, domestic water supply in the project area, wildlife habitat loss, and other economic and social factors.</li></ul>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr184"
    },
    "title": "Action Versus No Action Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Action Versus No Action Act</strong></p><p>This bill limits the scope of an environmental assessment (EA)\u00a0or environmental impact statement (EIS) conducted under the National Environmental Policy Act of 1969 for forest management activity on certain public lands to only the following two alternatives: (1) the effects of the forest management activity, and (2) no action.</p><p>The bill applies to any EA or EIS prepared by the Forest Service or the Department of the Interior for a forest management activity on public land\u00a0that is suitable for timber production and that</p><ul><li>occurs on land designated as an insect and disease treatment area under the\u00a0Healthy Forests Restoration Act of 2003,</li><li>is developed through a collaborative process,</li><li>is proposed by a resource advisory committee, or</li><li>is covered by a community wildfire protection plan.</li></ul><p>In the case of the alternative of no action, the Forest Service or Interior must consider whether to evaluate</p><ul><li>the effect of no action on forest health, potential losses of life and property, habitat diversity, wildfire potential, insect and disease potential, and timber production; and</li><li>the implications of a resulting decline in forest health, loss of habitat diversity, wildfire, or insect or disease infestation on potential losses of life and property, domestic water supply in the project area, wildlife habitat loss, and other economic and social factors.</li></ul>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr184"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr184ih.xml"
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
      "title": "Action Versus No Action Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T06:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Action Versus No Action Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T06:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require that only two alternatives be considered with respect to certain proposed collaborative forest management activities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T06:03:37Z"
    }
  ]
}
```
