# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3301?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3301
- Title: Chip EQUIP Act
- Congress: 119
- Bill type: S
- Bill number: 3301
- Origin chamber: Senate
- Introduced date: 2025-12-02
- Update date: 2026-01-29T12:03:18Z
- Update date including text: 2026-01-29T12:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in Senate
- 2025-12-02 - IntroReferral: Introduced in Senate
- 2025-12-02 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-12-02: Introduced in Senate

## Actions

- 2025-12-02 - IntroReferral: Introduced in Senate
- 2025-12-02 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3301",
    "number": "3301",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "K000377",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Kelly, Mark [D-AZ]",
        "lastName": "Kelly",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Chip EQUIP Act",
    "type": "S",
    "updateDate": "2026-01-29T12:03:18Z",
    "updateDateIncludingText": "2026-01-29T12:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-02",
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
      "actionDate": "2025-12-02",
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
            "date": "2025-12-02T17:21:29Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-02T17:21:29Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "TN"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-01-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3301is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3301\nIN THE SENATE OF THE UNITED STATES\nDecember 2, 2025 Mr. Kelly (for himself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prohibit purchases of certain semiconductor manufacturing equipment from foreign entities of concern or subsidiaries of foreign entities of concern, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Chip Equipment Quality, Usefulness, and Integrity Protection Act of 2025 or the Chip EQUIP Act .\n#### 2. Purchases of semiconductor manufacturing equipment\n##### (a) Definitions\nSection 9901 of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 15 U.S.C. 4651 ) is amended by adding at the end the following:\n(14) The term completed, fully assembled , with respect to semiconductor manufacturing equipment, means the state in which all (or substantially all) necessary parts, chambers, subsystems, and subcomponents have been put together, resulting in such equipment that is\u2014 (A) ready-to-use or ready-to-install; and (B) ready to be purchased directly from an entity. (15) The term ineligible semiconductor manufacturing equipment \u2014 (A) means completed, fully assembled equipment that is manufactured, assembled, or refurbished by a foreign entity of concern or subsidiary thereof and designed for use in the fabrication, assembly, testing, advanced packaging, production, or research and development of semiconductors; (B) includes\u2014 (i) deposition equipment; (ii) etching equipment; (iii) lithography equipment; (iv) inspection, measuring, and test equipment; (v) wafer slicing equipment; (vi) wafer dicing equipment; (vii) wire bonders; (viii) ion implantation equipment; (ix) chemical mechanical polishing; (x) diffusion or oxidation furnaces; (xi) thermal processing equipment; and (xii) automated material handling systems; and (C) does not include any part, chamber, subsystem, or subcomponent that enables or is incorporated into such equipment. .\n##### (b) Ineligible use of funds\nSection 9909 of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 15 U.S.C. 4659 ) is amended\u2014\n**(1)**\nby redesignating subsection (f) as subsection (g); and\n**(2)**\nby inserting after subsection (e) the following new subsection:\n(f) Ineligible use of funds (1) In general Subject to paragraph (2), the Secretary shall include in the terms of each agreement with a covered entity for the award of Federal financial assistance under section 9902, or with the recipient of an award made under section 9906, prohibitions with respect to a project relating to the procurement, installation, or use of ineligible semiconductor manufacturing equipment, to be effective for 10 years beginning on the date on which the agreement is signed. (2) Waiver The Secretary may waive the prohibitions referred to in paragraph (1) if\u2014 (A) the ineligible semiconductor manufacturing equipment to be purchased by the applicable covered entity is not produced in the United States or an allied or partner country in sufficient and reasonably available quantities or of a satisfactory quality to support established or expected production capabilities; (B) the ineligible semiconductor manufacturing equipment at issue was manufactured and assembled by an entity that is not a foreign entity of concern or subsidiary thereof and was refurbished by a foreign entity of concern or subsidiary thereof; or (C) (i) the use of the ineligible semiconductor manufacturing equipment complies with the requirements set forth in the Export Administration Regulations (as such term is defined in section 1742 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4801 )); and (ii) the Secretary, in consultation with the Director of National Intelligence or the Secretary of Defense, determines such waiver is in the national security interest of the United States. (3) Foreign entities of concern Nothing in this subsection may be construed to waive the application of section 9907. .",
      "versionDate": "2025-12-02",
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
        "actionDate": "2025-11-20",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6207",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Chip EQUIP Act",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-01-07T16:18:59Z"
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
      "date": "2025-12-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3301is.xml"
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
      "title": "Chip EQUIP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-29T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Chip EQUIP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Chip Equipment Quality, Usefulness, and Integrity Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit purchases of certain semiconductor manufacturing equipment from foreign entities of concern or subsidiaries of foreign entities of concern, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T05:03:58Z"
    }
  ]
}
```
