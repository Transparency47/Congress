# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5880?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5880
- Title: Fight Illicit Pill Presses Act
- Congress: 119
- Bill type: HR
- Bill number: 5880
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2026-03-31T16:24:12Z
- Update date including text: 2026-03-31T16:24:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-10-31: Introduced in House

## Actions

- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5880",
    "number": "5880",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Fight Illicit Pill Presses Act",
    "type": "HR",
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
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-31",
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
          "date": "2025-10-31T17:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-10-31T17:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NM"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "TX"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "CA"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "SC"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "VA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "CA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "CA"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "OH"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NJ"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "GA"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "NJ"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5880ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5880\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Ms. Hageman (for herself, Ms. Stansbury , Mr. Crenshaw , Mr. Harder of California , and Mr. Fry ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Controlled Substances Act to require regulated persons to identify tableting machines and encapsulating machines by serial number.\n#### 1. Short title\nThis Act may be cited as the Fight Illicit Pill Presses Act .\n#### 2. Regulation of certain machines\n##### (a) Definitions\nSection 102 of the Controlled Substances Act ( 21 U.S.C. 802 ) is amended\u2014\n**(1)**\nby striking paragraph (38) and inserting the following:\n(38) The term regulated person means a person who\u2014 (A) manufactures, distributes, imports, or exports a listed chemical; (B) manufactures, distributes, delivers, sells, imports, or exports a tableting machine, an encapsulating machine, or a critical part; or (C) who acts as a broker or trader for an international transaction involving a listed chemical, a tableting machine, an encapsulating machine, or a critical part. ;\n**(2)**\nby striking paragraph (39)(B) and inserting the following:\n(B) a distribution, delivery, sale, importation, or exportation of a tableting machine, encapsulating machine, or critical part. ; and\n**(3)**\nby adding at the end the following:\n(60) The term critical part , when used in reference to a tableting machine or encapsulating machine, means any of the following integral parts of a tableting or encapsulating machine: (A) An upper punch. (B) A lower punch. (C) A die. (61) The term die means a tool that serves as the mold in which a product is compressed to form the desired size and shape of a tablet or capsule. (62) The term lower punch means the punch inserted into the turret below the die. (63) The term punch means a rod-shaped tool used in producing tablets and other products. (64) The term upper punch means the punch inserted into the turret above the die. .\n##### (b) Regulation\n**(1) Records of regulated transactions**\nSection 310(a) of the Controlled Substances Act ( 21 U.S.C. 830(a) ) is amended by adding at the end the following:\n(4) Each regulated person who manufactures, distributes, delivers, sells, imports, or exports a tableting machine, an encapsulating machine, a critical part of a tableting machine, or a critical part of an encapsulating machine shall, when and as required by regulations of the Attorney General, identify the tableting machine, encapsulating machine, critical part of a tableting machine, or critical part of an encapsulating machine by means of a serial number that is engraved, cast, or otherwise permanently affixed to a nonremovable part of the tableting machine, encapsulating machine, or critical part of a tableting machine, or critical part of an encapsulating machine. .\n**(2) Reports to attorney general**\nSection 310(b)(1) of the Controlled Substances Act ( 21 U.S.C. 830(b)(1) ) is amended by striking subparagraph (D) and inserting the following:\n(D) any regulated transaction in a tableting machine, encapsulating machine, or critical part, including the serial number affixed to the tableting machine, encapsulating machine, or critical part. .\n**(3) Regulations**\n**(A) In general**\nNot later than 180 days after the date of enactment of this Act, the Attorney General shall promulgate regulations carrying out the amendments made by paragraph (1).\n**(B) Detailed guidance**\nThe regulations required under subparagraph (A) shall include detailed guidance on serial numbers affixed to tableting machines, encapsulating machines, or critical parts manufactured on or before the date of enactment of this Act.\n**(C) Requirement**\nNotwithstanding paragraph (4), a serial number affixed to a tableting machine, encapsulating machine, or critical part manufactured on or before the date of enactment of this Act in accordance with the guidance provided under subparagraph (B) shall be deemed required under paragraph (4) of section 310(a) of the Controlled Substances Act, as added by paragraph (1) of this subsection.\n**(4) Effective date**\nThe amendments made by paragraph (1) shall apply only to any tableting machine, encapsulating machine, or critical part manufactured, distributed, delivered, sold, imported, or exported after the effective date of the regulations promulgated under paragraph (2).\n##### (c) Prohibited acts\nSection 403(a) of the Controlled Substances Act ( 21 U.S.C. 843(a) ) is amended\u2014\n**(1)**\nin paragraph (8), by striking or at the end;\n**(2)**\nin paragraph (9), by striking the period at the end and inserting a semicolon; and\n**(3)**\nby adding at the end the following:\n(10) to remove, alter, or obliterate any serial number affixed to a tableting machine, encapsulating machine, a critical part of a tableting machine, or a critical part of an encapsulating machine, that is required to have a serial number and with reasonable cause to believe the serial number is so required; or (11) to transport, ship, receive, possess, distribute, deliver, sell, import, or export any tableting machine, encapsulating machine, a critical part of a tableting machine, or a critical part of an encapsulating machine that is required to have a serial number, knowing that the serial number has been removed, altered, or obliterated, and with reasonable cause to believe the serial number is so required. .",
      "versionDate": "2025-10-31",
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
        "actionDate": "2025-09-18",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "2870",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fight Illicit Pill Presses Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-10T18:38:28Z"
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
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5880ih.xml"
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
      "title": "Fight Illicit Pill Presses Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-05T10:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fight Illicit Pill Presses Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-05T10:53:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Controlled Substances Act to require regulated persons to identify tableting machines and encapsulating machines by serial number.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-05T10:48:15Z"
    }
  ]
}
```
