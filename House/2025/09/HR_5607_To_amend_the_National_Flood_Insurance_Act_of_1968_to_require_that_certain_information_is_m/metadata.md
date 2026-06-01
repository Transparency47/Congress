# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5607?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5607
- Title: Flood Insurance Transparency Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5607
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2025-12-18T23:27:48Z
- Update date including text: 2025-12-18T23:27:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5607",
    "number": "5607",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Flood Insurance Transparency Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-18T23:27:48Z",
    "updateDateIncludingText": "2025-12-18T23:27:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:05:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "FL"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5607ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5607\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Steube (for himself and Mr. Patronis ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the National Flood Insurance Act of 1968 to require that certain information is made publicly available, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Flood Insurance Transparency Act of 2025 .\n#### 2. Public availability of program information\nPart C of chapter II of the National Flood Insurance Act of 1968 ( 42 U.S.C. 4081 et seq. ) is amended by adding at the end the following:\n1349. Public availability of program information (a) Definitions In this section\u2014 (1) the term loss ratio means, with respect to the national flood insurance program in a fiscal year, the ratio of the amount of claims paid under that program during that fiscal year to the amount of premiums paid under that program during that fiscal year; and (2) the term multiple-loss property means\u2014 (A) a repetitive loss structure; or (B) a severe repetitive loss structure, as that term is defined in section 1366(h). (b) Flood risk information (1) In general To facilitate the national flood insurance program becoming a source of information and data for research and development of technology that better understands flooding, the risk of flooding, and the predictability of the perils of flooding, the Administrator shall make publicly available all data, models, assessments, analytical tools, and other information in the possession of the Administrator relating to that program under this title that is used in assessing flood risk or identifying and establishing flood elevations and premiums, including\u2014 (A) data relating to risk on individual properties, loss ratio information, and other information identifying losses under that program; (B) current and historical policy information, limited to the amount and term only, for properties covered by flood insurance under the national flood insurance program (as of the date on which the information is made available) and for properties that are no longer covered by flood insurance under the national flood insurance program (as of the date on which the information is made available); (C) current and historical claims information, limited to the date and amount paid only, for properties covered by flood insurance under the national flood insurance program (as of the date on which the information is made available) and for properties that are no longer covered by flood insurance under the national flood insurance program (as of the date on which the information is made available); (D) identification of whether a property was constructed before or after the effective date of the first flood insurance rate map for the community in which that property is located; (E) identification of properties that have been mitigated through elevation, a buyout, or any other mitigation action; and (F) identification of multiple-loss properties with respect to which mitigation measures have not been undertaken. (2) Open source data system In carrying out paragraph (1), the Administrator shall establish an open source data system by which all information required to be made publicly available by that paragraph may be accessed by the public on an immediate basis by electronic means. (c) Community information Not later than 1 year after the date of enactment of this section, the Administrator shall establish and maintain a publicly searchable database that provides information about each community participating in the national flood insurance program, which shall include the following information: (1) The status of the compliance by that community with the requirements of that program, including any findings of noncompliance, the status of any enforcement actions initiated by a State or by the Administrator, and the number of days of any such continuing noncompliance. (2) The number of properties located in areas having special flood hazards in the community that were built before the effective date of the first flood insurance rate map for the community. (3) The number of properties located in areas having special flood hazards in the community that were built after the effective date of the first flood insurance rate map for the community. (4) The total number of current and historical claims located outside areas having special flood hazards in the community. (5) The total number of multiple-loss properties in the community. (6) The portion of the community, stated as a percentage and in terms of square miles, that is located within areas having special flood hazards. (d) Identification of properties The information provided pursuant to subsections (b) and (c) shall\u2014 (1) be based on data that identifies properties at the ZIP Code or census block level; and (2) with respect to a property, include the name of the community and State in which the property is located. (e) Protection of personally identifiable information The information provided pursuant to subsections (b) and (c) shall be disclosed in a format that does not reveal individually identifiable information about property owners in accordance with section 552a of title 5, United States Code. .",
      "versionDate": "2025-09-26",
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
        "actionDate": "2025-06-12",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2052",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Flood Insurance Transparency Act of 2025",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-11-18T18:14:13Z"
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
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5607ih.xml"
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
      "title": "Flood Insurance Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T07:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Flood Insurance Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T07:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Flood Insurance Act of 1968 to require that certain information is made publicly available, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T07:33:37Z"
    }
  ]
}
```
