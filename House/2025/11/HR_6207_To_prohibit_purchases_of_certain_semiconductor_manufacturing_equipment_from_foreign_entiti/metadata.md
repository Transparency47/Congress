# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6207?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6207
- Title: Chip EQUIP Act
- Congress: 119
- Bill type: HR
- Bill number: 6207
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-05-22T08:07:50Z
- Update date including text: 2026-05-22T08:07:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6207",
    "number": "6207",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "L000397",
        "district": "18",
        "firstName": "Zoe",
        "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
        "lastName": "Lofgren",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Chip EQUIP Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:50Z",
    "updateDateIncludingText": "2026-05-22T08:07:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-20T15:00:30Z",
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
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "MI"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "OH"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "IN"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "TX"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "PA"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "ND"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6207ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6207\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Ms. Lofgren (for herself, Mr. Obernolte , Mr. Krishnamoorthi , Mr. Moolenaar , Mr. Landsman , and Mrs. Houchin ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit purchases of certain semiconductor manufacturing equipment from foreign entities of concern or subsidiaries of foreign entities of concern, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Chip Equipment Quality, Usefulness, and Integrity Protection Act of 2025 or the Chip EQUIP Act .\n#### 2. Purchases of semiconductor manufacturing equipment\n##### (a) Definitions\nSection 9901 of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 15 U.S.C. 4651 ) is amended by adding at the end the following:\n(14) The term completed, fully assembled , with respect to semiconductor manufacturing equipment, means the state in which all (or substantially all) necessary parts, chambers, subsystems, and subcomponents have been put together, resulting in such equipment that is\u2014 (A) ready-to-use or ready-to-install; and (B) ready to be purchased directly from an entity. (15) The term ineligible semiconductor manufacturing equipment \u2014 (A) means completed, fully assembled equipment that is manufactured, assembled, or refurbished by a foreign entity of concern or subsidiary thereof and designed for use in the fabrication, assembly, testing, advanced packaging, production, or research and development of semiconductors; (B) includes\u2014 (i) deposition equipment; (ii) etching equipment; (iii) lithography equipment; (iv) inspection, measuring, and test equipment; (v) wafer slicing equipment; (vi) wafer dicing equipment; (vii) wire bonders; (viii) ion implantation equipment; (ix) chemical mechanical polishing; (x) diffusion or oxidation furnaces; (xi) thermal processing equipment; and (xii) automated material handling systems; and (C) does not include any part, chamber, subsystem, or subcomponent that enables or is incorporated into such equipment. .\n##### (b) Ineligible use of funds\nSection 9909 of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 15 U.S.C. 4659 ) is amended\u2014\n**(1)**\nby redesignating subsection (f) as subsection (g); and\n**(2)**\nby inserting after subsection (e) the following new subsection:\n(f) Ineligible use of funds (1) In general Subject to paragraph (2), the Secretary shall include in the terms of each agreement with a covered entity for the award of Federal financial assistance under section 9902, or with the recipient of an award made under section 9906, prohibitions with respect to a project relating to the procurement, installation, or use of ineligible semiconductor manufacturing equipment, to be effective for 10 years beginning on the date on which the agreement is signed. (2) Waiver The Secretary may waive the prohibitions referred to in paragraph (1) if\u2014 (A) the ineligible semiconductor manufacturing equipment to be purchased by the applicable covered entity is not produced in the United States or an allied or partner country in sufficient and reasonably available quantities or of a satisfactory quality to support established or expected production capabilities; (B) the ineligible semiconductor manufacturing equipment at issue was manufactured or assembled by an entity that is not a foreign entity of concern or subsidiary thereof and was refurbished by a foreign entity of concern or subsidiary thereof; or (C) (i) the use of the ineligible semiconductor manufacturing equipment complies with the requirements set forth in the Export Administration Regulations (as such term is defined in section 1742 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4801 )); and (ii) the Secretary, in consultation with the Director of National Intelligence or the Secretary of Defense, determines such waiver is in the national security interest of the United States. (3) Foreign entities of concern Nothing in this subsection may be construed to waive the application of section 9907. .",
      "versionDate": "2025-11-20",
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
        "actionDate": "2025-12-02",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "3301",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Chip EQUIP Act",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-12-09T20:16:15Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6207ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Chip EQUIP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-21T13:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Chip Equipment Quality, Usefulness, and Integrity Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-21T13:23:20Z"
    },
    {
      "title": "Chip EQUIP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-21T13:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit purchases of certain semiconductor manufacturing equipment from foreign entities of concern or subsidiaries of foreign entities of concern, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-21T13:18:22Z"
    }
  ]
}
```
