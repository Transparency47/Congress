# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3470?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3470
- Title: Accountability for Federal Law Enforcement Act
- Congress: 119
- Bill type: S
- Bill number: 3470
- Origin chamber: Senate
- Introduced date: 2025-12-15
- Update date: 2026-04-21T11:03:28Z
- Update date including text: 2026-04-21T11:03:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-15: Introduced in Senate
- 2025-12-15 - IntroReferral: Introduced in Senate
- 2025-12-15 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S8731-8732)
- Latest action: 2025-12-15: Introduced in Senate

## Actions

- 2025-12-15 - IntroReferral: Introduced in Senate
- 2025-12-15 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S8731-8732)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-15",
    "latestAction": {
      "actionDate": "2025-12-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3470",
    "number": "3470",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
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
    "title": "Accountability for Federal Law Enforcement Act",
    "type": "S",
    "updateDate": "2026-04-21T11:03:28Z",
    "updateDateIncludingText": "2026-04-21T11:03:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S8731-8732)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-15",
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
            "date": "2025-12-15T21:21:18Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-15T21:21:18Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NJ"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "RI"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "MA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "OR"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-12-15",
      "state": "VT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "OR"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "IL"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "NJ"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "IL"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3470is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3470\nIN THE SENATE OF THE UNITED STATES\nDecember 15, 2025 Mr. Padilla (for himself, Mr. Blumenthal , Mr. Booker , Mr. Whitehouse , Mr. Markey , Mr. Wyden , Mr. Sanders , and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Revised Statutes of the United States to hold certain public employers liable in civil actions for deprivation of rights, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Accountability for Federal Law Enforcement Act .\n#### 2. Civil action for deprivation of rights\nSection 1979 of the Revised Statutes of the United States ( 42 U.S.C. 1983 ) is amended\u2014\n**(1)**\nby striking Every and inserting the following:\n(a) In this section, the term public employer means a Federal law enforcement agency that, at the time of a deprivation of any rights, privileges, or immunities described in section (b), employs, or contracts with an individual to perform the duties of, a Federal law enforcement officer or any other officer empowered by law to execute searches, to seize evidence, or to make arrests. (b) Every ;\n**(2)**\nin subsection (b), as so designated, by inserting the United States or before any State ; and\n**(3)**\nby adding at the end the following:\n(c) If, while acting under color of law, any officer who is empowered by law to execute searches, to seize evidence, or to make arrests subjects or causes to be subjected any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, the public employer of that officer shall be liable to the party injured for the conduct of the officer in an action at law, suit in equity, or other proper proceeding for redress, regardless of whether a policy or custom of the public employer caused the violation, and regardless of whether the officer has any defense or immunity from suit or liability. This paragraph shall constitute a waiver of sovereign immunity of the United States with respect to Federal law enforcement agencies for any claim brought under this section. Nothing in this paragraph shall be construed to limit or preclude any legal, equitable, or other remedy that is available, under this section or under any other source of law, against an individual officer. .",
      "versionDate": "2025-12-15",
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2026-01-08T17:21:46Z"
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
      "date": "2025-12-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3470is.xml"
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
      "title": "Accountability for Federal Law Enforcement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T11:03:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Accountability for Federal Law Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:39:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Revised Statutes of the United States to hold certain public employers liable in civil actions for deprivation of rights, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:33:33Z"
    }
  ]
}
```
