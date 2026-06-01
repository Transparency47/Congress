# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4481?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4481
- Title: ARMS Act
- Congress: 119
- Bill type: HR
- Bill number: 4481
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2025-08-01T17:25:20Z
- Update date including text: 2025-08-01T17:25:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4481",
    "number": "4481",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "A000055",
        "district": "4",
        "firstName": "Robert",
        "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
        "lastName": "Aderholt",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "ARMS Act",
    "type": "HR",
    "updateDate": "2025-08-01T17:25:20Z",
    "updateDateIncludingText": "2025-08-01T17:25:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "FL"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
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
      "sponsorshipDate": "2025-07-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4481ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4481\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Mr. Aderholt (for himself, Mr. Moskowitz , Mr. Panetta , and Mr. Zinke ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo amend the Arms Export Control Act to modify the authorities relating to the Special Defense Acquisition Fund.\n#### 1. Short title\nThis Act may be cited as the Accelerate Revenue for Manufacturing and Sales Act or the ARMS Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe United States defense industrial base plays a critical role in advancing both security and prosperity.\n**(2)**\nThere is increasing global demand for United States manufactured defense capabilities, highlighting the need to maintain a strong, agile, and scalable defense production capacity.\n**(3)**\nIn recent years, the combined value of Foreign Military Sales (FMS) and Direct Commercial Sales (DCS) has significantly exceeded domestic defense procurement budgets, with international demand for United States defense products approaching two-to-one over domestic acquisition.\n**(4)**\nDelays in delivering defense articles to allied and partner nations expose vulnerabilities in the current acquisition and sales process that risks undermining United States strategic credibility abroad.\n**(5)**\nThe Special Defense Acquisition Fund (SDAF) has demonstrated effectiveness in reducing delivery times and enabling advanced contracting for high-demand defense items prior to the completion of formal agreements.\n**(6)**\nStrengthening and expanding the SDAF would increase the efficiency and predictability of defense article deliveries to foreign partners, support the United States defense industrial base, and improve economies of scale.\n**(7)**\nTimely access to United States defense systems by allies and partners strengthens interoperability, improves coalition readiness, deters shared threats, and reinforces long-standing strategic relationships.\n**(8)**\nEnhancing SDAF authorities and capacity aligns with United States national interests and supports continued leadership in the global defense market.\n#### 3. Modifications to Special Defense Acquisition Fund\nSection 51(b)(1) of the Arms Export Control Act ( 22 U.S.C. 2795(b)(1) ) is amended by striking sales made under and all that follows through the actual value and inserting sales .",
      "versionDate": "2025-07-17",
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
        "name": "International Affairs",
        "updateDate": "2025-08-01T17:25:20Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4481ih.xml"
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
      "title": "ARMS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ARMS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T12:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Accelerate Revenue for Manufacturing and Sales Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T12:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Arms Export Control Act to modify the authorities relating to the Special Defense Acquisition Fund.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T12:33:40Z"
    }
  ]
}
```
