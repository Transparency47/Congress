# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4375?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4375
- Title: Great Lakes Icebreaker Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4375
- Origin chamber: House
- Introduced date: 2025-07-14
- Update date: 2026-01-05T22:01:03Z
- Update date including text: 2026-01-05T22:01:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-14: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-15 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- Latest action: 2025-07-14: Introduced in House

## Actions

- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-15 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-14",
    "latestAction": {
      "actionDate": "2025-07-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4375",
    "number": "4375",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001237",
        "district": "8",
        "firstName": "Kristen",
        "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
        "lastName": "McDonald Rivet",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Great Lakes Icebreaker Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-05T22:01:03Z",
    "updateDateIncludingText": "2026-01-05T22:01:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-14",
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
      "actionDate": "2025-07-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-14",
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
          "date": "2025-07-14T16:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-15T17:00:24Z",
              "name": "Referred to"
            }
          },
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
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
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "WI"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "OH"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4375ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4375\nIN THE HOUSE OF REPRESENTATIVES\nJuly 14, 2025 Ms. McDonald Rivet (for herself, Mr. Wied , and Mr. Miller of Ohio ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Commandant of the Coast Guard to submit to Congress a strategy detailing how the Coast Guard will complete design and construction of a Great Lakes Icebreaker, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Great Lakes Icebreaker Act of 2025 .\n#### 2. Great Lakes icebreaking\n##### (a) Great Lakes Icebreaker\n**(1) Strategy**\nNot later than 90 days after the date of enactment of this Act, the Commandant shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives a strategy detailing how the Coast Guard will complete design and construction of a Great Lakes icebreaker at least as capable as the Coast Guard cutter Mackinaw (WLBB\u201330) as expeditiously as possible after funding is provided for such icebreaker, including providing a cost estimate and an estimated delivery timeline that would facilitate the expedited delivery detailed in the strategy.\n**(2) Great Lakes icebreaker pilot program**\n**(A) In general**\nDuring the 5 ice seasons beginning after the date of enactment of this Act, the Commandant shall conduct a pilot program to determine the extent to which the Coast Guard Great Lakes icebreaking cutter fleet is capable of maintaining tier one and tier two waterways open 95 percent of the time during an ice season.\n**(B) Report**\nNot later than 180 days after the end of each of the 5 ice seasons beginning after the date of enactment of this Act, the Commandant shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives a report that details\u2014\n**(i)**\nthe results of the pilot program required under subparagraph (A); and\n**(ii)**\nany relevant new performance measures implemented by the Coast Guard, including the measures described in pages 5 through 7 of the report of the Coast Guard titled Domestic Icebreaking Operations and submitted to Congress on July 26, 2024, as required by section 11212(a)(3) of the Don Young Coast Guard Authorization Act of 2022 ( Public Law 117\u2013263 ), and the results of the implementation of such measures.\n##### (b) Modification to reporting requirement relating to icebreaking operations in Great Lakes\n**(1) In general**\nSection 11213(f) of the Don Young Coast Guard Authorization Act of 2022 ( Public Law 117\u2013263 ) is amended to read as follows:\n(f) Public report Not later than July 1 after the first winter in which the Commandant has submitted the report required by paragraph (3) of section 11212(a), the Commandant shall publish on a publicly accessible website of the Coast Guard a report on the cost to the Coast Guard of meeting the proposed standards described in paragraph (2) of such section. .\n**(2) Public report**\nSection 11272(c) of the James M. Inhofe National Defense Authorization Act for Fiscal Year 2023 is amended by adding at the end the following:\n(7) Public report (A) In general Not later than 30 days after the date of enactment of the Coast Guard Authorization Act of 2025, the Commandant shall brief the Committee on Transportation and Infrastructure of the House or Representatives and the Committee on Commerce, Science, and Transportation of the Senate on the cost to the Coast Guard of meeting the requirements of section 564 of title 14, United States Code, in fiscal year 2024. (B) Secondary briefings Not later than November, 2025 and November, 1, 2026, the Commandant shall brief the committees described in subparagraph (A) on the cost to the Coast Guard of meeting the requirements of section 564 of title 14, United States Code, in fiscal years 2025 and 2026, respectively. .",
      "versionDate": "2025-07-14",
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
        "actionDate": "2025-12-18",
        "text": "Became Public Law No: 119-60."
      },
      "number": "1071",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
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
        "updateDate": "2025-07-31T21:00:57Z"
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
      "date": "2025-07-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4375ih.xml"
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
      "title": "Great Lakes Icebreaker Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Great Lakes Icebreaker Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Commandant of the Coast Guard to submit to Congress a strategy detailing how the Coast Guard will complete design and construction of a Great Lakes Icebreaker, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T04:48:36Z"
    }
  ]
}
```
