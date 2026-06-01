# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7695?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7695
- Title: To provide that the final rule titled "Special Areas; Roadless Area Conservation" and issued on January 12, 2001 (66 Fed. Reg. 3244) shall have no force or effect and require the Secretary of Agriculture to construct certain roads on National Forest System lands, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 7695
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-05-27T08:05:56Z
- Update date including text: 2026-05-27T08:05:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-25 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-12 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-05-21 - Committee: Subcommittee Hearings Held
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-25 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-12 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-05-21 - Committee: Subcommittee Hearings Held

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7695",
    "number": "7695",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "To provide that the final rule titled \"Special Areas; Roadless Area Conservation\" and issued on January 12, 2001 (66 Fed. Reg. 3244) shall have no force or effect and require the Secretary of Agriculture to construct certain roads on National Forest System lands, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-27T08:05:56Z",
    "updateDateIncludingText": "2026-05-27T08:05:56Z"
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
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2026-02-25T14:05:30Z",
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
                "date": "2026-05-12T21:00:29Z",
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
          "date": "2026-02-25T14:05:25Z",
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
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "MT"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "UT"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "MN"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7695ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7695\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Ms. Hageman (for herself, Mr. Downing , Ms. Maloy , Mr. Stauber , and Mr. Tiffany ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide that the final rule titled Special Areas; Roadless Area Conservation and issued on January 12, 2001 (66 Fed. Reg. 3244) shall have no force or effect and require the Secretary of Agriculture to construct certain roads on National Forest System lands, and for other purposes.\n#### 1. Requirement for construction of certain roads on National Forest System lands\n##### (a) Roadless Rule nullification\n**(1) Nullification**\nThe final rule of the Department of Agriculture titled Special Areas; Roadless Area Conservation and issued on January 12, 2001 (66 Fed. Reg. 3244) shall have no force or effect.\n**(2) Prohibition**\nThe Secretary of Agriculture may not take any action to propose, finalize, implement, administer, or enforce any rule substantially similar to the rule described in paragraph (1).\n##### (b) Required road construction\nThe Secretary of Agriculture, acting through the Chief of the Forest Service, shall, subject to all applicable environmental requirements (including applicable requirements of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. )), construct on National Forest System lands such permanent and temporary roads as the Secretary determines necessary\u2014\n**(1)**\nto carry out restoration activities of the Forest Service;\n**(2)**\nto carry out hazardous fuels reduction activities of the Forest Service in\u2014\n**(A)**\nan at-risk community;\n**(B)**\nthe wildland-urban interface; or\n**(C)**\na municipal watershed;\n**(3)**\nto replace or decommission any existing permanent road determined by the Secretary to be adversely affecting the health of a forest, rangeland, or a watershed; or\n**(4)**\nto carry out the intent of the Act of June 4, 1897 ( 16 U.S.C. 473\u2013482 , 551).\n##### (c) Definitions\nIn this section:\n**(1) At-risk community; wildland-urban interface**\nThe terms at-risk community and wildland-urban interface have the meanings given such terms, respectively, in section 101 of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6511 ).\n**(2) National Forest System**\nThe term National Forest System has the meaning given the term in section 11(a) of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1609 ).",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-03-23T20:19:24Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7695ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide that the final rule titled \"Special Areas; Roadless Area Conservation\" and issued on January 12, 2001 (66 Fed. Reg. 3244) shall have no force or effect and require the Secretary of Agriculture to construct certain roads on National Forest System lands, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T03:18:30Z"
    },
    {
      "title": "To provide that the final rule titled \"Special Areas; Roadless Area Conservation\" and issued on January 12, 2001 (66 Fed. Reg. 3244) shall have no force or effect and require the Secretary of Agriculture to construct certain roads on National Forest System lands, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T09:07:02Z"
    }
  ]
}
```
