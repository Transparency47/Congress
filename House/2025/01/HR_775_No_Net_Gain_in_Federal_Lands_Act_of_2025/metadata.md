# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/775?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/775
- Title: No Net Gain in Federal Lands Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 775
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2026-02-06T19:46:03Z
- Update date including text: 2026-02-06T19:46:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-28 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-28 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/775",
    "number": "775",
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
    "title": "No Net Gain in Federal Lands Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-06T19:46:03Z",
    "updateDateIncludingText": "2026-02-06T19:46:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-28T16:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr775ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 775\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Ms. Hageman introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo ensure that there is no net gain in Federal land ownership in any fiscal year, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Net Gain in Federal Lands Act of 2025 .\n#### 2. No net gain in certain federal land ownership\n##### (a) No net gain\n**(1) In general**\nThe number of acres of land, water, and interests therein acquired by the United States and put under the administrative jurisdiction of the Secretary of the Interior or the Secretary of Agriculture in a State during a fiscal year may not exceed the number of acres of Federal land under the administrative jurisdiction of the Secretary of the Interior or the Secretary of Agriculture disposed of in that State during that fiscal year.\n**(2) Application**\nIn applying paragraph (1)\u2014\n**(A)**\nonly the disposal of fee title to lands or waters may be counted against acquisition of fee title to lands or waters; and\n**(B)**\nonly disposal of interests in lands or waters of less than fee may be counted against acquisition of comparable interests in lands or waters of less than fee.\n##### (b) Annual inventory; determination, report\n**(1) Inventory**\nThe Secretary shall complete an annual inventory of the total number of acres of Federal land, categorized according to the type of interest (such as fee, easement, mineral interest, etc.), under the administrative jurisdiction of each agency of the Department of the Interior or the Department of Agriculture, as the case may be\u2014\n**(A)**\nin each State; and\n**(B)**\nin the aggregate.\n**(2) Determination**\nBased on the inventory required by subparagraph (A), the Secretary shall make an annual determination of the increase or decrease in the previous fiscal year of the total number of acres of Federal land, categorized according to the type of interest (such as fee, easement, mineral interest), under the administrative jurisdiction of\u2014\n**(A)**\neach agency of the Department of the Interior or the Department of Agriculture, as the case may be; and\n**(B)**\nthe Department of the Interior, in total, and the Department of Agriculture, in total, as the case may be.\n**(3) Report**\nNot later than September 30 of each year, the Secretary shall submit to the President and Congress a report containing the inventory and determination required under this subsection.\n##### (c) Compliance land disposal\n**(1) In general**\nNot later than 24 months after the Secretary determines under subsection (b) that the Federal Government acquired more new Federal land under the administrative jurisdiction of that Secretary in a State than it disposed of in that State during a fiscal year, the President shall convey to that State sufficient Federal land under the administrative jurisdiction of that Secretary to comply with subsection (a) for that fiscal year.\n**(2) No Major Federal Action**\nA conveyance under paragraph (1) shall not be considered a major Federal action for the purposes of section 102(2)(C) of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4332(2)(C) ).\n##### (d) Definitions\nFor the purposes of this Act, the following definitions apply:\n**(1) Federal land**\nThe term Federal land \u2014\n**(A)**\nmeans Federal lands, waters, and interests therein, including lands held in trust by the Federal Government (except as provided in subparagraph (C));\n**(B)**\nincludes non-Federal land that is\u2014\n**(i)**\nleased by the Federal Government;\n**(ii)**\nheld as a conservation easement by the Federal Government; or\n**(iii)**\nrequires oversight by, involvement in, or other authority is exercised by the Federal Government to an extent that prohibits use of the non-Federal land that is not specifically authorized by the Federal Government; and\n**(C)**\ndoes not include land, water, and interests therein\u2014\n**(i)**\nheld by an Indian Tribe or individual Indian subject to a restriction by the Federal Government against alienation;\n**(ii)**\nacquired pursuant to a foreclosure under title 18, United States Code;\n**(iii)**\nacquired by any department, agency, or independent establishment in its capacity as a receiver, conserver, or liquidating agent which is held by that department, agency, or independent establishment in such capacity pending disposal;\n**(iv)**\nthat has reverted to the Federal Government pursuant to a reversionary clause in a deed or statute;\n**(v)**\nsubject to seizure, levy, or lien under the Internal Revenue Code of 1986; or\n**(vi)**\nsecuring a debt owed to the United States.\n**(2) Secretary**\nThe term Secretary means\u2014\n**(A)**\nthe Secretary of Agriculture with regard to the Federal land under the administrative jurisdiction of that Secretary; and\n**(B)**\nthe Secretary of the Interior with regard to Federal land under the administrative jurisdiction of that Secretary.\n**(3) State**\nThe term State means the several States and the District of Columbia.",
      "versionDate": "2025-01-28",
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
            "name": "Congressional oversight",
            "updateDate": "2026-02-06T19:46:03Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2026-02-06T19:45:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-01T19:54:33Z"
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
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr775ih.xml"
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
      "title": "No Net Gain in Federal Lands Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Net Gain in Federal Lands Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure that there is no net gain in Federal land ownership in any fiscal year, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:41Z"
    }
  ]
}
```
