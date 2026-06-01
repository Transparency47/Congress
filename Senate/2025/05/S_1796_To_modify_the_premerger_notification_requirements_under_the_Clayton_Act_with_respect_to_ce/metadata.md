# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1796?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1796
- Title: HART Act
- Congress: 119
- Bill type: S
- Bill number: 1796
- Origin chamber: Senate
- Introduced date: 2025-05-15
- Update date: 2025-11-19T12:03:17Z
- Update date including text: 2025-11-19T12:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in Senate
- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-05-15: Introduced in Senate

## Actions

- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1796",
    "number": "1796",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "HART Act",
    "type": "S",
    "updateDate": "2025-11-19T12:03:17Z",
    "updateDateIncludingText": "2025-11-19T12:03:17Z"
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
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
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
          "date": "2025-05-15T19:34:04Z",
          "name": "Referred To"
        }
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MN"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "OR"
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "OR"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-05-15",
      "state": "VT"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "CT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1796is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1796\nIN THE SENATE OF THE UNITED STATES\nMay 15, 2025 Ms. Klobuchar (for herself, Ms. Warren , Ms. Smith , Mr. Wyden , Ms. Hirono , Mr. Merkley , and Mr. Sanders ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo modify the premerger notification requirements under the Clayton Act with respect to certain acquisitions of residential property, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Acquisitions Review and Transparency Act or the HART Act .\n#### 2. Definitions\nIn this Act:\n**(1) Residential property**\nThe term residential property \u2014\n**(A)**\nmeans property that is zoned or intended to be used as a dwelling for individuals or households, including multifamily housing, condominiums, manufactured homes, or single-family homes; and\n**(B)**\ndoes not include any place of short-term lodging.\n**(2) Investment rental property**\nThe term investment rental property means real property that\u2014\n**(A)**\nwill not be rented to an entity, including any entity of the acquiring person, except for the sole purpose of maintaining, managing, or supervising the operation of the real property; and\n**(B)**\nwill be held solely for rental or investment purposes.\n**(3) Place of short-term lodging**\nThe term place of short-term lodging means a hotel, motel, inn, short-term rental, or other place of lodging that advertises at a price that is a nightly, hourly, or weekly rate.\n#### 3. Housing transactions reportable\n##### (a) Single acquisition\nSection 7A(a) of the Clayton Act ( 15 U.S.C. 18a(a) ) is amended by adding at the end the following: For purposes of this subsection, all acquisitions of residential property (as defined in section 2 of the HART Act ) by any person within a single calendar year shall be deemed to be a single acquisition and notification pursuant to this subsection shall be filed by the acquiring person upon acquiring the property that brings such single acquisition within any requirement described in paragraph (2) when aggregated with all other prior acquisitions of residential property by the person in that calendar year.\n##### (b) Exemption\nSection 7A(c)(1) of the Clayton Act ( 15 U.S.C. 18a(c)(1) ) is amended by inserting , unless the transaction includes residential property or investment rental property (as defined in section 2 of the HART Act ), including in the form of a real estate investment trust, that is not solely intended for the personal use of an individual.\n##### (c) Code of Federal Regulations\nThe Federal Trade Commission, with the concurrence of the Assistant Attorney General in charge of the Antitrust Division of the Department of Justice and by rule, in accordance with section 553 of title 5, United States Code, shall amend part 802 of title 16, Code of Federal Regulations to conform with the amendments to section 7A(a) of the Clayton Act ( 15 U.S.C. 18(a) ) made by this Act.\n##### (d) Rulemaking\nThe Federal Trade Commission, with the concurrence of the Assistant Attorney General in charge of the Antitrust Division of the Department of Justice and by rule, in accordance with section 553 of title 5, United States Code, shall issue rules relating to the form and documentary material and information relevant to any acquisition or aggregated acquisitions of residential property is necessary and appropriate under section 7A(a) of the Clayton Act ( 15 U.S.C. 18a(a) ), as amended by subsection (a), to enable the Federal Trade Commission and the Assistant Attorney General to determine whether such acquisition or aggregated acquisitions may violate the antitrust laws, as defined in subsection (a) of the first section of the Clayton Act ( 15 U.S.C. 12 ).",
      "versionDate": "2025-05-15",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-05-29T15:47:34Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1796is.xml"
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
      "title": "HART Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HART Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-29T01:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Housing Acquisitions Review and Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-29T01:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to modify the premerger notification requirements under the Clayton Act with respect to certain acquisitions of residential property, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-29T01:03:33Z"
    }
  ]
}
```
