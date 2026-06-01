# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2238?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2238
- Title: Ranching Without Red Tape Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2238
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2025-05-21T14:49:06Z
- Update date including text: 2025-05-21T14:49:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-18 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-18 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-18 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-18 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2238",
    "number": "2238",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "V000136",
        "district": "2",
        "firstName": "Gabe",
        "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
        "lastName": "Vasquez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Ranching Without Red Tape Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-21T14:49:06Z",
    "updateDateIncludingText": "2025-05-21T14:49:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-18",
      "committees": {
        "item": {
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Livestock, Dairy, and Poultry.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-18",
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
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2025-04-18T21:07:00Z",
                "name": "Referred to"
              }
            },
            "name": "Forestry and Horticulture Subcommittee",
            "systemCode": "hsag15"
          },
          {
            "activities": {
              "item": {
                "date": "2025-04-18T21:07:00Z",
                "name": "Referred to"
              }
            },
            "name": "Livestock, Dairy, and Poultry Subcommittee",
            "systemCode": "hsag29"
          }
        ]
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-18T16:02:45Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "UT"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2238ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2238\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Vasquez (for himself, Ms. Maloy , and Mr. Zinke ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo allow holders of certain grazing permits to make minor range improvements and to require that the Secretary of Agriculture and the Secretary of the Interior respond to requests for range improvements within 30 days, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ranching Without Red Tape Act of 2025 .\n#### 2. Minor range improvements under USFS grazing permits\n##### (a) Minor range improvements by permittees\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall issue regulations allowing a permittee to carry out a minor range improvement on the lands with respect to which the permittee holds a grazing permit if\u2014\n**(1)**\nthe permittee notifies the applicable Forest Service district ranger at least 30 days prior to carrying out such minor range improvement; and\n**(2)**\nsuch applicable district ranger\u2014\n**(A)**\napproves the minor range improvement; or\n**(B)**\ndoes not respond to the minor range improvement.\n##### (b) Range improvements by the Secretary\nThe Secretary, acting through the applicable District Ranger, shall\u2014\n**(1)**\nrespond to a covered request not later than 30 days after the date on which such request is submitted; and\n**(2)**\nif such response confirms that the Secretary, acting through the applicable District Ranger, will carry out the range improvement requested\u2014\n**(A)**\nnotify the district office that serves the area in which such range improvement will occur; and\n**(B)**\nexpedite the carrying out of such range improvement using any available administrative tools or authorities, including categorical exclusions.\n##### (c) Definitions\nIn this section:\n**(1) CFR terms**\nThe terms grazing permit , permittee , and range improvement have the meanings given those terms, respectively, in section 222.1 of title 36, Code of Federal Regulations (or successor regulations).\n**(2) Covered request**\nThe term covered request means a request submitted by a permittee to the Secretary requesting that the Secretary carry out a range improvement.\n**(3) Minor range improvement**\nThe term minor range improvement includes improvements to existing fences and fence lines, wells, water pipelines, and stock tanks.\n**(4) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n#### 3. Minor range improvements under BLM grazing permits\n##### (a) Minor range improvements by grazing permit holders\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall issue regulations allowing a grazing permit or lease holder to carry out a minor range improvement on the lands with respect to which the grazing permit or lease applies if\u2014\n**(1)**\nthe grazing permit or lease holder notifies the applicable Bureau of Land Management district or field manager at least 30 days prior to carrying out such minor range improvement; and\n**(2)**\nsuch applicable district or field manager\u2014\n**(A)**\napproves the minor range improvement; or\n**(B)**\ndoes not respond to the minor range improvement.\n##### (b) Range improvements by the Secretary\nThe Secretary, acting through the applicable State Director of the Bureau of Land Management, shall\u2014\n**(1)**\nrespond to a covered request not later than 30 days after the date on which such request is submitted; and\n**(2)**\nif such response confirms that the Secretary, acting through the applicable State Director of the Bureau of Land Management, will carry out the range improvement requested\u2014\n**(A)**\nnotify the State office that serves the area in which such range improvement will occur; and\n**(B)**\nexpedite the carrying out of such range improvement using any available administrative tools or authorities, including categorical exclusions.\n##### (c) Definitions\nIn this section:\n**(1) Covered request**\nThe term covered request means a request submitted by a grazing permit holder to the Secretary requesting that the Secretary carry out a range improvement.\n**(2) Grazing permit or lease**\nThe term grazing permit or lease means a grazing permit or lease described in section 4130.2 of title 43, Code of Federal Regulations (or success regulations).\n**(3) Minor range improvement**\nThe term minor range improvement includes improvements to existing fences and fence lines, wells, water pipelines, and stock tanks.\n**(4) Range improvement**\nThe term range improvement means a range improvement carried out pursuant to subpart 4120 of title 43, Code of Federal Regulations (or successor regulations).\n**(5) Secretary**\nThe term Secretary means the Secretary of the Interior.",
      "versionDate": "2025-03-18",
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
        "updateDate": "2025-05-21T14:49:06Z"
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
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2238ih.xml"
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
      "title": "Ranching Without Red Tape Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ranching Without Red Tape Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allow holders of certain grazing permits to make minor range improvements and to require that the Secretary of Agriculture and the Secretary of the Interior respond to requests for range improvements within 30 days, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:42Z"
    }
  ]
}
```
