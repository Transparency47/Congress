# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2775?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2775
- Title: Measuring the Cost of Disasters Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2775
- Origin chamber: Senate
- Introduced date: 2025-09-11
- Update date: 2025-12-09T22:33:15Z
- Update date including text: 2025-12-09T22:33:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in Senate
- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-09-11: Introduced in Senate

## Actions

- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2775",
    "number": "2775",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "Measuring the Cost of Disasters Act of 2025",
    "type": "S",
    "updateDate": "2025-12-09T22:33:15Z",
    "updateDateIncludingText": "2025-12-09T22:33:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T16:49:23Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "MA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "MD"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "MD"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "OR"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "CT"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "RI"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "RI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "CO"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "NJ"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "MN"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-09-11",
      "state": "VT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "OR"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2775is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2775\nIN THE SENATE OF THE UNITED STATES\nSeptember 11, 2025 Mr. Welch (for himself, Mr. Markey , Mr. Van Hollen , Ms. Alsobrooks , Mr. Merkley , Mr. Blumenthal , Mr. Reed , Mr. Whitehouse , Mr. Bennet , Mr. Booker , Ms. Smith , Mr. Sanders , Mr. Wyden , and Mr. Heinrich ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Administrator of the National Oceanic and Atmospheric Administration to establish and maintain a database and webpage that is available to the public and contains information on the billion-dollar disasters that occur each year in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Measuring the Cost of Disasters Act of 2025 .\n#### 2. Database and webpage for information on billion-dollar disasters\n##### (a) In general\nThe Administrator of the National Oceanic and Atmospheric Administration (in this section referred to as the Administrator ) shall establish and maintain a database and webpage that is available to the public and contains information on each billion-dollar disaster that occurs each year in the United States.\n##### (b) Update\nNot less frequently than biannually, the Administrator shall update the database and webpage required under subsection (a) as new information is available.\n##### (c) Matters To Be included\nThe database and webpage required under subsection (a) shall include the following:\n**(1)**\nWith respect to each billion-dollar disaster included in the database and webpage\u2014\n**(A)**\nthe estimated cost of the disaster;\n**(B)**\nthe type of disaster;\n**(C)**\nthe location of the disaster;\n**(D)**\nthe date or dates of the disaster; and\n**(E)**\nsuch other information regarding the disaster as the Administrator considers appropriate.\n**(2)**\nVisual graphs and mapping features showing the trajectory of disasters over time and the distribution of types of disasters across the United States that are similar, if not identical, to those features produced by the National Centers for Environmental Information from 1980 through 2024 and that were available and updated online at www.ncei.noaa.gov/access/billions/ until May 9, 2025.\n##### (d) Data To Be used\nIn establishing and maintaining the database required under subsection (a), the Administrator shall use data available to the Administrator and may collaborate with Federal and non-Federal partners as necessary, such as those partners with which the Administrator collaborated previously while the database specified under subsection (c)(2) was active from 1980 through 2024.\n##### (e) Inclusion of other disasters\nThe Administrator may include in the database required under subsection (a) a disaster that is not a billion-dollar disaster if the Administrator determines that the inclusion of the disaster in the database would be appropriate.\n##### (f) Maintenance of existing database\nThe Administrator shall maintain and update information contained in the previously existing disaster database specified under subsection (c)(2) on the webpage for the National Centers for Environmental Information for archiving and research purposes.\n##### (g) Billion-Dollar disaster defined\nIn this section, the term billion-dollar disaster means a storm or severe weather event that results in $1,000,000,000 or more in combined direct costs and market costs as determined by the National Centers for Environmental Information.",
      "versionDate": "2025-09-11",
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
        "actionDate": "2025-10-28",
        "text": "Referred to the House Committee on Science, Space, and Technology."
      },
      "number": "5855",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Measuring the Cost of Disasters Act of 2025",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-09-29T18:26:04Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2775is.xml"
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
      "title": "Measuring the Cost of Disasters Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-27T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Measuring the Cost of Disasters Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-27T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Administrator of the National Oceanic and Atmospheric Administration to establish and maintain a database and webpage that is available to the public and contains information on the billion-dollar disasters that occur each year in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-27T03:48:17Z"
    }
  ]
}
```
