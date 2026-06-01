# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6283?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6283
- Title: FOSTER Act
- Congress: 119
- Bill type: HR
- Bill number: 6283
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2026-05-14T08:07:47Z
- Update date including text: 2026-05-14T08:07:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-21: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-11-21: Introduced in House

## Actions

- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-21",
    "latestAction": {
      "actionDate": "2025-11-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6283",
    "number": "6283",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001159",
        "district": "10",
        "firstName": "Marilyn",
        "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
        "lastName": "Strickland",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "FOSTER Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:07:47Z",
    "updateDateIncludingText": "2026-05-14T08:07:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-21",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-21",
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
          "date": "2025-11-21T14:01:45Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "PA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "NE"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "WA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6283ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6283\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Ms. Strickland (for herself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the 21st Century Cures Act to support State and local agencies with responsibility for children services in their response to the opioid abuse crisis, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Furthering Opioid Services, Training, and Education Resources Act or the FOSTER Act .\n#### 2. Opioid grants to support caregivers, kinship care families, and kinship caregivers\n##### (a) Opioid grants\nSection 1003(b)(4) of the 21st Century Cures Act ( 42 U.S.C. 290ee\u20133 note) is amended\u2014\n**(1)**\nby redesignating subparagraph (F) as subparagraph (G); and\n**(2)**\nby inserting after subparagraph (E) the following:\n(F) Supporting opioid abuse prevention and treatment services within a State provided by State and local agencies for children and caregivers, kinship care families, and kinship caregivers through\u2014 (i) workforce recruitment and training; (ii) health care services (including such services described in subparagraph (D)); and (iii) foster and adoptive parent recruitment and training. .\n##### (b) Definitions\nSection 1003 of the 21st Century Cures Act ( 42 U.S.C. 290ee\u20133 note) is amended\u2014\n**(1)**\nby redesignating subsections (h), (i), and (j) as subsections (i), (j), and (k), respectively; and\n**(2)**\nby inserting after subsection (g) the following:\n(h) Definitions In this section: (1) The term kinship care family means a family with a kinship caregiver. (2) The term kinship caregiver means a relative of a child by blood, marriage, or adoption, who\u2014 (A) lives with the child; (B) is the primary caregiver of the child because the biological or adoptive parent of the child is unable or unwilling to serve as the primary caregiver of the child; and (C) has a legal relationship to the child or is raising the child informally. .\n##### (c) Authorization of appropriations\nParagraph (1) of section 1003(j) of the 21st Century Cures Act ( 42 U.S.C. 290ee\u20133 note), as redesignated by subsection (b), is amended by inserting , and $255,000,000 for each of fiscal years 2028 through 2033 after 2027 .\n##### (d) Set aside\nSection 1003(j)(3)(B) of the 21st Century Cures Act ( 42 U.S.C. 290ee\u20133 note), as redesignated, is amended\u2014\n**(1)**\nby striking , and up to and inserting , up to ; and\n**(2)**\nby inserting before the period at the end , and 1 percent of such amount for such fiscal year shall be made available to carry out subsection (b)(4)(F) .",
      "versionDate": "2025-11-21",
      "versionType": "Introduced in House"
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
        "name": "Health",
        "updateDate": "2025-12-19T15:56:23Z"
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
      "date": "2025-11-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6283ih.xml"
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
      "title": "FOSTER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FOSTER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T05:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Furthering Opioid Services, Training, and Education Resources Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T05:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the 21st Century Cures Act to support State and local agencies with responsibility for children services in their response to the opioid abuse crisis, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-18T05:18:29Z"
    }
  ]
}
```
