# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2061?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2061
- Title: Molly R. Loomis Research for Descendants of Toxic Exposed Veterans Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2061
- Origin chamber: Senate
- Introduced date: 2025-06-12
- Update date: 2026-04-15T11:03:26Z
- Update date including text: 2026-04-15T11:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in Senate
- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-06-12: Introduced in Senate

## Actions

- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2061",
    "number": "2061",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Molly R. Loomis Research for Descendants of Toxic Exposed Veterans Act of 2025",
    "type": "S",
    "updateDate": "2026-04-15T11:03:26Z",
    "updateDateIncludingText": "2026-04-15T11:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2026-03-18T20:00:12Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T21:00:16Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-12-10T21:00:16Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-06-12T17:42:56Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "WA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "MI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NJ"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "IL"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "NV"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "RI"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "RI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2061is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2061\nIN THE SENATE OF THE UNITED STATES\nJune 12, 2025 Mr. Blumenthal (for himself and Mrs. Murray ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo require the Interagency Working Group on Toxic Exposure to conduct research on the diagnosis and treatment of health conditions of descendants of individuals exposed to toxic substances while serving as members of the Armed Forces, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Molly R. Loomis Research for Descendants of Toxic Exposed Veterans Act of 2025 .\n#### 2. Research on diagnosis and treatment of health conditions of descendants of individuals exposed to toxic substances while serving in Armed Forces\n##### (a) In general\nSubsection (b) of section 501 of the Sergeant First Class Heath Robinson Honoring our Promise to Address Comprehensive Toxics Act of 2022 ( Public Law 117\u2013168 ) is amended by adding at the end the following new paragraph:\n(3) Establish Federal interagency task forces to conduct collaborative research activities. .\n##### (b) Reporting\nSubsection (c) of such section is amended by striking paragraphs (2) and (3) and inserting the following:\n(2) Not later than one year after the date of the enactment of the Molly R. Loomis Research for Descendants of Toxic Exposed Veterans Act of 2025 \u2014 (A) a report containing a description of the collaborative research activities identified by the Working Group under subsection (b); (B) the findings of the members of the Working Group with respect to the collaborative research activities described in subparagraph (A); and (C) such recommendations as the Working Group may have for legislative or administrative action to improve collaborative research activities among the members of the Working Group. (3) Not less frequently than annually during the five-year period covered by the strategic plan developed under subsection (b)\u2014 (A) a summary of the collaborative research activities carried out by the members of the Working Group and the findings of the members with respect to such research activities; (B) a progress report on implementation of the strategic plan developed by the Working Group under subsection (b); and (C) such recommendations as the Working Group may have for legislative or administrative action to improve collaborative research activities among members of the Working Group. .\n##### (c) Research requirements\nSuch section is amended\u2014\n**(1)**\nby redesignating subsections (c) through (e) as subsections (d) through (f), respectively;\n**(2)**\nin subsection (e), as redesignated by paragraph (1), by striking under subsection (c) and inserting under subsection (d) ; and\n**(3)**\nby inserting after subsection (b) the following new subsection (c):\n(c) Requirements relating to certain research on impacts to descendants Not later than 180 days after the date of the enactment of the Molly R. Loomis Research for Descendants of Toxic Exposed Veterans Act of 2025 , the Working Group and the Agency for Toxic Substances and Disease Registry shall\u2014 (1) establish an interagency task force to conduct research on the diagnosis and treatment of health conditions of descendants of toxic-exposed veteran (as defined in section 101 of title 38, United States Code); and (2) maintain a publicly available website with information on the activities and findings of the Agency under paragraph (1), including a review of all relevant data to determine the strength of evidence for a positive association between a health condition researched and a toxic exposure risk activity (as defined in section 1710(e)(4) of title 38, United States Code) based on the categories set forth under section 1173(c)(2) of title 38, United States Code. .",
      "versionDate": "2025-06-12",
      "versionType": "Introduced in Senate"
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
            "name": "Advisory bodies",
            "updateDate": "2025-12-19T17:32:49Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-12-19T17:32:46Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-12-19T17:32:30Z"
          },
          {
            "name": "Hazardous wastes and toxic substances",
            "updateDate": "2025-12-19T17:32:24Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-12-19T17:32:57Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-12-19T17:32:40Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-12-19T17:32:35Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-12-19T17:32:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-01T16:26:28Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2061is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Molly R. Loomis Research for Descendants of Toxic Exposed Veterans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-15T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Molly R. Loomis Research for Descendants of Toxic Exposed Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-25T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Interagency Working Group on Toxic Exposure to conduct research on the diagnosis and treatment of health conditions of descendants of individuals exposed to toxic substances while serving as members of the Armed Forces, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-25T03:03:28Z"
    }
  ]
}
```
