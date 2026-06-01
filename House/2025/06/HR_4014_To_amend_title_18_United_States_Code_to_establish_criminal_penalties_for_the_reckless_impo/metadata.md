# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4014?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4014
- Title: Preventing Lethal Agricultural and National Threats (PLANT) Act
- Congress: 119
- Bill type: HR
- Bill number: 4014
- Origin chamber: House
- Introduced date: 2025-06-13
- Update date: 2026-05-12T08:06:02Z
- Update date including text: 2026-05-12T08:06:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-13: Introduced in House
- 2025-06-13 - IntroReferral: Introduced in House
- 2025-06-13 - IntroReferral: Introduced in House
- 2025-06-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-13: Introduced in House

## Actions

- 2025-06-13 - IntroReferral: Introduced in House
- 2025-06-13 - IntroReferral: Introduced in House
- 2025-06-13 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-13",
    "latestAction": {
      "actionDate": "2025-06-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4014",
    "number": "4014",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Preventing Lethal Agricultural and National Threats (PLANT) Act",
    "type": "HR",
    "updateDate": "2026-05-12T08:06:02Z",
    "updateDateIncludingText": "2026-05-12T08:06:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-13",
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
          "date": "2025-06-13T13:30:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-06-13",
      "state": "NY"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "MD"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4014ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4014\nIN THE HOUSE OF REPRESENTATIVES\nJune 13, 2025 Mr. Nunn of Iowa (for himself and Mr. Riley of New York ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to establish criminal penalties for the reckless importation or handling of dangerous agricultural pathogens.\n#### 1. Short title\nThis Act may be cited as the Preventing Lethal Agricultural and National Threats (PLANT) Act .\n#### 2. Reckless importation of dangerous agricultural pathogens\nTitle 18 U.S.C. is amended by inserting after section 175b the following:\n175c. Reckless importation of dangerous agricultural pathogens. (a) Offense Whoever knowingly or recklessly imports a biological agent, toxin, or organism\u2014 (1) without the required permit or authorization from the U.S. Department of Agriculture or other appropriate agency; and (2) where such agent, toxin, or organism is designated by regulation as a high-risk agricultural pathogen capable of causing significant harm to U.S. crops, livestock, or agricultural ecosystems, Shall be fined under this title or imprisoned not more than 10 years, or both. (b) Aggravating factors If the offense: (1) involves concealment of origin; (2) is committed by a person acting on behalf of, or funded by, a foreign government; or (3) results in actual economic damage exceeding $1,000,000; Then the term of imprisonment may be up to 20 years. (c) Definitions In this section: (1) the term recklessly means the person consciously disregarded a substantial and unjustifiable risk that the pathogen could cause significant harm. (2) the term high-risk agricultural pathogen shall be defined by the Secretary of Agriculture and published via regulation. .",
      "versionDate": "2025-06-13",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-30T13:01:45Z"
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
      "date": "2025-06-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4014ih.xml"
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
      "title": "Preventing Lethal Agricultural and National Threats (PLANT) Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-27T02:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventing Lethal Agricultural and National Threats (PLANT) Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-27T02:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to establish criminal penalties for the reckless importation or handling of dangerous agricultural pathogens.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-27T02:18:20Z"
    }
  ]
}
```
