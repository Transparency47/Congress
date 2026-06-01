# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2870?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2870
- Title: Fight Illicit Pill Presses Act
- Congress: 119
- Bill type: S
- Bill number: 2870
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2026-03-31T16:24:12Z
- Update date including text: 2026-03-31T16:24:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2870",
    "number": "2870",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Fight Illicit Pill Presses Act",
    "type": "S",
    "updateDate": "2026-03-31T16:24:12Z",
    "updateDateIncludingText": "2026-03-31T16:24:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
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
            "date": "2025-09-18T18:28:01Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-18T18:28:01Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "DE"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "KS"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "PA"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "NC"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MN"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "AZ"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "WA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "TN"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
      "state": "WV"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "NV"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "MS"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-02-12",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2870is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2870\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mr. Cornyn (for himself, Mr. Coons , Mr. Moran , Mr. Fetterman , Mr. Tillis , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Controlled Substances Act to require regulated persons to identify tableting machines and encapsulating machines by serial number.\n#### 1. Short title\nThis Act may be cited as the Fight Illicit Pill Presses Act .\n#### 2. Regulation of certain machines\n##### (a) Definitions\nSection 102 of the Controlled Substances Act ( 21 U.S.C. 802 ) is amended\u2014\n**(1)**\nby striking paragraph (38) and inserting the following:\n(38) The term regulated person means a person who\u2014 (A) manufactures, distributes, imports, or exports a listed chemical; (B) manufactures, distributes, delivers, sells, imports, or exports a tableting machine, an encapsulating machine, or a critical part; or (C) who acts as a broker or trader for an international transaction involving a listed chemical, a tableting machine, an encapsulating machine, or a critical part. ;\n**(2)**\nby striking paragraph (39)(B) and inserting the following:\n(B) a distribution, delivery, sale, importation, or exportation of a tableting machine, encapsulating machine, or critical part. ; and\n**(3)**\nby adding at the end the following:\n(61) The term critical part , when used in reference to a tableting machine or encapsulating machine, means any of the following integral parts of a tableting or encapsulating machine: (A) An upper punch. (B) A lower punch. (C) A die. (62) The term die means a tool that serves as the mold in which a product is compressed to form the desired size and shape of a tablet or capsule. (63) The term lower punch means the punch inserted into the turret below the die. (64) The term punch means a rod-shaped tool used in producing tablets and other products. (65) The term upper punch means the punch inserted into the turret above the die. .\n##### (b) Regulation\n**(1) Records of regulated transactions**\nSection 310(a) of the Controlled Substances Act ( 21 U.S.C. 830(a) ) is amended by adding at the end the following:\n(4) Each regulated person who manufactures, distributes, delivers, sells, imports, or exports a tableting machine, an encapsulating machine, a critical part of a tableting machine, or a critical part of an encapsulating machine shall, when and as required by regulations of the Attorney General, identify the tableting machine, encapsulating machine, critical part of a tableting machine, or critical part of an encapsulating machine by means of a serial number that is engraved, cast, or otherwise permanently affixed to a nonremovable part of the tableting machine, encapsulating machine, or critical part of a tableting machine, or critical part of an encapsulating machine. .\n**(2) Reports to attorney general**\nSection 310(b)(1) of the Controlled Substances Act ( 21 U.S.C. 830(b)(1) ) is amended by striking subparagraph (D) and inserting the following:\n(D) any regulated transaction in a tableting machine, encapsulating machine, or critical part, including the serial number affixed to the tableting machine, encapsulating machine, or critical part. .\n**(3) Regulations**\n**(A) In general**\nNot later than 180 days after the date of enactment of this Act, the Attorney General shall promulgate regulations carrying out the amendments made by paragraph (1).\n**(B) Detailed guidance**\nThe regulations required under subparagraph (A) shall include detailed guidance on serial numbers affixed to tableting machines, encapsulating machines, or critical parts manufactured on or before the date of enactment of this Act.\n**(C) Requirement**\nNotwithstanding paragraph (4), a serial number affixed to a tableting machine, encapsulating machine, or critical part manufactured on or before the date of enactment of this Act in accordance with the guidance provided under subparagraph (B) shall be deemed required under paragraph (4) of section 310(a) of the Controlled Substances Act, as added by paragraph (1) of this subsection.\n**(4) Effective date**\nThe amendments made by paragraph (1) shall apply only to any tableting machine, encapsulating machine, or critical part manufactured, distributed, delivered, sold, imported, or exported after the effective date of the regulations promulgated under paragraph (2).\n##### (c) Prohibited acts\nSection 403(a) of the Controlled Substances Act ( 21 U.S.C. 843(a) ) is amended\u2014\n**(1)**\nin paragraph (8), by striking or at the end;\n**(2)**\nin paragraph (9), by striking the period at the end and inserting a semicolon; and\n**(3)**\nby adding at the end the following:\n(10) to remove, alter, or obliterate any serial number affixed to a tableting machine, encapsulating machine, a critical part of a tableting machine, or a critical part of an encapsulating machine, that is required to have a serial number and with reasonable cause to believe the serial number is so required ; or (11) to transport, ship, receive, possess, distribute, deliver, sell, import, or export any tableting machine, encapsulating machine, a critical part of a tableting machine, or a critical part of an encapsulating machine that is required to have a serial number, knowing that the serial number has been removed, altered, or obliterated, and with reasonable cause to believe the serial number is so required. .",
      "versionDate": "2025-09-18",
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
        "actionDate": "2025-10-31",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5880",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fight Illicit Pill Presses Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-10T18:39:11Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2870is.xml"
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
      "title": "Fight Illicit Pill Presses Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fight Illicit Pill Presses Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Controlled Substances Act to require regulated persons to identify tableting machines and encapsulating machines by serial number.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:34Z"
    }
  ]
}
```
