# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5704?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5704
- Title: Repeal the Smith-Mundt Modernization Act of 2013
- Congress: 119
- Bill type: HR
- Bill number: 5704
- Origin chamber: House
- Introduced date: 2025-10-08
- Update date: 2026-05-22T08:08:40Z
- Update date including text: 2026-05-22T08:08:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-08: Introduced in House
- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-10-08: Introduced in House

## Actions

- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-08",
    "latestAction": {
      "actionDate": "2025-10-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5704",
    "number": "5704",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001184",
        "district": "4",
        "firstName": "Thomas",
        "fullName": "Rep. Massie, Thomas [R-KY-4]",
        "lastName": "Massie",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Repeal the Smith-Mundt Modernization Act of 2013",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:40Z",
    "updateDateIncludingText": "2026-05-22T08:08:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-08",
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
      "actionDate": "2025-10-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-08",
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
          "date": "2025-10-08T19:02:15Z",
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
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "PA"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "GA"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "MO"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "NC"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "TX"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "AZ"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "WI"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "FL"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "AZ"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5704ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5704\nIN THE HOUSE OF REPRESENTATIVES\nOctober 8, 2025 Mr. Massie (for himself and Mr. Perry ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo repeal the Smith-Mundt Modernization Act of 2013 and to prohibit domestic propagandization by the Federal Government.\n#### 1. Short title\nThis Act may be cited as the Repeal the Smith-Mundt Modernization Act of 2013 .\n#### 2. Repeal smith-mundt domestic propagandization\n##### (a) United states information and educational exchange act of 1948\nSection 501 of the United States Information and Educational Exchange Act of 1948 ( 22 U.S.C. 1461 ) is amended to read as follows:\n501. General authorization (a) Dissemination of information abroad The Secretary of State and the Chief Executive Officer of the United States Agency for Global Media (USAGM) are authorized to provide for the preparation and dissemination abroad of information about the United States, its people, and its policies, through press, publications, radio, motion pictures, the internet, and other information media, and through information centers and instructors abroad, except that such dissemination may not include the use of social media accounts, websites, or podcasts other than official platforms maintained by the Department of State or USAGM for purposes of foreign dissemination. (b) Ability To review information domestically (1) Any materials produced under subsection (a) shall, upon request, be made available in the English language, at all reasonable times following their release abroad, for examination at the Department of State or the United States Agency for Global Media, as appropriate, by representatives of United States press associations, newspapers, magazines, radio systems, and stations, and by Members of Congress. Except as provided in subsection (c), such materials may not be disseminated within the United States, except that Members of Congress may use such materials in the exercise of their official oversight functions. (2) No funds authorized to be appropriated to the Department of State or the United States Agency for Global Media, or its component networks, shall be used for the purpose of influencing public opinion or propagandizing in the United States. (c) Archival of records (1) In general The Secretary of State and the Chief Executive Officer of the United States Agency for Global Media shall make available to the Archivist of the United States any materials produced under subsection (a). Such materials shall be maintained by the Archivist and made accessible to the public only for examination in a format that permits viewing but not reproduction or redistribution\u2014 (A) beginning on the date that is 20 years after the date on which such material was initially disseminated abroad; or (B) in the case of material that was prepared but never disseminated abroad, beginning on the date that is 20 years after the date on which such material was prepared. (2) Restriction on domestic dissemination Any materials produced under subsection (a)\u2014 (A) may not be distributed domestically by the Archivist before the expiration of the 20-year period described in paragraph (1); and (B) any materials made accessible by the Archivist after such period, shall bear a clear and permanent identifier, watermark, or disclaimer indicating\u2014 (i) the United States Government entity responsible for its production; (ii) the foreign country or region for which the material was originally prepared or disseminated; and (iii) the purpose or program under which the material was produced, if applicable. (3) Responsibilities of the archivist The Archivist\u2014 (A) shall be the official custodian of the material described in paragraph (1); (B) shall promulgate regulations to\u2014 (i) facilitate public examination of such materials in accordance with paragraph (1); and (ii) govern the release of such materials in accordance with paragraph (2), including requirements that any person seeking such release\u2014 (I) has secured all necessary United States rights and licenses; and (II) has paid a fee, in accordance with section 2116(c) of title 44, United States Code, sufficient to cover the costs incurred by the Archivist in providing such materials; and (C) shall ensure that all fees collected under subparagraph (B)(ii)(II) are deposited into, administered, and expended as part of the National Archives Trust Fund. (d) Rule of construction Nothing in this section may be construed to require the Secretary of State or the Chief Executive Officer of the United States Agency for Global Media to make material disseminated abroad available in any format other than in the format disseminated abroad. .\n##### (b) Foreign relations authorizations act, fiscal years 1986 and 1987\n**(1) In general**\nSection 208 of the Foreign Relations Authorization Act, Fiscal Years 1986 and 1987 ( 22 U.S.C. 1461\u20131a ) is amended to read as follows:\n208. Ban on domestic distribution of program material (a) In general (1) Use of funds No funds authorized to be appropriated to the Department of State or the United States Agency for Global Media (USAGM), or any of its component networks, may be used to influence public opinion in the United States. (2) Restriction on domestic distribution No program material prepared by USAGM may be distributed in the United States, except as provided in section 501 of the United States Information and Educational Exchange Act of 1948 ( 22 U.S.C. 1461 ). (3) Transparency exception Nothing in this subsection shall be construed to prohibit or delay the Department of State or USAGM from providing factual information about their operations, policies, or programs, or from making such information available to members of the media, the public, or Congress, in accordance with other applicable law. (b) Rules of construction Nothing in this section may be construed\u2014 (1) to apply to programs carried out pursuant to the Mutual Educational and Cultural Exchange Act of 1961 ( 22 U.S.C. 2451 et seq. ); or (2) to prohibit any employee of USAGM from responding to inquiries from members of the public about USAGM operations, policies, or programs. .\n**(2) Clerical amendment**\nThe table of contents for the Foreign Relations Authorization Act, Fiscal Years 1986 and 1987 ( 22 U.S.C. 1461\u20131a ) is amended by striking the item relating to section 208 and inserting the following:\nSec. 208 Ban on domestic distribution of program material. .",
      "versionDate": "2025-10-08",
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
        "updateDate": "2025-12-10T21:29:37Z"
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
      "date": "2025-10-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5704ih.xml"
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
      "title": "Repeal the Smith-Mundt Modernization Act of 2013",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Repeal the Smith-Mundt Modernization Act of 2013",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To repeal the Smith-Mundt Modernization Act of 2013 and to prohibit domestic propagandization by the Federal Government.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:18:22Z"
    }
  ]
}
```
