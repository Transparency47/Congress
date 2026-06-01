# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2042?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2042
- Title: Space National Guard Establishment Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2042
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2026-01-10T06:48:25Z
- Update date including text: 2026-01-10T06:48:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-03-11: Introduced in House

## Actions

- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2042",
    "number": "2042",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001121",
        "district": "6",
        "firstName": "Jason",
        "fullName": "Rep. Crow, Jason [D-CO-6]",
        "lastName": "Crow",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Space National Guard Establishment Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-10T06:48:25Z",
    "updateDateIncludingText": "2026-01-10T06:48:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T14:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "CO"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "FL"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "CO"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "NY"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "HI"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "OH"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CO"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "CO"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "CO"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "CO"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "CO"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "SC"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "OH"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "HI"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "CA"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "OH"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2042ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2042\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Mr. Crow (for himself and Ms. Boebert ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo establish the Space National Guard.\n#### 1. Short title\nThis Act may be cited as the Space National Guard Establishment Act of 2025 .\n#### 2. Establishment of Space National Guard\n##### (a) Establishment\n**(1) In general**\nThere is established a Space National Guard that is part of the organized militia of the States specified in paragraph (3), active and inactive, that\u2014\n**(A)**\nis a space force;\n**(B)**\nis trained, and has its officers appointed, under the sixteenth clause of section 8, article I of the Constitution;\n**(C)**\nis organized, armed, and equipped wholly or partly at Federal expense; and\n**(D)**\nis federally recognized.\n**(2) Reserve component**\nThe Space National Guard shall be the reserve component of the Space Force all of whose members are members of the Space National Guard.\n**(3) States specified**\nThe States specified in this paragraph are:\n**(A)**\nAlaska.\n**(B)**\nCalifornia.\n**(C)**\nColorado.\n**(D)**\nFlorida.\n**(E)**\nHawaii.\n**(F)**\nNew York.\n**(G)**\nOhio.\n##### (b) Composition\n**(1) Director of the Space National Guard**\n**(A) In general**\nThe Director of Space Operations for the National Guard Bureau shall be transferred to the Space National Guard and be known as the Director of the Space National Guard.\n**(B) Rank**\nThe Director of the Space National Guard shall carry the rank of Brigadier General and shall report to the Director of the Air National Guard.\n**(2) Transfer of space operations**\n**(A) In general**\nThe staff assigned to space operations in the National Guard Bureau, and the units specified in subparagraph (B), shall be transferred to the Space National Guard.\n**(B) Units specified**\nThe units specified in this subparagraph are the following:\n**(i)**\n213th Space Warning Squadron, Alaska Air National Guard.\n**(ii)**\n148th Space Operations Squadron, California Air National Guard.\n**(iii)**\n216th Electromagnetic Warfare Squadron, California Air National Guard.\n**(iv)**\n234th Intelligence Squadron, California Air National Guard.\n**(v)**\n137th Space Warning Squadron, Colorado Air National Guard.\n**(vi)**\n138th Electromagnetic Warfare Squadron, Colorado Air National Guard.\n**(vii)**\n233d Space Group, Colorado Air National Guard.\n**(viii)**\n233d Space Communications Squadron, Colorado Air National Guard.\n**(ix)**\n233d Space Group, Det-1 (Combat Training Detachment) Colorado Air National Guard.\n**(x)**\n114th Electromagnetic Warfare Squadron, Florida Air National Guard.\n**(xi)**\n150th Electromagnetic Warfare Squadron, Hawaii Air National Guard.\n**(xii)**\n109th Electromagnetic Warfare Squadron, Hawaii Air National Guard.\n**(xiii)**\n126th Intelligence Squadron, Ohio Air National Guard.\n**(xiv)**\n222nd Command and Control Squadron, New York Air National Guard.\n**(3) Prohibition on additional personnel**\n**(A) In general**\nThere shall be no personnel assigned or allocated to the Space National Guard other than the personnel provided for by paragraphs (1) and (2).\n**(B) Assistant Adjutant General**\nEach Space National Guard unit shall be organized under the Assistant Adjutant General for the Air Force in the State in which the unit is located on the day before the enactment of this Act.\n**(C) Effect on States**\nExcept as provided in paragraphs (1) and (2), no State shall receive any additional personnel, to include any general officer or staff, to assist with the administration and operation of the Space National Guard\n#### 3. No effect on military facilities, infrastructure, and installations\n##### (a) In general\nThe Space National Guard shall make use of the facilities, infrastructure, and installations being for space operations by the Air National Guard on the day before the date of the enactment of this Act.\n##### (b) Prohibition on new construction\nExcept as provided by subsection (a), no additional facility, infrastructure, or installation shall be constructed or modified to accommodate the Space National Guard.\n#### 4. Implementation of Space National Guard\n##### (a) Requirement\nExcept as specifically provided by this Act, the Secretary of the Air Force and the Chief of the National Guard Bureau shall implement this Act and the amendments made by this Act not later than one year after the date of the enactment of this Act.\n##### (b) Briefing required\n**(1) In general**\nNot later than 90 days after the date of the enactment of this Act, and annually thereafter for 5 years, the Secretary of the Air Force, the Chief of the Space Force, and the Chief of the National Guard Bureau shall jointly provide to the congressional defense committees (as defined in section 101 of title 10, United States Code) a briefing on the status of the implementation of the Space National Guard pursuant to this Act and the amendments made by this Act.\n**(2) Elements**\nThe briefing required by paragraph (1) shall address\u2014\n**(A)**\nthe current missions, operations and activities, personnel requirements and status, and budget and funding requirements and status of the Space National Guard; and\n**(B)**\nsuch other matters with respect to the implementation and operation of the Space National Guard as the Secretary and the Chiefs jointly determine appropriate to keep Congress fully and currently informed on the status of the implementation of the Space National Guard.\n#### 5. Conforming amendments and clarification of authorities\n##### (a) Definitions\n**(1) Title 10, United States Code**\nTitle 10, United States Code, is amended\u2014\n**(A)**\nin section 101\u2014\n**(i)**\nin subsection (c)\u2014\n**(I)**\nin paragraph (1), by striking and the Air National Guard and inserting , the Air National Guard, and the Space National Guard ;\n**(II)**\nby redesignating paragraphs (6) and (7) as paragraphs (8) and (9), respectively; and\n**(III)**\nby inserting after paragraph (5) the following new paragraphs:\n(6) The term Space National Guard means that part of the organized militia of the States specified in section 2(a)(3) of the Space National Guard Establishment Act of 2025 , active and inactive, that\u2014 (A) is a space force; (B) is trained, and has its officers appointed under the sixteenth clause of section 8, article I of the Constitution; (C) is organized, armed, and equipped wholly or partly at Federal expense; and (D) is federally recognized. (7) The term Space National Guard of the United States means the reserve component of the Space Force all of whose members are members of the Space National Guard. ; and\n**(ii)**\nin subsection (d)\u2014\n**(I)**\nin paragraph (4), by striking or inactive Air National Guard and inserting , in the inactive Air National Guard, in the inactive Space National Guard, ; and\n**(II)**\nin paragraph (5), by striking or the Air National Guard of the United States and inserting , the Air National Guard of the United States, or the Space National Guard of the United States ; and\n**(B)**\nin section 10101\u2014\n**(i)**\nin the matter preceding paragraph (1), by inserting the following before the colon; and\n**(ii)**\nby adding at the end the following new paragraph:\n(8) The Space National Guard of the United States. .\n**(2) Title 32, United States Code**\nSection 101 of title 32, United States Code is amended\u2014\n**(A)**\nin paragraph (1), by striking and the Air National Guard and inserting the Air National Guard of the United States, and the Space National Guard ;\n**(B)**\nin paragraph (3), by striking and the Air National Guard and inserting , the Air National Guard, and the Space National Guard ;\n**(C)**\nby redesignating paragraphs (8) through (19) as paragraphs (10) through (21), respectively;\n**(D)**\nby inserting after paragraph (7) the following new paragraphs:\n(8) The term Space National Guard means that part of the organized militia of the States specified in section 2(a)(3) of the Space National Guard Establishment Act of 2025 , active and inactive, that\u2014 (A) is a space force; (B) is trained, and has its officers appointed under the sixteenth clause of section 8, article I of the Constitution; (C) is organized, armed, and equipped wholly or partly at Federal expense; and (D) is federally recognized. (9) The term Space National Guard of the United States means the reserve component of the Space Force all of whose members are members of the Space National Guard. ; and\n**(E)**\nin paragraph (21), as redesignated by subparagraph (C), by striking or the Air National Guard of the United States and inserting , the Air National Guard of the United States, or the Space National Guard of the United States .\n##### (b) Reserve components\nChapter 1003 of title 10, United States Code, is amended\u2014\n**(1)**\nby adding at the end the following new sections:\n10115. Space National Guard of the United States: composition The Space National Guard of the United States is the reserve component of the Space Force that consists of\u2014 (1) federally recognized units and organizations of the Space National Guard; and (2) members of the Space National Guard who are also Reserves of the Space Force. 10116. Space National Guard: when a component of the Space Force The Space National Guard while in the service of the United States is a component of the Space Force. 10117. Space National Guard of the United States: status when not in Federal service When not on active duty, members of the Space National Guard of the United States shall be administered, armed, equipped, and trained in their status as members of the Space National Guard. ; and\n**(2)**\nin the table of sections at the beginning of such chapter, by adding at the end the following new items:\n10115. Space National Guard of the United States: composition. 10116. Space National Guard: when a component of the Space Force. 10117. Space National Guard of the United States: status when not in Federal service. .",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-03-11",
        "text": "Read twice and referred to the Committee on Armed Services."
      },
      "number": "963",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Space National Guard Establishment Act of 2025",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-20T02:45:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr2042",
          "measure-number": "2042",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-11",
          "originChamber": "HOUSE",
          "update-date": "2025-09-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2042v00",
            "update-date": "2025-09-03"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Space National Guard Establishment Act of 2025</strong></p><p>This bill establishes a Space National Guard as the reserve component of the U.S. Space Force, specifically in Alaska, California, Colorado, Florida, Hawaii, New York, and Ohio. The Space National Guard\u00a0consists of specified units of the Air National Guard and must use existing facilities, infrastructure, and installations.</p>"
        },
        "title": "Space National Guard Establishment Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2042.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Space National Guard Establishment Act of 2025</strong></p><p>This bill establishes a Space National Guard as the reserve component of the U.S. Space Force, specifically in Alaska, California, Colorado, Florida, Hawaii, New York, and Ohio. The Space National Guard\u00a0consists of specified units of the Air National Guard and must use existing facilities, infrastructure, and installations.</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119hr2042"
    },
    "title": "Space National Guard Establishment Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Space National Guard Establishment Act of 2025</strong></p><p>This bill establishes a Space National Guard as the reserve component of the U.S. Space Force, specifically in Alaska, California, Colorado, Florida, Hawaii, New York, and Ohio. The Space National Guard\u00a0consists of specified units of the Air National Guard and must use existing facilities, infrastructure, and installations.</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119hr2042"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2042ih.xml"
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
      "title": "Space National Guard Establishment Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Space National Guard Establishment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Space National Guard.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:47Z"
    }
  ]
}
```
