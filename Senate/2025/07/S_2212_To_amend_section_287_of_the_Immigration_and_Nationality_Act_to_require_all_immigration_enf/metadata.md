# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2212?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2212
- Title: VISIBLE Act
- Congress: 119
- Bill type: S
- Bill number: 2212
- Origin chamber: Senate
- Introduced date: 2025-07-08
- Update date: 2026-01-31T13:48:18Z
- Update date including text: 2026-01-31T13:48:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-08: Introduced in Senate
- 2025-07-08 - IntroReferral: Introduced in Senate
- 2025-07-08 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S4258-4259)
- Latest action: 2025-07-08: Introduced in Senate

## Actions

- 2025-07-08 - IntroReferral: Introduced in Senate
- 2025-07-08 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S4258-4259)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-08",
    "latestAction": {
      "actionDate": "2025-07-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2212",
    "number": "2212",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "VISIBLE Act",
    "type": "S",
    "updateDate": "2026-01-31T13:48:18Z",
    "updateDateIncludingText": "2026-01-31T13:48:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-08",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S4258-4259)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-08",
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
            "date": "2025-07-08T21:24:36Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-08T21:24:36Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "NJ"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "CA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "MD"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "IL"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "CT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "WA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "HI"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "VT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "OR"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "MN"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "MI"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "MI"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "NJ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "MN"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NV"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CT"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "IL"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "DE"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "MA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "MD"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "NM"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "RI"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2212is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2212\nIN THE SENATE OF THE UNITED STATES\nJuly 8, 2025 Mr. Padilla (for himself, Mr. Booker , Mr. Schiff , Mr. Van Hollen , Ms. Duckworth , Mr. Blumenthal , Mrs. Murray , Ms. Hirono , Mr. Welch , Mr. Wyden , Ms. Smith , Ms. Slotkin , Mr. Peters , Mr. Kim , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend section 287 of the Immigration and Nationality Act to require all immigration enforcement officers to display visible identification during public-facing immigration enforcement actions and to promote transparency and accountability.\n#### 1. Short titles\nThis Act may be cited as the Visible Identification Standards for Immigration-Based Law Enforcement Act of 2025 or the VISIBLE Act .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\ntransparency and accountability in public immigration enforcement are essential to maintaining public trust and upholding constitutional governance; and\n**(2)**\nimmigration enforcement officers should be visibly identifiable during any civil immigration enforcement activity at which members of the public may be directly engaged or present, including actions involving civil and criminal authority, unless the activity is truly covert and not observable by the public.\n#### 3. Requirement for visible identification during immigration enforcement\nSection 287 of the Immigration and Nationality Act ( 8 U.S.C. 1357 ) is amended by adding at the end the following:\n(i) (1) In this subsection: (A) The term covered immigration officer means any individual who is\u2014 (i) authorized to perform immigration enforcement functions; and (ii) (I) an officer or employee of U.S. Customs and Border Protection; (II) an officer or employee of U.S. Immigration and Customs Enforcement; or (III) an individual authorized, deputized, or designated under Federal law, regulation, or agreement to perform immigration enforcement functions, including pursuant to section 287(g) or any other delegation or agreement with the Department of Homeland Security. (B) The term public immigration enforcement function \u2014 (i) means any activity that involves the direct exercise of Federal immigration authority through public-facing actions, including a patrol, a stop, an arrest, a search, an interview to determine immigration status, a raid, a checkpoint inspection, or the service of a judicial or administrative warrant; and (ii) does not include covert, non-public operations or non-enforcement activities. (C) The term visible identification means a display of an immigration officer\u2019s agency and name or badge number in a size and format that complies with the requirements under paragraph (3). (2) Each covered immigration officer who directly engages in a public immigration enforcement function within the United States shall, at all times during such engagement, wear visible identification, which shall include\u2014 (A) the full name or widely recognized initials of the officer\u2019s employing agency; and (B) (i) the officer\u2019s last name; or (ii) the officer\u2019s unique badge or identification number. (3) The identifying information described in this paragraph shall be\u2014 (A) for the immigration officer\u2019s agency, displayed in a size and format that is clearly legible from a distance of not less than 25 feet, using materials or markings suitable for visibility in both daylight and low-light conditions, under normal operation conditions; (B) for the officer\u2019s name or badge number, displayed in a manner that is clearly visible and readable during direct engagement with the public; and (C) displayed on the outermost garment or gear and not obscured by tactical equipment, body armor, or accessories. (4) Covered immigration officers may not wear non-medical face coverings, including masks or balaclavas, that impair the visibility of the identifying information required under this subsection or obscure the officer\u2019s face unless such face coverings are operationally necessary\u2014 (A) to protect the integrity of a covert, non-public operation; or (B) to guard against hazardous environmental conditions. .\n#### 4. Compliance and reporting\n##### (a) Internal accountability\nThe Secretary of Homeland Security shall ensure that any covered immigration officer who fails to comply with the requirements under section 287(i) of the Immigration and Nationality Act, as added by section 3, receive appropriate administrative discipline, including written reprimand, suspension, or other personnel actions, consistent with agency policy and any applicable collective bargaining agreement.\n##### (b) Annual report to Congress\nNot later than one year after the date of the enactment of this Act, and annually thereafter, the Secretary of Homeland Security shall submit a report to the Office for Civil Rights and Civil Liberties of the Department of Homeland Security, the Committee on the Judiciary of the Senate , the Committee on Homeland Security and Governmental Affairs of the Senate , the Committee on the Judiciary of the House of Representatives , and the Committee on Homeland Security of the House of Representatives that includes\u2014\n**(1)**\nthe total number of public immigration enforcement functions conducted during the reporting period;\n**(2)**\nthe number of documented instances of noncompliance with section 287(i) of the Immigration and Nationality Act, as added by section 3; and\n**(3)**\na summary of disciplinary or remedial actions taken against those responsible for such instances of noncompliance.\n#### 5. Role of the Office for Civil Rights and Civil Liberties\nThe Office for Civil Rights and Civil Liberties of the Department of Homeland Security shall\u2014\n**(1)**\nreceive and investigate complaints from the public concerning violations of section 287(i) of the Immigration and Nationality Act, as added by section 3;\n**(2)**\nissue recommendations to relevant Department of Homeland Security components concerning compliance and corrective actions that should be taken;\n**(3)**\ninclude findings and actions taken pursuant to this Act, including information contained in the report received pursuant to section 4(b), in its annual public report submitted pursuant to section 705(b) of the Homeland Security Act of 2002 ( 6 U.S.C. 345(b) ); and\n**(4)**\ncarry out the responsibilities under this section in accordance with its statutory authorities, which may include coordination with the Office of Inspector General of the Department, as appropriate.",
      "versionDate": "2025-07-08",
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
        "actionDate": "2025-07-23",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4667",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "VISIBLE Act",
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
        "name": "Immigration",
        "updateDate": "2025-07-31T12:20:25Z"
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
      "date": "2025-07-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2212is.xml"
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
      "title": "VISIBLE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-31T13:48:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "VISIBLE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-23T02:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Visible Identification Standards for Immigration-Based Law Enforcement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-23T02:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 287 of the Immigration and Nationality Act to require all immigration enforcement officers to display visible identification during public-facing immigration enforcement actions and to promote transparency and accountability.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-23T02:03:33Z"
    }
  ]
}
```
