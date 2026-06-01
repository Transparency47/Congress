# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1793?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1793
- Title: COUNTER Act
- Congress: 119
- Bill type: S
- Bill number: 1793
- Origin chamber: Senate
- Introduced date: 2025-05-15
- Update date: 2025-12-05T22:01:40Z
- Update date including text: 2025-12-05T22:01:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in Senate
- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-05-15: Introduced in Senate

## Actions

- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1793",
    "number": "1793",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "COUNTER Act",
    "type": "S",
    "updateDate": "2025-12-05T22:01:40Z",
    "updateDateIncludingText": "2025-12-05T22:01:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-15",
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
        "item": {
          "date": "2025-05-15T19:19:59Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NY"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "IN"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TN"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CT"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "AR"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "AL"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NC"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "WV"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "ME"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "IA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "HI"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "ND"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "WV"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "AZ"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "OK"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "WY"
    },
    {
      "bioguideId": "M000355",
      "firstName": "Mitch",
      "fullName": "Sen. McConnell, Mitch [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "McConnell",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "KY"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "KS"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NE"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NV"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "MO"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "FL"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NH"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "AK"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NC"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "IN"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "OK"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "VA"
    },
    {
      "bioguideId": "J000293",
      "firstName": "Ron",
      "fullName": "Sen. Johnson, Ron [R-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "WI"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MI"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "AZ"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-10-07",
      "state": "OH"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NV"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "CO"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-11-05",
      "state": "ME"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-11-05",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1793is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1793\nIN THE SENATE OF THE UNITED STATES\nMay 15, 2025 Mr. Cotton (for himself, Mrs. Gillibrand , Mr. Banks , Mrs. Blackburn , Mr. Blumenthal , Mr. Boozman , Mrs. Britt , Mr. Budd , Mrs. Capito , Ms. Collins , Mr. Cornyn , Ms. Ernst , Ms. Hirono , Mr. Hoeven , Mr. Justice , Mr. Kelly , Mr. Lankford , Ms. Lummis , Mr. McConnell , Mr. Moran , Mr. Ricketts , Ms. Rosen , Mr. Schmitt , Mr. Scott of Florida , Mrs. Shaheen , Mr. Sullivan , Mr. Tillis , Mr. Young , Mr. Mullin , Mr. Cruz , Mr. Kaine , Mr. Johnson , and Ms. Slotkin ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo protect the United States and assets of the United States from incursions.\n#### 1. Short title\nThis Act may be cited as the Comprehensive Operations for Unmanned-System Neutralization and Threat Elimination Response Act or the COUNTER Act .\n#### 2. Protection of United States assets from incursions\nSection 130i of title 10, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking Notwithstanding and inserting (1) Notwithstanding ;\n**(B)**\nby striking any provision of title 18 and inserting sections 32, 1030, and 1367 and chapters 119 and 206 of title 18 ; and\n**(C)**\nby adding at the end the following new paragraph:\n(2) The Secretary of Defense shall delegate the authority under paragraph (1) to take actions described in subsection (b)(1) to the commander of a unified combatant command, the Secretary concerned, or such other official of the Department of Defense as the Secretary of Defense considers appropriate. ;\n**(2)**\nin subsection (b)(1)(B), by inserting before the period at the end the follow: , including through the use of remote identification broadcast or other means ;\n**(3)**\nin subsection (e)(4)\u2014\n**(A)**\nin subparagraph (B), by striking ; or and inserting a semicolon;\n**(B)**\nby redesignating subparagraph (C) as subparagraph (D); and\n**(C)**\nby inserting after subparagraph (B) the following new subparagraph:\n(C) would support another Federal agency with authority to mitigate the threat of unmanned aircraft systems or unmanned aircraft in mitigating such threats; or ;\n**(4)**\nby redesignating subsections (g), (h), (i), and (j) as subsections (h), (j), (k) and (l), respectively;\n**(5)**\nby inserting after subsection (f) the following new subsection:\n(g) Exemption from disclosure Information pertaining to the technology, procedures, and protocols used to carry out this section, including any regulations or guidance issued to carry out this section, shall be exempt from disclosure under section 552(b)(3) of title 5 and any State or local law requiring the disclosure of information. ;\n**(6)**\nin subsection (h)(1), as so redesignated, in the matter preceding subparagraph (A), by striking March 1, 2018 and inserting January 1, 2026 ;\n**(7)**\nby inserting after subsection (h), as redesignated by paragraph (4), the following new subsection:\n(i) Applicability of other laws to activities related to the mitigation of threats from unmanned aircraft systems or unmanned aircraft Sections 32, 1030, and 1367 and chapters 119 and 206 of title 18, and section 46502 of title 49, may not be construed to apply to activities of the Department of Defense or the Coast Guard, whether under this section or any other provision of law, that\u2014 (1) are conducted outside the United States; and (2) are related to the mitigation of threats from unmanned aircraft systems or unmanned aircraft. ;\n**(8)**\nin subsection (k), as so redesignated\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking subsection (j)(3)(C) and inserting subsection (l)(3)(C) ; and\n**(ii)**\nby striking December 31, 2026 and inserting December 31, 2030 ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking 180 days and inserting one year ; and\n**(ii)**\nby striking November 15, 2026 and inserting November 15, 2030 ; and\n**(9)**\nin subsection (l), as so redesignated\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (B), by inserting the Committee on Homeland Security and Governmental Affairs, after the Committee on the Judiciary, ; and\n**(ii)**\nin subparagraph (C), by inserting the Committee on Homeland Security, after the Committee on the Judiciary, ;\n**(B)**\nby redesignating paragraphs (3) through (6) as paragraphs (4) through (7), respectively;\n**(C)**\nby inserting after paragraph (2) the following new paragraph (3):\n(3) The term unified combatant command has the meaning given that term in section 161 of this title. ; and\n**(D)**\nin paragraph (4), as redesignated by subparagraph (B)\u2014\n**(i)**\nin clause (viii), by striking ; or and inserting a semicolon;\n**(ii)**\nin clause (ix), by striking the period at the end and inserting a semicolon; and\n**(iii)**\nby adding at the end the following new clauses:\n(x) protection of the buildings, grounds, and property to which the public are not permitted regular, unrestricted access and that are under the jurisdiction, custody, or control of the Department of Defense and the persons on that property pursuant to section 2672 of this title; (xi) assistance to Federal, State, or local officials in responding to incidents involving nuclear, radiological, biological, or chemical weapons, high-yield explosives, or related materials or technologies, including pursuant to section 282 of this title or the Robert T. Stafford Disaster Relief and Emergency Assistance Act (42 U.S.C. 5121 et seq); (xii) activities listed in section 2692(b) of this title; or (xiii) emergency response that is limited to a specified timeframe and location. .",
      "versionDate": "2025-05-15",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-05-16",
        "text": "Referred to the Subcommittee on Aviation."
      },
      "number": "3463",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "COUNTER Act",
      "type": "HR"
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
        "updateDate": "2025-06-23T17:22:42Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1793is.xml"
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
      "title": "COUNTER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-06T12:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "COUNTER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Comprehensive Operations for Unmanned-System Neutralization and Threat Elimination Response Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to protect the United States and assets of the United States from incursions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T02:18:25Z"
    }
  ]
}
```
