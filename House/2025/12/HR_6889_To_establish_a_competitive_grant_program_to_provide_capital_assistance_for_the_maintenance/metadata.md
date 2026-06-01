# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6889?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6889
- Title: BRIDGE Act
- Congress: 119
- Bill type: HR
- Bill number: 6889
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-05-13T08:05:59Z
- Update date including text: 2026-05-13T08:05:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6889",
    "number": "6889",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "Q000023",
        "district": "5",
        "firstName": "Mike",
        "fullName": "Rep. Quigley, Mike [D-IL-5]",
        "lastName": "Quigley",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "BRIDGE Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:05:59Z",
    "updateDateIncludingText": "2026-05-13T08:05:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:06:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:45:10Z",
              "name": "Referred to"
            }
          },
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
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
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6889ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6889\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Quigley introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo establish a competitive grant program to provide capital assistance for the maintenance, replacement, and rehabilitation needs of commuter rail bridges.\n#### 1. Short title\nThis Act may be cited as the Building Rail Infrastructure for a Durable and Growing Economy Act or the BRIDGE Act .\n#### 2. Commuter rail bridge grants\n##### (a) In general\nChapter 53 of title 49, United States Code, is amended by inserting after section 5312 the following:\n5313. Commuter rail bridge grants (a) Definitions In this section: (1) Commuter rail The term commuter rail shall have the meaning given the term by the Secretary for purposes of reporting to the national transit database under section 5335. (2) Commuter rail bridge The term commuter rail bridge \u2014 (A) means a bridge used in commuter rail operations; and (B) includes a bridge described in subparagraph (A) that is also utilized for\u2014 (i) intercity passenger railroad service; (ii) other public transportation service; or (iii) a roadway. (3) Covered grant The term covered grant means a grant awarded under subsection (b). (b) Grant authority The Secretary may make grants to operators of public transportation systems for capital costs of maintenance, replacement, or rehabilitation of a commuter rail bridge. (c) Grant requirements (1) Terms and conditions Except as otherwise provided in this section, a covered grant shall be subject to the same terms and conditions as a grant under section 5337. (2) Eligible costs Eligible costs for a project funded by a covered grant shall be limited to the net capital costs of the public transportation costs attributable to the project based on projected use of the commuter rail bridge. (3) Bridge access agreement Before executing a grant agreement with the Secretary under this section, an operator of a public transportation system seeking a covered grant for a commuter rail bridge that is not owned by the operator shall establish and maintain an agreement with the owner of the bridge that ensures bridge access by the operator. (d) Competitive process The Secretary shall\u2014 (1) not later than 30 days after the date on which amounts are made available for obligation under this section for a full fiscal year, solicit applications for covered grants on a competitive basis; and (2) award a covered grant based on the solicitation under paragraph (1) not later than the earlier of\u2014 (A) 75 days after the date on which the solicitation expires; or (B) the last day of the fiscal year in which the Secretary solicits the applications for covered grants. (e) Consideration In awarding covered grants, the Secretary shall consider\u2014 (1) the size of the commuter rail system of the applicant; (2) the amount of funds available to the applicant under section 5337; (3) the age and condition of the commuter rail bridge; and (4) whether the applicant has identified replacement of the commuter rail bridge as a priority in the investment prioritization portion of the transit asset management plan developed by the applicant pursuant to part 625 of title 49, Code of Federal Regulations (or successor regulations). .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 53 of title 49, United States Code, is amended by inserting after the item relating to section 5312 the following:\n5313. Commuter rail bridge grants. .\n##### (c) Authorization of appropriations\nSection 5338 of title 49, United States Code, is amended by adding at the end the following:\n(f) Commuter rail bridge grants There are authorized to be appropriated to carry out section 5313 $1,500,000,000 for each of fiscal years 2027 through 2031. .",
      "versionDate": "2025-12-18",
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
        "actionDate": "2026-01-27",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "3701",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "BRIDGE Act",
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
        "updateDate": "2026-01-22T15:56:47Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6889ih.xml"
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
      "title": "BRIDGE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BRIDGE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Building Rail Infrastructure for a Durable and Growing Economy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a competitive grant program to provide capital assistance for the maintenance, replacement, and rehabilitation needs of commuter rail bridges.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:33:36Z"
    }
  ]
}
```
