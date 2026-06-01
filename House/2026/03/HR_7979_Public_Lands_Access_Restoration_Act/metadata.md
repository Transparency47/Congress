# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7979?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7979
- Title: Public Lands Access Restoration Act
- Congress: 119
- Bill type: HR
- Bill number: 7979
- Origin chamber: House
- Introduced date: 2026-03-18
- Update date: 2026-04-07T15:05:54Z
- Update date including text: 2026-04-07T15:05:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-18: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-18 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-19 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-03-26 - Committee: Subcommittee Hearings Held
- Latest action: 2026-03-18: Introduced in House

## Actions

- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-18 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-19 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-03-26 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-18",
    "latestAction": {
      "actionDate": "2026-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7979",
    "number": "7979",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C001137",
        "district": "5",
        "firstName": "Jeff",
        "fullName": "Rep. Crank, Jeff [R-CO-5]",
        "lastName": "Crank",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Public Lands Access Restoration Act",
    "type": "HR",
    "updateDate": "2026-04-07T15:05:54Z",
    "updateDateIncludingText": "2026-04-07T15:05:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-19",
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
      "actionCode": "H11100",
      "actionDate": "2026-03-18",
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
      "actionDate": "2026-03-18",
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
      "actionDate": "2026-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-18",
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
          "date": "2026-03-18T14:01:25Z",
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
                "date": "2026-03-26T19:33:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-03-19T14:00:00Z",
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
          "date": "2026-03-18T14:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
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
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7979ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7979\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2026 Mr. Crank (for himself and Mr. Kennedy of Utah ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo restore the presumption of access on lands managed by the Forest Service and the Bureau of Land Management.\n#### 1. Short title\nThis Act may be cited as the Public Lands Access Restoration Act .\n#### 2. Restoration of Historic Access Policy\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act\u2014\n**(1)**\na covered road or trail shall be presumed to be open to motorized access unless the Secretary concerned restricts motorized access to the covered road or trail in accordance with subsection (b); and\n**(2)**\nthe Secretary concerned shall issue or revise regulations as necessary to implement paragraph (1).\n##### (b) Standards for restriction\nThe Secretary concerned may only restrict motorized access to a covered road or trail if\u2014\n**(1)**\na need for the restriction is identified based on clear and convincing evidence for resource protection or public safety; and\n**(2)**\nthe restriction is\u2014\n**(A)**\nclearly indicated with signage posted at the points on the covered road or trail at which the restriction begins and ends;\n**(B)**\ndepicted on updated official maps of the covered road or trail, to be made available in both digital and printed form;\n**(C)**\nsubject to\u2014\n**(i)**\npublic notice in the Federal Register and at least one local newspaper; and\n**(ii)**\na 30-day comment period;\n**(D)**\nreviewed by the Secretary concerned at least once every 5 years to determine if the restriction is still justified; and\n**(E)**\napplied to the smallest area, and for the least amount of time, as is practicable.\n#### 3. Public nomination of trails\n##### (a) Public nominations for motorized routes\nThe Secretary of the Interior, acting through the Director of the Bureau of Land Management, and the Secretary of Agriculture, acting through the Chief of the Forest Service, shall accept and consider proposals submitted by the public for additions to designated motorized road and trail networks at any time, including during the development or revision of transportation or travel management plans carried out pursuant to the National Forest Management Act of 1976 ( 16 U.S.C. 472a et seq. ), the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. ), and the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ).\n##### (b) Eligible nominations\nProposals submitted under subsection (a) may include\u2014\n**(1)**\nthe designation of new motorized roads or trails;\n**(2)**\nthe repurposing or conversion of roads or trails; or\n**(3)**\nthe inclusion of roads or trails not previously identified in agency transportation or travel inventories.\n##### (c) Consideration priority\nIn considering proposals under this section, the Secretary of the Interior and the Secretary of Agriculture shall give priority to proposals that\u2014\n**(1)**\nimprove connectivity within existing road or trail networks;\n**(2)**\nprotect natural resources;\n**(3)**\nenhance access for fuels reduction, wildfire response, or other land management activities; or\n**(4)**\nprovide additional or enhanced opportunities for motorized recreation.\n##### (d) Expedited review\nThe Secretary of the Interior or the Secretary of Agriculture, as applicable, shall consider a proposal for the conversion of an administrative or currently closed road to a designated motorized trail as expeditiously as practicable, and not later than 90 days after the date of submission of the proposal.\n#### 4. Rule of construction\nNothing in this Act shall be construed, with respect to a covered road or trail, to restrict or otherwise limit\u2014\n**(1)**\npublic access (except as described in subsection (b)); or\n**(2)**\nother uses.\n#### 5. Definitions\nIn this Act:\n**(1) Covered road or trail**\n**(A) In general**\nExcept as provided in subparagraph (B), the term covered road or trail means a road or trail designated for motorized use that is a\u2014\n**(i)**\na National Forest System road;\n**(ii)**\na National Forest System trail;\n**(iii)**\na Bureau of Land Management road; or\n**(iv)**\na Bureau of Land Management trail.\n**(B) Exception**\nThe term covered road or trail does not apply to a road or trail within an area within a congressionally designated wilderness area or national park.\n**(2) Motorized access**\nThe term motorized access means access or use by a motor or self-propelled vehicle capable of off-highway travel during winter or summer including all-terrain vehicles, four-wheelers, three-wheelers, dirt bikes, motorcycles, trail bikes, and snowmobiles.\n**(3) National Forest System road**\nThe term National Forest System road means a road within a unit of the National Forest System other than a road which has been authorized by a legally documented right-of-way held by a State, county, or other local public road authority.\n**(4) National Forest System trail**\nThe term National Forest System trail means a trail within a unit of the National Forest System other than a trail which has been authorized by a legally documented right-of-way held by a State, county, or other local public road authority.\n**(5) Bureau of Land Management road**\nThe term Bureau of Land Management road means a road on public lands other than a road which has been authorized by a legally documented right-of-way held by a State, county, or other local public road authority.\n**(6) Bureau of Land Management trail**\nThe term Bureau of Land Management trail means a trail on public lands other than a trail which has been authorized by a legally documented right-of-way held by a State, county, or other local public road authority.\n**(7) Public lands**\nThe term public lands has the meaning given such term in section 103 of the Federal Land Policy Management Act of 1976 ( 43 U.S.C. 1702 ).\n**(8) Secretary concerned**\nThe term Secretary concerned means\u2014\n**(A)**\nthe Secretary of Agriculture, with respect to a National Forest System road or National Forest System trail; and\n**(B)**\nthe Secretary of the Interior, with respect to a Bureau of Land Management road or Bureau of Land Management trail.",
      "versionDate": "2026-03-18",
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
            "name": "Forests, forestry, trees",
            "updateDate": "2026-04-07T15:05:28Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2026-04-07T15:05:49Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-07T15:05:54Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-04-07T15:05:23Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2026-04-07T15:05:45Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2026-04-07T15:05:33Z"
          },
          {
            "name": "Roads and highways",
            "updateDate": "2026-04-07T15:05:40Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-04-03T14:57:53Z"
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
      "date": "2026-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7979ih.xml"
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
      "title": "Public Lands Access Restoration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Public Lands Access Restoration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To restore the presumption of access on lands managed by the Forest Service and the Bureau of Land Management.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T05:33:29Z"
    }
  ]
}
```
